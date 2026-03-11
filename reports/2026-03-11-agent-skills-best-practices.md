---
title: "Research Report: Agent Skills Best Practices"
question: "I want a deep research on agent skills. What is the best practice of using agent skills? What should be transformed into skills? Should skills be project related or globally installed?"
---
# Research Report: Agent Skills Best Practices

## Research Question

What are the best practices for agent skills? What types of work should be transformed into skills? Should skills be project-scoped or globally installed? This report synthesizes knowledge base entries with current web sources to provide a comprehensive, actionable guide.

## Executive Summary

Agent Skills are a file-based format for packaging reusable procedural knowledge so AI agents can apply it reliably without being re-instructed every session. The decision to create a skill should be driven by repetition, multi-step complexity, and domain specificity — not novelty or simplicity. The project vs. global scope decision maps cleanly to whether the skill belongs to a team (project) or a person (global). Good skill design follows the principle of progressive disclosure: tiny metadata at discovery, full instructions only when the skill is activated, and external references for heavy content. The most common mistakes — vague descriptions, context bloat, overpermissioning, and hardcoded paths — each have straightforward fixes. The field has matured rapidly; Anthropic now treats Agent Skills as an open interoperability standard, and the authoring patterns are well-established.

---

## 1. What Are Agent Skills and Why They Matter

Agent Skills are directory-based packages that combine a `SKILL.md` control file with optional scripts, assets, and reference documents [KB-1]. Unlike CLAUDE.md (always-loaded project context) or one-shot prompts (ephemeral, conversational), skills are loaded on demand — only when the model determines the skill is relevant to the current task [KB-2].

This distinction matters because it solves a fundamental tension in AI-assisted work: models are broad generalists, but real workflows are specific. A general-purpose model can write code, but it doesn't know your company's deployment checklist, your team's PR review conventions, or your preferred report format — unless you tell it, every time [KB-1]. Skills package that domain knowledge once and inject it consistently across sessions and users.

The runtime architecture uses **progressive disclosure** [KB-3]:
1. At session start, the agent sees only each skill's `name` and `description` (~30–50 tokens per skill).
2. When a task matches a skill, the agent reads the full `SKILL.md`.
3. Scripts, templates, and reference documents in subdirectories are loaded only when explicitly needed.

This means a well-structured skill library imposes minimal token overhead at startup while still enabling rich, deep workflows on demand.

---

## 2. What to Skillify: Criteria for Good Skill Candidates

Not every task benefits from a skill. The investment in authoring, testing, and maintaining a skill must be paid back through reuse and reliability gains [KB-7].

### The Repeated-Context Test

The most reliable heuristic: complete the task once without a skill, noticing what context, instructions, or domain knowledge you had to provide [W-1]. If the same information would be needed in a future session for a similar task, that information is skill material. The test reveals actual reuse value rather than speculative value.

### Strong Candidates

**Multi-step workflows with clear sequencing.** Any procedure requiring ordered steps benefits from explicit skill instructions. Without a skill, the agent reconstructs the sequence from scratch each time, risking inconsistency. Publishing a document, running a data pipeline, creating a knowledge base entry, and executing a deployment checklist are all examples [KB-7][W-2].

**Recurring domain expertise.** Tasks requiring specialized context a general model lacks — legal review conventions, internal naming rules, compliance requirements, company-specific API patterns — benefit enormously from a skill that injects this expertise reliably every time.

**Bundled resource workflows.** When a task depends on templates, reference docs, or executable scripts, a skill co-locates all of these so they are always available together. PDF report generation, code scaffolding from templates, and knowledge ingestion workflows are canonical examples [KB-5][KB-7].

**Consistent-output-format tasks.** When output must conform to a specific structure every time — PR descriptions, commit messages, status reports — a skill's template instructions enforce this reliably, avoiding format drift across sessions.

