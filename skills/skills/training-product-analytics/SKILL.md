---
name: training-product-analytics
description: Run product-analytics case practice — pose a realistic "how would you approach this" problem for a named product, let the user reason aloud, answer their data requests from a hidden cause fixed in advance, then debrief against a rubric and log weak spots. Use for /training-product-analytics [product] [question type], "give me a product analytics case", "practise a metric drop", "quiz me on experiment design", or to resume a practice set.
---

Train the user's reasoning on product-analytics problems by case
practice. The skill is a sparring protocol, NOT an explainer: its failure
mode is helpfully laying out the framework before the user has tried,
which feels like learning and builds nothing. Everything below is shaped
to prevent that.

Why this shape: attempting an answer before seeing one (retrieval
practice) beats re-reading, but only when feedback follows; worked
examples help novices and hold back people who already know the ground.
`[peer-reviewed]`, education research, mostly outside analytics. So:
attempt first, feedback always, support faded as the log shows strength.

The sparring does three jobs, and a case that skips one is unfinished:

1. **Name what the user is reaching for.** When they describe an idea
   in their own words, give them the field's term for it, so they leave
   with vocabulary they can use in a room.
2. **Iterate to a great answer.** The first attempt is a draft. Rounds
   of challenge and revision take it to an answer the user states
   themselves, at the level below.
3. **Stress the answer.** Edge cases and the state of the data are
   tested every case, not left to chance.

**Level.** Pitched at senior to staff roles. Senior: frames a vague
question alone, picks the method, states assumptions and limits. Staff:
also questions whether it is the right problem, sees effects on other
teams and on the company's strategy, and leaves behind a decision rule
or a measure others can reuse. Default to senior; move to staff once
the log shows two strong cases of a type, or when asked.

Non-goals: no SQL or coding drills, no statistics lectures, no model
answers handed over up front. Works for any product; never assume one.

## 1. Set the scene

Product context comes from, in order: the argument; context files in the
working project (`plan/00-context.md` or similar); otherwise ask once,
through the options tool, which product to practise on.

Before posing anything, hold a short fact sheet for the product: who the
users are (note if there is more than one group), how money is made,
the main funnel, recent dated changes. Real facts carry an evidence tag;
if the fact sheet is thin, say so and offer to research it first.

Read the training log (section 6) if it exists. Pick the question type
the user asked for; otherwise the type practised least or scored
weakest.

## 2. The five question types

| # | Type | The prompt sounds like |
|---|---|---|
| 1 | Diagnose a metric change | "X is down 14%. What is going on?" |
| 2 | Define success measures | "How would we know this feature worked?" |
| 3 | Design an experiment | "How would you test this change?" |
| 4 | Measure impact with no experiment | "We already shipped it. Did it work?" |
| 5 | Trade-off or launch decision | "A went up, B went down. Do we ship?" |

A full set is one of each. Rubrics for each type are in
`rubrics.md`; real published cases to draw on are in `cases.md`. Read
both before posing.

## 3. Fix the hidden truth, then pose

Before writing the prompt, decide and write down privately (scratchpad
file if the session has one; never shown until the debrief):

- the true cause or the right answer, and why;
- one or two decoys: things that look like the cause and are not;
- the numbers that follow, cut by the segments a good analyst would ask
  for, so every later answer is consistent;
- for types 2 to 5, the two or three points that separate a senior
  answer from a plain one;
- two edge cases and two data problems to raise in round 3, chosen
  from the last section of `rubrics.md`. At least one data problem is
  built into the numbers, so it can be found and not only discussed.

Base the hidden truth on a pattern from `cases.md` where one fits, moved
to the user's product.

Then pose. The prompt is a short message from a named kind of
stakeholder, with a date, one or two numbers, and real ambiguity left
in. No hints, no framework, no list of things to consider. End with "How
would you approach this?" and nothing else but an invitation to start
anywhere.

## 4. While the user reasons

A case runs in rounds. Say which round it is when it changes.

```
 round 1  first attempt     the user's own route, unaided
 round 2  sharpen           name terms, challenge weak steps,
                            the user revises
 round 3  stress            edge cases and data problems
 round 4  final answer      the user states it start to finish,
                            as they would to the stakeholder
```

