---
name: sharpen
description: Turn a vague request into an explicit one before answering it — name the terms doing the work, offer concrete readings the user can pick from, build the measure with them, state any remaining assumptions. Claude invokes this unprompted when a load-bearing word in the request has wide room for interpretation ("best", "quality", "runs hot", "simple", "fast", "good enough"). The user invokes it as /sharpen [prompt] to tighten a prompt before the final answer.
---

Sharpen a request until the answer can't be wrong for a definitional reason.
The failure this guards against: the user says "I run hot, what's the best
sheet", Claude silently decides "hot" means overnight heat retention and
"best" means cooling-then-durability, and four turns of confident advice
rest on definitions the user never gave.

## When to run

- **Unprompted**, when a request contains a word that (a) decides the
  answer and (b) has two or more readings that would lead to materially
  different answers. Test: "if I picked the other reading, would my
  recommendation change?" If yes, sharpen. If the readings converge on the
  same answer, don't — just state the assumption and proceed.
- **On `/sharpen`**, with or without an argument. With an argument, sharpen
  that prompt. Without, sharpen the user's most recent request.
- **Not** for small factual questions, follow-ups inside an already-sharpened
  thread, or when the user has said "just answer".

## How to sharpen

1. **Name the terms doing the work.** Pick at most three. Say in one line
   why each is load-bearing ("'best' decides the ranking order; 'runs hot'
   decides which property I optimise").

2. **Offer readings, not open questions.** For each term, use the
   AskUserQuestion tool with two to four concrete readings as options.
   The tool adds an "Other" option automatically — rely on it; that is the
   user's escape hatch. Make readings concrete and distinct, written in the
   user's situation not in the abstract:
   - "runs hot" → wake up sweaty / sheets feel warm to the touch / room is
     hot and I want the bedding to help / all of these
   - "best quality" → lasts longest / coolest through the night / softest on
     first touch / lowest upkeep
   Use `multiSelect: true` when readings aren't mutually exclusive.
   Batch up to three terms in one AskUserQuestion call rather than three
   round trips.

3. **Build the measure when the term is evaluative.** "Best", "quality",
   "good", "ideal" each hide a scoring rule. Once the user has picked the
   axes, ask them to order the axes (one more question, or infer from their
   phrasing and confirm). Write the resulting measure back in one line:
   "So quality here = cool through the night, then durability, then
   first-touch feel — feel is a tiebreaker, not a driver."

4. **Elicit the baseline** when the request is comparative or a
   recommendation to switch: what they use now, what they like about it,
   what they'd miss. Fold it into the same AskUserQuestion call where it
   fits, otherwise one short question.

5. **Restate the sharpened prompt** in two or three lines and get a yes
   before answering. On `/sharpen` this restatement is the deliverable;
   stop there unless they say go.

6. **State residual assumptions as assumptions.** Anything still
   unconfirmed when you answer goes in a visible line: "Assuming X; tell me
   if not." Never let an assumption appear as a fact in a table or ranking.

## Rules

- One sharpening pass per request. If it still isn't clear after one round
  of questions, proceed on stated assumptions rather than interrogating.
- Readings go in the user's words and situation. "Thermal effusivity vs
  breathability" is not a reading; "feels cool when you touch it vs stays
  cool at 3am" is.
- Option labels short and distinct — they are read aloud by a screen
  reader, not scanned.
- Don't pad with questions whose answer wouldn't change the output. Every
  question must map to a branch in the answer.
- When the user picks "Other", read their text as the definition and echo
  it back before continuing.
- The sharpened prompt and the measure are reusable: in a plan/ project,
  offer to record the measure in DECISIONS.md.

## Example

User: "My body runs hot, what's the best sheet material, order by quality."

Sharpen: name "runs hot" and "quality" as load-bearing. One
AskUserQuestion with two questions: how "hot" shows up (sweaty on waking /
sheets warm to touch / room heat / several), and which axes define quality
for them (multi-select: overnight cooling, first-touch feel, durability,
upkeep, price). Then one line eliciting the baseline: "What are you
sleeping on now and what do you like about it?" Restate: "Ranking sheet
materials for someone who wakes sweaty, currently on smooth sateen they
like the cool feel of, scoring on overnight cooling first and first-touch
feel second." Then answer, with the ranking's caveat column promoted to a
flag wherever a top pick loses on a chosen axis.