**Permission-scoped operations.** When a task needs specific tools but should not have broader access, a skill's `allowed-tools` frontmatter constrains the agent precisely, improving both security and auditability [W-2].

### Weak Candidates (Do Not Skillify These)

- **One-off tasks**: The authoring cost exceeds the benefit if you will never repeat this.
- **Simple tool operations**: A single read/write/search with no domain guidance needs no skill.
- **Highly variable tasks**: If each instance is significantly different, a general skill adds friction without benefit.
- **Trivially short instructions**: If the full guidance fits in one sentence, it belongs in CLAUDE.md or as a direct prompt.
- **Tasks better suited to subagents**: If true isolation or a separate execution context is needed, a subagent is the right primitive — not a skill [W-1].

The anti-pattern of over-skillifying is underappreciated. A bloated skill library with dozens of rarely-used, overlapping skills degrades trigger accuracy and adds maintenance burden without proportional benefit [KB-8].

---

## 3. Project-Local vs. Global: The Scope Decision

This is perhaps the most practically important decision in skill management. The answer is almost always clear once you apply a single principle:

> **Project scope for team workflows. Global scope for personal utilities.**

### Project-Local Scope (`<project>/.claude/skills/`)

Project-local skills live inside the repository and are committed to version control. This means:

- **Team sharing**: Everyone who checks out the repo gets the same skills [KB-9][W-3].
- **Per-project specificity**: Different projects can have entirely different skill sets without conflict.
- **Version-controlled operational knowledge**: Skill changes are reviewed alongside code changes.
- **Override precedence**: When a project-local skill shares a name with a global skill, the project-local version wins [KB-9].

Use project scope for: deployment workflows, code review conventions, internal documentation standards, report templates, anything that belongs to the project as much as the code does.

### Global Scope (`~/.claude/skills/`)

Global skills are available in every session, regardless of which project is active. This makes them ideal for:

- **Personal style preferences**: A code review checklist that reflects your own standards, not team standards.
- **Cross-project utilities**: Research workflows, writing helpers, generic report generation.
- **Proven, widely-applicable patterns**: Skills that have already demonstrated value across multiple unrelated projects.

The token cost consideration is non-trivial: every global skill contributes its metadata to every session's token budget [KB-9]. A user with 30 global skills pays that overhead on every interaction, even when none of those skills are relevant. Keep global installs lean and intentional.

### Recommended Workflow

1. Author the skill at **project scope** first.
2. Use it across real tasks to validate effectiveness.
3. Promote to **global** only after confirming the skill generalizes across multiple unrelated projects.
4. When in doubt, prefer project scope — it's easier to promote than to demote.

---

## 4. Best Practices for Skill Design

### 4.1 The `SKILL.md` Structure

The specification requires a `SKILL.md` with YAML frontmatter and a markdown body [KB-4]. The frontmatter critical fields are:

```yaml
name: my-skill-name        # lowercase, hyphen-separated, ≤64 chars
description: "Use this skill when..."  # ≤1024 chars, the primary trigger signal
```

Optional but important:
```yaml
allowed-tools: Read,Write,Bash(git:*)   # minimize to exactly what's needed
```

The body should define: when to use the skill, required inputs and constraints, workflow steps in order, and expected outputs and quality checks [KB-4].

### 4.2 Writing Descriptions That Trigger Accurately

The description field is the primary mechanism by which the model decides whether to load a skill [KB-6]. Claude uses language understanding — not embeddings or algorithmic matching — to compare user intent against skill descriptions. This has direct implications:

- Write descriptions in natural human language that mirrors how users ask for help.
- Be concrete and action-oriented: "Use this skill when the user wants to create a knowledge base entry from a URL or PDF."
- Avoid vague, generic descriptions: "Helps with content" is useless as a trigger signal.
- Make the scope explicit so the model can disambiguate between similar skills quickly.

The recommended development loop [KB-6]:
1. Draft a clear one-sentence description focused on problem and outcome.
2. Build a set of realistic queries that should and should not trigger the skill.
3. Test activation against those queries.
4. Refine wording; repeat.

