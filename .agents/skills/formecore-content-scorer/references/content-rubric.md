# Content quality and AI-pattern rubric

## Hard gates

Any failed gate makes the result `blocked` or `rewrite` regardless of points.

1. **Truth:** no material factual error, invented price, unsupported result, or
   fabricated hands-on experience.
2. **Promise match:** the body answers the title's primary search intent.
3. **Evidence:** consequential current claims have traceable sources.
4. **Disclosure:** a material commercial relationship, including FORMECORE's
   ownership of Play.formecore.com, is visible where it could affect trust.
5. **Claim safety:** no treatment, productivity, learning, fitness, financial,
   or health guarantee unsupported by evidence.
6. **Reader usability:** the main answer is accessible on mobile and is not
   hidden inside an image, script-only chart, or vague teaser.
7. **Originality boundary:** the article does not copy substantial competitor,
   source, or copyrighted text.

## Content quality: 100 points

### 1. Search intent and direct answer — 12

- 11–12: answers one recognisable query near the top and sustains it.
- 7–10: useful answer, but delayed, broad, or partly mixed.
- 1–6: the subject is present but the reader's decision remains unclear.
- 0: does not answer the promised query.

### 2. Depth and decision consequences — 13

Reward explanation of why a difference matters, trade-offs, limitations,
failure cases, and what changes the reader's choice. Do not reward length.

### 3. Necessary breadth and promise coverage — 9

Reward complete coverage of the title's promised dimensions. Deduct for missing
sections and for unrelated padding added only to look comprehensive.

### 4. Evidence and concrete specificity — 12

Reward verified prices, dates, platforms, examples, screenshots, methods,
limitations, and direct source links. Deduct for vague attribution or old data.

### 5. Insight and original synthesis — 10

Reward a useful comparison model, a non-obvious distinction, first-party data,
or a conclusion built from sources rather than a rewritten feature list.

### 6. Structure and reading flow — 10

Reward answer-first organisation, useful headings, proportionate sections,
scannable tables, transitions that express a real relationship, and a clear
ending. Deduct for repeated introductions or conclusions after every section.

### 7. Natural expression and sentence craft — 10

Reward concrete nouns and verbs, varied but controlled sentence length,
audience-appropriate language, and consistent locale. Deduct for stiff keyword
phrasing, mechanical parallelism, mixed scripts, or conversational cosplay.

### 8. Rhetoric and narrative usefulness — 8

Reward analogy, contrast, scene, pacing, question, or humour only when it helps
the reader understand or keep moving. Deduct for hype, false suspense,
overwritten metaphors, dramatic fragments, and emotional manipulation.

### 9. Trust, fairness, and editorial judgement — 9

Reward visible disclosures, fair comparison criteria, acknowledgement of
limitations, distinction between fact and judgement, and proportional claims.

### 10. SEO/GEO extractability — 7

Reward clear entities, answer passages, comparison tables, FAQ only when real
questions exist, descriptive links, citations, metadata, and structured data
that matches visible content. Deduct for keyword stuffing or schema inflation.

## AI-writing-pattern risk: 100 points, lower is better

This score describes visible editing risk. It is not the probability that AI
wrote the text. Add risk only when a pattern is present, and weigh density,
repetition, and severity.

| Risk group | Maximum | What raises risk |
|---|---:|---|
| Staging instead of stating | 15 | `not X but Y`, staged honesty, fake objections, one-line closers |
| Mechanical rhythm | 15 | forced triads, repeated openings, identical paragraph shapes, dashes everywhere |
| Inflation and sales language | 15 | importance claims without facts, hype, borrowed authority, generic praise |
| Generic vagueness | 15 | abstract benefits, weak subjects, unsupported qualifiers, no concrete nouns |
| Template formatting | 10 | decorative bold labels, emoji headings, repeated card formulas, excessive rules |
| Repetition and predictability | 10 | each section makes the same moves in the same order with no editorial reason |
| Chat or drafting residue | 10 | greetings, offers to continue, method narration, knowledge-cutoff disclaimers |
| Unsupported persona or experience | 10 | invented first-person testing, fabricated reactions, fake quotes or intimacy |

Risk guidance:

- 0–15: little pattern risk; normal editing may still help.
- 16–25: mild; publishable when quality gates pass.
- 26–45: noticeable; edit the repeated structures and vague passages.
- 46–65: strong; prose needs a substantial rewrite.
- 66–100: dominant template or fabrication risk.

One occurrence of a weak pattern does not justify a large penalty. Repeated
high-strength patterns, or one fabricated experience, do.

## Decision bands

- `publish-ready`: quality 85–100, risk 0–25, all gates pass.
- `edit`: quality 70–84 or risk 26–45, all truth and safety gates pass.
- `rewrite`: quality below 70 or risk above 45, without an unresolvable block.
- `blocked`: a hard gate cannot be resolved from the available evidence.

## Re-score discipline

Use the same evidence date and rubric for before-and-after comparison. Report
dimension deltas, not only a new total. A revision that merely adds length,
headings, or synonyms should not gain points unless the reader's answer improves.
