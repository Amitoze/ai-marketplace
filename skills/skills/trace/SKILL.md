---
name: trace
description: Map the data flow through a file or workflow — inputs, transformations, outputs, and where each field/value is born — diagram-first, then tables, minimal prose. Use for /trace <file>, "trace X", "how does data flow through X", or BEFORE building something to preview its data path.
---

Produce a data-flow map of one file or workflow (existing or proposed):
what goes in, how it is transformed, what comes out, and where every
field/value on the output is born. The user's benchmark is understanding,
not code shipped — a trace exists so a built (or about-to-be-built)
artifact never outruns their mental model of it.

## Two modes

- **Existing thing** (`/trace scripts/foo.py`): read the file and the real
  things it touches, then map what it actually does.
- **Before it's built** (`/trace` on a plan item, or invoked from a
  walkthrough): map the *intended* data path from the plan and the
  surrounding system, before any code exists. This is the high-value case
  — a bad data path (a value with no source, a config knob nothing will
  read, an ordering hazard) is far cheaper to catch here than after
  building.

## Ground it first — never trace from imagination

1. **Existing thing:** read it in full. Then read the real things it reads
   and writes — the sibling scripts it imports, the config, the
   input/output files — enough to name actual sources, not guess them.
2. **Before it's built:** read the plan item (and its "In plain terms"
   block), the config the artifact will use, and the existing pieces it
   will call or whose output it consumes. Trace the path those imply.
3. Either way, if you can't source a value, say so — an honest "this
   value's origin is unclear" is the point of the exercise, not a gap to
   paper over.

## Representation priority: diagram > table > prose

Draw it wherever it can be drawn; tabulate the field-by-field detail; keep
prose to the minimum a diagram or table can't carry. The user rejected a
verbose stage-by-stage prose section — lead with pictures. Reserve prose for
a one-sentence purpose, jargon definitions, and the *why* behind a decision
that a diagram can't hold.

## The shape that works — adapt, don't pad

Use these parts; drop any that don't apply. Do not manufacture a section to
fill the template.

1. **What it's for — one sentence.** Plain words.
2. **Definitions.** Only the terms the reader needs, each defined
   descriptively at first use. A few lines, not a glossary.
3. **The big picture — an INPUTS → [thing] → OUTPUTS diagram.** Every input
   named with where it came from; every output named with what reads it
   next.
4. **Inside the run — a flow diagram.** The path through the thing: setup,
   the transformation with real judgement in it, the per-item loop, the
   write. Show measured effect where known. Label every arrow with what
   actually flows, in plain words — never a type name.
5. **The field table — where each field or value is born.** One row per
   output field: the field, its source, and the step that produced it.
   This is usually the single most useful part; make it complete.
6. **Decisions with real judgement — a compact table.** Only the choices a
   reader couldn't infer: the decision, what happens, and why. Skip the
   obvious.
7. **Honest flags found while tracing — a compact table.** Surface what the
   trace reveals: config set but never consumed (dead value), values that
   are always null here (deferred / filled elsewhere), silent-mismatch
   hazards. This is the standing "flag proactively" behaviour applied to
   data flow — it is often where the trace earns its keep.

## Rules

- **Diagram arrows carry plain-language cargo labels** and connect to the
  real system (which script/config/dir each end touches), so the reader
  answers "what calls this, what does it call, what moves between them?"
  without opening a file.
- **Before-it's-built traces flag design risks, not bugs** — a value the
  plan can't source, a config knob nothing will read, a coupling that pins
  order. Raise them before code hardens the mistake.
- **No line-by-line code narration.** Describe what data does, not how the
  code is written. Depth on one hop is available on request.
- **End with one concrete next move**, not a summary: offer to go a level
  deeper on the single hop with the most judgement in it, or to turn a flag
  into a quick fix.