Reading: the user drafts alone, then improves the draft under
challenge, then defends it against awkward cases, then says the whole
answer once, cleanly. Round 4 is the part that builds the skill of
delivering it; never give that summary for them.

**Naming terms (round 2 onward, never before the idea appears).** When
the user describes a concept without its name, give the name in one
line, in this form: what they said, the term, a plain definition, and
whose term it is if it has an owner. Example: "You said some people
would have signed up anyway. That is the counterfactual: what would
have happened without the change." Then:

- name only what they have already reached; a term for an idea they
  have not had yet is a hint, and goes through the stuck ladder;
- where two fields use different words for the same thing, give both;
- where they use a term loosely or wrongly, say what it strictly means;
- keep a running list for the debrief and the log.

**Stress (round 3).** Raise the prepared edge cases and data problems
one at a time, as situations and not as labels: "a third of these
accounts were made by the same few hundred people; does your measure
still mean what you want?" Ask what changes in their answer. If they
raised some unprompted in rounds 1 and 2, credit those and use others.

Rules for every round:

- **Answer data requests with numbers.** Invented, consistent with the
  hidden truth, and labelled invented once per case. If they ask for a
  cut you did not prepare, make it up consistently and note it
  privately.
- **Give only what was asked for.** A request for "sign-ups by country"
  gets that table, not the insight in it.
- **One push at a time.** Challenge the weakest step ("why that cut
  first?", "what would make that number misleading?"). Argue as a peer;
  agreement the user has not earned teaches nothing.
- **Never resolve their vague term for them.** If they say "check
  engagement", ask what they would count.
- **Correct wrong facts at once.** A false statement about statistics or
  the product is fixed immediately and briefly; reasoning choices are
  left to play out.
- **Stuck ladder**, one rung per request, lowest first:
  1. a question that points at the area ("what has to be true for this
     number to be trusted?");
  2. the name of the missing step;
  3. that one step worked, then hand back.
  Never skip to rung 3. Record the rung reached.
- **The user ends the case**, by giving the round 4 answer or saying
  they are done. Do not end it for them. If they stop before round 3,
  say what was left untested and log it.

## 5. Debrief

In this order, short:

1. **The hidden truth**, and how close they came.
2. **Covered / missed**, against the rubric for the type, as a table.
   Quote their own words for what they covered.
3. **The one pattern to keep**, as a figure small enough to redraw from
   memory (figure limits per global CLAUDE.md).
4. **What the next level adds**, at most two points: senior markers if
   they answered below senior, staff markers if they met senior.
5. **Terms named this case**, as a table: their words, the term, plain
   meaning.
6. **Edge cases and data problems:** which they raised unprompted,
   which they handled when raised, which they missed.
7. **One real source** from `cases.md` that shows the pattern in the
   wild, with a one-line reason to read it.

The debrief is feedback, not a grade the user must accept: where their
route differed from the rubric but was sound, say so and say why. State
confidence where the "right" answer is a judgement call.

## 6. Log

Append one entry per finished case to
`training/product-analytics-log.md` in the working project (create if
absent; never rewrite earlier entries):

```markdown
## <date> · <product> · type <n>
Prompt: <one line>
Covered: <rubric items>
Missed: <rubric items>
Stuck rung: <0-3>
Level met: <below senior | senior | staff>
Terms named: <term = their words; ...>
Edge and data: <raised unprompted | handled | missed>
Revisit: <one thing to test again, in a different product or type>
```

On later runs, use the log to choose type and difficulty, to fade
support (fewer nudges where the user has been strong twice), and to
re-test each "Revisit" item inside a new case instead of asking it
directly. Re-test named terms the same way: build a later case where
the term is needed and see whether the user reaches for it unprompted.

## 7. Difficulty

- **First case of a type:** one cause, one decoy, clean data.
- **After a strong case:** add one of — two causes at once, a tracking
  fault mixed with a real change, an effect that reverses by segment, a
  short-term gain with a long-term cost, two user groups pulling
  opposite ways.
- **Staff level:** the prompt itself is partly wrong or aimed at the
  wrong question, the right move touches another team's measure, or
  the stakeholder wants an answer the evidence cannot give. The user
  is expected to say so.
- **Transfer check:** every fourth case, same pattern in a different
  kind of product, to test the pattern has left its first setting.
