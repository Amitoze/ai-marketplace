---
name: sharpen
description: The exception path for vague requests. The preamble (Reading / Assumptions / Open) handles ordinary ambiguity by stating assumptions; this skill fires only when a term falls in one of four trigger classes where guessing would produce a materially different answer — then it asks with concrete readings to pick from, builds the measure, and records the confirmed reading to the user's vocabulary. Claude invokes it unprompted when a trigger class fires; the user invokes /sharpen [prompt] to tighten a prompt before the answer.
---

Ask only when guessing is worse than asking. The default for an unclear
term is the preamble's Assumptions list; this skill is the exception that
turns an assumption into a question, and then makes sure the same question
is never needed twice.

## Config

- **Vocabulary section:** `## My vocabulary` in the global context file
  `~/.claude/CLAUDE.md` (symlink to `ai-marketplace/context/CLAUDE.md`).
  Entries load every session without a read.
- **Entry format:** `- **term** (domain, YYYY-MM-DD): reading. Not: alt.`
- **Question tool:** AskUserQuestion. It appends an "Other" option itself;
  that is the user's escape hatch — never add your own.
- **Caps:** three terms per pass, one pass per request.

## Trigger classes (fire on any of these; otherwise assume and proceed)

1. **Evaluative superlative with no measure.** "best", "ideal", "quality",
   "good enough", "right one" — the word hides a scoring rule.
2. **"Order by X" or "rank by X" with X undefined.** Same hidden rule,
   made explicit as a sort key.
3. **Personal-state claim used as an input.** "I run hot", "I'm
   time-poor", "I'm not technical", "this is urgent" — a fact about the
   user that the answer will optimise around, with several readings.
4. **A comparison or switch with no baseline.** "Should I move to X",
   "which is better" — with nothing said about what they have now and
   what they like about it.

Second gate, applied after a class matches: *would the other reading
change my answer materially?* If every reading lands on the same answer,
do not ask — state the reading in Assumptions and continue.

Before asking, check **My vocabulary**. A term already defined there is
not asked; the preamble says "using your definition of X".

## Running it

1. **Name the terms doing the work**, at most three, one line each on
   why they decide the answer.

2. **Ask with readings, not open questions.** One AskUserQuestion call
   batching all terms. Two to four concrete readings per term, written in
   the user's situation, short labels (they are read aloud, not scanned).
   `multiSelect: true` where readings can co-exist.
   - "runs hot" → wake up sweaty / sheets feel warm to touch / room is hot
     and bedding should help / several of these
   - "best quality" → lasts longest / coolest through the night / softest
     on first touch / lowest upkeep
   For trigger class 4, add the baseline as its own question: what they
   use now, what they like about it, what they would miss.

3. **Build the measure** when the term is evaluative. After the axes are
   picked, get an order (one more question, or infer from phrasing and
   confirm). Write it back in one line: "quality = cool through the
   night, then durability, then first-touch feel as tiebreaker."

4. **Echo "Other" verbatim.** If the user picked Other, their text is the
   definition; repeat it back before continuing.

5. **Record to vocabulary.** Append one entry per confirmed reading to
   `## My vocabulary` in the context file, scoped by domain. Do not record
   a reading the user did not confirm. Do not record one-off facts that
   are not definitions (a measurement, a preference for a colour).

6. **Restate the sharpened request** in two or three lines. On an
   unprompted fire, continue straight into the answer with the preamble
   reflecting the confirmed readings. On `/sharpen`, the restatement is
   the deliverable: stop and wait for "go".

## Rules

- One pass. If it is still unclear after one round, proceed on stated
  assumptions rather than asking again.
- Every question must map to a branch in the answer. A question whose
  answer would not change the output is padding; drop it.
- Readings in the user's words and situation, never in mechanism words.
  "Feels cool when you touch it vs stays cool at 3am", not "effusivity vs
  breathability".
- The skill never fires on follow-ups inside a thread already sharpened,
  or after the user says "just answer".
- In a `plan/` project, offer to copy the measure into `DECISIONS.md`.

## Example

Request: "My body runs hot, what is the best sheet material, order by
quality."

Classes 1, 2 and 3 fire; class 4 fires too because it is a buying
decision with no baseline. One AskUserQuestion with three questions:
how "hot" shows up (four readings, multi-select), which axes define
quality (five readings, multi-select), and what they sleep on now and
like about it (free text via Other). Suppose they pick "wake up sweaty",
axes "cool through the night, first-touch feel, durability", and say
"sateen, I love how cool it feels when I get in".

Record:
`- **runs hot** (bedding, 2026-10-22): wakes sweaty overnight. Not: sheets warm to the touch.`
`- **quality** (bedding, 2026-10-22): cool through the night, then first-touch feel, then durability.`

Preamble on the answer then reads "using your definition of runs hot"
and "quality per your ranking", and the ranking table carries a
first-touch column because it is now a scored axis, not a caveat.
