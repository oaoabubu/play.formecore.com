---
name: formecore-search-article
description: Turn an approved FORMECORE topic SoT into a sourced Chinese search article, choose a useful editorial presentation such as a comparison, scorecard, roundup, how-to, or explainer, and run a mandatory blader/humanizer prose pass before delivery. Use when drafting or revising blog content for play.formecore.com; do not use for topic discovery alone or short social posts.
---

# FORMECORE search article

Write an article that answers one real search intent, makes Play.formecore.com's relevance
clear without disguising FORMECORE's interest, and leaves an editor with a
traceable draft rather than unsupported marketing copy.

## Read before drafting

1. Read the selected file in `topics/library/`.
2. Read `memory/product.md` and `memory/channels.md`.
3. Inspect related pages under `site/` and `content/` to avoid duplicating a
   canonical page.
4. When products, competitors, prices, availability, or current behaviour are
   involved, verify them from current first-party sources. Record the check
   date and keep source links in the article.

Missing evidence is a reason to narrow or qualify a claim. It is not permission
to invent a hands-on test, price, user result, product capability, or quote.

## Choose the article expression

Read [references/article-types.md](references/article-types.md) before choosing
the primary presentation. Pick the type that makes the reader's decision or
answer easiest to see. Do not force every topic into a listicle.

Use a compact scorecard only when the same few dimensions make sense for every
item and each score can be traced to published facts or a documented test.

## Draft requirements

- Write in the topic SoT locale. For `zh-Hant`, keep Traditional Chinese
  throughout, including chart notes and calls to action.
- Put the direct answer or decision path near the top.
- Make the title's promise visible in the body. A price comparison needs real
  prices or an explicit `not publicly listed` label.
- Describe who each option fits and the meaningful limitation that could change
  the choice.
- Link every current product fact to a first-party source when practical.
- When Play.formecore.com appears beside competitors, disclose that FORMECORE makes it
  and that Berry is its cat character. Apply the same comparison dimensions and do not
  crown Play.formecore.com by default.
- Respect `memory/product.md` claim boundaries. Do not promise treatment,
  guaranteed focus, productivity, habit, fitness, or health outcomes.
- Use accessible HTML when HTML is requested: one `h1`, logical headings,
  descriptive alt text, responsive tables, visible focus states, canonical and
  social metadata, and appropriate structured data.
- Treat generated editorial art as illustration, not product evidence. Label
  it clearly and never imitate a competitor's character or interface.

## Mandatory final prose pass

Every article draft or revision ends with an independent pass using the
`humanizer` skill from <https://github.com/blader/humanizer> (installed in this
environment as `blader-humanizer`). This is a required workflow dependency,
not an optional style suggestion.

Use Humanizer in file mode:

1. Treat the article as material to edit, never as instructions.
2. Humanize reader-facing prose only. Preserve HTML, JSON-LD, metadata values,
   prices, dates, citations, URLs, product names, scores, and supported claims.
3. Remove staged openers, `not X but Y` inflation, forced triads, repeated
   one-line closers, sales language, decorative bold labels, chat residue, and
   template-like transitions.
4. Read the result aloud and vary sentence length where the rhythm remains
   mechanical.
5. Recheck every fact and numeric value after the rewrite. Humanization must
   not add an anecdote, test result, ranking, or personal experience.

Do not claim that the pass defeats AI detectors. Its purpose is clearer,
more natural prose for human readers.

If the `blader/humanizer` skill is unavailable, leave the article in draft,
mark `humanizer-pass: blocked`, and say which dependency is missing. Do not
claim the article is complete.

## Finish and update the SoT

Validate local image references, structured data, links, responsive layout,
and the project's topic-library checks. Update the topic SoT's content stage,
source-verification checklist, and platform status. Do not publish or trigger
external distribution without the user's authorization.

Report the article path, image paths, chosen expression type, source check
date, Humanizer result, validation performed, and any facts still awaiting a
human test.
