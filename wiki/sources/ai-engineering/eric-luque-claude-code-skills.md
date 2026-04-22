---
title: "Skills no Claude Code: O Guia Definitivo (Eric Luque)"
type: source
created: 2026-04-22
updated: 2026-04-22
sources: [eric-luque-claude-code-skills.md]
tags: [claude-code, skills, agentic-ai, context-engineering, ai-engineering, opus-4.7]
---

Practical deep-dive into Claude Code's Skills system: a directory-based context-delivery mechanism for AI agents, covering 9 skill categories, best practices, and the amplifying effect of Claude Opus 4.7.

## Metadata

| Field | Value |
|---|---|
| Author | Eric Luque (Co-founder Ecotrace) |
| Published | April 18, 2026 |
| Platform | LinkedIn Pulse |
| URL | https://www.linkedin.com/pulse/skills-claude-code-o-guia-definitivo-para-quem-quer-parar-eric-luque-kosuf/ |
| Language | Portuguese (Brazilian) |
| Inspired by | Mario Tort (Anthropic engineer) internal guide |
| Raw file | `raw/eric-luque-claude-code-skills.md` |

---

## Core Claim

A Claude Code Skill is not a Markdown file with instructions — it is a **directory** containing scripts, assets, templates, reference docs, config files, and examples. The .md file is merely the entry point. The metaphor: if Claude Code is an intelligent intern without company context, a skill is the complete onboarding kit that makes them productive on day one.

---

## The 9 Skill Categories

| # | Category | Problem Solved | Key Examples |
|---|---|---|---|
| 1 | Library & API Reference | Claude knows popular libraries but misses version-specific details | billing-lib, internal-platform-cli, frontend-design |
| 2 | Product Verification | Code compiles and passes unit tests but fails in real usage | signup-flow-driver (Playwright), checkout-verifier (Stripe), tmux-cli-driver |
| 3 | Data Recovery & Analysis | Claude has no access to dashboards or data warehouses | funnel-query, cohort-compare, grafana (dashboard mapping) |
| 4 | Business Process Automation | Repetitive team tasks that require no creativity | standup-post, create-ticket, weekly-recap |
| 5 | Code Templates & Scaffolding | Architectural decisions already made by the team shouldn't be redecided | new-workflow (docker+CI), new-migration (rollback+seed), create-app (auth+logging) |
| 6 | Code Quality & Code Review | Quality standards are inconsistently enforced across the team | adversarial-review (sub-agents), code-style (deterministic), testing-practices |
| 7 | CI/CD & Deploy | Deploy requires constant attention but little creativity — perfect for an agent | babysit-pr, deploy-service (canary), cherry-pick-prod (worktrees) |
| 8 | Runbooks | On-call investigation follows a known pattern but pressure causes steps to be skipped | service-debugging, oncall-runner, log-correlator (trace IDs) |
| 9 | Infrastructure Operations | Maintenance involves potentially destructive operations | resource-orphans, dependency-management, cost-investigation |

---

## Skill Folder Structure

```
.claude/skills/my-skill/
  skill.md          ← entry point: when/how to use
  config.json       ← user-configurable values
  references/       ← documentation Claude reads on demand
  assets/           ← templates, boilerplate
  scripts/          ← reusable utility scripts
  examples/         ← concrete usage patterns
```

---

## Best Practices (Key Quotes)

> "The most valuable content of any skill is the gotchas section." — Mario Tort (Anthropic)

| Practice | Why it matters |
|---|---|
| **Don't write the obvious** | Context is the scarcest resource in an LLM; waste none on what Claude can infer |
| **Gotchas section** | Production-discovered pitfalls Claude repeats — most valuable content; start with one |
| **Folder structure as progressive disclosure** | Main file = overview + rules; subfolders = details retrieved on demand |
| **Flexibility over rigidity** | Overly rigid skills break when edge cases arise; give Claude the information, not a checklist |
| **config.json** | Makes skills portable and team-shareable; missing file → Claude asks via AskUserQuestion |
| **Description = trigger conditions** | Description tells the model *when* to invoke the skill, not what the skill does to humans |
| **$CLAUDE_PLUGIN_DATA** | Persistent data directory that survives skill updates; use for logs, history, state |
| **Reusable scripts** | Shift Claude from reimplementing boilerplate to composing pre-built utilities |
| **Conditional hooks** | `/careful` (block destructive commands) and `/freeze` (lock a directory) — opt-in only |

---

## Distribution Paths

| Path | Best for |
|---|---|
| `.claude/skills/` commit in repo | Small teams, project-specific skills, fast iteration |
| Plugin in Claude Code marketplace | Generic multi-project skills, large teams, community sharing |

---

## Opus 4.7 Impact on Skills (April 16, 2026)

### What improved
| Capability | Opus 4.6 | Opus 4.7 |
|---|---|---|
| Instruction reading | Superficial before acting | Absorbs context, plans, then acts |
| Tool call error rate | Baseline | 1/3 of baseline (-66%) |
| Self-verification | Manual only | Native proactive (writes tests, runs them) |
| Filesystem memory | Limited | Natively improved (reads and writes notes between turns) |
| Literal instruction following | Fills implicit gaps | Follows exactly what is written |
| Multi-agent coordination | Baseline | Improved parallel orchestration |
| Visual acuity | 54.5% (XBOW) | 98.5% (+44pp) |
| Image resolution | 1.15 megapixels | 3.75 megapixels |

### Breaking changes for existing skills
1. **Sampling parameters removed:** `temperature`, `top_p`, `top_k` → HTTP 400
2. **New tokenizer:** text inputs cost 1.0x–1.35x more tokens; high-res images jump from ~1,600 to ~4,784 tokens
3. **Prefill blocked:** assistant message prefilling → HTTP 400

---

## Key Quotes

- "Uma skill é uma pasta" (A skill is a folder) — the author's corrective reframing
- "Skills muito rígidas quebram assim que aparece um caso que você não previu" (Overly rigid skills break as soon as an unforeseen case appears)
- "No 4.6, uma skill era como dar um mapa para alguém que enxergava razoavelmente bem. No 4.7, é como dar um mapa para alguém com visão perfeita. Se o mapa estiver errado, essa pessoa vai seguir as instruções erradas com muito mais convicção." (In 4.6, a skill was like giving a map to someone with decent eyesight. In 4.7, it's like giving a map to someone with perfect vision. If the map is wrong, they'll follow the wrong instructions with much more conviction.)

---

## Cross-Domain Connections

- **[[ai-engineering/mcp-architecture]]** — Claude Code is an MCP client; skills are the customization layer above the MCP client layer
- **[[ai-engineering/llm-wiki-pattern]]** — Gotcha-driven, incrementally-growing skill mirrors how this wiki builds knowledge: non-obvious facts compound over time
- **[[ai-engineering/claude-code-skills]]** — Concept page for this domain
- **[[ai-engineering/enterprise-ai-deployment]]** — "Start with one gotcha" mirrors "start with one working use case before architecting"
- **[[ai-engineering/rag-approaches]]** — Progressive disclosure in skill folders parallels vectorless RAG reasoning over document structure

## Related Pages

- [[ai-engineering/claude-code-skills]]
- [[ai-engineering/mcp-architecture]]
- [[ai-engineering/llm-wiki-pattern]]
- [[ai-engineering/enterprise-ai-deployment]]
