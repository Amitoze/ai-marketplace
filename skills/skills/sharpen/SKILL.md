---
name: sharpen
description: The exception path for vague requests. The preamble lists the drivers behind a request with a status of known, assuming or asking; this skill runs when a driver is `asking` — unknown and the answer flips on it — it asks with concrete values to pick from, builds the measure for evaluative terms, and records the confirmed reading to the user's vocabulary. Claude invokes it unprompted when any driver is `asking`; the user invokes /sharpen [prompt] to tighten a prompt before the answer.
---

Ask only when guessing is worse than asking. The preamble finds the
drivers and plugs assumed values in; this skill is what happens when a
driver cannot be assumed, and it makes sure the same question is never
needed twice.

## Config

- **Driver definition, trigger classes and the ask gate** live in the
  global context file `~/.claude/CLAUDE.md` (symlink to
  `ai-marketplace/context/CLAUDE.md`), section "Query preamble". That
  copy is canonical; do not restate it here.
- **Vocabulary section:** `## My vocabulary` in the same file. Entries
  load every session without a read.
- **Entry format:** `- **term** (domain, YYYY-MM-DD): reading. Not: alt.`
- **Question tool:** AskUserQuestion. It appends an "Other" option itself;
  that is the user's escape hatch — never add your own.
- **Caps:** up to four drivers in one call, one call per request.

## When it runs

- **Unprompted:** a driver in the preamble has status `asking`. The four trigger classes in the context file are
  ask-by-default; check **My vocabulary** first — a term defined there
  is not asked, the preamble says "using your definition of X".
- **On `/sharpen [prompt]`:** sharpen that prompt, or the most recent
  request if no argument. Here the restated request is the deliverable;
  stop and wait for "go".
- **Never** on follow-ups inside a thread already sharpened, or after the
  user says "just answer".

## Running it

1. **Start from the Drivers list**, not from the words. For each driver
   marked `asking`, decide whether one question settles it.

2. **Ask with values, not open questions.** One AskUserQuestion call
   batching every unknown driver. Two to four concrete values per driver,
   written in the user's situation, short labels (they are read aloud,
   not scanned). `multiSelect: true` where values can co-exist.
   - how the heat shows up → wake up sweaty / sheets warm on first touch /
     room is hot and bedding should help / several of these
   - what quality means → lasts longest / coolest through the night /
     softest on first touch / lowest upkeep
   - baseline (class 4) → its own question: what is in use now, what is
     liked about it, what would be missed.
   - for someone else → can you ask them / it is a surprise

3. **Build the measure** when a driver is an evaluative term. After the
   axes are picked, get an order (one more option in the same call, or
   infer from phrasing and confirm). Write it back in one line:
   "quality = cool through the night, then first-touch feel, then
   durability as tiebreaker."

4. **Echo "Other" verbatim.** The user's text is the value; repeat it
   back before continuing.

5. **Record to vocabulary.** Append one entry per confirmed reading of a
   *term* to `## My vocabulary`, scoped by domain. Record definitions
   only — not one-off facts (a budget, a colour, a mattress depth), and
   never a reading the user did not confirm.

6. **Restate and continue.** Two or three lines restating the request
   with the confirmed values. Unprompted: continue straight into the
   answer, with the preamble's drivers now reading `known: <value>`. On `/sharpen`:
   stop here.

## Rules

- Every question maps to a driver, and every driver asked flips the
  answer. A question whose answer would not change the output is
  padding; drop it.
- Values in the user's words and situation, never mechanism words.
  "Feels cool when you touch it vs stays cool at 3am", not "effusivity
  vs breathability".
- One round. If still unclear, proceed on stated assumptions.
- In a `plan/` project, offer to copy the measure into `DECISIONS.md`.

## Example

Request: "I want to buy the best bed sheets for someone that runs hot."

Preamble drivers: how the heat shows up for them; whether they can be
asked; what they sleep on now; budget. Classes 1, 3 and 4 fire and the
first three drivers are `asking`. One
AskUserQuestion with three questions: can you ask them (yes / surprise /
other); how it shows up (four values, multi-select, answered on their
behalf if known); what they sleep on now and like about it (free text
via Other). Budget stays `assuming: Australia, mid-range`.

Suppose the answers are "yes I can ask", "wakes sweaty", "sateen, loves
the cool feel getting in". Record:

`- **runs hot** (bedding, 2026-10-22): wakes sweaty overnight. Not: sheets warm to the touch.`

Restate: "Ranking sheet materials for a person who wakes sweaty,
currently on sateen they like the cool first touch of, mid-range in
Australia." Then answer, with first-touch feel as a scored column
because the baseline made it an axis, not a caveat.
