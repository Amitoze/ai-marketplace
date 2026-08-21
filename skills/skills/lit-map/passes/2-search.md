# Pass 2 — Search

**Goal:** execute the ratified protocol — database-equivalent API
search + grey-literature sweep + snowballing — producing a fully
logged, screened source list the user has spot-checked.

**Sits on:** evidence that database search + snowballing combined beats
either alone [peer-reviewed, software-engineering SLR studies] ·
single-reviewer screening misses ~13% vs ~3% dual, mitigated by
dual-screening a sample [peer-reviewed] · PRISMA flow reporting.

## Sources (no institutional access — open APIs + web)

- **OpenAlex** `api.openalex.org/works?search=...` — keyword search,
  and per-work `referenced_works` (backward) + `cited_by_api_url`
  (forward) for snowballing. Free, no key.
- **Semantic Scholar** `api.semanticscholar.org/graph/v1/paper/search`
  — second opinion, abstracts, citation graphs.
- **PubMed E-utilities** `eutils.ncbi.nlm.nih.gov` — health literature.
- **Crossref** `api.crossref.org/works/<doi>` — citation verification.
- **Grey sweep** (WebSearch): charity/NGO publications, practice
  guidelines, OT resources, community content — only the types the
  protocol admits.

## Process

1. Run each protocol search string; log in search-log.md: source,
   string, date, hit count. Idempotent: re-runs append a dated round,
   never overwrite.
2. Screen title/abstract against the inclusion criteria. Every
   exclusion gets a one-line reason in the log. Borderline calls are
   marked BORDERLINE, not silently resolved.
3. Snowball from included sources: backward (references) and forward
   (cited-by), one round minimum, repeat until a round adds nothing.
   Log each round separately (PRISMA wants supplementary-search counts
   distinct from database counts).
4. Write PRISMA-style totals: found → deduplicated → screened out
   (reasons bucketed) → included.
5. **GATE (user): spot-check screening.** Present a ~20% random sample
   of screening decisions (mixed includes and excludes, all
   borderlines) with the criteria alongside. The user judges; disagreements
   recalibrate the criteria and force a re-screen of affected records.
   Record the sample, verdicts, and any recalibration in search-log.md.

## Exit check

search-log.md holds every query with counts, every exclusion with a
reason, snowballing rounds to closure, PRISMA totals, and a dated
user spot-check. The included list exists but nothing has been
extracted or appraised yet.
