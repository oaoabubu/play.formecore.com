#!/usr/bin/env python3
"""Validate topic SoTs and deterministically rebuild the top-five queue."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "topics" / "library"
QUEUE = ROOT / "topics" / "selection" / "queue.md"
RUNS = ROOT / "runs"

REQUIRED = {
    "id",
    "title",
    "locale",
    "created_on",
    "updated_on",
    "source",
    "discovery_run",
    "status",
    "content_stage",
    "score",
    "decision",
    "hard_gate",
    "type",
    "content_type",
    "primary_expression",
    "intent_key",
    "demand_evidence",
}

REQUIRED_PLATFORMS = (
    "play.formecore.com/blog",
    "Xiaohongshu",
    "WeChat Official Account",
    "Medium",
    "TikTok",
    "Douyin",
    "Threads",
    "Instagram",
    "Facebook",
    "YouTube Shorts",
)

STATUSES = {
    "qualified",
    "selected",
    "briefing",
    "drafting",
    "review",
    "approved",
    "published",
    "update-due",
    "merged",
    "rejected",
}

ELIGIBLE = {"qualified", "selected"}
DEMAND = {"measured", "observed", "inferred", "unverified"}


@dataclass
class Topic:
    path: Path
    meta: dict[str, str]
    body: str

    @property
    def score(self) -> int:
        return int(self.meta["score"])


def parse_topic(path: Path) -> Topic:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n?(.*)\Z", text, re.S)
    if not match:
        raise ValueError(f"{path}: missing frontmatter")
    meta: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"{path}: invalid frontmatter line: {raw}")
        key, value = raw.split(":", 1)
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return Topic(path, meta, match.group(2))


def load_topics() -> list[Topic]:
    return [parse_topic(path) for path in sorted(LIBRARY.glob("*.md"))]


def validate(topics: list[Topic]) -> list[str]:
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}
    seen_intents: dict[str, Path] = {}
    seen_titles: dict[str, Path] = {}

    for topic in topics:
        missing = sorted(REQUIRED - topic.meta.keys())
        if missing:
            errors.append(f"{topic.path}: missing {', '.join(missing)}")
            continue
        try:
            score = topic.score
        except ValueError:
            errors.append(f"{topic.path}: score must be an integer")
            continue
        if not 0 <= score <= 100:
            errors.append(f"{topic.path}: score must be between 0 and 100")
        if topic.meta["status"] not in STATUSES:
            errors.append(f"{topic.path}: invalid status {topic.meta['status']}")
        if topic.meta["demand_evidence"] not in DEMAND:
            errors.append(
                f"{topic.path}: invalid demand_evidence {topic.meta['demand_evidence']}"
            )
        if topic.meta["hard_gate"] != "pass" and topic.meta["status"] not in {
            "rejected",
            "merged",
        }:
            errors.append(f"{topic.path}: failed gate topic cannot remain active")
        if score < 75 and topic.meta["status"] in ELIGIBLE:
            errors.append(f"{topic.path}: active queue topic must score at least 75")
        for field, seen in (
            ("id", seen_ids),
            ("intent_key", seen_intents),
            ("title", seen_titles),
        ):
            value = topic.meta[field].casefold()
            if value in seen:
                errors.append(
                    f"{topic.path}: duplicate {field} with {seen[value]} ({value})"
                )
            else:
                seen[value] = topic.path
        for heading in (
            "## Search intent",
            "## Content promise",
            "## Hook and distinctive highlight",
            "## Product bridge",
            "## Platform production plan",
        ):
            if heading not in topic.body:
                errors.append(f"{topic.path}: missing section {heading}")
        for platform in REQUIRED_PLATFORMS:
            if f"| {platform} |" not in topic.body:
                errors.append(
                    f"{topic.path}: platform production plan missing {platform}"
                )
    return errors


def replace_status(topic: Topic, status: str) -> None:
    text = topic.path.read_text(encoding="utf-8")
    updated, count = re.subn(
        r"(?m)^status:\s*[^\n]+$", f"status: {status}", text, count=1
    )
    if count != 1:
        raise ValueError(f"{topic.path}: could not update status")
    topic.path.write_text(updated, encoding="utf-8")
    topic.meta["status"] = status


def rebuild(topics: list[Topic], run_date: str) -> None:
    eligible = [topic for topic in topics if topic.meta["status"] in ELIGIBLE]
    eligible.sort(
        key=lambda topic: (
            -topic.score,
            topic.meta["created_on"],
            topic.meta["id"],
        )
    )
    selected = eligible[:5]
    selected_paths = {topic.path for topic in selected}
    for topic in eligible:
        wanted = "selected" if topic.path in selected_paths else "qualified"
        if topic.meta["status"] != wanted:
            replace_status(topic, wanted)

    QUEUE.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for rank, topic in enumerate(selected, 1):
        rel = (Path("..") / "library" / topic.path.name).as_posix()
        rows.append(
            f"| {rank} | [{topic.meta['title']}]({rel}) | {topic.score} | "
            f"{topic.meta['type']} | {topic.meta['demand_evidence']} | "
            f"{topic.meta['content_stage']} |"
        )
    body = (
        "# Current top-five topic queue\n\n"
        "This file is generated by `scripts/topic_library.py`; do not edit it "
        "manually. It contains the highest-scoring unpublished topics that are "
        "still eligible for production.\n\n"
        f"Last rebuilt: {run_date} (Australia/Brisbane)\n\n"
        "| Rank | Topic | Score | Type | Demand evidence | Content stage |\n"
        "|---:|---|---:|---|---|---|\n"
        + "\n".join(rows)
        + "\n"
    )
    QUEUE.write_text(body, encoding="utf-8")


def fail(errors: list[str]) -> None:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate-all")
    rebuild_parser = sub.add_parser("rebuild")
    rebuild_parser.add_argument("--date", default=date.today().isoformat())
    daily = sub.add_parser("validate-daily")
    daily.add_argument("--date", required=True)
    daily.add_argument("--expected", type=int, default=5)
    count_daily = sub.add_parser("daily-count")
    count_daily.add_argument("--date", required=True)
    args = parser.parse_args()

    topics = load_topics()
    errors = validate(topics)
    if errors:
        fail(errors)

    if args.command in {"validate-daily", "daily-count"}:
        discovered = [
            topic
            for topic in topics
            if topic.meta["source"] == "daily"
            and topic.meta["discovery_run"] == args.date
        ]
        if args.command == "daily-count":
            print(len(discovered))
            return
        if len(discovered) != args.expected:
            fail(
                [
                    f"expected {args.expected} daily topics for {args.date}, "
                    f"found {len(discovered)}"
                ]
            )
        weak = [topic.path for topic in discovered if topic.score < 75]
        if weak:
            fail([f"daily topics below 75: {', '.join(map(str, weak))}"])
        report = RUNS / args.date / "report.md"
        receipt = RUNS / args.date / "status.json"
        if not report.is_file():
            fail([f"missing daily report: {report}"])
        if not receipt.is_file():
            fail([f"missing daily receipt: {receipt}"])
        try:
            status = json.loads(receipt.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            fail([f"invalid daily receipt {receipt}: {exc}"])
        if status.get("status") != "done":
            fail([f"daily receipt is not done: {receipt}"])
        print(f"Validated {len(discovered)} daily topics for {args.date}")
    elif args.command == "rebuild":
        rebuild(topics, args.date)
        print(f"Rebuilt queue with up to five topics for {args.date}")
    else:
        print(f"Validated {len(topics)} topic SoTs")


if __name__ == "__main__":
    main()
