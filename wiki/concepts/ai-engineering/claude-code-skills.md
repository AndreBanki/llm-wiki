---
title: Claude Code Skills
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [eric-luque-claude-code-skills.md]
tags: [claude-code, skills, agentic-ai, context-engineering, ai-engineering]
---

Claude Code Skills are directory-based context packages that give an AI coding agent specialized knowledge, tools, and operational patterns for a specific task domain — turning a general-purpose model into a competent specialist for that domain.

## What is a Skill?

A skill is a **folder**, not a file. The entry point is a Markdown file (`skill.md`) that tells Claude when and how to invoke the skill, but the real value is the package of resources alongside it:

```
.claude/skills/my-skill/
  skill.md          ← entry point: trigger conditions + usage instructions
  config.json       ← user-configurable values (team-specific settings)
  references/       ← documentation Claude reads on demand
  assets/           ← templates and boilerplate
  scripts/          ← reusable utility scripts Claude can invoke
  examples/         ← concrete usage patterns
```

The structural analogy: if Claude Code is a brilliant new hire with no company context, a skill is the complete onboarding kit — not a list of rules, but a survival kit.

---

## How Skills Work

1. Claude reads the skill's `skill.md` description to determine *when* to invoke it
2. When invoked, Claude has access to the entire folder: docs, scripts, templates
3. Claude composes the resources rather than generating everything from scratch
4. For stateful skills, persistent data lives in `${CLAUDE_PLUGIN_DATA}` — a stable directory that survives skill updates

This enables **progressive disclosure**: the main file gives the overview and rules; subfolders hold details that Claude retrieves on demand. Context budget is preserved — Claude isn't forced to load everything upfront.

---

## The 9 Skill Categories

### 1. Library & API Reference
Fill gaps where the model knows a library's general shape but misses version-specific details, internal conventions, or production gotchas.

- Include: `examples/` with real usage, breaking changes, gotchas section
- Key value: production-discovered details that aren't in the official docs

### 2. Product Verification
Test real behavior beyond unit tests. Use Playwright, Cypress, or tmux to exercise actual user flows.

- Catches: mobile viewport issues, Stripe edge cases, TTY-dependent CLI behavior
- Shift from "code compiles" to "product works"

### 3. Data Recovery & Analysis
Give Claude access to production metrics, dashboards, and funnels via query libraries and credential configs.

- Examples: funnel query scripts, Grafana dashboard mappings, cohort analysis utilities
- Use case: evidence-based implementation decisions ("how much traffic does this route actually get?")

### 4. Business Process Automation
Automate team-level repetitive tasks that require no creativity but do require context from multiple sources.

- Pattern: aggregate from tracker + GitHub + Slack → format → post/create
- Persistent logs (via `${CLAUDE_PLUGIN_DATA}`) allow the agent to maintain consistency across sessions

### 5. Code Templates & Scaffolding
Encode architectural decisions already made by the team. Claude adapts templates rather than deciding structure from scratch.

- Key principle: structural decisions made by humans → Claude focuses on customization
- Prevents: inconsistent folder structures, missing CI config, forgotten auth boilerplate

### 6. Code Quality & Code Review
Combine deterministic linting (catches syntax/style) with semantic analysis (catches auth gaps, data leakage).

- Can run as manual invocation (`/review`) or automated hooks (pre-commit, pre-push, GitHub Actions)
- The adversarial-review pattern: sub-agents argue against each other, forcing the model to defend its choices

### 7. CI/CD & Deploy
Orchestrate the full deploy lifecycle: monitor pipeline, handle flaky checks, resolve merge conflicts, canary traffic shift, rollback on anomaly.

- Perfect agent use case: constant attention required, little creativity needed
- Can reference other skills (e.g., data analysis skill to check health metrics before continuing)

### 8. Runbooks
Map incident symptoms to investigation sequences. Deliver structured diagnostic reports under pressure.

- Pattern: symptom in → investigate metrics + logs + deploys → structured report out
- Value: prevents skipped steps under production pressure

### 9. Infrastructure Operations
Routine but potentially destructive maintenance: orphan cleanup, dependency updates, cost investigation.

- **Guard rails are mandatory**: hooks on `PreToolUse` must block `rm -rf`, `DROP TABLE`, force-push, `kubectl delete` without explicit human confirmation
- No skill should perform destructive actions autonomously

---

## Best Practices

### Write gotchas, not documentation
> "The most valuable content of any skill is the gotchas section." — Mario Tort (Anthropic)

A gotcha is a production-discovered mistake the model makes repeatedly. Skills without a gotchas section probably aren't solving a real problem. Best skills begin with a single gotcha and grow organically.

