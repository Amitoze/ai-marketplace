---
name: resume-bullet
description: Shape one resume bullet (or a rough description of some work) toward the full "outcome, measure vs baseline, method, consequence" form by diagnosing what a screener still doubts, asking for the specific missing facts, and deciding whether the material is one bullet or several. Use for /resume-bullet, "fix this bullet", "turn this into a resume bullet", "is this bullet strong enough", or when pasting a line from a CV for review.
---

Turn a line of work history into a bullet a hiring manager reads as a
peer wrote it. Work one role's material at a time. Never invent a number:
anything unknown goes in ⟨angle brackets⟩ for the user to fill or cut.

Longer treatment with worked rewrites: `~/work/jobs/linktree/bullet-writing.md`.

## The principle the whole skill serves

A resume reader cannot see the user work. They infer quality from text,
in about thirty seconds, against a pile. Each clause of a good bullet
closes one specific doubt. Stop adding clauses when the only doubts left
belong in an interview.

```
 Clause                          Doubt it closes           Doubt still open
 ──────────────────────────────  ────────────────────────  ─────────────────────────
 "Ran A/B tests"                 held the job?             how well? did it matter?
 + "lifted conversion"           anything change?          by how much?
 + "3.1 pts"                     by how much?              is 3.1 good here?
 + "vs 12 months flat"           is that good?             did you do it, or watch?
 + "by adding power analysis
    and guardrails"              did you do it?            what happened next?
 + "; PM killed the redesign,
    template became standard"    did it matter?            (nothing worth a line)
```

Three sources, one idea. Bock (ex-Google People): duties prove you held
the job; the number makes the claim powerful; the baseline makes it
meaningful; the method adds credibility. Green (Ask a Manager): "what did
you accomplish that someone else in the seat wouldn't have?" Statsig and
Eppo (experiment reporting): bottom line first, then the decision, in
business units. Caveat the user knows: this is practitioner consensus,
not a measured effect; no field experiment isolates quantified bullets.

## Anatomy of the target (tier 3)

```
 Accomplished [X]  as measured by [Y]  (vs baseline)  by doing [Z]  → consequence
      │                  │                │              │               │
      │                  │                │              │               └ who acted; shipped, killed,
      │                  │                │              │                 adopted, became standard
      │                  │                │              │
      │                  │                │              └ one clause of method; the posting's
      │                  │                │                noun, used truthfully
      │                  │                └ prior period, control arm, peers, target
      │                  └ numerals, units, absolute beside %, interval if an estimate
      └ a change in the business, stated as outcome or decision, not activity
```

- **X**: verb plus a change in the world. Killed, shipped, replaced,
  redirected, cut, lifted. Not worked on, supported, helped, was
  responsible for.
- **Y**: for experiment results, Statsig wording: what the sample showed,
  with the interval. "+3.1 pts (CI 1.8–4.4)" signals craft; "+3.1%" with
  no baseline signals nothing.
- **Baseline**: Bock's grocery example. 85 customers a day is good;
  "vs a peer average of 70" is better.
- **Z**: where the job posting's vocabulary goes, only where true.
- **Consequence**: the senior signal. Level of the person who acted and
  what changed: launch killed, roadmap re-sequenced, standard adopted.
- **No number available**: Green's substitutes. The counterfactual
  ("cleared an inherited four-month backlog in three weeks") or a
  qualitative fact ("cited unprompted in the board paper").

## Grading ladder

```
 Tier 1  duty            "Conducted A/B experiments to support rollout of the
                          search engine to APAC markets."
 Tier 2  outcome+number  "Ran ⟨N⟩ A/B tests across ⟨k⟩ markets, lifting apply
                          rate ⟨x⟩%."
 Tier 3  full            "Shipped the search engine to ⟨k⟩ APAC markets on the
                          evidence of ⟨N⟩ A/B tests I designed and read: apply
                          rate +⟨x⟩ pts vs control (CI ⟨a⟩–⟨b⟩), ⟨y⟩ variants
                          killed on guardrail breaches; sized each market's
                          window by power analysis."
```

Tier 1 is a duty. Tier 2 passes a keyword sorter. Tier 3 is what a
hiring manager who does the work recognises.

## Mechanics (apply silently, report only failures)

