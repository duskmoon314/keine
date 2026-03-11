---
title: "Adding Agent Skills Support to an Agent Client"
description: "Client integration requires discovery, retrieval, loading policy, and execution controls aligned with progressive disclosure."
tags: ["agent-skills", "skill-integration", "progressive-disclosure", "ai-agents"]
source: "https://agentskills.io/adding-skills-support"
source_type: "url"
---
# Adding Agent Skills Support to an Agent Client

## Summary
Client-side support turns Agent Skills from static files into runtime capability. The documented integration model follows progressive disclosure: discover available skills, let the model choose relevance, and load details only when needed. Implementations also need safety guardrails around script execution and environment access. A robust client balances autonomy, transparency, and policy control.

## Content
### Integration stages
1. Discover available skills from configured locations.
2. Expose name and description metadata to the model.
3. Decide activation strategy (model-driven, explicit invocation, or hybrid).
4. Load `SKILL.md` and related files only for selected skills.
5. Execute instructions and optional scripts under client policies.

### Activation strategies
- Model-driven invocation: dynamic and flexible, requires good descriptions.
- Explicit invocation: user/tool chooses skill directly, strong control.
- Hybrid: combine explicit controls with model recommendation.

### Runtime concerns
- Trust boundaries for third-party skills
- Script permissioning and sandboxing
- Logging for observability and debugging
- Caching and deduplication of loaded content

### Design goal
Keep the integration minimal but predictable: small metadata at discovery time, full instructions at execution time, and explicit policy enforcement for side effects.

## Related
- [Agent Skills Core Concepts and Lifecycle](./2026-03-11-agent-skills-core-concepts.md)
- [Agent Skills Specification and Organization](./2026-03-11-agent-skills-specification.md)
- [skill-integration tag](./tags/skill-integration.md)
- [agent-skills map](./maps/agent-skills.md)
