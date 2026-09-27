# Work event format

```markdown
---
project: <name>
event: pr-merged | pr-rejected | deployment | incident | correction | milestone | other
occurred: <ISO 8601>
source: <URL or identifier>
head: <SHA or unavailable>
---

# <Event> Reflection

## Verified event
<Observed state, verification source, and distinction from intent.>

## Expected versus observed
- Expected: <outcome>
- Observed: <outcome or unknown>
- Gap: <difference and consequence>

## Evidence
- <current source identifiers>

## Prior learning
- Applied: <lesson IDs and effect, or none>
- Rejected: <lesson IDs and reason, or none>
- Effectiveness: <prediction met, missed, or not yet measurable>

## Candidate lessons
| Candidate | Gate result | Reason |
|---|---|---|
| <lesson> | promote / provisional / reject | <conditions> |

## Effort and friction
<Supported cost, retries, waiting, or no finding.>

## Open loop
<Smallest action, owner, and observable proof, or none.>

## Confidence and gaps
<Facts, inference, unavailable evidence.>

<Insert required quality assessment from quality-rubric.md.>
```
