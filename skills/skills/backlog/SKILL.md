---
name: backlog
description: Capture an idea into the active project's plan/backlog.md — typed, structured, zero questions asked. Use for /backlog <thought>, "backlog this", "add to the project backlog", or to read it back ("what's in the backlog?"). For ideas not tied to the current project, use /idea instead.
---

Project-scoped capture with zero friction: the user fires a thought and
moves on. Structure it yourself; never ask questions during capture —
wrong guesses are cheap, lost ideas are not. The backlog is the inbox
*below* the roadmap: items wait here until /review-backlog prioritises
them and /roadmap cuts cards from the survivors.

## Config

- **Backlog file:** `plan/backlog.md` in the active project. If the
  project has no `plan/` directory, say so and offer /idea (global
  inbox) instead — don't manufacture a plan/ dir for one thought.
- **Types (fixed, pick exactly one):** `feature` (user-visible new
  value) · `bug` (something built behaves wrongly) · `debt` (invisible
  structural work: refactors, architecture, infrastructure, tooling) ·
  `spike` (exploratory: a question to answer or an approach to try
  before committing). These follow Kruchten's backlog quadrants, with
  architecture folded into `debt` — right for solo projects.
- **Effort scale:** S / M / L — S ≲ one session, M ≈ a step or two of a
  phase, L ≈ its own phase. A capture-time estimate is a guess: write
  it with a trailing `?` (e.g. `M?`); /review-backlog firms it up.

## Capture (`/backlog <raw thought>`)

1. If the backlog file doesn't exist, create it starting with this
   skeleton, then continue — never overwrite an existing file:

   ```markdown
   # Backlog

   Captured by /backlog, prioritised by /review-backlog.
   Inbox = raw, unreviewed. Prioritised is ordered: P1 = raise at next
   /roadmap · P2 = agreed valuable, sequenced behind current cards ·
   P3 = keep, revisit when the named condition triggers.

   ## Inbox

   ## Prioritised

   ## Dropped
   ```

2. Build one entry from the raw thought:
   - **Title:** ~5 words, concrete, written by you.
   - **Description:** 1–3 sentences (hard max 100 words). Keep the
     user's own words where possible; keep what prompted the idea if
     they mentioned it — provenance helps at review.
   - **Impact:** one sentence — what it unlocks, naming the roadmap
     outcome, milestone, or goal it serves. If you can't name one,
     write `serves nothing I can name — challenge at review`; that is
     signal, not failure.
   - **Effort:** S/M/L guess with `?`, plus a one-line reason.
   - **Needs / Blocks:** only when a dependency is actually evident —
     `Needs:` names work that must land first, `Blocks:` names work
     waiting on this. Omit the line entirely when empty.
   - **No priority.** Priority is a review-time judgement against
     current project state; capture never assigns it.

3. Insert the entry directly under `## Inbox` (newest first), in
   exactly this format:

   ```markdown
   ### Offline export of journal entries
   `feature` · added 2026-08-26 · effort M? — one serializer over the
   existing store
   Users can take their data out. Came up while writing the
   trust-model section of the dossier.
   Impact: removes the lock-in worry; serves the trust/retention
   outcome.
   Needs: stable entry schema (02-ontology).
   ```

4. Echo the entry back verbatim so a misclassification can be fixed
   with one word ("that's debt") — apply such a correction by editing
   the entry in place. Do not commit; capture is a working-tree edit
   like any other plan change.

## Read-back ("what's in the backlog?")

Read the file and present titles + one-liners grouped by section, not
the raw markdown. Filter by whatever they asked (type, priority,
keyword). If the Inbox has items older than ~a month, mention that a
/review-backlog is due.

## Rules

- Capture is append-only and edit-in-place; never reorder, rewrite, or
  delete other entries — that is /review-backlog's job, with the user.
- Never ask questions before writing the entry.
- If a near-identical item already exists anywhere in the file, say so
  and point at it instead of appending a duplicate.
- Don't editorialize on quality during capture — this is an inbox, not
  a review.
