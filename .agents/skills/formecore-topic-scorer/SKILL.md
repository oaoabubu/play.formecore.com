---
name: formecore-topic-scorer
description: Generate, evaluate, rank, and rewrite content topics for play.formecore.com when planning searchable blog posts, rankings, comparisons, roundups, explainers, or product-led articles. Use it to judge whether a topic is direct, written in natural user language, clear about the promised content, plausibly searchable, relevant to the product, and compelling without becoming misleading clickbait.
---

# FORMECORE Topic Scorer

Create topics that ordinary users may actually search for and understand. Treat the score as a decision aid backed by evidence, not a substitute for search data.

## Choose the mode

- **Generate:** produce a diverse candidate set from the product facts and topic gaps.
- **Score:** evaluate supplied topics without silently rewriting them.
- **Refine:** score first, then rewrite weak topics while preserving their intended search intent.
- **Select:** compare candidates, reject overlaps, and recommend a prioritized shortlist.
- **Daily discovery:** research current public sources, consider at least 15
  candidates internally, and add exactly five new qualified topic SoTs when the
  evidence supports them.

If the request does not specify a mode, infer it from the requested outcome. Do not draft full articles unless explicitly asked.

## Read before judging

Read the available project sources in this order:

1. Product and audience truth: `memory/`, `sot/`, product documentation, and the playable product source.
2. Existing plans and output: `topics/`, `content/`, `site/`, and published URLs.
3. Performance evidence: `data/`, `learnings.md`, Search Console exports, or supplied keyword research.

Missing files are not permission to invent facts. State what evidence is absent. When current competitors, product features, prices, search results, or search demand matter, verify them with current sources.

Read [references/topic-types.md](references/topic-types.md) when generating or expanding a topic set. Read [references/scoring-rubric.md](references/scoring-rubric.md) whenever scoring, ranking, selecting, or refining topics. Read [references/topic-sot-schema.md](references/topic-sot-schema.md) before writing any topic to the library.

## Non-negotiable distinctions

- A **candidate topic** belongs in the backlog and may still be rejected.
- A **topic SoT** is created only after a topic qualifies. It is the single factual and editorial source for all channel versions.
- Searchability is not the same as verified search volume. Label demand evidence as `measured`, `observed`, `inferred`, or `unverified`.
- Excitement comes from a sharp benefit, tension, novelty, contrast, or useful specificity—not unsupported superlatives, fear, or withheld context.

## Workflow

1. Identify one primary audience, one user situation, one search intent, and one language/locale per topic.
2. Inventory existing topics and canonical URLs. Flag duplicates and keyword cannibalization before proposing new pages.
3. Generate across several relevant topic types rather than repeating one title formula.
4. Score each topic with the 100-point rubric and apply every hard gate.
5. For weak topics, diagnose the specific failure before rewriting.
6. Recommend the best content action:
   - `new`: genuinely new search intent;
   - `update`: strengthen an existing canonical page;
   - `merge`: combine overlapping topics;
   - `reject`: weak, misleading, irrelevant, or unsupported.
7. Create a topic SoT only when requested or when the workflow explicitly proceeds beyond topic selection.

## Daily discovery invariants

- Use the Brisbane calendar date supplied by the task.
- Search current sources; do not recycle five synonyms from the static examples.
- Consider at least 15 candidates internally, then choose five distinct search
  intents that pass every hard gate and score at least 75.
- Compare against the complete library, not only yesterday's topics.
- Write one new immutable topic file per accepted idea. Never overwrite an
  existing SoT or manually edit the generated top-five queue.
- A daily run that cannot support five qualified topics must return
  `needs-human`; it must not lower the threshold or fabricate demand evidence.

## Natural-language title rules

- Use words a general user would type or immediately understand.
- Put the recognisable subject early: `貓咪番茄鐘`, `虛擬寵物專注 App`, `線上運動計時器`.
- Make the content visible from the title: recommendation, comparison, explanation, steps, limitations, or answer.
- Prefer concrete nouns and verbs over internal jargon such as `GEO`, `SOT`, `內容矩陣`, `賦能`, or `閉環` in public titles.
- Use years, numbers, `最佳`, `免費`, or `推薦` only when the article can substantiate and maintain them.
- Do not imply medical, fitness, productivity, or financial outcomes the product and sources cannot support.

## Output for scoring or selection

Return a compact table containing:

| Field | Required content |
|---|---|
| Topic | Original title |
| Intent | The user question or decision behind the search |
| Type | Ranking, roundup, comparison, explainer, how-to, problem, use case, trust, or update |
| Demand evidence | `measured`, `observed`, `inferred`, or `unverified`, with the evidence |
| Score | Total out of 100 |
| Gate | `pass` or the failed hard gate |
| Decision | `priority`, `qualified`, `rewrite`, or `reject` |
| Content action | `new`, `update`, `merge`, or `reject` |
| Diagnosis | The most important reason |
| Suggested title | Only when refinement would materially improve it |

After the table, provide:

1. the top three recommended topics;
2. the search intent each one uniquely owns;
3. any evidence that must be collected before publication;
4. conflicts with existing pages or topics.

Do not reward a title merely for sounding dramatic. A topic that fails a hard gate cannot pass by accumulating points elsewhere.
