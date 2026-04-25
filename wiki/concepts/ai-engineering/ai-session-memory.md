---
title: AI Session Memory
type: concept
created: 2026-04-25
updated: 2026-04-25
sources: [daniel-rusnok-mem0-mcp-semantic-memory.md]
tags: [mem0, session-memory, ai-amnesia, vector-store, chromadb, mcp, persistent-memory, claude-code]
---

# AI Session Memory

The capability for an AI coding agent to retain and retrieve decisions, preferences, and context across sessions — solving the problem that every new session starts from scratch.

---

## The Problem It Addresses

AI coding assistants like Claude Code have no persistent episodic memory. Each session is stateless:
- Architectural decisions made in previous sessions are gone
- Rationale for past choices must be re-explained manually
- CLAUDE.md provides deterministic context loading, but is a flat file — no semantic search, no history, no indexing

This is distinct from the synthesis problem the [[ai-engineering/llm-wiki-pattern]] addresses. The wiki solves *knowledge accumulation across sources*; session memory solves *decision retention across interactions*.

---

## The Three-Tier Memory Model

| Tier | What | Mechanism | Lifetime |
|---|---|---|---|
| **Session context** | Current conversation | LLM context window | Session only |
| **Session memory** | Decisions made in past sessions | Mem0/vector DB (MCP) | Persistent across sessions |
| **Domain knowledge** | Synthesized understanding of sources | LLM Wiki (file-based) | Permanent, curated |

The first tier is built-in. CLAUDE.md and the LLM Wiki pattern cover the third. Session memory (tier 2) requires an explicit tool like Mem0.

---

## Mem0 + MCP Implementation Pattern

The canonical pattern for tier-2 memory in Claude Code:

### Components

- **Mem0 (mem0ai)** — Python library that wraps LLM-based fact extraction + vector storage
- **ChromaDB** — local SQLite-backed vector store; no infrastructure required
- **sentence-transformers (all-MiniLM-L6-v2)** — local embedding model; no API calls for embedding
- **FastMCP** — Python MCP server framework; exposes tools via stdio

### Tool Interface

```python
mem0_add(text, user_id, metadata)    # Capture a decision or fact
mem0_search(query, user_id, limit)   # Semantic search (natural language)
mem0_get_all(user_id)                # Dump all memories
mem0_delete(memory_id)               # Remove a specific memory
```

### Architecture Flow

```
Claude Code → MCP (stdio) → mem0-mcp-server.py → Mem0 library
                                                     ↓          ↓
                                              ChromaDB       Anthropic API
                                             (embeddings)   (extraction LLM)
```

Local embeddings; only fact extraction calls the cloud API.

---

## Vectorless vs. Semantic Retrieval: An Architectural Tension

| Approach | LLM Wiki (Karpathy) | Mem0 Session Memory |
|---|---|---|
| Storage | Structured markdown files | Vector database (ChromaDB) |
| Navigation | Structured index (vectorless) | Semantic similarity search |
| Knowledge type | Curated, synthesized, stable | Ephemeral, conversational, project-specific |
| Search method | LLM reads index, reasons about relevance | Embedding similarity + metadata filter |
| Maintenance | AI-curated on ingest | Auto-captured on session end |

Both solve knowledge retention; neither is a substitute for the other. The tension is real: the LLM Wiki argument is that structure + index enables precise navigation without vectors. Mem0's argument is that unstructured decisions benefit from semantic search because you can't predict which keywords you'll use when querying.

See [[ai-engineering/semantic-memory-vs-wiki]] for a detailed comparison.

---

## Production Hazards: Hook Design

Automating memory capture via a session-end hook introduces reliability risks. Four failure modes documented in production:

1. **Per-session locks** — silently allow N concurrent extractions when N sessions end simultaneously
2. **Over-eager hook events** — `PreCompact` fires on every context compaction, not just at session end
3. **Unbounded background processes** — `nohup ... &` with no timeout creates permanent zombies
4. **Orphaned MCP servers** — each spawned extraction starts its own server subprocess

**Mitigations:**
- Global concurrency cap: `pgrep -f <pattern>` before spawning
- Register on `SessionEnd` only — not `PreCompact`
- Hard timeout: `gtimeout 300 cmd &`
- Recursion guard via environment variable

### The Meta-Lesson

AI-generated automation code passes a dry-run and fails under real-world concurrency. Wrong assumptions are invisible until load reveals them. This reinforces the principle from [[ai-engineering/ai-agent-governance]]: AI-generated infrastructure must be reviewed like any production PR.

---

## Limitations

- Not deterministic: memory retrieval depends on query phrasing (similarity-based, not structural)
- Memory extraction costs API tokens per session end
- Cold start: ~3 seconds on first call to load embedding model
- No project isolation by default: filter via `metadata` field
- Complementary to CLAUDE.md, not a replacement — keep both

---

## Related Pages

- [[ai-engineering/llm-wiki-pattern]] — The complementary long-term knowledge system
- [[ai-engineering/mcp-architecture]] — The MCP protocol this pattern runs on
- [[ai-engineering/claude-code-skills]] — Another context engineering pattern for Claude Code
- [[ai-engineering/ai-agent-governance]] — Production risk framework for AI automation
- [[ai-engineering/rag-approaches]] — The vectorless vs. vector retrieval tension at the architectural level
- [[ai-engineering/semantic-memory-vs-wiki]] — Analysis of how session memory and the LLM Wiki complement each other
- [[sources/ai-engineering/daniel-rusnok-mem0-mcp-semantic-memory]] — Source article
