---
name: idea
description: Capture a raw product/feature/business idea into the global ideas file (~/.claude/ideas/IDEAS.md) — timestamped, auto-classified, zero questions asked. Use for /idea <thought>, "log this idea", "add to my ideas", or to read back ("show my ideas", "what business ideas do I have?").
---

Capture a fleeting idea with zero friction, or read the ideas file back.
The whole point is speed: the user fires a raw thought and moves on. Never
ask a clarifying question during capture — structure it yourself and let
them correct you in one word afterwards.

## Config

- **Ideas file:** `~/.claude/ideas/IDEAS.md` (single global file; change here
  if it ever moves)
- **Kind tags (fixed, pick exactly one):** `#product` `#feature` `#business`
  `#tooling`
- **Status tags:** `#spark` (new, the default) · `#framed` (promoted to a
  /frame dossier)

## Capture (`/idea <raw thought>`)

1. If the ideas file doesn't exist, create it (with its directory) starting
   with the header below, then continue — never overwrite an existing file:

   ```markdown
   # Ideas

   Captured by /idea. Newest first. `#spark` = raw, `#framed` = has a dossier.
   ```

2. Build one entry from the raw thought:
   - **Title:** ~5 words, concrete, written by you.
   - **Tags:** one kind tag, one or two free domain tags you invent
     (`#marketplace`, `#health`, …), and `#spark`.
   - **Body:** 1–3 sentences. Keep the user's own words where possible; add
     the mechanism or context only if the thought implies it. If they
     mentioned what prompted the idea, keep that — provenance helps later.

3. Insert the entry **directly under the header block** (newest first), in
   exactly this format:

   ```markdown
   ## 2026-08-22 — Studio-time rental marketplace
   `#business` `#marketplace` `#spark`
   Musicians rent idle recording-studio hours from owners; two-sided,
   utilization play. Came from noticing studios dark on weekdays.
   ```

4. If `~/.claude/ideas/` is a git repo, commit the append with message
   `idea: <title>`. If it isn't, skip silently — no nagging.

5. Echo the entry back verbatim so a misclassification can be fixed with one
   word ("that's a feature") — apply such a correction by editing the entry
   in place.

## Read-back ("show my ideas", "what X ideas do I have?")

Read the file, filter by whatever they asked (tag, keyword, date), and
present titles + one-liners — not the raw markdown. If they ask about a
theme rather than a tag, match on content, not just tags.

## Promotion

If the user decides to pursue an idea seriously, suggest `/frame` — the
ideas file is the inbox, the dossier is the workbench. When an idea gets a
dossier, flip its `#spark` to `#framed` and append the dossier slug to the
entry body.

## Rules

- Capture is append-only and edit-in-place; never reorder, rewrite, or
  delete other entries.
- Never ask questions before writing the entry. Wrong guesses are cheap;
  lost ideas are not.
- If the same-day file already has a near-identical entry, say so instead of
  appending a duplicate.
- Don't editorialize on idea quality during capture — this is an inbox, not
  a review.
