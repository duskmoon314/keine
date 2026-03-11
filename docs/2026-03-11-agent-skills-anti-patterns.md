---
title: "Agent Skill Anti-Patterns"
description: "Common mistakes in skill authoring: overpermissioning, context bloat, hardcoded paths, vague descriptions, and single-responsibility violations."
tags: ["agent-skills", "skill-authoring", "skill-evaluation"]
source: "https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/"
source_type: "url"
---
# Agent Skill Anti-Patterns

## Summary
Several failure modes appear repeatedly in poorly designed skills. Recognizing them by name allows authors to avoid them during design and catch them during review. Most anti-patterns have a straightforward fix.

## Content

### Overpermissioning
Granting access to tools the skill does not actually use. This expands the attack surface unnecessarily. Fix: audit `allowed-tools` and restrict to exactly what the workflow requires (e.g., `Bash(git:*)` instead of unrestricted `Bash`).

### Context bloat
Embedding large documentation, full API references, or extensive examples directly in `SKILL.md`. This loads heavy content into the context window on every skill activation. Fix: move verbose material to `references/` and link it; the agent loads it only if needed.

### Hardcoded paths
Using absolute paths (e.g., `/home/user/project/`) inside skill instructions or scripts. This makes the skill non-portable across machines, users, and CI environments. Fix: use relative paths or the `{baseDir}` variable convention.

### Hidden operation
Executing Bash commands or making side-effecting operations without communicating clearly to the user what is happening. This erodes trust and makes debugging difficult. Fix: write skill instructions that surface what commands will be run and what their effect is.

### Vague descriptions
Descriptions that are too generic to reliably trigger the skill for the right tasks, or too broad and cause false positives. Example: "This skill helps with code." Fix: write concrete, action-oriented descriptions that specify both what the skill does and when it should be used.

### Single-responsibility violation
Bundling unrelated workflows into a single skill because they seem superficially related. This produces confusing instructions and poor trigger accuracy. Fix: split into separate, focused skills.

### Over-specialization
Creating skills for tasks better served by direct tool use. If a task requires one Read and one Write call with no domain-specific guidance, there is no need for a skill. Fix: reserve skills for tasks where procedural or domain knowledge genuinely adds value.

### Concurrency assumption
Designing skills that assume serial execution or that share mutable state. Skills are not concurrency-safe. Fix: treat each skill invocation as independent; avoid designs that depend on shared in-progress state across concurrent agent runs.

## Related
- [Agent Skills Specification and Organization](./2026-03-11-agent-skills-specification.md)
- [Evaluating Agent Skill Output Quality](./2026-03-11-agent-skills-output-evaluation.md)
- [What to Skillify: Criteria for Good Skill Candidates](./2026-03-11-agent-skills-skillification-criteria.md)
- [skill-authoring tag](./tags/skill-authoring.md)
- [skill-evaluation tag](./tags/skill-evaluation.md)
- [agent-skills map](./maps/agent-skills.md)
