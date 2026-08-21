---
name: lit-map
description: Map the research literature onto a problem dossier — identify relevant research domains, chart questions and key findings, expose gaps — via a four-pass scoping review that writes verified, appraised artifacts. Use for /lit-map <dossier-slug>, "map the literature", "literature review for the dossier", or to resume/extend an existing lit map when new sources or questions arrive.
---

Run a solo-scale scoping review of the literature around a framed
problem, accruing verified sources and appraised findings into review
artifacts that feed the dossier. The skill is a verification protocol,
NOT a summary generator: its failure mode is a plausible map built on
confabulated, misquoted, or unread sources. Everything below is shaped
to prevent that.

**Genre, declared:** scoping + multivocal review (PRISMA-ScR-lite),
grey literature included and appraised separately, rapid-review
shortcuts taken openly. This is honest solo-scale rigor — never label
the output a "systematic review". Ratified 2026-08-21.

Non-goals, hard: no solution design, no roadmap input beyond the
dossier, no pretending exhaustiveness. "No evidence found" is a
recorded result, not a failure to hide.

## Hard rules (all passes — these are the skill)

1. **No unfetched citation, anywhere.** A source enters an artifact
   only after Claude has fetched it (WebFetch, or an API record from
   OpenAlex / Semantic Scholar / Crossref / PubMed) and confirmed
   title, authors, venue, year match the claim. LLM-generated citation
   lists run ~20% fabricated and ~45% bibliographically wrong
   [peer-reviewed]; this rule is architectural, not aspirational.
2. **Read-depth is tagged per claim:** `/full-text` vs `/abstract-only`.
   Paywalled sources enter tagged `/abstract-only`; a dossier claim
   resting solely on abstract-only sources is flagged "needs full-text
   confirmation" before it may become load-bearing.
3. **Every screening exclusion is logged with its reason.** The search
   log keeps PRISMA-style counts: found → screened out (why) → included.
4. **Declared shortcuts:** single (Claude) reviewer mitigated by user
   spot-check of a ~20% screening sample [peer-reviewed: solo screening
   misses ~13% vs ~3% dual]; no institutional database access (open
   APIs + web only); protocol states both.
5. **Never self-certify a gate.** Three gates belong to the user:
   ratify the protocol (before any search), spot-check screening
   (before extraction), ratify the map (before dossier write-back).

## Artifacts

Live in the project at `plan/research/lit/<dossier-slug>/`:

- `protocol.md` — review questions (PEO-framed), candidate domains,
  inclusion/exclusion criteria, search strings, declared shortcuts.
  Written BEFORE searching; scope changes are dated amendments, never
  silent edits.
- `search-log.md` — every query (source, string, date, hit count),
  screening decisions with reasons, snowballing rounds, PRISMA counts.
- `sources.md` — one entry per included source: verified citation,
  read-depth tag, appraisal (design qualifier; AACODS for grey),
  extracted findings.
- `map.md` — Webster–Watson concept matrix (sources × concepts),
  evidence gap map (domains × review questions, cells show density +
  confidence), synthesis per question, and the "what the literature
  cannot answer" list.

## Evidence tags

Extend the global ladder with qualifiers; the ladder stays the
interface: `[peer-reviewed/<design>/<depth>]` (e.g.
`[peer-reviewed/RCT/full-text]`, `[peer-reviewed/qual-interview/
abstract-only]`), `[grey/AACODS: pass|caution/<depth>]`,
`[measured]` reserved for things this project observed itself.

## State machine

1. No `plan/research/lit/<slug>/` for the named dossier → confirm the
   dossier's §1 is ratified (if not, stop: /frame first), create the
   directory, start Pass 1.
2. Artifacts exist → resume at the first incomplete pass (protocol
   unratified → 1; search-log open → 2; unextracted sources → 3;
   map unratified → 4).
3. New sources or questions arrive after ratification → REVISE: amend
   the protocol (dated), run the delta through passes 2–4.

**Load only the active pass's file** from `passes/` (1-scope.md,
2-search.md, 3-extract.md, 4-map.md) — never all four. One pass per
session is the default.

## Hand-offs

- Consumes: the dossier's §1 kept frame and §2 open evidence requests
  (`plan/dossiers/<slug>.md`, from /frame).
- Feeds: distilled tagged findings + artifact pointers into dossier §2
  (evidence) and §3 (landscape) — full resolution stays in the
  artifacts, the dossier gets the digest.
- The "cannot answer" list becomes dossier §2 open evidence requests —
  i.e. the user's interview questions. This output is as valuable as
  the findings.
