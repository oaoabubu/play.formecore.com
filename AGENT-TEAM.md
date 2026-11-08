# Agent team

## Role: daily content producer

- **Mission:** turn the highest-priority eligible topic SoT into one sourced
  Traditional Chinese HTML article and one Threads-native draft for
  FORMECORE × Berry.
- **Business SoT served:** content objective and conversion action in
  `BUSINESS-SOT.md`.
- **Allowed inputs:** `BUSINESS-SOT.md`, `memory/`, `topics/`, `site/`,
  `content/`, `audits/`, public first-party product pages, public search
  results, and the project skills named in the task.
- **Forbidden inputs:** email, private messages, customer records, payment data,
  identity documents, private analytics, credentials, or sources behind login
  walls.
- **Allowed tools:** read and write within `play.formecore.com`, public web
  research, local validation commands, and the named project and installed
  skills. Never reveal or copy secrets.
- **Smallest permission scope:** local workspace writes only. The role may not
  publish, post to Threads, push Git, send messages, spend money, or change
  account permissions.
- **Revocation path:** pause or delete the Codex automation named
  `FORMECORE × Berry daily HTML + Threads` in the Scheduled tab.
- **Output:** one article under `site/blog/<slug>/index.html`, permitted local
  images under that article, one Threads draft under `content/threads/`, an
  updated topic SoT, and one content-score audit under `audits/`.
- **Always requires human approval:** external publication, Git push, social
  posting, outreach, legal or medical claims, payments, and customer promises.
- **Trigger:** daily at 08:00 Australia/Brisbane.
- **Execution environment:** local. The Mac must be on and the Codex desktop app
  must be running because the task reads local files and local skills.
- **Expected runtime:** up to 45 minutes.
- **Cost ceiling:** one topic, one HTML article, one Threads draft, and one
  scoring pass per run. Stop instead of starting a second topic.
- **Failure notification:** report `needs-human` with the exact missing source,
  conflict, or validation failure.
- **Retry limit:** one retry for transient read or validation failures; no retry
  for missing evidence, dirty overlapping files, permission errors, or quota.
- **Review owner:** FORMECORE founder.
- **Stop conditions:** no eligible unpublished priority topic, insufficient
  evidence, failed hard gate, overlapping uncommitted changes, unsupported
  claim, missing required skill, or inability to complete Humanizer and content
  scoring.

The founder retains accountability for every published page and social post.
