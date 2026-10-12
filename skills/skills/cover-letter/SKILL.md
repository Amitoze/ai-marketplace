---
name: cover-letter
description: Draft or review a cover letter so it reads as written by a person, maps to the position description, and survives a screener's seven-second read. Use for /cover-letter, "write a cover letter", "review my cover letter", "does this sound AI", or any request to fix a sentence in an application letter.
---

Draft or review a cover letter. The user writes for the Victorian public
sector and mission-driven organisations as often as for commercial ones, and
has a sharp ear for machine-sounding prose. The bar is: every sentence could
have been written by them, and every paragraph earns its place against the
position description (PD).

## Inputs to gather first

- The PD or job ad (path or pasted). If absent, ask for it; do not draft
  against a guessed PD.
- The user's existing draft, if reviewing.
- Prior letters in `~/work/jobs/<employer>/` for voice and reusable examples.
  Reuse the user's own sentences before inventing new ones.

## Process

1. **Criteria map first.** List the PD's essential and desirable criteria,
   then assign each to a paragraph. Anything unassigned is either a gap to
   flag or a sentence to add. Output the map as a table at the end.
2. **Draft or edit in the user's voice.** Short declarative sentences, past
   tense, first person. Use their actual examples (Mable customer economics,
   SEEK business case and candidate-journey measurement, Canva metrics
   framework, RMIT survey-plus-outcomes linkage, DepressioNet facilitation)
   unless told otherwise.
3. **Run the sentence rules** below on every sentence, then the **send
   checks**.
4. **Report**: the letter, then a short list of what changed and why, the
   criteria table, and any claim the user must verify before sending.

## Structure that works

- **Opener (two to three sentences).** Name the role. One sentence of
  credentials. One sentence on why this organisation, which must pass the
  swap test (below).
- **Two or three evidence paragraphs.** Each opens with a plain claim in the
  "I have [verb]" form, then two concrete examples, then at most one sentence
  tying it to the PD. One number per paragraph at most.
- **Close.** Tools named honestly, the career motive stated once if it is a
  sector change, one sentence of offer. End on the organisation, not on the
  applicant.
- Length: 350 to 550 words. One page.

## Sentence rules (the human test)

The recurring machine tell in this user's drafts is **compression**: several
claims folded into one balanced sentence through nominalisation and stacked
clauses. The fix is always the same.

**One claim per sentence. Start with "I" and the verb for the thing that was
done, not a noun that describes having done it.**

Concretely:

1. **Verb, not nominalisation.** "I led" not "I have experience leading".
   "I studied" not "trained in". "My analysis changed the decision" not
   "a track record of turning analysis into decisions". If the sentence's
   main noun is *experience*, *track record*, *expertise*, *capability* or
   *skills*, rewrite around the underlying verb.
2. **No fronted participle.** Sentences beginning "Trained in...", "Having
   led...", "Drawing on..." are a literary opener nobody uses when speaking.
   Make it its own sentence or move it after the main clause.
3. **No gerund-subject maxim.** "[Doing X] is the core of my craft", "[Measuring
   Y] is the work I know best". A sentence about the applicant should have the
   applicant as its subject. Rewrite as "Most of my work has involved..." or
   "I have spent much of the last decade...".
4. **No self-ranking superlatives.** "The work I know best", "my strongest
   craft", "genuinely". Nobody has ranked the applicant's skills; the phrase
   only sounds assured.
5. **Evidence before slogan.** Do not open a paragraph with a quotable claim
   the paragraph then proves. Open with the plain claim or the first example.
6. **Mirror the PD's words once, as a fact, never as an aphorism.** The
   reader recognises their own phrase; returned as a flourish it reads hollow.
7. **No "A is the shape of B" closers, no "not X but Y" antithesis, no
   colon-then-flourish, no em dashes, no semicolons joining two full
   clauses.** Each is a cadence tell.
8. **Keep adjacency honest.** If a criterion is covered only by a related
   example, say so in the notes and do not claim the criterion by name in the
   letter.

Worked example of the rule:

> Before: *Trained in social science, psychology and statistics, I have
> almost a decade of experience leading data and analytics projects at SEEK,
> Canva, Mable and RMIT University, and a strong track record of turning
> analysis into decisions at executive level.*

Three claims, a participle opener, two nominalisations, one stock phrase.

> After: *I studied social science, psychology and statistics. For almost ten
> years I have led data and analytics projects at SEEK, Canva, Mable and RMIT
> University, and in each role my analysis has shaped decisions at executive
> level.*

## The swap test

Replace the employer's name with a plausible rival (another agency, another
tribunal, another firm). Any sentence about "why this organisation" that
still reads fine is not specific enough. Fix by naming one thing only this
employer does, or one fact from their annual report, and tie it to one piece
of the user's own evidence.

## Public sector specifics (Victoria)

- Salutation "Dear Selection Panel" unless a named person is confirmed.
  Address block and salutation must agree.
- Name the role and reference number in a "Re:" line.
- State a sector change once, as a decision already made, then move on. The
  VPS guidance wants it addressed, not dwelt on.
- Show a public sector value (impartiality, integrity, respect) through an
  example; never list the values.
- Do not criticise the employer's published failures (audits, surveys). Name
  the finding as a professional standard the user shares.
- Salary bands and tenure come from the ad, not the PD; check the ad before
  advising on either.

## Send checks (give these as a list the user runs)

- Search the document for the employer's name misspelt (common:
  Inquiry/Injury, Workforce/Workplace), for lowercase brand casing (Seek,
  Rmit), and for tab characters.
- Read the "why here" sentence with a rival's name swapped in.
- Read the letter aloud once; any sentence that needs a breath mid-way has
  two claims in it.
- Confirm the date is the send date, without "th".
- Confirm every number in the letter appears in a source the user can cite.

## Output format

1. The letter, in a blockquote, ready to paste.
2. "What changed and why", three to six bullets.
3. Criteria map table: PD criterion, where covered, or "not covered" with a
   one-line suggestion.
4. Claims to verify before sending, if any.

Save the draft to `~/work/jobs/<employer>/cover_letter_draft.md` only when
asked; otherwise output in chat.
