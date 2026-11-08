---
name: formecore-content-scorer
description: Score and diagnose FORMECORE long-form content for depth, breadth, evidence, insight, rhetoric, expression, readability, trust, SEO/GEO usefulness, and observable AI-writing-pattern risk. Use for article review, editorial QA, before-and-after comparison, or publish-readiness decisions; do not use to score topic ideas or to guess whether a human or model authored a text.
---

# FORMECORE content scorer

Evaluate the finished content, not the title idea. Keep content quality and
AI-pattern risk as two separate results: a clear reference article may use a
plain style without being weak, and unusual prose is not automatically good.

## Choose the mode

- **Score:** issue the full quality and AI-pattern report without rewriting.
- **Diagnose:** explain the few problems that most affect the reader.
- **Compare:** score two versions with the same rubric and show the deltas.
- **Re-score:** verify whether named revisions fixed the earlier problems.

Do not edit the article unless the user also asks for a revision. When a
revision is requested, route the writing work through
`$formecore-search-article`, including its mandatory Humanizer pass, then
re-score the result independently.

## Read before scoring

1. Read the article, its topic SoT, `memory/product.md`, and linked sources.
2. Read [references/content-rubric.md](references/content-rubric.md) completely.
3. For the AI-pattern assessment, read the installed `humanizer` skill from
   <https://github.com/blader/humanizer> completely. Its patterns are editing
   signals, not proof of authorship.
4. For current prices, products, competitors, laws, medical claims, or other
   changing facts, verify the source before rewarding evidence quality.

Score the reader-facing article. Do not penalize necessary HTML, JSON-LD,
frontmatter, citations, tables, or code as if they were prose.

## Non-negotiable distinctions

- `AI-pattern risk` is not an AI-detector probability and does not identify the
  author. Report it as a 0–100 editorial risk where lower is better.
- Depth means the article explains causes, trade-offs, limitations, or decision
  consequences. Word count alone earns nothing.
- Breadth means the article covers the parts required by its promise. Adding
  loosely related sections can lower the score.
- Rhetoric earns points only when it improves understanding or momentum.
  Decorative drama, clickbait, and false intimacy do not count.
- Natural expression is specific, varied, and appropriate to the audience. It
  does not require slang, first-person anecdotes, or grammatical roughness.
- A factual error or fabricated experience cannot be offset by polished prose.

## Output contract

Start with:

- `Content quality: N/100`
- `AI-pattern risk: N/100 (lower is better)`
- `Decision: publish-ready | edit | rewrite | blocked`
- one sentence naming the most important reason.

Then provide:

1. hard-gate results;
2. the complete quality score table with score, weight, evidence, and diagnosis;
3. the AI-pattern risk table with observed examples and density;
4. the three revisions most likely to improve the reader's experience;
5. facts or screenshots still needing human verification;
6. a re-score target.

Quote only the shortest passage needed to locate a problem. For local files,
include headings or line numbers. Every numeric score needs a reason grounded
in the content; do not assign numbers from general impression alone.

Do not call a draft `publish-ready` unless it passes every hard gate, scores at
least 85 for quality, and has AI-pattern risk of 25 or less.
