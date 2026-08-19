---
name: step
description: Execute the next unchecked step of the active phase plan — state a prediction of what the diff will show, apply the edits, hand the user the checks, wait for their verdict against the prediction, tick the box, commit with observed results. One step per invocation. Use for /step, "do the next step", "advance the phase".
---

Execute exactly ONE step from `plan/phases/<active>.md` (the phase plan
/phase-plan wrote). Claude applies the edits; the user reviews the diff
and runs the checks. The prediction-before-diff discipline is the core:
reviewing against a stated expectation is active checking; reviewing
cold is proofreading, and humans are bad proofreaders of trusted
sources.

## Sequence

**0 · BASELINE.** `git status` first. A dirty tree means the last step's
work (or the user's own) isn't committed — stop and hand the commit
back to the user before touching anything. Claude's edits must be the
only thing between HEAD and the working tree, or diff review and
rollback both break.

**1 · LOCATE.** Read the phase plan; find the first unchecked step. If
the user named a different step, take that one. If all steps are
ticked, say so and point at /phase-done.

**2 · PREDICT — before any edit.** State, in plain words:
- which files will change, and which pointedly will NOT;
- what the diff will show, per file, at the level of "renderer gains a
  pure function; nothing below initControls() changes";
- a small flow diagram whenever the step creates or changes something
  other code touches (new config field, new function other stages
  call), arrows labelled with what flows;
- the check that will prove it worked, and what the user should expect
  to see.

**3 · APPLY.** Make the edits with Write/Edit. Match the surrounding
code's comment density, naming, and idiom. Anything tunable goes to
config. Carry SAFETY-type constraints named in the step. No edits
outside the prediction's scope — if mid-step you discover the scope was
wrong, stop, say so, and re-predict before continuing.

**4 · HAND OVER.** Tell the user: review the diff in the Source Control
panel AGAINST THE PREDICTION (does it show what step 2 said, and
nothing else?), then run the check — handed as copy-paste bash blocks,
one command per block, never chained with anything destructive. The
user runs the checks and reports; do not run them for the user unless
they explicitly say "you run it".

**5 · VERDICT — the user's, not Claude's.**
- **Pass:** tick the checkbox in the phase plan; suggest the commit
  (message includes the observed result, per convention). If the step
  scaffolded or completed an architecture component, **invoke the
  architecture skill** to flip its mark (🟦 → 🟧 / ◐ / 🟩 as the
  evidence supports).
- **Surprise:** diagnose WITH the user — offer an isolating tweak
  (exaggerate the parameter, log the value) before proposing the fix;
  record the finding in DECISIONS.md if it changed a judgement.
- **Rollback wanted:** `git restore .` for tracked files; `git clean
  -nd` shown and READ before any `git clean -fd` — separate blocks,
  never chained.

## Rules

- **One step per invocation.** The next step is a fresh /step — small
  review units are the point (defect detection collapses with diff
  size).
- Never blur two steps because the second "is small".
- If a step's learning is in the typing itself (the user wants to build
  it by hand), offer /walkthrough for that step instead — same plan,
  different delivery.
- If the phase plan's step is now wrong (the codebase moved under it),
  don't improvise a different design silently — flag it; small fixes
  amend the step, big ones go back to /phase-plan.
- Report outcomes faithfully: failed checks reported with their output,
  skipped verifications named as skipped.
