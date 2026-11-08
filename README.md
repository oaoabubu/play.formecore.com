# play.formecore.com content operations

This repository is the source of truth for discoverable marketing content for
the Play.formecore.com game. Berry is the cat character inside the game.

## Content loop

1. Product truth lives in `memory/`.
2. Every candidate that enters the library gets its own topic SoT in
   `topics/library/`.
3. The project skill `.agents/skills/formecore-topic-scorer/` generates,
   scores, rejects, or refines topics.
4. `scripts/topic_library.py rebuild` keeps the five highest-scoring,
   unpublished topics in `topics/selection/queue.md`.
5. `.github/workflows/daily-topic-discovery.yml` runs every day at 05:00 in
   Australia/Brisbane, researches current demand, adds five qualified topic
   SoTs, validates them, and rebuilds the queue.

The daily workflow requires an `OPENAI_API_KEY` repository secret. Keep API
keys in GitHub Secrets only.

## Status lifecycle

`qualified → selected → briefing → drafting → review → approved → published`

Topics may also become `update-due`, `merged`, or `rejected`. The daily
workflow creates `qualified` topics; the deterministic queue script owns the
transition between `qualified` and `selected`.

## Useful commands

```bash
python3 scripts/topic_library.py validate-all
python3 scripts/topic_library.py rebuild --date 2026-11-08
python3 scripts/topic_library.py validate-daily --date 2026-11-08 --expected 5
```
