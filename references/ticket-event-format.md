# Ticket event format

```markdown
---
project: <name>
event: ticket-created | ticket-closed
ticket: <number>
ticket_url: <url>
occurred: <ISO 8601>
head: <SHA or unavailable>
---

# Ticket <number> <Created|Closed> Reflection

## Event
<Verified ticket state and reason.>

## Intent and interpretation
- User intent: <exact wording or faithful summary>
- Agent interpretation: <assumptions and success criteria>
- User response: <response, Unknown, or Pending after delivery>
- Alignment gap: <difference and effect, or none found>

## Memory preflight
- Applied lessons: <lesson IDs and effect, or none>
- Rejected lessons: <lesson IDs and reason, or none>

## Outcome or intent
<Created: intended outcome. Closed: delivered, rejected, duplicate, superseded, or otherwise resolved outcome.>

## Evidence
- <ticket, PR, commit, check, code, documentation, or chat identifier>

## Candidate lessons
| Candidate | Gate result | Reason |
|---|---|---|
| <lesson> | promote / provisional / reject | <failed or passed conditions> |

## Effort and friction
<Observed churn, delays, failed approaches, uncertainty, or no supported finding.>

## Memory update
- Lesson ID and status: <ID/status or none>
- Canonical owner: <current or proposed owner>
- Revisit when: <condition or not applicable>
- Decision: <promoted, provisional, adopted, rejected, or no promotion with reason>

## Open loop
<Smallest remaining action and proof, or none.>

## Confidence and gaps
<Facts, inference, unavailable evidence.>

<Insert required quality assessment from quality-rubric.md.>
```

Created-ticket notes assess decision quality, not delivery. Closed-ticket notes require outcome proof and name closure type.
