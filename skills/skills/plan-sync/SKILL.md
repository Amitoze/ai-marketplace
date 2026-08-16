---
name: plan-sync
description: Sync plan/ docs to the actual state of the repo — tick checkboxes, update the status table, sweep the session for unrecorded decisions, prompt for DECISIONS.md entries. Use after completing work, or when the user says "update the plan".
---

Bring `plan/` back in line with reality. This is mechanical except the
final step, which needs the user's judgement.

## Steps

1. **Establish what changed**: `git log --oneline` since the last plan
   update, plus `git status`, plus the current session's work.
2. **Tick checkboxes** in the relevant `plan/*.md` files — `[ ]` → `[x]`
   only for items genuinely done and verified (a gate is done when its
   condition was checked, not assumed — and if the project's gates are
   the user's call, a gate is done only when the user said so). Add a
   dated note where helpful (e.g. "(2026-08-13)").
3. **Update the status table** in `plan/00-context.md`: mark completed
   phases `✅ done <date>`, set the next phase to "next up", and update
   any deferred/gated-phase markers.
4. **Capture discussion insights**: if the session produced a design
   discussion worth keeping, add or extend an "In plain terms" section in
   the relevant plan file — simple language, jargon defined descriptively,
   placed above the terse checklist it explains.
5. **Prompt for DECISIONS.md**: list the session's judgement calls
   (tuned values with the results they produced, threshold findings with
   measured numbers, approaches tried and rejected, renames), and propose
   a dated entry for each. **Sweep the whole conversation, not just the
   work performed**: decisions made verbally in chat — a choice stated in
   one sentence, a recommendation accepted, a plan restructure — count
   even when no file changed at the time. The failure mode this guards:
   decide-in-chat, record-never, and the trail dies with the session.
   Ask the user which to record — the judgement of what is
   decision-worthy is theirs. Then append the approved entries.
6. **Report**: summarise what was ticked, updated, and recorded, with file
   links. Offer to commit (do not commit unasked). Flag uncommitted
   verified work once.

## Rules

- Never tick an unverified item to make the plan look tidy.
- Plan wording follows project terminology — use the project's own names
  for things, not generic jargon the plan doesn't use.
- Keep original checklist/intent text intact — plain-language additions
  sit alongside, never replace.
