---
title: "Agent Skills"
tags: [agent-skills, skill-authoring, skill-integration]
---
# Agent Skills

## Overview
Agent Skills are a portable way to package operational knowledge for AI agents. The ecosystem centers on a simple folder structure with `SKILL.md` as the entry point, plus optional assets, scripts, and references. The key runtime idea is progressive disclosure: keep discovery lightweight, then load detailed instructions only when the task requires them.

## Landscape
### Foundations and mental model
Start with the broad framing and lifecycle:
- [Agent Skills Overview and Value](../2026-03-11-agent-skills-overview.md)
- [Agent Skills Core Concepts and Lifecycle](../2026-03-11-agent-skills-core-concepts.md)

### Structure and interoperability
Use the specification to standardize packaging and metadata:
- [Agent Skills Specification and Organization](../2026-03-11-agent-skills-specification.md)

### Authoring and quality loop
High-performing skills come from an iterative loop:
- [Optimizing Skill Descriptions for Trigger Accuracy](../2026-03-11-agent-skills-description-optimization.md)
- [Using Scripts in Agent Skills](../2026-03-11-agent-skills-scripts-patterns.md)
- [Evaluating Agent Skill Output Quality](../2026-03-11-agent-skills-output-evaluation.md)

### Runtime/client implementation
If you are building an agent product, add controlled runtime support:
- [Adding Agent Skills Support to an Agent Client](../2026-03-11-agent-skills-client-integration.md)

## Where to Start
- If you are new to the concept, read overview and lifecycle first.
- If you are writing skills, move from specification to description optimization and script patterns.
- If you are building a product, read client integration after understanding the core lifecycle.

## Learning Path
1. [Agent Skills Overview and Value](../2026-03-11-agent-skills-overview.md)
2. [Agent Skills Core Concepts and Lifecycle](../2026-03-11-agent-skills-core-concepts.md)
3. [Agent Skills Specification and Organization](../2026-03-11-agent-skills-specification.md)
4. [Optimizing Skill Descriptions for Trigger Accuracy](../2026-03-11-agent-skills-description-optimization.md)
5. [Using Scripts in Agent Skills](../2026-03-11-agent-skills-scripts-patterns.md)
6. [Evaluating Agent Skill Output Quality](../2026-03-11-agent-skills-output-evaluation.md)
7. [Adding Agent Skills Support to an Agent Client](../2026-03-11-agent-skills-client-integration.md)

## Entries
- [Agent Skills Overview and Value](../2026-03-11-agent-skills-overview.md): Open-standard framing, motivation, and ecosystem direction.
- [Agent Skills Core Concepts and Lifecycle](../2026-03-11-agent-skills-core-concepts.md): Folder anatomy and progressive disclosure lifecycle.
- [Agent Skills Specification and Organization](../2026-03-11-agent-skills-specification.md): Required metadata and structural conventions.
- [Optimizing Skill Descriptions for Trigger Accuracy](../2026-03-11-agent-skills-description-optimization.md): How to improve activation precision with query-driven iteration.
- [Using Scripts in Agent Skills](../2026-03-11-agent-skills-scripts-patterns.md): Patterns for one-off commands versus bundled reusable scripts.
- [Evaluating Agent Skill Output Quality](../2026-03-11-agent-skills-output-evaluation.md): Test design and iterative quality improvement.
- [Adding Agent Skills Support to an Agent Client](../2026-03-11-agent-skills-client-integration.md): Runtime integration patterns and policy controls.