### 4.3 Progressive Disclosure in Practice

Keep `SKILL.md` under 5,000 words. Heavy content belongs in subdirectories [W-2]:

- `scripts/`: Executable automation — deterministic operations better expressed in code than prose.
- `references/`: Verbose documentation, API references, style guides — loaded into context on demand.
- `assets/`: Templates and binary files — referenced by path but not loaded into context automatically.

This structure keeps activation cost low while enabling richly detailed execution.

### 4.4 The Claude A / Claude B Development Method

The most effective authoring approach: use one Claude instance ("Claude A") to design and refine the skill, and a separate instance ("Claude B") to test it on real tasks [W-1]. Claude A understands how to write effective agent instructions. Claude B reveals gaps through real usage rather than assumptions. The cycle is: observe → refine → test → repeat.

### 4.5 Permission Minimization

`allowed-tools` should list exactly the tools the skill needs, with specific scoping where possible. `Bash(git:*)` is better than `Bash`. `Read,Write` is better than `Read,Write,Bash,WebFetch` for a skill that only reads and writes files [W-2]. Over-permissioning expands the attack surface and reduces auditability.

---

## 5. Named Design Patterns

Several structural patterns recur across well-designed skills [KB-10][W-2]. Recognizing them helps authors choose the right skeleton:

| Pattern | When to use |
|---|---|
| **Read-Process-Write** | Format/convert/normalize a file |
| **Search-Analyze-Report** | Find patterns across files, synthesize findings |
| **Script Automation** | Complex deterministic logic offloaded to `scripts/` |
| **Command Chain** | Sequential shell steps with dependencies |
| **Wizard-Style** | High-stakes irreversible ops requiring confirmation |
| **Template-Based Generation** | Consistent document/artifact creation from templates |
| **Iterative Refinement** | Review and improve existing work across multiple passes |
| **Context Aggregation** | Synthesize from multiple sources before generating output |

The `keine-research` skill used in this project is a good example of a **Search-Analyze-Report + Template-Based Generation** hybrid: mine the KB, fill gaps with web research, produce a structured long-form report.

---

## 6. Anti-Patterns to Avoid

These failure modes appear frequently and have documented fixes [KB-8]:

**Vague descriptions.** The most common and costly mistake. If the description doesn't reliably match user intent, the skill won't trigger when needed and may trigger when irrelevant.

**Context bloat.** Embedding large documentation in `SKILL.md` itself loads heavy content on every activation. Move verbose material to `references/`.

**Overpermissioning.** Listing all available tools in `allowed-tools` when the skill uses only two. Restrict permissions to exactly what's required.

**Hardcoded paths.** Absolute paths break portability across machines and environments. Use relative paths or `{baseDir}` variables.

**Hidden operation.** Executing Bash commands or making side-effecting operations without communicating clearly what is happening. Skills should surface their actions.

**Single-responsibility violation.** Combining unrelated workflows in one skill to avoid creating a second file. Split them.

**Concurrency assumption.** Skills are not concurrency-safe. Do not design workflows that depend on shared in-progress state across parallel agent runs.

---

## 7. Skills vs. Adjacent Mechanisms

Understanding where skills fit helps avoid misusing them [W-1]:

| Mechanism | Persistence | Scope | Best for |
|---|---|---|---|
| `SKILL.md` | Session (on demand) | Skill-defined | Reusable domain workflows |
| `CLAUDE.md` | Always loaded | Project/global | Permanent project context |
| Prompt | Ephemeral | Conversation | One-time instructions |
| Subagent | Independent | Isolated | Self-contained parallel work |
| MCP Server | Persistent | Tool-level | External service integration |

Skills and subagents compose well: a subagent can have its own skills for specialized expertise while operating independently from the main agent [W-1].

---

## 8. Synthesis

