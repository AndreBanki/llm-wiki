---
title: Obsidian Knowledge Graph
type: concept
created: 2026-05-01
updated: 2026-05-01
sources: [Your Obsidian Vault Is a Knowledge Graph. Here's How to Make It Think (quickly)..md]
tags: [obsidian, knowledge-graph, pkm, graph-analysis, vault-maintenance, compound-knowledge, claude-code]
---

# Obsidian Knowledge Graph

An Obsidian vault is an implicit graph database: notes are nodes, wikilinks are directed edges, tags are labels, and YAML frontmatter provides node attributes. Connecting an AI agent (Claude Code) to this existing graph unlocks querying, maintenance, and synthesis capabilities that are impractical manually.

---

## The Vault-as-Graph Model

Every vault with wikilinks already has graph structure. The question is not "how to build a graph" (see [[ai-engineering/how-to-use-graphify-knowledge-graph]] for that) but "how to leverage the graph you already have."

| Vault Element | Graph Equivalent |
|---|---|
| Markdown note | Node |
| `[[wikilink]]` | Directed edge |
| Backlinks (Obsidian UI) | Bidirectional navigation layer |
| Tags (`#domain/topic`) | Node labels / subgraph membership |
| YAML frontmatter | Node attributes (queryable) |

Obsidian's Graph View visualizes this structure but is passive. Graph-aware tools (TurboVault, obsidian-mcp-plugin) enable programmatic analysis: centrality ranking, cluster detection, bridge identification.

---

## Graph Metrics for Knowledge Management

Four metrics that make vault structure actionable:

### Centrality Ranking
Identifies true hub notes — the concepts with the most connections. Key insight: official MOCs (Maps of Content) often don't match actual hubs. When "Feedback Loops" has 38 incoming links and the Systems Thinking MOC has 7, the structure is telling you something the taxonomy isn't.

### Orphan Detection
Notes with zero incoming or outgoing links — captured ideas that were never connected. At scale (5,000+ notes), orphan rates can reach 9%. Monthly audits bring this below 2%.

### Cluster Analysis
Reveals natural groupings and, more importantly, **disconnected islands**. Two topic areas with obvious conceptual overlap but zero links between them represent a missed integration opportunity.

### Bridge Note Identification
Finds the rare notes connecting otherwise isolated clusters. These are often the most original insights — cross-field connections that other people keep separate.

---

## Compound Maintenance

The central insight: consistent AI-assisted maintenance creates a virtuous cycle.

```
Better-linked notes → better context for AI → better suggestions → better links
```

Quantifiable progression:
- **Month 0:** 9% orphan rate, inconsistent frontmatter
- **Month 3:** Automated backlinking converts daily notes from dead ends to connected nodes
- **Month 6:** Orphans below 2%, frontmatter compliance above 95%
- **Ongoing:** Each improvement compounds — the graph becomes denser, more navigable, and more useful for both human and AI

This is the trajectory the Zettelkasten method promised but few achieve manually. The organizational work — backlinking, tagging, formatting, consistency — is exactly what AI excels at. Human brings the thinking; AI brings the bookkeeping.

---

## CLAUDE.md Design Patterns

Three non-obvious patterns for effective CLAUDE.md files in vault contexts:

### Active Context Refresh
Update a dedicated "Active Context" section before each session. Stale context sends Claude pursuing yesterday's priorities. At session end, ask Claude to append a brief session log for cross-session continuity.

*Parallels [[ai-engineering/ai-session-memory]] — the Active Context pattern is a manual, deterministic equivalent of Mem0's automated session capture.*

### Reference, Don't Inline
Interests, active projects, and professional context live in separate notes. CLAUDE.md references them rather than inlining. Keeps the root file focused; avoids burning tokens on irrelevant context.

### Negative Instructions
"Never modify `_templates/`" is more effective than hoping Claude will figure it out. Include explicit prohibitions for directories and files the AI should never touch.

See also: [[ai-engineering/claude-code-skills]] — the `description` field and folder structure patterns; [[ai-engineering/shereshevsky-obsidian-vault-knowledge-graph]] for full production context.

---

## Four-Tier Tool Taxonomy

| Tier | Tools | When to Use |
|---|---|---|
| **1. Direct Filesystem** | CLI + CLAUDE.md + obsidian-skills (Kepano) | Start here — handles 80% of needs; zero infrastructure |
| **2. MCP Server** | MCPVault, obsidian-claude-code-mcp, obsidian-mcp-tools | When vault crosses ~2,000 notes and search-heavy workflows slow down |
| **3. Graph Analysis** | TurboVault, obsidian-mcp-plugin | 10,000+ notes; graph-level insights (centrality, clusters, bridges) |
| **4. Embedded Sidebar** | Claudian, Cortex | Preference for in-Obsidian UX; dependent on plugin maintenance |

MCPVault is the recommended Tier 2 starting point: zero Obsidian plugin dependencies, 14 methods, BM25-ranked search, 40–60% smaller token usage.

TurboVault is the power tool for Tier 3: Rust engine, 47 specialized tools, sub-500ms BM25 search on 100K notes, SQL queries against frontmatter.

---

## Production Workflows

| Workflow | Frequency | Key Result |
|---|---|---|
| Automated backlinking | Daily | Daily notes become connected nodes; highest ROI workflow |
| Cross-domain synthesis | As needed | Surfaces latent connections between separate knowledge domains |
| Vault health audit | Monthly | Orphan rate, frontmatter compliance, broken links — PKM test suite |
| Gap analysis | Quarterly | Identifies structural holes invisible to the human owner |
| CLI piping (`-p` flag) | Ad hoc | Batch operations: folder summaries, stub generation, claim extraction |

---

## Safety Principles

1. **Git for the vault** — every AI change becomes a reviewable diff; every mistake is reversible
2. **`_ai-drafts/` staging** — AI output is a draft until reviewed; never writes directly to main structure
3. **"Use ONLY content from my notes"** — the PKM equivalent of input sanitization; prevents hallucination from training data
4. **Scope to specific folders** — avoids token bombs; produces deeper results on focused areas

---

## Relationship to Other Concepts

| Concept | Connection |
|---|---|
| [[ai-engineering/llm-wiki-pattern]] | LLM Wiki is the AI-built knowledge base; Obsidian vault is the human-built one. Both are graph structures; both benefit from AI maintenance. Complementary perspectives on "Obsidian as reader" vs. "Obsidian as builder" |
| [[ai-engineering/how-to-use-graphify-knowledge-graph]] | Graphify builds graphs from scratch (3-pass pipeline); Obsidian leverages the graph you've already built via years of wikilinks |
| [[ai-engineering/ai-session-memory]] | Active Context refresh pattern is a manual, deterministic equivalent of Mem0's automated session capture |
| [[ai-engineering/claude-code-skills]] | CLAUDE.md is the skill file for vault operations; obsidian-skills (Kepano) is a pre-packaged vault skill |
| [[ai-engineering/rag-approaches]] | Graph metrics (centrality, clusters) parallel graph-based RAG but serve maintenance, not retrieval |

## Related Pages

- [[ai-engineering/shereshevsky-obsidian-vault-knowledge-graph]] — source article
- [[ai-engineering/llm-wiki-pattern]]
- [[ai-engineering/claude-code-skills]]
- [[ai-engineering/how-to-use-graphify-knowledge-graph]]
- [[ai-engineering/ai-session-memory]]
