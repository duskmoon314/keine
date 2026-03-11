# Keine (Knowledge Base) -- Agent Guidelines

This is an agent-assisted knowledge base. All knowledge is Markdown in `docs/`.
Agents help users research, create, ingest, and connect knowledge.
The repo is managed with **git** and uses **uv** for Python tools.

## Structure

```
docs/
  <yyyy-mm-dd-slug>.md    - Individual knowledge entries
  tags/<slug>.md          - Tag index: lists docs with this tag
  maps/<slug>.md          - Topic map: structured overview of a topic and links to docs
```

## Skills

Read the relevant skill before performing any task. Skills are in
`.agents/skills/`.

## Core Rules

1. All knowledge MUST be `.md` under `docs/`. No exceptions.
2. No original files in repo. `source` in frontmatter links to originals.
3. Always search before creating to avoid duplicates.
4. Read the skill before acting. Skills define the full workflow.
