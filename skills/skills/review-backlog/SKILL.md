---
name: review-backlog
description: Review plan/backlog.md against the current state of the project — triage raw captures, re-stamp priorities, propose drops, promotions, and missing items. Use for /review-backlog, "review the backlog", "groom the backlog", after a phase gate or roadmap change, or when deciding what to tackle next.
---

Bring the backlog back in line with reality. Priority is a perishable
judgement — every review re-derives it from current project state and
re-stamps it with today's date. Analysis is yours; verdicts on drops
and promotions are the user's.

## Ground it first

Read, in order: `plan/backlog.md`, `plan/roadmap.md` (or
`plan/00-context.md` if no roadmap), `plan/architecture.md` if present,
`DECISIONS.md`, and `git log --oneline` since the last review stamp in
the backlog. No backlog file → say so and point at /backlog.

## Priority scale

- **P1** — candidate for the roadmap now: raise at the next /roadmap
  (or immediately, if Now is empty).
- **P2** — agreed valuable; sequenced behind the current cards.
- **P3** — keep, revisit **when \<named condition\>** — a P3 without a
  reopening condition is a drop that hasn't admitted it yet.

Every priority line carries a one-line rationale and the review date:
`Priority: P2 — valuable but nothing in Now depends on it (reviewed
2026-08-26)`.

## The review

1. **Triage the Inbox** — for each raw item: check the type, firm up
   the effort guess against the codebase as it exists today (drop the
   `?`), test the impact line against the roadmap ("serves nothing I
   can name" items must either find something to serve or be proposed
   as drops), assign a priority, and move it under `## Prioritised` in
   priority order.
2. **Re-review Prioritised** — for each existing item:
   - *Drift:* does the rationale still hold after roadmap/phase
     changes? Re-stamp or re-rank.
   - *Dependencies:* a `Needs:` that has since landed unblocks the
     item; a `Blocks:` that gained urgency raises it.
   - *Staleness:* an item ~3 months old that has never ranked above P3
     is a drop candidate — age is evidence about revealed priority.
   - *Duplicates / merges:* fold overlapping items together, keeping
     both provenance notes.
3. **Gap scan** — propose *new* items the backlog is missing: a
   DECISIONS.md deferral whose reopening condition has triggered, debt
   observed in recent commits, a spike implied by an assumption the
   dossier left thin, a bug mentioned in session but never captured.
   Tag any world-facts in your reasoning with evidence strength per the
   global conventions.
4. **Propose, then apply** — present one table: item · verdict
   (keep/re-rank/drop/promote/add) · one-line why. Drops and
   promotions are the user's call — never self-certify them. On
   approval:
   - Drops move to `## Dropped` with a dated one-line reason; a drop
     that might deserve resurrection gets a reopening condition, and a
     significant kill also gets a DECISIONS.md entry.
   - P1 promotions hand off to /roadmap to become cards (the backlog
     item then notes `→ card: <slug>` and moves to Dropped as
     `promoted`); a large `spike` may instead hand off to /frame.
5. **Report** — what moved and why, with file links. Note the review
   date at the top of the file (`Last reviewed: <date>`). Offer to
   commit; don't commit unasked.

## Rules

- Never rewrite an item's description or provenance while re-ranking —
  edit priority/effort/dependency lines only, unless merging
  duplicates.
- Every re-rank states what changed in the project to justify it; "felt
  more important" is not a rationale.
- Keep Prioritised strictly in priority order (P1 top) so the file
  reads as a queue.
- Don't let the review balloon into planning — how to build an item is
  /phase-plan's job once it becomes the Now card.
