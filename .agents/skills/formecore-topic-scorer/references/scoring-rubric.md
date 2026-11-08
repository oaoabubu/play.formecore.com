# Topic scoring rubric

Score each topic from 0 to 100. Give a short evidence-based reason for every dimension; do not assign unexplained numbers.

## Hard gates

A failed gate forces `rewrite` or `reject`, regardless of total score.

1. **Understandable:** a general target user can understand the title without internal context.
2. **Visible promise:** the reader can predict what the page will contain and what question it answers.
3. **Single intent:** the title does not combine unrelated searches or promise several incompatible articles.
4. **Truthful:** the claim, ranking, year, number, comparison, and implied result can be supported.
5. **Product fit:** the topic has a credible path to Play.formecore.com, not just generic traffic.
6. **Safe claim:** it does not promise treatment, guaranteed focus, fitness results, or another unsupported outcome.
7. **Distinct page:** it does not duplicate an existing canonical page; otherwise choose `update` or `merge`.

## Weighted dimensions

### 1. Search-intent clarity — 15

- 13–15: one recognisable query and one clear answer or decision.
- 8–12: intent is understandable but broad or slightly mixed.
- 1–7: subject exists, but the user need is vague.
- 0: no identifiable search intent.

### 2. Natural human language and directness — 12

- 10–12: sounds like language users search or say; subject appears early.
- 6–9: readable but formal, indirect, or padded.
- 1–5: internal jargon, keyword stuffing, or unnatural phrasing.
- 0: incomprehensible to the target user.

### 3. Content visibility — 10

Can the reader anticipate the actual contents?

- 9–10: format and scope are explicit.
- 5–8: subject is clear but coverage is uncertain.
- 1–4: curiosity depends on hiding the content.
- 0: title and likely article do not match.

### 4. Demand evidence — 13

- 11–13: supported by Search Console, keyword data, or repeated real-user queries.
- 8–10: supported by current search-result patterns, suggestions, competitor coverage, or community questions.
- 4–7: plausible natural query but only inferred.
- 1–3: weak speculation.
- 0: no plausible user demand.

Never invent search volume. Record the evidence level.

### 5. Product and audience relevance — 12

- 10–12: directly matches a real Play.formecore.com feature and a priority user situation.
- 6–9: adjacent problem with a credible product bridge.
- 1–5: traffic might be relevant, but the product connection is forced.
- 0: unrelated traffic.

### 6. Compelling strength — 12

Judge whether the title creates a reason to continue through specificity, tension, contrast, novelty, or a valuable outcome.

- 10–12: strong and specific without overstating.
- 6–9: useful but ordinary.
- 1–5: flat, generic, or interchangeable.
- 0: misleading clickbait or unsupported shock value.

### 7. Usefulness and answer depth — 8

- 7–8: can support a substantial answer, decision, test, comparison, or procedure.
- 4–6: useful but narrow.
- 1–3: likely to become thin or repetitive.
- 0: no meaningful answer beyond promotion.

### 8. Distinctive highlight — 5

- 5: one specific contrast, tension, novelty, or overlooked question makes the angle memorable.
- 3–4: the angle is useful but only moderately distinct.
- 1–2: mostly interchangeable with existing articles.
- 0: copied or undifferentiated premise.

The highlight must be visible in the topic description or title; a vague promise
to make the eventual article interesting does not earn points.

### 9. First-party evidence — 3

- 3: real product tests, screenshots, design records, usage data, or founder experience are available.
- 2: the evidence can be collected before drafting.
- 1: only a minor product example is available.
- 0: the article would be generic synthesis or require invented experience.

### 10. Format and SERP/GEO fit — 5

- 5: format matches intent and is easy to extract: answer-first, table, list, steps, FAQ, or explicit comparison.
- 3–4: workable with structural changes.
- 1–2: format does not suit the query.
- 0: unclear deliverable.

### 11. Maintainability and freshness — 5

- 5: has a clear update trigger, source set, and stable canonical URL.
- 3–4: maintainable with periodic review.
- 1–2: likely to decay quickly or require unavailable data.
- 0: cannot be kept truthful.

## Decision bands

- **85–100 · priority:** strong candidate for the next production queue.
- **75–84 · qualified:** useful; schedule after higher-priority gaps.
- **65–74 · rewrite:** intent or title needs material refinement.
- **0–64 · reject:** do not create a page without new evidence or a different angle.

Any failed hard gate caps the decision at `rewrite`; unrecoverable truth, safety, relevance, or duplication failures are `reject`.

## Refinement order

When rewriting, fix problems in this order:

1. search intent;
2. truthful content promise;
3. natural user language;
4. product relevance;
5. specificity, compelling strength, and one defensible highlight;
6. first-party evidence;
7. formatting details such as year or number.

Do not add `2026`, `最佳`, a large number, or emotional wording merely to increase the score.
