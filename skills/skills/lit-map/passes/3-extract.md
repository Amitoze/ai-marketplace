# Pass 3 — Extract

**Goal:** for each included source — fetch it, verify it, appraise it,
and pull its findings into the concept matrix. This pass is where the
hard rules bite; it is deliberately the slowest.

**Sits on:** Webster & Watson (MISQ 2002) concept-centric synthesis —
build the concept matrix WHILE reading, not after · AACODS checklist
(Tyndall, Flinders) for grey-literature appraisal · GRADE's insight
that design determines starting confidence.

## Per-source procedure (sources.md, one entry each)

1. **Fetch & verify.** Retrieve the work (WebFetch full text where
   open; else abstract via API). Confirm title/authors/venue/year
   against the API record (Crossref/OpenAlex). Mismatch → back to the
   search log with a note, not into sources.md.
2. **Tag read-depth:** `/full-text` or `/abstract-only` (paywalled
   sources stay in, so tagged — ratified choice).
3. **Appraise.**
   - Academic: record the design qualifier (RCT, cohort, qual-interview,
     survey, review, theory) — design sets starting confidence; note
     obvious downgrade flags (tiny n, indirect population, conflicts).
     This is appraisal-lite, declared as such — not GRADE certified.
   - Grey: AACODS — Authority, Accuracy, Coverage, Objectivity, Date,
     Significance → `pass` or `caution` with the failing letters named.
4. **Extract findings.** Each finding: one sentence, the evidence tag
   (`[peer-reviewed/<design>/<depth>]` or `[grey/AACODS:.../<depth>]`),
   and which review question(s) it bears on. Findings answer the
   protocol's questions; interesting-but-off-question material gets one
   PARKED line, not a paragraph.
5. **Update the concept matrix** (map.md): add the source row, tick the
   concept columns it addresses. New concepts earn a column only when a
   second source touches them; singletons wait in a candidate list.

## Conduct

- Never quote from memory — every quotation is copied from fetched
  text. Reproduce at most short attributed fragments.
- A source that turns out to say less than its abstract promised is
  recorded as exactly that.
- Batch mechanically: fetch/verify several sources in parallel, but
  write each entry before moving on — a half-extracted source is
  indistinguishable from an unread one later.

## Exit check

Every included source has a sources.md entry with verified citation,
depth tag, appraisal, and tagged findings; the concept matrix covers
all sources; nothing in any artifact cites a work that was not fetched.
