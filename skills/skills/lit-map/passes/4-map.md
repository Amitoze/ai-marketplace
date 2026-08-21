# Pass 4 — Map

**Goal:** synthesize the extracted findings into the map, expose the
gaps, get the user's ratification, and write the digest back into the
dossier. The "cannot answer" list is a first-class output — it becomes
the user's interview questions.

**Sits on:** 3ie/Campbell evidence-gap-map practice (a grid of evidence
density + confidence as "a starting point for strategic evidence
production") · Webster & Watson: synthesize concept-by-concept, never
source-by-source.

## Output (map.md, completed)

- **Synthesis per review question**, concept-centric prose: what the
  body of included sources says, where they agree, where they conflict
  (conflicts stated, not averaged away). Every claim carries its tag;
  claims resting only on `/abstract-only` sources are flagged "needs
  full-text confirmation".
- **Evidence gap map:** grid of research domains × review questions.
  Each cell: source count + dominant confidence (peer-reviewed/full-text
  high; abstract-only or grey/caution low; empty = gap). ASCII grid,
  arrows and cells labeled in plain words.
- **What the literature cannot answer:** the questions with empty or
  low-confidence cells, phrased as askable interview/observation
  questions.
- **Revisit triggers** (recommended, not required): "re-run when X"
  notes — a pending trial, an annual review series, a dataset.

## Process

1. Read map.md's concept matrix and sources.md. Synthesize per
   question, tags carried through.
2. Build the gap map grid from the matrix — density and confidence come
   from the entries, never from impression.
3. Draft the cannot-answer list and revisit triggers.
4. **GATE (user): ratify the map.** Present synthesis, grid, and
   cannot-answer list. The user judges whether the map answers the
   protocol — and whether any finding changes the dossier's frame
   itself (if so: flag for /frame REVISE, don't absorb silently).
   Record ratification date in map.md.
5. **Write back into the dossier** (only after the yes):
   - §2 Evidence: distilled tagged findings + pointer to the artifacts;
     cannot-answer items appended as OPEN EVIDENCE REQUESTS.
   - §3 Landscape: what the literature says people currently hire /
     what services exist, where each falls short — as evidenced, tagged
     input (Pass 3 of /frame still interrogates it).
6. Prompt a dated DECISIONS.md entry if any project decision now rests
   on a mapped finding.

## Exit check

map.md holds per-question synthesis, the gap grid, the cannot-answer
list, and a dated user ratification; the dossier's §2/§3 carry the
digest with pointers; any frame-threatening finding has been flagged to
/frame rather than papered over.
