---
title: "Using Scripts in Agent Skills"
description: "Scripts extend skills with deterministic automation, from one-off shell commands to reusable bundled tools."
tags: ["agent-skills", "skill-authoring", "skill-scripting"]
source: "https://agentskills.io/using-scripts"
source_type: "url"
---
# Using Scripts in Agent Skills

## Summary
Scripts are the execution layer that turns skill instructions into repeatable automation. The guidance distinguishes lightweight one-off command snippets from packaged scripts stored with the skill. Bundled scripts are preferred for non-trivial workflows because they improve maintainability, reuse, and testability. Skills should keep script dependencies explicit and local so behavior stays portable.

## Content
### Two script usage styles
- One-off commands inside `SKILL.md`: useful for simple, short actions.
- Reusable files in `scripts/`: preferred for multi-step or logic-heavy tasks.

### Why bundle scripts with the skill
- Better version control and code review for operational logic.
- Reuse across many runs without re-writing commands.
- Easier local testing and CI-style validation.

### Portability recommendations
- Keep scripts self-contained.
- Declare dependencies clearly.
- Use relative paths to files in the same skill folder.
- Document expected inputs and outputs.

### Authoring pattern
Use `SKILL.md` for orchestration and decision logic, then call scripts for deterministic work such as parsing, normalization, transformation, and reporting.

## Related
- [Agent Skills Specification and Organization](./2026-03-11-agent-skills-specification.md)
- [Evaluating Agent Skill Output Quality](./2026-03-11-agent-skills-output-evaluation.md)
- [skill-scripting tag](./tags/skill-scripting.md)
- [skill-authoring tag](./tags/skill-authoring.md)
- [agent-skills map](./maps/agent-skills.md)

