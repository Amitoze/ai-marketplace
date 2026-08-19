---
name: roadmap
description: Create or update plan/roadmap.md from a VALIDATED problem dossier — outcome root, assumption-retiring milestone ladder (RAT → Earliest Testable → Earliest Usable → Earliest Lovable), and Now/Next/Later cards. Use for /roadmap, "update the roadmap", "cut cards", after a dossier reaches VALIDATED, or after a phase gate teaches something that should reorder the cards.
---

Turn a validated dossier into `plan/roadmap.md`: the assumption register
made into a sequence of bets. The roadmap owns ORDER — sequence lives
here and nowhere else (never in filenames), so reordering is free.

No implementation content anywhere in this file, ever. Cards say what,
why, and how we'll know — never how. The how is /phase-plan's job, at
the last responsible moment, against the codebase as it exists that day.

## Inputs — ground it first

1. The dossier (`plan/dossiers/<slug>.md`): §4 outcome statements become
   the roadmap root; §5's ranked assumptions + kill conditions become
   the milestones. A dossier not yet VALIDATED gets sent back to /frame,
   not roadmapped around.
2. `plan/architecture.md` — what already exists (don't plan to build
   what's built).
3. `DECISIONS.md` — deferrals with reopening conditions; check none has
   triggered.

## Structure of plan/roadmap.md

```markdown
# Roadmap: <product/track name>
Outcome: <from dossier §4 — the one-sentence root>
Dossier: <link>          Last updated: <absolute date>

## Milestones            <!-- only for high-uncertainty tracks -->
M1 · RAT · <assumption id> | pass: <evidence that counts> |
  kill: <written BEFORE any work> | releases: <appetite for next chunk>
M2 · Earliest Testable · ...
M3 · Earliest Usable   · ...
M4 · Earliest Lovable  · ...

## Now                   <!-- exactly ONE card -->
## Next                  <!-- full cards -->
## Later                 <!-- one line each: slug + outcome sketch -->
```

Milestones are assumption checkpoints, not progress markers: each is
named for the assumption it retires, its pass/kill evidence is written
before work starts, and passing it releases the appetite for the next
chunk. A failed milestone stops spend cheaply — that is its job.

**Graceful degradation:** low-uncertainty tracks (e.g. a portrait
project where the bet is validated by the user's own experience) skip
the milestone ladder entirely — cards and their gates suffice. Don't
manufacture ceremony.

## The card template (~10 lines, one screen)

```markdown
### Card: <slug>
Serves: <milestone name, or "—" with the track named>
Outcome: <one sentence — the user-visible change when done>
Gate: <the observable check, and whose call it is>
Appetite: <time budget — bends scope, never the reverse>
Constraints: <cross-phase pressures only: safety caps, "must land as X">
Prereqs: <named preparatory work, only if THIS card justifies it>
Evidence riding on it: <which dossier assumption(s) its gate feeds>
```

Two failure tests, one per direction: a card naming a mechanism, file,
or technology is too fat (smuggled phase-plan content); a card
/phase-plan couldn't plan from (card + codebase alone) is too thin.

## Rules

- **Now holds exactly one card.** Direction changes happen between
  cards, where they cost nothing.
- **A card that can't name what it serves doesn't get cut** — the
  anti-pattern filter. Technical/preparatory work appears only as a
  named prereq on the card(s) it makes easy (preparatory refactoring),
  never as a free-floating "enabler".
- **Detail scales with column** (rolling wave): Later = one line;
  Next = full template; Now = full template + the phase plan it spawns.
- **Kill conditions and pass evidence are written before work starts** —
  written after, they are rationalisations.
- World-facts entering the roadmap carry evidence tags; resist milestone
  pass-evidence resting on `[my-synthesis]`.
- Big functions are sliced, not swallowed: first slice is the walking
  skeleton (thinnest end-to-end path), later slices fatten it.

## On update (not first creation)

Report what moved and why: cards reordered, promoted to Now, killed
(→ dated DECISIONS.md entry with reopening condition), milestones
passed/failed. Never silently rewrite a milestone's pass/kill evidence
— that change is itself a DECISIONS.md entry.

## Hand-offs

- A card entering Now → /phase-start cuts the branch, /phase-plan plans
  it.
- A milestone verdict → DECISIONS.md entry; a failed one stops the
  track and returns to /frame (REVISE) with the new evidence.
