# Topic SoT schema and lifecycle

Every accepted topic is a maintained source of truth, not merely a title. Use
`topics/TEMPLATE.md` and create one file in `topics/library/` per topic.

## Required metadata

- `id`: immutable unique identifier.
- `title`: current public-facing Traditional Chinese title.
- `locale`: normally `zh-Hant` for the initial article.
- `created_on`, `updated_on`: Brisbane calendar dates.
- `source`: `initial`, `daily`, or another explicit source.
- `discovery_run`: the daily run date or `initial`.
- `status`: workflow state.
- `content_stage`: production state, normally `planned` at discovery.
- `score`: integer 0–100 from the current rubric.
- `decision`: `priority`, `qualified`, `rewrite`, or `reject`.
- `hard_gate`: `pass` for active topics.
- `type`: the primary topic type.
- `intent_key`: stable, unique canonical search intent.
- `demand_evidence`: `measured`, `observed`, `inferred`, or `unverified`.

## Required content

1. Search intent.
2. One primary audience and situation.
3. A visible content promise.
4. Core answer or viewpoint.
5. One defensible hook and distinctive highlight.
6. Honest product bridge.
7. Evidence required before drafting.
8. Claims and boundaries.
9. Concrete deliverables and status for every planned platform.
10. Production checklist.

## Status lifecycle

- `qualified`: passed the rubric and waits in the library.
- `selected`: currently in the deterministic top-five queue.
- `briefing`, `drafting`, `review`, `approved`: content-production stages.
- `published`: the canonical page is live.
- `update-due`: published facts or rankings require review.
- `merged`: its intent has been consolidated into another SoT.
- `rejected`: it cannot meet the gates or minimum score.

Only the queue script should move active topics between `qualified` and
`selected`. Content-production workflows own later states.

## Platform plan

The SoT records deliverables for `play.formecore.com/blog`, Xiaohongshu,
Instagram, and YouTube Shorts. Discovery sets them to `planned`; it does not
draft or publish them. Remove or add a channel only when the project channel
SoT changes.
