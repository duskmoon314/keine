---
title: "Optimizing Skill Descriptions for Trigger Accuracy"
description: "Skill descriptions are the primary trigger signal; iterative query testing improves activation precision and reduces missed use cases."
tags: ["agent-skills", "skill-authoring", "skill-evaluation", "progressive-disclosure"]
source: "https://agentskills.io/optimizing-descriptions"
source_type: "url"
---
# Optimizing Skill Descriptions for Trigger Accuracy

## Summary
Agent Skills documentation treats the description field as the most important retrieval feature for automatic skill activation. Good descriptions improve both precision and recall by matching how users actually ask for help. The recommended approach is iterative and evidence-driven: collect representative prompts, test, and refine. Description tuning is therefore part of skill engineering, not cosmetic polish.

## Content
### Why description quality matters
Descriptions are often the first and strongest signal used by the model or client to decide whether to load a skill. A vague or overloaded description can cause both false positives and false negatives.

### Practical optimization loop
1. Draft a clear one-sentence description focused on problem and outcome.
2. Build a test set of realistic user queries that should and should not trigger the skill.
3. Run activation tests repeatedly across those queries.
4. Update wording to increase correct triggers while reducing accidental matches.
5. Keep a separate validation set to check generalization, not just memorization.

### Authoring guidance
- Prefer concrete verbs and domain terms users naturally use.
- Avoid broad phrasing that overlaps many unrelated skills.
- Keep the scope explicit so the model can disambiguate quickly.

## Related
- [Evaluating Agent Skill Output Quality](./2026-03-11-agent-skills-output-evaluation.md)
- [Agent Skills Core Concepts and Lifecycle](./2026-03-11-agent-skills-core-concepts.md)
- [skill-evaluation tag](./tags/skill-evaluation.md)
- [skill-authoring tag](./tags/skill-authoring.md)
- [agent-skills map](./maps/agent-skills.md)