The core insight running through all of this is that **skills externalize procedural knowledge that would otherwise live in the user's head or be repeated in every conversation**. The decision tree is:

1. Is this task repeated? If no → direct prompt. If yes → consider a skill.
2. Does this task require multi-step guidance or domain expertise? If no → CLAUDE.md or direct prompt. If yes → skill candidate.
3. Does this skill belong to a team or a project? If yes → project scope. If no → global scope.
4. Is this skill proven across multiple unrelated contexts? If yes → consider promoting to global.

The quality of the description field determines whether the right skill gets loaded. The quality of the workflow instructions determines whether the skill produces the right output. Both must be iterated on based on real usage, not assumptions. The evaluation loop — baseline without skill, comparison with skill, analyze delta, refine — is the mechanism that separates high-performing skills from mediocre ones.

---

## 9. Gaps and Open Questions

- **Skill discoverability across organizations**: As skill libraries grow, how do teams discover skills authored by other teams? The ecosystem currently relies on manual sharing and community registries.
- **Versioning and deprecation**: The specification has minimal guidance on skill versioning. How should breaking changes to a skill's workflow be communicated to dependent workflows?
- **Skill composition**: Can skills call other skills? The current model does not formally support skill-to-skill invocation; this is an open design question in the ecosystem.
- **Concurrency safety**: The concurrency limitation is documented but not addressed. Workflows requiring parallel skill invocations need workarounds today.
- **Evaluation tooling**: The recommended evaluation loop is manual. Automated skill evaluation frameworks are nascent.

---

## References

### Knowledge Base Entries
- [KB-1] [Agent Skills Overview and Value](../docs/2026-03-11-agent-skills-overview.md) — Open-standard framing, motivation, and ecosystem direction
- [KB-2] [Agent Skills Core Concepts and Lifecycle](../docs/2026-03-11-agent-skills-core-concepts.md) — Progressive disclosure lifecycle and folder anatomy
- [KB-3] [Agent Skills Core Concepts and Lifecycle](../docs/2026-03-11-agent-skills-core-concepts.md) — Runtime progressive disclosure model
- [KB-4] [Agent Skills Specification and Organization](../docs/2026-03-11-agent-skills-specification.md) — Required metadata and structural conventions
- [KB-5] [Using Scripts in Agent Skills](../docs/2026-03-11-agent-skills-scripts-patterns.md) — Script bundling patterns and portability
- [KB-6] [Optimizing Skill Descriptions for Trigger Accuracy](../docs/2026-03-11-agent-skills-description-optimization.md) — Description iteration and activation precision
- [KB-7] [What to Skillify: Criteria for Good Skill Candidates](../docs/2026-03-11-agent-skills-skillification-criteria.md) — Decision criteria for skill creation
- [KB-8] [Agent Skill Anti-Patterns](../docs/2026-03-11-agent-skills-anti-patterns.md) — Named failure modes and fixes
- [KB-9] [Project-Local vs Global Skill Installation Scope](../docs/2026-03-11-agent-skills-scope-project-vs-global.md) — Scope decision guide
- [KB-10] [Agent Skill Design Patterns](../docs/2026-03-11-agent-skills-design-patterns.md) — Named structural patterns for skill workflows

### Web Sources
- [W-1] [Claude Agent Skills: A First Principles Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/) — Design patterns, anti-patterns, authoring methods, scope decisions
- [W-2] [Skill authoring best practices — Claude API Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — Official Anthropic guidance
- [W-3] [How to Use Skills in Claude Code: Install Path, Project Scoping & Testing](https://skywork.ai/blog/how-to-use-skills-in-claude-code-install-path-project-scoping-testing/) — Scope and installation guide
- [W-4] [Skills explained: How Skills compares to prompts, Projects, MCP, and subagents](https://claude.com/blog/skills-explained) — Official comparison of adjacent mechanisms
- [W-5] [Agent Skills — Claude Docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) — Official overview documentation
