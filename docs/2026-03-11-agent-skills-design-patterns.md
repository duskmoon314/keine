---
title: "Agent Skill Design Patterns"
description: "Named patterns for structuring agent skill workflows: Read-Process-Write, Search-Analyze-Report, Wizard-Style, Template Generation, and others."
tags: ["agent-skills", "skill-authoring", "skill-scripting"]
source: "https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/"
source_type: "url"
---
# Agent Skill Design Patterns

## Summary
Several recurring structural patterns emerge across well-designed agent skills. Naming these patterns helps authors select the right skeleton for a new skill and helps reviewers recognize what a skill is doing. The patterns are not mutually exclusive — complex skills often combine two or more.

## Content

### Read-Process-Write
The simplest general pattern. Load an input → apply transformation logic → write the result. Sufficient for many formatting, conversion, or normalization tasks. The processing step may be a direct model operation or a call to a bundled script.

### Search-Analyze-Report
Use Grep or search tools to find relevant patterns or files → read matches in depth → synthesize findings → produce a structured report. Effective for code audits, knowledge base research, and compliance checks.

### Script Automation
Offload deterministic, complex, or side-effecting operations to a script in `scripts/`. The `SKILL.md` handles decision logic and orchestration; the script handles computation, parsing, or I/O. Use this when the operation is too complex or fragile to describe purely in natural language.

### Command Chain Execution
Sequential shell commands with dependencies, executed in order. Example: `git pull && npm install && npm run lint && npm test`. Effective for CI-style local workflows where each step must succeed before the next.

### Wizard-Style Workflow
Break a complex task into discrete phases with explicit checkpoints or user confirmations between steps. Reduces error risk on irreversible operations. Example: a deployment skill that pauses for confirmation before each environment promotion.

### Template-Based Generation
Load a template from `assets/`, fill placeholders using task inputs or model reasoning, write the rendered output. Effective for boilerplate, documentation scaffolding, and consistent artifact creation.

### Iterative Refinement
Multiple passes over the same material: broad scan → deep analysis → recommendations → optional revision. Effective for review, editing, and quality improvement tasks where a single pass is insufficient.

### Context Aggregation
Pull information from multiple sources (files, APIs, search results) into a unified context before generating output. Effective when the answer requires synthesizing scattered information.

## Choosing a pattern
| Task type | Suggested pattern |
|---|---|
| Format/convert one file | Read-Process-Write |
| Find and summarize patterns | Search-Analyze-Report |
| Run complex automation | Script Automation |
| Sequential build/deploy steps | Command Chain |
| High-stakes irreversible ops | Wizard-Style |
| Consistent document creation | Template-Based Generation |
| Review and improve existing work | Iterative Refinement |
| Multi-source synthesis | Context Aggregation |

## Related
- [Using Scripts in Agent Skills](./2026-03-11-agent-skills-scripts-patterns.md)
- [Agent Skills Specification and Organization](./2026-03-11-agent-skills-specification.md)
- [What to Skillify: Criteria for Good Skill Candidates](./2026-03-11-agent-skills-skillification-criteria.md)
- [skill-authoring tag](./tags/skill-authoring.md)
- [agent-skills map](./maps/agent-skills.md)
