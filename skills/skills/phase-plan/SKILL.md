---
name: phase-plan
description: Generate the implementation plan for the card in Now, at phase start, against the codebase as it exists today — sketch the design, contest the significant choices with options tables, get each ratified, record decisions, then write the data-flow trace and checkboxed step list that /step executes. Use for /phase-plan, "plan this phase", right after /phase-start.
---

Write the Tier-2 plan for the active card into
`plan/phases/<card-slug>.md`. This document is written at the last
responsible moment — never ahead of the phase — and is disposable after
merge: the durable outputs are the DECISIONS.md entries and the
architecture marks it leaves behind.

The plan is written AGAINST A RATIFIED DESIGN, not the first design that
comes to mind. Stages 1–4 exist to earn stage 5.

## Inputs — ground it first

1. The Now card in `plan/roadmap.md` (or the phase entry in `plan/` on
   pre-roadmap projects): outcome, gate, appetite, constraints, prereqs.
2. **The codebase as it exists today** — read the real files the phase
   touches; never plan from memory of them.
3. `plan/architecture.md` — current component map and states.
4. `DECISIONS.md` — standing choices this phase must not silently
   relitigate; deferrals whose reopening condition may have triggered.

## The five stages

**1 · SKETCH.** Candidate component diagram for this phase, text form:
new/changed parts marked `← NEW`, arrows labelled with what flows in
plain words, connections to existing modules shown. Short prose reading.

**2 · CONTEST.** Apply the significance filter: a component gets the
options treatment only if reversing the choice later would cost more
than a step. For each component passing the filter, produce an options
table:

```markdown
**Component: <name>** (why it's significant)
| Option | For | Against |
|---|---|---|
**Recommendation:** <option> — <one-sentence reason>.
Confidence: <high/medium/low>. **Your call.**
```

2–3 real options, trade-offs scored against the CARD's constraints and
appetite (not abstract elegance). Everything below the filter gets
decided silently inside the relevant /step, where reversal is one
commit.

**3 · RATIFY.** One component at a time; the user's call, never
self-certified. Present the recommendation to be pushed against. If the
user rejects all options, that is a finding — widen the search or
revisit the card.

**4 · RECORD.** Each ratified choice → dated DECISIONS.md entry
(rejected options included, evidence tagged). Then **invoke the
architecture skill** to add/update the affected components, marked
🟦 planned, linked to the entry date.

**5 · PLAN.** Now the plan itself, into `plan/phases/<card-slug>.md`:

- **Opening data-flow trace** of the artifact to be built (the trace
  skill's before-it's-built mode): what flows in, how it transforms,
  what appears where each new value is born. Design risks surface here
  before code hardens them — a value with no source, a config knob
  nothing reads.
- **The ratified design** — the stage-1 diagram as amended, plus
  pointers to the stage-4 DECISIONS entries.
- **Checkboxed steps.** Each step is the smallest VERIFIABLE increment:
  it ends with something runnable or observable, and states its check
  inline. Steps are sized for one /step session. Verifiability pressure
  shapes decomposition — prefer "stitcher first, trivially verifiable,
  then extract one piece at a time" over big-bang.
- **The gate**, copied from the card, with the reminder of whose call
  it is.

## Rules

- No implementation detail beyond this phase — pressure from future
  phases arrives as card constraints, not as plans.
- Anything tunable in the design goes to config, never hardcoded;
  SAFETY-type constraints from the card are named in every step they
  touch.
- Steps that the preview/served app can verify say what to look for,
  concretely; user-run checks are handed as copy-paste blocks.
- Honour the appetite: if the step list obviously exceeds it, say so
  now and cut scope with the user — not silently at step 7.

## Finish with

The path to the new phase plan, the DECISIONS entries written, the
architecture marks flipped, and the first unchecked step named — ready
for /step.
