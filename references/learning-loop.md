# Learning loop

Use this reference for ticket preflight, ticket-event promotion, and deep-review lesson maintenance.

## Retrieve before work

Search `Project Memory.md` by ticket terms, affected component, failure symptom, tool, and verification path. Follow evidence links for plausible matches. Apply `supported` and `adopted` lessons when still relevant. Treat `provisional` lessons as experiments. Exclude `contradicted` and `retired` lessons while preserving their history.

Every relevant lesson must be applied or rejected with reason. Retrieval is complete when resulting ticket or execution plan names concrete scope, acceptance-criteria, implementation, or verification changes.

Record each application in the lesson-effectiveness ledger. State predicted effect before work; later record success, failure, or unknown with evidence. Application count alone does not prove value.

## Promotion gate

A candidate lesson earns `supported` only when all conditions pass:

1. **Non-obvious:** work revealed information not cheaply available from current code, tests, or authoritative docs.
2. **Grounded:** evidence proves outcome or repeated pattern. Ticket creation alone can support only a provisional observation.
3. **Durable:** likely useful beyond current incident and stable long enough to reuse.
4. **Material:** changes future scope, implementation, validation, safety, or effort.
5. **Canonical gap:** existing test, code, documentation, rule, skill, or memory does not already preserve it.
6. **Actionable:** states trigger plus changed behavior or verification.

Record rejected candidates and failed condition in event note. Zero promotions is healthy.

## Lifecycle

- `provisional`: plausible observation from one event; include `revisit_when`.
- `supported`: promotion gate passed through repeated or independently verified evidence.
- `adopted`: supported lesson encoded in canonical owner and verified there.
- `contradicted`: later evidence disproves lesson; retain replacement link.
- `retired`: no longer relevant or superseded; retain reason.

Use IDs `L-YYYYMMDD-NN`, incrementing within date. Update existing lesson instead of creating semantic duplicate. Each entry needs evidence, status, canonical owner, and revisit condition where relevant.

## Canonical routing

Choose narrowest owner:

- runtime invariant or regression: code and test;
- architecture or product decision: ADR or project documentation;
- team execution rule: repository `AGENTS.md`, runbook, or workflow;
- reusable agent procedure: relevant skill;
- personal cross-tool preference or evidence index: Obsidian memory.

Project Memory retains lesson ID, status, summary, evidence links, and canonical pointer. It does not copy full canonical rule. Editing owner requires task authorization; otherwise record proposed route.

## Effectiveness

Track lifecycle status separately from outcome:

- `Applied`: count of evidenced uses.
- `Successful`: uses where predicted material benefit occurred.
- `Failed/unknown`: contradicted uses or uses not yet measurable.
- `Last applied` and `Last validated`: date or evidence link.

Do not promote because counts increased. Contradict or retire lessons whose observed effects repeatedly fail. Preserve unknown separately from failure.

## Interpretation check

For ticket events, record separately:

- user's stated intent;
- agent's interpretation, assumptions, and success criteria;
- user response when available;
- alignment gap and effect on work.

Promote recurring interpretation gaps only when promotion gate passes.
