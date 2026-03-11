---
title: "What to Skillify: Criteria for Good Skill Candidates"
description: "Not every task warrants a skill. Good candidates share traits: repetition, multi-step sequencing, domain expertise, and bundled resources."
tags: ["agent-skills", "skill-authoring"]
source: "https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/"
source_type: "url"
---
# What to Skillify: Criteria for Good Skill Candidates

## Summary
A skill is only worth creating when the investment in packaging and maintaining it pays off through repeated reuse and improved reliability. The decision to "skillify" a workflow should follow a clear set of criteria. Tasks that are one-off, trivial, or fully handled by a single tool call are poor candidates. Tasks that are multi-step, domain-specific, repeated across sessions, or require bundled resources are strong candidates.

## Content

### The core heuristic
Complete the task once without a skill. Notice what context, instructions, or domain knowledge you repeatedly had to provide. If the same guidance would be useful in a future session for a similar task, package it as a skill.

### Strong skill candidates

**Multi-step workflows with clear sequencing**
Any procedure requiring multiple ordered steps benefits from explicit skill instructions. Without a skill, Claude must reconstruct the sequence from scratch each time, risking inconsistency. Examples: publishing a blog post, running a data pipeline, creating a knowledge base entry.

**Recurring domain expertise**
When tasks require specialized context that a general model lacks — legal review conventions, company-specific API patterns, internal style guides — a skill injects that expertise reliably. Examples: compliance review, internal documentation standards.

**Bundled resource workflows**
When a task depends on templates, reference documentation, or executable scripts, a skill can co-locate all of these so they are always available together. Examples: PDF report generation, code scaffolding from templates.

**Consistent-output-format tasks**
When the output must conform to a specific structure (report formats, PR descriptions, commit messages) every time, skill instructions enforce the template reliably.

**Permission-scoped operations**
When a task needs access to specific tools but should not have broader access, a skill's `allowed-tools` frontmatter can constrain the agent appropriately.

### Weak skill candidates (avoid skillifying these)

- **One-off tasks**: If you will never do this again, the authoring cost exceeds the benefit.
- **Simple tool operations**: A single read/write/search that needs no procedural guidance.
- **Highly variable tasks**: If each instance is significantly different, a general-purpose skill adds friction without benefit.
- **Trivially short instructions**: If the full guidance fits in a sentence, it belongs in CLAUDE.md or as a direct prompt, not a skill.
- **Tasks better handled by subagents**: If the task requires true isolation or a separate execution context, a subagent is the right primitive.

### The "repeated context" test
After any complex task, ask: "What information did I provide that I would provide again next time?" That information is skill material.

## Related
- [Agent Skills Overview and Value](./2026-03-11-agent-skills-overview.md)
- [Agent Skills Core Concepts and Lifecycle](./2026-03-11-agent-skills-core-concepts.md)
- [Agent Skill Design Patterns](./2026-03-11-agent-skills-design-patterns.md)
- [agent-skills map](./maps/agent-skills.md)
