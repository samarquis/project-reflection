# Reflection report format

Use sections below when evidence exists. Omit empty decoration, not coverage gaps.

```markdown
---
project: <name>
repository: <absolute path>
github: <owner/repo or unavailable>
window_start: <ISO 8601>
window_end: <ISO 8601>
generated: <ISO 8601>
head: <SHA>
---

# Project Reflection - <date>

## Executive judgment
<Outcome-focused assessment.>

## Evidence coverage
- Chats: <count/range/limits>
- Issues: <count/range/limits>
- Pull requests and CI: <count/range/limits>
- Git activity: <count/range/limits>
- Code and docs: <areas reviewed/limits>

## Learning-loop effectiveness
- Lessons consulted before ticket work: <IDs and outcomes>
- Lessons promoted or adopted: <IDs and evidence>
- Lessons contradicted or retired: <IDs and reasons>
- Candidate lessons rejected: <candidate and failed gate>

## What succeeded
### <outcome>
- Evidence: <linked or exact identifiers>
- Why it worked: <cause, fact or labeled inference>
- Keep: <repeatable practice>

## What failed or remained unproved
### <outcome>
- Evidence: <identifiers>
- Cause: <root cause or unknown>
- Consequence: <impact>
- Change: <specific correction or experiment>

## Disproportionate effort
### <workstream>
- Evidence of cost: <timestamps, retries, churn, or rework>
- Value produced: <outcome>
- Friction source: <cause>
- Cheaper next approach: <action>

## Timeline and workstreams
<Concise chronological synthesis.>

## Documentation and code drift
<Contradictions, stale claims, missing decisions, or none found.>

## Durable lessons
| ID | Status | Lesson | Evidence | Canonical owner | Revisit when |
|---|---|---|---|---|---|
| ... | provisional/supported/adopted/contradicted/retired | ... | ... | ... | ... |

## Current risks and open loops
<Ranked, evidence-backed list.>

## Next actions
1. <small, testable action with expected evidence>

## Evidence ledger
| Claim | Source | Date | Confidence |
|---|---|---|---|
| ... | ... | ... | High/Medium/Low |

## Unknowns and coverage gaps
<Unavailable sources and effect on confidence.>

<Insert required quality assessment from quality-rubric.md.>
```

Write decisive prose. Preserve nuance where sources conflict. Avoid generic praise, blame, transcript dumps, and productivity scoring.