```markdown
## Gotchas

### Don't use findOne without .lean() on read queries
Mongoose returns full documents by default. Without .lean(), each query allocates ~3x more memory.

### The status field accepts null in the database but not via API
The migration allowed null, but the API schema validates as required. Always use the default value "pending".
```

### Folder structure = context engineering
Use the file system as progressive disclosure. Don't load everything into the main file — reference subfolders from `skill.md` so Claude knows where to look when it needs details.

### Description = trigger conditions, not a summary
The `description` field in a skill determines **when the model considers invoking it**. Write it as conditions, not as a human-readable explanation.

**Wrong:** `"Skill para fazer deploy de serviços na AWS"`  
**Right:** `"Use when the user asks to deploy, publish, or push a service. Also when they mention staging, production, canary, rollback, or when a PR has been approved and needs to go to production."`

With Opus 4.7's more literal instruction-following, a vague description means skills are never invoked at the right moment.

### config.json over hardcoded values
Variable configuration (Slack channel, staging URL, branch name) belongs in `config.json`. When absent, Claude asks the user via `AskUserQuestion`. This makes a personal skill portable across the team.

### Maintain flexibility
Overly prescriptive skills break when edge cases arise — and edge cases are the norm, not the exception. Give Claude the information, not a numbered checklist.

### Persist state intelligently
- **Skill directory**: templates, scripts, examples — these are part of the skill definition
- **$CLAUDE_PLUGIN_DATA**: logs, history, session state — this survives skill updates

### Conditional hooks
- `/careful`: activates a `PreToolUse` hook blocking destructive commands during the session
- `/freeze`: blocks edits outside a specified directory

Hooks should be opt-in, not always-on.

---

## Skill Composition

Skills can reference other skills by name (e.g., the deploy skill calls the metrics skill to check health before continuing). No formal dependency management exists yet — by convention, referenced skills must be installed and available. A `package.json`-style system is a likely future development.

---

## Distribution

| Method | Best for |
|---|---|
| `.claude/skills/` committed in the repo | Small teams, project-specific skills, fast iteration |
| Claude Code marketplace plugin | Generic cross-project skills, large teams, community sharing |

At Anthropic, useful skills emerge organically, spread informally via GitHub/Slack, and are promoted to the official marketplace via PR when adoption is sufficient.

---

## Measuring Adoption

Use `PreToolUse` hooks to log skill invocations. Track:
- Which skills are used most
- Which are invoked but don't complete their flow (signals problems)
- Which are abandoned (candidates for removal or improvement)

---

## Opus 4.7 Impact (April 2026)

Claude Opus 4.7 fundamentally changes the ROI calculation for skills:

| Change | Skill Impact |
|---|---|
| "Thinks more, acts less" | Claude reads skill instructions fully before acting; well-written skills have much higher return |
| Native auto-verification | Product verification skills gain a much stronger engine (Claude self-tests autonomously) |
| Better filesystem memory | State-maintaining skills (deploy logs, standup history) work dramatically better |
| Literal instruction following | Vague descriptions and missing gotchas are now much more costly — Claude follows exactly what's written |
| Task budgets (beta) | Set token budgets per agentic loop; critical skills run at `xhigh` effort, routine at `high` |
| Multi-agent coordination | Skill composition (one skill calling another) runs with less friction |

**The analogy:** In Opus 4.6, a skill was like giving a map to someone with decent eyesight. In Opus 4.7, it's like giving a map to someone with perfect vision. If the map is wrong, they'll follow the wrong instructions with far more conviction.

---

## Relationship to Other Concepts

| Concept | Relationship |
|---|---|
| [[ai-engineering/mcp-architecture]] | Claude Code is an MCP client; skills are the customization layer above the client — they define what the agent knows and how it behaves, not what tools are exposed |
| [[ai-engineering/llm-wiki-pattern]] | The LLM Wiki is itself a skills-like pattern: structured knowledge accumulation, gotcha-capture, and progressive indexing |
| [[ai-engineering/rag-approaches]] | Progressive disclosure in skill folders parallels vectorless RAG: structure guides reasoning rather than brute-force similarity |
| [[ai-engineering/enterprise-ai-deployment]] | "Start with one gotcha" mirrors "start with one working use case before architecting" — empirical, not theological |

## Related Pages

- [[ai-engineering/mcp-architecture]]
- [[ai-engineering/llm-wiki-pattern]]
- [[ai-engineering/rag-approaches]]
- [[ai-engineering/enterprise-ai-deployment]]
- [[ai-engineering/eric-luque-claude-code-skills]]
