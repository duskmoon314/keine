---
title: "Project-Local vs Global Skill Installation Scope"
description: "Skills can be installed at project scope (committed to the repo) or globally (per-user). Each scope has distinct use cases and trade-offs."
tags: ["agent-skills", "skill-authoring", "skill-integration"]
source: "https://skywork.ai/blog/how-to-use-skills-in-claude-code-install-path-project-scoping-testing/"
source_type: "url"
---
# Project-Local vs Global Skill Installation Scope

## Summary
Agent Skills can be installed at two distinct scopes: project-local (inside the repo, committed to version control) or global (in the user's home config directory, available across all projects). Choosing the right scope is a fundamental decision that affects team sharing, token budget, and skill precedence. The guiding principle is: project scope for shared team workflows, global scope for personal utilities.

## Content

### The two paths

| Scope | Path (Claude Code) | Scope |
|---|---|---|
| Project-local | `<project>/.claude/skills/` | Only this project |
| Global | `~/.claude/skills/` | All projects, all sessions |

### When to use project-local scope
- Team-specific procedures that all contributors should follow (e.g., a deployment checklist, a PR review workflow)
- Project-specific conventions that don't generalize (e.g., company API naming rules, specific output formats)
- Skills that should be version-controlled alongside the code they describe
- When you want per-project overrides of global skills (project-local takes precedence on name collision)

### When to use global scope
- Personal utilities reflecting your own development style (e.g., a personal code review checklist)
- Reusable helpers that apply across all your projects (e.g., a generic research skill, a writing helper)
- Skills proven effective across many contexts before being shared

### Token budget considerations
Every installed skill contributes its `name` and `description` to every session's token budget (~30–50 tokens per skill). Global skills count toward every session; project skills only count within that project. Keep global installs lean.

### Conflict resolution
When both scopes define a skill with the same name, the project-local skill wins. This enables: define a global default, override per-project as needed.

### Recommended workflow
1. Author a new skill at project scope first.
2. Validate effectiveness across real usage.
3. Promote to global only if it genuinely applies across multiple unrelated projects.

## Related
- [Agent Skills Overview and Value](./2026-03-11-agent-skills-overview.md)
- [Agent Skills Specification and Organization](./2026-03-11-agent-skills-specification.md)
- [agent-skills map](./maps/agent-skills.md)
