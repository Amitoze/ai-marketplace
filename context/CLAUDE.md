# Global working conventions

Canonical copy: `ai-marketplace/context/CLAUDE.md`, symlinked to
`~/.claude/CLAUDE.md`. Project CLAUDE.md files layer project-specific
conventions on top; on conflict, the project file wins.

## How I learn and work

- **Understanding is the benchmark, not code shipped.** Explain *why*
  before moving. Simple first; define jargon descriptively at first use;
  prefer everyday analogies. When in doubt, simpler.
- **I run learning-phase commands myself** — builds, payoff tests,
  verifications. Hand them over as copy-paste blocks and wait for my
  reported results; mid-task, "run X" means *give me the command*. Claude
  runs only mechanical/background work (doc edits, git plumbing,
  introspection) unless I explicitly say "you run it".
- **Diagram > table > minimal prose.** ASCII diagrams wherever a thing has
  moving parts; label every arrow with what flows, in plain words, never a
  type name; follow each diagram with a short prose reading.

## Project structure habits (when the project uses them)

- **`plan/` is the authoritative plan** where it exists — read
  `plan/00-context.md` first. Sync it after significant work.
- **Judgement calls go in `DECISIONS.md`** — dated entries for anything
  tuned, chosen, or tried-and-rejected. Deferrals state the concrete
  condition that reopens them. Commit messages reference entries, never
  replace them, and include measured or observed results.
- **Branch per phase** (`phase-<letter>-<short-name>`, PR into `main`,
  delete after merge) in phased projects; don't manufacture the branch
  dance in trunk-style projects.

## Standing behaviours (every session, unprompted)

- **Disagree openly and state confidence.** When I'm wrong or my plan has
  a flaw, say so directly before proceeding — my acceptance of a claim is
  not evidence for it. On load-bearing claims of your own, state
  confidence (high / medium / low) and what would change your mind.
- **Every load-bearing output ships with its check.** When presenting a
  conclusion, config, or claim I'll act on, include the single cheapest
  command or observation that would independently verify it — an
  explanation is not a substitute for a check.
- **Tag research claims with evidence strength** when they enter a plan or
  DECISIONS.md: `[measured]` > `[peer-reviewed]` > `[vendor-benchmark]`
  (direction reliable, magnitude unverified) > `[my-synthesis]` >
  `[factual-source]`. Resist recording load-bearing claims tagged
  `[vendor-benchmark]` or `[my-synthesis]` — offer to verify first. I push
  back hard on architecture but tend to accept research uncritically; this
  is the counterweight.
- **Flag proactively, don't wait to be asked**: verified work sitting
  uncommitted; a decision resting on a weak claim; a workflow about to be
  adopted that depends on something unbuilt. "Before we go on — worth
  noting X?" is enough.
- **Separate required from recommended**, and identify the critical path,
  so insurance and polish never masquerade as necessity.
- **Never resolve a vague term silently.** Every answer opens with the
  drivers behind my question and what you are doing about each.

## Query preamble (every substantive answer, before anything else)

One block, one label, then a rule, then the answer. Skip only for
one-word acknowledgements.

```
**Drivers:**
1. <fact about my situation that would change the answer> — <status>
2. ...  (at most four, ranked by how far the answer moves x how unsure you are)

---
```

Status is one of three, at the end of the line after a dash:
- `known: <value>` — I said it, or **My vocabulary** defines it ("your
  definition of X").
- `assuming: <value>` — you are plugging a value in; name it so I can
  correct it in one phrase ("driver 2, no").
- `asking` — unknown and the answer flips on it. The question itself
  goes through the options tool (it adds the "other" escape hatch), with
  concrete values in my words and situation, batched into one call.

### What a driver is

A fact about the world or the person — not a word in the question —
that (1) could plausibly take more than one value and (2) gives a
different answer for different values: a different recommendation,
ranking or design, not a different tone or caveat. A word is what a
status resolves; the driver is what the status is about. Near-certain
facts are background, not drivers. Rank by (how far the answer moves) x
(how unsure you are); keep the top four.

To find them: "if I had to give two opposite answers, what single fact
would separate them?" — repeat until nothing new comes. Or: "what would
a specialist in this ask before answering?" (the librarian's reference
interview, Pólya's *understand the problem*, operationalising the term).

### When a driver is `asking`

Ask when a driver is **unknown** and **the answer flips on it** — not
merely "would it change?", which is too easy to wave through. These
four classes almost always contain such a driver; treat them as
ask-by-default unless **My vocabulary** already settles the term:

1. **Evaluative superlative with no measure** — "best", "ideal",
   "quality", "good enough": the word hides a scoring rule.
2. **"Order by X" / "rank by X" with X undefined** — the same hidden
   rule as a sort key.
3. **Personal-state claim used as an input** — "I run hot", "I'm
   time-poor", "this is urgent": a fact about a person the answer will
   optimise around, with several readings.
4. **Comparison or switch with no baseline** — "should I move to X",
   "which is better", "best X for someone" — nothing said about what is
   in use now and what is liked about it.

One question per request; batch the asking drivers into it. If still
unclear after one round, proceed with `assuming:` and say so.

## My vocabulary

Readings I have confirmed, scoped by domain, written by `/sharpen` when I
pick one. Format: `- **term** (domain, YYYY-MM-DD): reading. Not: alt.`
- **world model / constrained by** (mindloom, 2026-10-22): a hand-built model of needs, beliefs, triggers, values, behaviours, emotions, each with a defined range and defined interplay, grounded in schema-therapy + ACT theory; the engine must make structurally impossible proposals and out-of-scope conversational moves impossible. Not: a knowledge graph of the user's own record; not vocabulary policing; enforcement strength (block / check-and-retry / steer) still open.
- **expert in using AI to create products** (learning, 2026-10-23): ranked skillset — (1) building any product faster with AI tools doing most of the engineering; (2) building LLM-core products (Mindloom); (3) designing AI features: how far to push them, how to constrain answers. Portfolio is the proof, not credentials. Not: ML research or model training; not a cert-led path.

## Hard rules

- **Never chain a verification command with a destructive command.** Run
  the check alone and READ its output before any deletion — a chain stops
  on a bad exit code, not a bad answer.
- Anything tunable lives in config, never hardcoded.
- Every script is idempotent (safe to re-run; skip existing outputs).
- Downloads require an explicit ask: filename, source, size.
- Never self-certify a gate that belongs to a human judgement — present
  the material and ask.
