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

## Hard rules

- **Never chain a verification command with a destructive command.** Run
  the check alone and READ its output before any deletion — a chain stops
  on a bad exit code, not a bad answer.
- Anything tunable lives in config, never hardcoded.
- Every script is idempotent (safe to re-run; skip existing outputs).
- Downloads require an explicit ask: filename, source, size.
- Never self-certify a gate that belongs to a human judgement — present
  the material and ask.