| Rule | Source |
|------|--------|
| Past-tense action verb first for past roles, present for the current one. No pronouns. | Harvard, MIT, Google |
| One to two lines. A word spilling onto a new line means cut words, not accept three. | MIT, Google |
| 3–5 bullets for the last two roles, 1–2 for older. | Emory (convention, not measured) |
| Most relevant bullet first within a role. | MIT |
| Numerals not words; absolute figure beside any percentage; consistent units. | Harvard sample, Bock |
| Jargon only when the reader certainly knows it. QoQ fine at a tech firm; internal codenames not. | Google |
| Different verbs across a role's bullets. | Harvard |
| Banned openers: Responsible for, Helped, Assisted, Worked on, Participated in, Involved in, Supported. | Bock, Harvard, Emory |
| Accomplishments only for a senior profile; no daily duties. | Green, Emory |

## Bullet types (a role needs a mix; four of one type reads narrow)

| Type | Must contain |
|------|--------------|
| Experiment → decision | design and scale; primary metric vs control with interval; guardrail or null handled; who adopted what |
| Metric definition | what it replaced; how built (tool); who adopted it; what it revealed; what investment moved |
| Opportunity sizing | range; method; what an exec funded or cut |
| Data infrastructure | what was built; time or cost from a to b; who now self-serves |
| Influence / narrative | finding; level presented to; recommendation adopted; consequence |
| Standards / mentoring | the standard; how many teams; who grew to do what |
| PM work in DS terms | hypothesis funded; metric defined; test or analysis that settled it; shipped or cut |

## Process

1. **Intake.** Take what the user gives: a current bullet, a rough
   description, or a story told in prose. Note the role, dates, and the
   target posting if one exists in `~/work/jobs/<employer>/` (research or
   PD files hold the posting's nouns). Keep the user's own phrases where
   they already work.

2. **Diagnose.** State the tier (1, 2 or 3) and list the doubts still
   open, using the ladder's language. Name the bullet type it is trying
   to be. Two or three lines, no more.

3. **Ask for the missing facts, one round.** Ask only what flips the
   draft. Use the options tool for anything with a small set of answers
   (bullet type, which decision followed, the level of the person who
   acted) and list the free-text facts as a short numbered list in the
   same message, in concrete terms from the user's own situation:
   - count and scale ("how many tests, over what period, on how many
     users or markets")
   - the primary measure, its value, and what it is compared with
     ("control, prior quarter, peer squads, a target")
   - the method in one clause, and which tool from the posting it used
   - what happened next and who made it happen ("shipped, iterated,
     killed; by whom, at what level")
   - for anything the user cannot defend from a deck, dashboard or
     document: say so and offer the qualitative form instead.
   Do not ask what the user already said. If after one round something
   is still unknown, draft with ⟨placeholders⟩ and say which.

4. **Decide the split.** Recommend one bullet or several, and say why:
   - one decision or outcome per bullet; two outcomes with different
     consequences are two bullets
   - two different bullet types in the material (an experiment and a
     standard it produced) are two bullets
   - a bullet still over two lines after cutting words is two bullets or
     one bullet with the weaker half dropped
   - the same outcome restated with a second number is one bullet with
     the stronger number
   - check the role's running count against 3–5; if the split would push
     it past five, name which existing bullet to drop or merge.

5. **Draft.** Show tier 2 and tier 3 side by side for each bullet.
   Tier 3 is the recommendation; tier 2 is the fallback when the user
   cannot defend the extra clauses. ⟨Placeholders⟩ for every unknown.
   Never fill one with a plausible figure.

6. **Test and report.** Run the four tests and say which pass:
   - **Temp test**: could a mediocre temp in the seat write this line?
   - **So-what test**: cover everything after the number; does the
     reader know whether it was good and what happened next?
   - **Defend test**: can the user reconstruct every number in an
     interview? One indefensible number makes the whole page suspect.
   - **Posting test**: at least one noun from the target posting, used
     truthfully. If no posting is known, skip and say so.

## Output format

1. Diagnosis: tier, bullet type, open doubts (two or three lines).
2. The questions, one round (skipped if nothing is missing).
3. Split recommendation with the reason, one or two lines.
4. Drafts: tier 2 and tier 3 per bullet, placeholders marked.
5. Tests: which pass, which fail and why. Mechanics failures only.
6. Running count for the role, if known.

Do not pad with praise, restate the principles, or append general
advice. Edit the user's CV file only when asked; otherwise output in chat.
