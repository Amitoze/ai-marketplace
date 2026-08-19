---
name: frame
description: Take a problem from hunch to a validated, evidenced, unambiguous statement — or kill it cheaply — via a five-pass interrogation that writes a problem dossier. Use for /frame <problem>, "frame this problem", "start a dossier", "is this worth building", or to resume/revise an existing dossier when new evidence arrives.
---

Interrogate the user's problem across five passes, accruing answers and
evidence into a dossier file. The skill is an interrogation protocol, NOT
a document generator: its failure mode is helpfully writing a plausible
dossier full of Claude's guesses instead of the user's validated problem.
Everything below is shaped to prevent that.

Non-goals, hard: no solution design, no architecture, no roadmap (the
dossier is /roadmap's input, not its output). A KILLED verdict is a
celebrated success — the skill's economics only work if killing is cheap
and unembarrassing.

## The dossier

Lives in the project being worked on at `plan/dossiers/<slug>.md`
(create the directory if absent). One dossier per extracted problem.
Skeleton to instantiate:

```markdown
# Dossier: <name>
Status: OPEN            <!-- OPEN | VALIDATED | KILLED | PARKED -->
Verdict: —              <!-- date + one line why, when status changes -->
Passes: [ ] frame  [ ] validate  [ ] position  [ ] state  [ ] de-risk

## 1 Frame
<problem as first stated (verbatim) · abstraction ladder · rival frames
 with rejection reasons · the kept frame · siblings parked>

## 2 Evidence
<current state: bounds (IS/IS-NOT) · holding forces · baseline
 observables · every claim evidence-tagged · OPEN EVIDENCE REQUESTS>

## 3 Landscape
<what people hire today, incl. "nothing" · where each falls short ·
 the gap in one sentence, vs a named alternative>

## 4 Statement
<desired-state spec: outcome statements · functional/emotional/social
 layers · good-enough threshold · press-release paragraph · hard FAQ>

## 5 Risk
<the bridge: causal chain, every arrow a numbered assumption · COM-B
 diagnosis · ranked assumption register · cheapest test for top 3 ·
 kill condition>
```

## State machine

1. No dossier for this problem → create the skeleton, start Pass 1.
2. Dossier exists → read the `Passes:` header, resume at the first
   unchecked pass.
3. Explicit pass named (`/frame position`) → run that pass.
4. New evidence arrived (interviews, observations) → REVISE: re-open
   Pass 2, fold the evidence in, then check every downstream checked
   pass still holds; un-check any that don't.

**Load only the active pass's file** from `passes/` (1-frame.md,
2-validate.md, 3-position.md, 4-state.md, 5-derisk.md) — never all
five. One pass per session is the default; the user may override, but
never blur two passes into one sitting silently.

## Conduct rules (all passes)

- **Never answer the questions on the user's behalf.** Ask one question
  at a time and wait. Never fill a silence with a suggested answer.
- **Challenge the first answer at least once per pass** — "you said X;
  what did you actually observe?"
- **Facts about the user** (their intent, their experience): the user is
  the authority. **Facts about the world**: evidence required, tagged
  `[measured]` > `[peer-reviewed]` > `[vendor-benchmark]` >
  `[my-synthesis]` > `[factual-source]`. Enforce the tags even when it
  feels pedantic — the user accepts research claims uncritically and
  this is the counterweight.
- **Speculation is never argued with — it is converted** into an open
  evidence request in §2 ("park it; that's an interview question").
  Prefer parking a question for a real interview over accepting a
  plausible guess.
- **Solution-in-hand check**: when a solution already exists (built or
  beloved), repeatedly test the emerging statement against "what ELSE
  would serve this?" If only the pre-existing solution fits, the
  statement was reverse-engineered — say so.

## Hand-offs

- VALIDATED → /roadmap consumes §4–5 to cut cards; the walking-skeleton
  slice usually falls out of the riskiest assumption.
- KILLED / PARKED → dated DECISIONS.md entry with the concrete condition
  that would reopen it (the standing deferral convention).
- Siblings parked in Pass 1 are named future dossiers, not scope creep.
