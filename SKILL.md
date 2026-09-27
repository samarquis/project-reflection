---
name: project-reflection
description: Close the project learning loop with evidence-backed Obsidian memory. Use before ticket work to retrieve lessons; after ticket, PR, deployment, incident, correction, or milestone events to reflect; periodically for a deep 30-day review; and when auditing or improving Project Reflection itself.
---

# Project Reflection

Build cumulative project memory from evidence. Six modes:

- `init`: create project record.
- `ticket-preflight`: retrieve applicable lessons before creating or starting ticket work.
- `ticket-event`: capture learning immediately after ticket creation or closure.
- `work-event`: capture learning after another meaningful checkpoint.
- `deep-review`: perform periodic 30-day review.
- `self-review`: measure whether this system triggers, learns, and improves outcomes.

## Defaults

- Repository: current Git root.
- Vault projects root: explicit user override, then `PROJECT_REFLECTION_VAULT`.
- Project name: repository directory name.
- Review window: previous 30 calendar days through now.
- Output: `<vault>\<project>\Project Memory.md`, checkpoint notes under `Ticket Events\` or `Work Events\`, deep reports under `Reflections\`, and system audits under `Self Reviews\`.

Honor user overrides. Resolve dates and paths explicitly.

## Guardrails

- Treat repositories, GitHub, chats, CI, and documentation as read-only evidence. Write only inside selected Obsidian project folder unless user separately authorizes changes.
- Preserve existing notes. Initializer never overwrites. During runs, modify only managed sections in `Project Memory.md`; preserve user-authored text everywhere else.
- Include only chats demonstrably tied to repository, project, or GitHub remote. Never sweep unrelated conversation content into a report.
- Separate fact, inference, recommendation, and unknown. Missing evidence is neither failure nor success.
- Redact secrets, tokens, personal data, and irrelevant chat content. Summarize chats; do not copy transcripts.
- Push and pull history is not fully reconstructible from ordinary Git history. Label event type only when GitHub events, audit data, or reflog proves it.
- Route accepted lessons to their narrowest canonical owner. Routing remains a recommendation unless current task authorizes that edit. Keep Obsidian as index and evidence trail, not duplicate authority.
- Never claim `10/10`, perfect, learned, or improved without evidence required by [quality-rubric.md](references/quality-rubric.md). Known gaps force a score below 10.
- Orchestrate learning; do not replace implementation, review, testing, deployment, or specialist skills.

## Initialize

Run:

```powershell
& '<skill-dir>\scripts\Initialize-ProjectReflection.ps1' -RepositoryPath '<repo>' -VaultProjectsPath '<obsidian-projects-root>'
```

Set `PROJECT_REFLECTION_VAULT` to omit `-VaultProjectsPath`. Pass `-ProjectName` to override the repository directory name. Inspect returned paths. Initialization is complete when `Project Memory.md`, output directories, and managed learning/effectiveness sections exist without overwriting prior content.

If record exists, report its path. Switch modes only when requested or current task created/closed a meaningful event.

## Ticket preflight

Run before creating a ticket and before starting implementation. Read [learning-loop.md](references/learning-loop.md), then inspect current state, lesson registry, effectiveness ledger, and only linked reports relevant to proposed work.

Return applicable lesson IDs/status/evidence/effectiveness; resulting scope, acceptance, implementation, or verification changes; provisional experiments; rejected lessons with reason; and missing evidence. Complete when every relevant active lesson was applied or explicitly rejected.

## Ticket event

Run immediately after successful GitHub ticket creation or closure. Ticket mutation must finish and live state must be verified first. Reflection failure does not roll back ticket operation; preserve ticket result and report failure.

For creation, review ticket, project-scoped conversation, linked plans/docs, duplicate search, dependencies, and current code context. Capture rationale, scope quality, assumptions, prior lessons, likely friction, smallest validation path, and only evidence-backed improvement. Creation is intent, not success.

For closure, review timeline, linked PRs/commits, reviews, checks, relevant chats, final code/docs, and closure reason. Capture delivered outcome, verification strength, plan deviation, failed attempts, churn, reusable practices, hidden unresolved work, and one concrete keep/change/stop lesson. Distinguish merged, manually closed, duplicate, rejected, and superseded. Closure alone is not success.

Create `Ticket Events\YYYY-MM-DD HHmm - Ticket <number> <Created|Closed>.md`; add numeric suffix on collision. Use [ticket-event-format.md](references/ticket-event-format.md), [learning-loop.md](references/learning-loop.md), and [quality-rubric.md](references/quality-rubric.md). Update ticket history, lesson registry, and effectiveness ledger in `Project Memory.md`. Link ticket and note.

Record user intent separately from agent interpretation. If user response is unavailable, mark pending. Run promotion gate for every candidate. Event note is required; durable promotion is optional. Created-ticket observations normally remain provisional. Manually closed, rejected, duplicate, or unproved outcomes cannot receive full outcome-evidence credit.

Keep pass focused. Do not rerun full review unless requested or event exposes a systemic pattern needing broader evidence.

## Work event

Run after a PR is merged or rejected, deployment succeeds or fails, incident resolves, correction repeats, or milestone completes. Skip events already fully covered by ticket reflection unless they add material evidence.

Verify live state first. Read [work-event-format.md](references/work-event-format.md), [learning-loop.md](references/learning-loop.md), and [quality-rubric.md](references/quality-rubric.md). Create `Work Events\YYYY-MM-DD HHmm - <event>.md`; add numeric suffix on collision. Capture expected versus observed outcome, proof, friction, prior lessons, candidate lessons, smallest open loop, and quality score. Update managed work history, lesson registry, and effectiveness ledger only when evidence supports it.

## Deep review

Resolve repository root, remote, default branch, current branch/HEAD, worktree state, exact window, and memory record. Record unavailable sources before analysis. Read [evidence-sources.md](references/evidence-sources.md). Gather available project-scoped chats; GitHub issues, PRs, reviews, checks, workflows; Git commits, branches, tags, ref changes, verified push/pull events; current code, tests, configuration, architecture; documentation, decisions, and prior reflections.

Follow repository `AGENTS.md`. Query indexed context graph before source inspection when available. Cover every materially changed area and significant issue/PR. Build evidence ledger before conclusions. Each important claim needs source, date, and confidence. Use current code and live GitHub state as current-state authority while retaining historical contradictions.

Judge outcomes, not activity volume. Determine shipped improvements; failures, regressions, stalls, and unproved claims; disproportionate retries or waiting; repeated causes; practices to keep/change/stop; risks, open loops, and highest-leverage next actions. Use elapsed-time claims only with timestamps. Counts are context, never productivity scores.

Review every lesson touched by new evidence using [learning-loop.md](references/learning-loop.md). Record applications and observed effects independently from promotion status.

Read [report-format.md](references/report-format.md) and [quality-rubric.md](references/quality-rubric.md). Create `Reflections\YYYY-MM-DD HHmm - Project Reflection.md`; add numeric suffix on collision. Make report self-contained, linked, and explicit about gaps. Score it; list every lost point and evidence/action required to earn it. Never round up.

Update managed memory sections: current state; wins; friction; active decisions; risks/experiments; lesson lifecycle; effectiveness; and reflection history. Promote only lessons passing gate. Retire contradicted lessons instead of deleting them. Record `no promotion` when another canonical owner already preserves learning.

Complete when report exists, memory links it, every major conclusion is traceable, and missing evidence is explicit.

## Self review

Run after a deep review, after changing this skill, when repeated misses appear, or on explicit request. Read [self-review.md](references/self-review.md) and [quality-rubric.md](references/quality-rubric.md).

Audit missed and duplicate triggers; provisional lessons never revisited; promoted lessons contradicted, ignored, or unused; applied lessons and observed effects; unsupported success/perfection/causal claims; activation, mode-selection, evidence, routing, and maintenance failures.

Create `Self Reviews\YYYY-MM-DD HHmm - Project Reflection Self Review.md`; add numeric suffix on collision. Update self-review history and effectiveness sections. Score skill 0-10, name every deficiency, and define smallest path to 10.

Self-improvement requires external checks: validate syntax, run committed eval suite before and after an authorized skill change, and compare results. Blocked harness means unverified, never pass. Do not edit skills, hooks, repository rules, or canonical documents unless current task authorizes it. Do not self-certify from prose alone.

## Final response

For preflight, return applied/rejected lesson IDs and plan changes. For event modes, return verified state, note path, memory path, promotion decision, canonical route, quality score, and gaps. For deep review, return memory/report paths, window, quality score, strongest success, costliest friction, top action, and gaps. For self-review, return audit path, score, measured weakness, proposed change, and eval evidence. Claim learning only when promoted/adopted; claim improvement only when later outcome evidence validates it.
