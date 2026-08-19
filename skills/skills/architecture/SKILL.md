---
name: architecture
description: Maintain the living architecture description (plan/architecture.md) — three-level ASCII diagrams (concepts → pipeline → per-stage) with per-component status marks. Run for /architecture, "update the architecture", AFTER a ratified design decision changes the design (phase-plan stage 4), and AFTER work changes a component's state — a step scaffolds or completes a component, a phase gate passes, plan-sync flips checkboxes.
---

Produce a single living document, `plan/architecture.md`, holding the
project architecture at three zoom levels in plain-text (ASCII) diagrams.
It is **idempotent**: create the file if absent, otherwise refresh it in
place so it always matches the latest state of `plan/`, `DECISIONS.md`,
and the code. (Migration: if `plan/diagrams.md` exists and
`plan/architecture.md` does not, `git mv` it first — same file, promoted
role.)

This file is the **living architecture description** — current truth,
updated in place. It pairs with `DECISIONS.md`, the **decision log** —
append-only, dated, the why behind each choice. Never blur the two:
history lives in DECISIONS.md, the present lives here. Components whose
shape came from a ratified choice carry a pointer to their DECISIONS.md
entry date; the entry names the component back.

No Mermaid, no images — ASCII diagrams that render anywhere.
Representation priority: **diagram > table > minimal prose**.

## When this skill runs (not only on request)

1. **A design decision is ratified** (phase-plan stage 4, or any ad-hoc
   architecture call recorded in DECISIONS.md): add/update the affected
   components, mark them 🟦 planned, link the decision date.
2. **Work changes a component's state:** a /step scaffolds or completes
   a component (◐ / 🟧 → 🟩 candidates), a phase gate passes
   (phase-done), plan-sync flips checkboxes. Flip only the markers the
   evidence supports.
3. **Explicit invocation** (/architecture) or after any plan
   restructure.

phase-plan and step invoke this skill directly at those moments — treat
their call as authoritative about WHICH component changed, but still
derive the new state from the source of truth below.

## Ground it first — read the source of truth, don't recall it

Every status marker must be derived, not remembered:

1. `plan/00-context.md` (or `plan/roadmap.md` where it exists) — status
   table / card columns, the arc.
2. The phase files — ticked checkboxes and gate results tell you what
   is actually built vs specced.
3. The fast-follow / deferred register, if present.
4. `DECISIONS.md` — gate passes, "tried and rejected", anything that
   flips a marker.

If a stage's state is genuinely ambiguous, mark the nearest state and
say so in a one-line note rather than guessing confidently.

## The status key — Levels 2 and 3 ONLY

Level 1 is conceptual and timeless: **no status markers on it.**
Levels 2 and 3 open with this key and use it on every stage:

```
🟩 Built       — code exists in the repo, its gate/verification passed
🟧 In progress — the active phase is currently building it
◐  Scaffolded  — code exists but has not been verified yet
🟦 Planned     — ratified design on the critical path, not yet started
🟨 Proposed    — evaluated, deferred OFF the critical path
```

Emoji are the colour coding (ANSI doesn't render in the target medium).
Keep the key block identical every time so a reader learns it once.

## The three levels

**Level 1 — the whole idea (NO key).** The biggest concepts and how they
flow into each other. Three or four boxes, plain nouns, one-line
captions. Timeless — it does not change when a phase ships.

**Level 2 — the pipeline (keyed).** The main data path as a single
annotated spine, stage by stage, naming the real files/modules each
stage lives in. Attach 🟨 proposed extensions at the stage each belongs
to; follow with a compact table keying each 🟨 item to where it
attaches, what it adds, and its revisit-trigger.

**Level 3 — per-stage deep dive (keyed).** One focused
`inputs → transform → outputs` diagram per stage, headed with its status
marker and (where applicable) its DECISIONS.md pointer, arrows carrying
plain-language cargo labels. For 🟦 planned stages, draw the *intended*
shape from the ratified design and say it's not built.

## Writing / updating the file

- Header block: one line noting the file is maintained by
  `/architecture`, that the source of truth is `plan/` + `DECISIONS.md`,
  and a **Last updated** date (absolute, never relative).
- On **update**: regenerate from the current source of truth, then
  report to chat **what changed since the previous version** — which
  markers flipped (e.g. "stitcher 🟦 → 🟧"), which components were
  added, which 🟨 items moved.
- Arrows labelled with what actually flows; jargon defined at first
  use; prose kept to what diagrams and tables can't carry.

## Finish with

- The path and the marker changes since last run.
- Offer to commit `plan/architecture.md` with a message noting the
  state it now reflects. Pairs naturally with plan-sync — run this
  right after it, so the diagrams reflect the freshly-synced plan.
