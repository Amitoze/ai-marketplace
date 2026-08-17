---
name: walkthrough
description: Produce a guided, copy-paste walkthrough for a build step or plan item. Use when the user wants to build something themselves with explanations, or says "guide me through X" / "as we did previously".
---

Guide the user through building the requested item themselves. They
learn by doing — the explanation quality matters as much as the artifact.

## Hand off — do not run the steps yourself

The walkthrough is the USER's to execute; running it IS the learning. You
write the copy-paste blocks, the user runs them and reports results. This
holds for EVERY block, including the payoff / build / verification at the end.

Do not run these yourself, even if the user says "run the build" or "run step
4" mid-walkthrough — here that means *give me the command*, so hand it over and
wait for their results. Running it yourself is worse on every axis: it takes
away the hands-on payoff (the point of the format); the command executes on the
user's machine either way, so you gain nothing; and long or stateful commands
(model downloads, installs, servers) tie the session up babysitting them.
Only when the user explicitly says *you* run it ("you run it", "go ahead and
run it for me") is that a stated exception — otherwise default to handing off.

## Before writing

1. Read the relevant plan or design doc section for the item (and its "In
   plain terms" block if present). Honour every intent note.
2. Check any project config — anything tunable must come from config,
   never be hardcoded in what you guide them to write.
3. Check what already exists in the project so steps build on real current
   state, not an imagined one.

## Open with a trace (the shape before the code)

Before the first build step, open the walkthrough with a **data-flow trace
of the artifact you're about to build** — the `trace` skill's format,
run in its before-it's-built mode. Map, from the plan and the surrounding
system: what the thing will read, how it transforms it, what it writes, and
where each output is born.

Why at the top: the user's benchmark is understanding, not code shipped.
Seeing the whole data path first gives them the mental model to build
*into*, turns each later step from "type this" into "fill in this known
slot", and catches design risks (a value with no source, a config knob
nothing will read, an ordering hazard) before any code hardens them. Follow
`trace`'s representation priority: diagram > table > minimal prose. Then
proceed to the build steps below; the per-step flow diagrams show each piece
joining the map you just drew.

## Per step

1. `## Step N — <what this step achieves>`
2. The exact change, fully copy-paste-ready: one fenced `bash` block
   (heredocs for file content; `>>` appends for building files in
   sections — large files MUST be sectioned, see "Writing the bash
   blocks") — or, when the project is edited in an editor rather than
   via shell, a fenced code block of the new/changed code with enough
   surrounding context to place it unambiguously.
3. `**Simple:**` one sentence, plain words, what the command does.
4. A detailed explanation ("Slow walkthrough" when the user asked for
   extra-simple): why this design, where each parameter value flows, what
   would break without it. Define every jargon term descriptively at first
   use — "connector — a pre-built bridge that lets Claude read another
   app's data". Never use an unexplained term. Prefer everyday analogies.
5. **A flow diagram** whenever the step creates or changes a function that
   other code calls, or that reads/writes a shared file. See below.

## Flow diagrams — required in slow walkthroughs

When a step adds or changes anything other parts of the project touch, draw
the flow as plain text. The reader should be able to answer "what calls
this, what does it call, and what information moves between them?" without
opening a single file.

Rules:

- **Label every arrow with what is actually flowing**, in plain words — "the
  routing decision", "which folder to write to" — never a type name or an
  internal term.
- **Show the reach beyond the step**: which existing script, config file, or
  output directory each end connects to. New code in isolation is not the
  point; how it joins the system is.
- **Mark what is new or changed** in this step (e.g. `← NEW`), so the reader
  can see their own work inside the wider picture.
- **Follow the diagram with a short prose reading of it** — two or three
  sentences walking the path in order, in the same plain language.
- Keep it small. One diagram per step at most, only the parts that matter.

Example of the expected shape and labelling (illustrative — from a
pipeline project):

```
config/settings.yaml
   │  folder names + which workspace to use
   ▼
load_config(workspace)  ← CHANGED: now takes a workspace name
   │  settings, plus the chosen workspace
   ├────────────► wpath(cfg, "ocr")  ← NEW: builds one path
   │                  │  e.g. tests/.workspace/ocr/
   ▼                  ▼
triage.py main()   ocr.py main()
   │  the verdict for each file      │  repaired PDFs + recognised text
   ▼                                 ▼
manifest.json  ──── read by ────►  corpus/ocr/
```

Then read it aloud in prose: "The settings file says which workspace to
use. `load_config` reads it and remembers the choice; `wpath` turns a short
name like *ocr* into a full folder path on that workspace. Triage writes
each file's verdict into the manifest, and every later stage reads that
manifest rather than deciding again."

## Writing the bash blocks

- **Before closing any fenced block containing shell, check its final
  line.** Stray `</parameter>` tags have leaked into long final blocks
  before — the tool-call syntax shares its shape with a fenced block, so
  the wrong closer sometimes wins. It has always happened in the LAST,
  LONGEST block of a long walkthrough. Nothing but an explicit check
  catches it; the user finds out as a shell parse error.
- **Prefer several short blocks over one long `&&` chain.** When one link
  of a chain fails, the later links never run, so the diagnostic output the
  user needs is exactly what they lose. Chain only when a later command is
  genuinely meaningless if an earlier one failed, and keep it to two.
- **Never ship a large file as one heredoc — build it in sections.** This
  failed in practice (2026-08-17, MCP-server walkthrough): a ~250-line
  heredoc paste lost its closing delimiter to terminal/clipboard clipping,
  and the shell sat waiting at `heredoc>` with nothing written. Cap each
  block at roughly 60–80 lines. The first block is `cat > file <<'EOF'`;
  every later one appends with `cat >> file <<'EOF'`. Cut along coherent
  units — docstring + imports; one function group; the entry point — never
  mid-function, so each block is readable on its own and the accompanying
  explanation can walk that unit. Number the blocks ("Block 2 of 4") so a
  re-paste is unambiguous.
- **Follow every sectioned build with an assembly check** before anything
  runs: `wc -l` with the expected ballpark ("roughly 250 — the ballpark
  matters"), then a parse check (`python -c "import ast;
  ast.parse(open('f').read())"` or the language's equivalent). A syntax
  error's line number localises which block got clipped; the fix is to
  rebuild from Block 1 — appends make partial repair ambiguous.
- **State the recovery rule once per walkthrough**: a `heredoc>`
  continuation prompt after pasting means the paste was clipped — Ctrl-C
  is safe (the shell reads the whole heredoc before the redirect ever
  touches the file), then re-paste. This is also why sectioned builds are
  safe: an aborted block leaves the file exactly as the previous block
  left it.

## Finish with

- A **payoff test step**: a command or action that demonstrates the new
  thing working, with expected results stated concretely — measured
  numbers ("expect roughly X; the gap matters, not the absolute number")
  or observable behaviour ("the slider should now do Y"). Split
  verification into separate blocks (run it / inspect the result) rather
  than one chained command.
- Ask the user to report the actual results back — observed or measured
  results feed tuning and belong in commit messages and DECISIONS.md.
- A suggested `git commit` command including any measured/observed results.

## Calibration notes

- The user once asked for a redo because explanations were too
  jargon-heavy. When in doubt, simpler.
- If a step's result surprises, diagnose it WITH the user — show a quick
  verification command before presenting the fix, and record the finding
  in the code's docstring and DECISIONS.md.
