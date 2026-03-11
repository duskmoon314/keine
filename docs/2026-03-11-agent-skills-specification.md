---
title: "Agent Skills Specification and Organization"
description: "The Agent Skills spec defines a minimal folder format, required metadata, and conventions for portable skill packaging."
tags: ["agent-skills", "skill-specification", "progressive-disclosure", "skill-authoring"]
source: "https://agentskills.io/specification"
source_type: "url"
---
# Agent Skills Specification and Organization

## Summary
The specification defines how a skill is structured so any compatible client can discover and execute it. It centers on a required `SKILL.md` file with YAML frontmatter and descriptive, procedural markdown content. The spec also formalizes optional support folders, metadata fields, and activation guidance. This creates predictable interoperability while still allowing flexible skill design.

## Content
### Required file and frontmatter
A valid skill includes a `SKILL.md` with frontmatter and markdown body. Core metadata includes:
- `name`: short lowercase-hyphenated identifier
- `description`: plain-language trigger description in third person

Optional fields support attribution and integrations:
- `version`
- `author`
- `license`
- `homepage`
- `tags`

### Body expectations
The body should define:
- When to use the skill
- Required inputs and constraints
- Explicit workflow steps
- Expected outputs and quality checks

### Optional folder conventions
The spec documents three common subdirectories:
- `assets/` for reusable templates and data
- `scripts/` for executable tooling
- `references/` for supplemental docs

### Organization principles from the spec
- Keep skills self-contained and portable.
- Use relative links when referencing local files.
- Make activation intent explicit in description text.
- Prefer concise top-level guidance with detail in linked files.

## Related
- [Agent Skills Core Concepts and Lifecycle](./2026-03-11-agent-skills-core-concepts.md)
- [Using Scripts in Agent Skills](./2026-03-11-agent-skills-scripts-patterns.md)
- [Optimizing Skill Descriptions for Trigger Accuracy](./2026-03-11-agent-skills-description-optimization.md)
- [skill-specification tag](./tags/skill-specification.md)
- [agent-skills map](./maps/agent-skills.md)

