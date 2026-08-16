# Personal skills marketplace

This repo is a personal Claude Code plugin marketplace: the single source of truth for
skills shared across all my projects and machines. Skills are promoted here from
project-local `.claude/skills/` folders once they prove useful in more than one project.

- Install once per machine: `/plugin marketplace add <you>/claude-marketplace` then `/plugin install skills`
- Update flow: edit → push → Claude Code auto-syncs (see diagram below)
- Docs: [Plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces) · [Plugins reference](https://code.claude.com/docs/en/plugins-reference) · [Skills](https://code.claude.com/docs/en/skills)

## Repo layout

One plugin per component type. Only `skills` has content so far; the others are empty
scaffolds ready to be filled (install them once they have something in them).

```text
claude-marketplace/
├── .claude-plugin/marketplace.json   ← the catalog (lists all plugins below)
├── skills/                           ← /skills:<name> — workflow skills
│   ├── .claude-plugin/plugin.json
│   └── skills/<skill-name>/SKILL.md
├── agents/                           ← custom subagent definitions (agents/*.md)
├── hooks/                            ← event-driven automation (hooks/hooks.json)
├── mcp-servers/                      ← bundled MCP configs (.mcp.json at plugin root)
├── lsp-servers/                      ← language server configs
└── monitors/                         ← background watchers
```

Every plugin folder has its own `.claude-plugin/plugin.json` (no `version` field — see
rule 1 below). To add a skill: create `skills/skills/<name>/SKILL.md`, commit, push.

## Two rules that make auto-sync work

1. **Omit the `version` field** in `plugin.json` and `marketplace.json`. The plugin's
   version then falls back to the git commit SHA, so every push is automatically a new
   version. If you set `"version": "1.0.0"` and forget to bump it, pushes silently stop
   propagating.
2. **Use an SSH remote if the repo is private.** The background auto-update pull disables
   HTTPS credential helpers; an SSH key in `ssh-agent` works normally. (Public repo: no
   issue either way.)

## The flow

```text
PHASE 1 — ONE-TIME SETUP
════════════════════════

┌─────────────────────────────────────┐
│ 1. Create the marketplace repo      │
│    my-skills/                       │
│    ├── .claude-plugin/              │
│    │   └── marketplace.json         │  ← catalog: lists your plugins
│    └── my-plugin/                   │
│        ├── .claude-plugin/          │
│        │   └── plugin.json          │  ← NO "version" field (important!)
│        └── skills/                  │
│            ├── trace/SKILL.md       │
│            └── plan-sync/SKILL.md   │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 2. Push to GitHub                   │
│    git init / commit / push         │
│    (private repo? use SSH remote    │
│     so auto-update can pull)        │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 3. Register it (once per machine)   │
│    /plugin marketplace add          │
│        you/my-skills                │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ 4. Install the plugin               │
│    /plugin install my-plugin        │
│    → copied to ~/.claude/plugins/   │
│      cache, skills now available    │
│      as /my-plugin:trace etc.       │
│      in EVERY project               │
└─────────────────────────────────────┘


PHASE 2 — UPDATING A SKILL (the everyday loop)
══════════════════════════════════════════════

        ┌──────────────────────────────┐
   ┌───▶│ Edit SKILL.md in the repo    │
   │    └──────────────┬───────────────┘
   │                   │
   │                   ▼
   │         ┌───────────────────┐
   │         │ Happy with it?    │
   │         └────┬─────────┬────┘
   │           no │         │ yes
   │              ▼         │
   │  ┌─────────────────┐   │
   └──┤ Test locally:   │   │
      │ claude          │   │
      │  --plugin-dir   │   │
      │  ./my-plugin    │   │
      │ (reads straight │   │
      │  from disk, no  │   │
      │  push needed)   │   │
      └─────────────────┘   │
                            ▼
      ┌─────────────────────────────────┐
      │ git commit && git push          │
      └──────────────┬──────────────────┘
                     │
  ═══════════════════╪═══════════════════════════
   everything below  │  happens WITHOUT you
  ═══════════════════╪═══════════════════════════
                     ▼
      ┌─────────────────────────────────┐
      │ Background auto-update:         │
      │ Claude Code git-pulls the       │
      │ marketplace repo periodically   │
      └──────────────┬──────────────────┘
                     │
                     ▼
      ┌─────────────────────────────────┐
      │ Version check:                  │
      │ no "version" field              │
      │   → version = commit SHA        │
      │   → new commit = new version    │
      └──────────────┬──────────────────┘
                     │
                     ▼
      ┌─────────────────────────────────┐
      │ Cache refreshed:                │
      │ ~/.claude/plugins/cache gets    │
      │ the new copy                    │
      └──────────────┬──────────────────┘
                     │
                     ▼
      ┌─────────────────────────────────┐
      │ Every NEW session, on every     │
      │ machine with the marketplace    │
      │ added, uses the updated skill   │
      └─────────────────────────────────┘

  Impatient? skip the wait:  /plugin marketplace update amitoz-marketplace
                             /plugin update skills
```

## Notes

- Sessions that are already open keep the skill version they loaded; updates land in the
  next session.
- Plugin skills are namespaced (`/my-plugin:trace`), so a project can still keep its own
  specialized `/trace` in `.claude/skills/` without conflict.
- Promotion rule of thumb: a skill graduates from a project into this repo once it's
  used (or copy-pasted) in a second project.
