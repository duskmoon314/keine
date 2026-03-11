---
tag: agent-skills
---

- [Agent Skill Anti-Patterns](../2026-03-11-agent-skills-anti-patterns.md) — Common mistakes in skill authoring: overpermissioning, context bloat, hardcoded paths, vague descriptions, and single-responsibility violations.
- [Adding Agent Skills Support to an Agent Client](../2026-03-11-agent-skills-client-integration.md) — Client integration requires discovery, retrieval, loading policy, and execution controls aligned with progressive disclosure.
- [Agent Skills Core Concepts and Lifecycle](../2026-03-11-agent-skills-core-concepts.md) — Agent Skills use progressive disclosure: discover skills, activate relevant ones, and execute detailed instructions only when needed.
- [Optimizing Skill Descriptions for Trigger Accuracy](../2026-03-11-agent-skills-description-optimization.md) — Skill descriptions are the primary trigger signal; iterative query testing improves activation precision and reduces missed use cases.
- [Agent Skill Design Patterns](../2026-03-11-agent-skills-design-patterns.md) — Named patterns for structuring agent skill workflows: Read-Process-Write, Search-Analyze-Report, Wizard-Style, Template Generation, and others.
- [Evaluating Agent Skill Output Quality](../2026-03-11-agent-skills-output-evaluation.md) — Skill quality evaluation uses realistic test cases, clear assertions, and iteration on both instructions and supporting scripts.
- [Agent Skills Overview and Value](../2026-03-11-agent-skills-overview.md) — Agent Skills are an open, file-based format for giving agents reusable capabilities through on-demand instructions and resources.
- [Project-Local vs Global Skill Installation Scope](../2026-03-11-agent-skills-scope-project-vs-global.md) — Skills can be installed at project scope (committed to the repo) or globally (per-user). Each scope has distinct use cases and trade-offs.
- [Using Scripts in Agent Skills](../2026-03-11-agent-skills-scripts-patterns.md) — Scripts extend skills with deterministic automation, from one-off shell commands to reusable bundled tools.
- [What to Skillify: Criteria for Good Skill Candidates](../2026-03-11-agent-skills-skillification-criteria.md) — Not every task warrants a skill. Good candidates share traits: repetition, multi-step sequencing, domain expertise, and bundled resources.
- [Agent Skills Specification and Organization](../2026-03-11-agent-skills-specification.md) — The Agent Skills spec defines a minimal folder format, required metadata, and conventions for portable skill packaging.