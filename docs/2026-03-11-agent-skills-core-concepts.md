---
title: "Agent Skills Core Concepts and Lifecycle"
description: "Agent Skills use progressive disclosure: discover skills, activate relevant ones, and execute detailed instructions only when needed."
tags: ["agent-skills", "ai-agents", "progressive-disclosure", "skill-authoring"]
source: "https://agentskills.io/what-are-skills"
source_type: "url"
---
# Agent Skills Core Concepts and Lifecycle

## Summary
Agent Skills combine model intelligence with externalized procedural knowledge. The central runtime idea is progressive disclosure: list what skills exist, activate only the relevant skill, and expose detailed instructions at execution time. This keeps context focused while still allowing deep domain workflows. Skill folders also support modular resources such as templates, references, and scripts.

## Content
### Canonical skill folder pattern
Agent Skills are directory-based. A typical skill includes `SKILL.md` plus optional resources.

```text
my-skill/
  SKILL.md
  assets/
  scripts/
  references/
```

### Progressive disclosure workflow
The documented lifecycle is:
1. Discovery: the agent sees skill names and short descriptions.
2. Activation: the agent opens the selected skill file only when it decides the skill is relevant.
3. Execution: full instructions and resources are loaded and followed.

### Why this lifecycle matters
- It limits context bloat by not loading every skill at once.
- It keeps skills modular and composable.
- It improves relevance and model focus during complex tasks.

### Role of `SKILL.md`
`SKILL.md` is the control point for trigger conditions and workflow instructions. High-quality descriptions determine when a skill is selected; clear step-by-step instructions determine how reliably it executes.

## Related
- [Agent Skills Overview and Value](./2026-03-11-agent-skills-overview.md)
- [Agent Skills Specification and Organization](./2026-03-11-agent-skills-specification.md)
- [Optimizing Skill Descriptions for Trigger Accuracy](./2026-03-11-agent-skills-description-optimization.md)
- [agent-skills tag](./tags/agent-skills.md)
- [progressive-disclosure tag](./tags/progressive-disclosure.md)
- [agent-skills map](./maps/agent-skills.md)
