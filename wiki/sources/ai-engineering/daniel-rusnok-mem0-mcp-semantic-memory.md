---
title: "How I Added Persistent Semantic Memory to Claude Code in 15 Minutes"
type: source
created: 2026-04-25
updated: 2026-04-25
sources: []
tags: [mem0, mcp, chromadb, semantic-memory, claude-code, ai-amnesia, hooks, vector-store, session-memory]
---

# How I Added Persistent Semantic Memory to Claude Code in 15 Minutes

*Mem0 + MCP + ChromaDB — plus what happens when your "helpful" hook spawns seven parallel Claude instances*

---

## Metadata

| Field | Value |
|---|---|
| Author | Daniel Rusnok |
| Publication | Generative AI (Medium) |
| Original URL | https://generativeai.pub/how-i-added-persistent-semantic-memory-to-claude-code-in-15-minutes-9b91f9399a76 |
| Date | ~April 2026 |

---

## One-line Summary

Practical walkthrough of adding persistent semantic memory to Claude Code via Mem0 + MCP + ChromaDB, plus a production incident documenting four stacked bugs that spawned seven parallel Claude instances.

---

## The Problem: AI Amnesia

Every Claude Code session starts from scratch. CLAUDE.md helps but is a flat file with no semantic search — querying your own decisions means grepping markdown. Decisions made weeks earlier in a different session are permanently lost unless manually re-explained.

> *"CLAUDE.md is deterministic (always loaded), Mem0 is probabilistic (search-based). Keep both."*

The author tried **claude-mem** first (46K+ GitHub stars) but hit critical Apple Silicon bugs (MCP loopback not saving, worker daemon timeouts, Bun crashes on macOS). Built a simpler alternative.

---

## The Solution: Mem0 as MCP Server

Three components:

| Component | Role |
|---|---|
| **Mem0 (mem0ai)** | Memory layer — LLM extracts key facts; stores as vector embeddings |
| **MCP (Model Context Protocol)** | Exposes 4 tools to Claude Code via stdio |
| **ChromaDB** | Local SQLite-backed vector store at `~/.mem0/chroma/` |

**Embedding model:** `all-MiniLM-L6-v2` (HuggingFace, runs fully local on CPU, ~80MB)  
**LLM for extraction:** Anthropic API (claude-sonnet-4) — only this hits the network  
**Infrastructure:** zero — no Docker, no server process, just a SQLite file on disk

### Four MCP Tools

```python
mem0_add(text, user_id, metadata)    # Store a memory
mem0_search(query, user_id, limit)   # Semantic search
mem0_get_all(user_id)                # List all memories
mem0_delete(memory_id)               # Delete by ID
```

### Key Design Decisions

- **Lazy loading** — embedding model loads on first tool call, not server start; keeps Claude Code startup fast
- **Local embeddings** — no API calls for embedding; only extraction uses Anthropic
- **ChromaDB on disk** — survives reboots; no server process needed
- **No project isolation by default** — memories are global; use `metadata` field to tag by project

### Registration

```bash
claude mcp add mem0 -s user -- python3 ~/.claude/mem0-mcp-server.py
```

The `-s user` flag makes it available across all projects.

---

## Step 4: The Hook — and the Incident

The author automated memory capture via a hook: on `SessionEnd`, a background `claude -p` instance reads the transcript, extracts non-obvious decisions, and stores them via `mem0_add`.

**It worked for about a week.** Then the MacBook Air M4 fans ramped to max and wouldn't stop.

### The Incident: 7 Parallel Claude Instances

```
claude -p "Extract key..."   72.9% CPU
claude -p "Extract key..."   66.1% CPU
claude -p "Extract key..."   44.9% CPU
claude -p "Extract key..."   36.8% CPU
claude -p "Extract key..."   25.0% CPU
claude -p "Extract key..."   19.1% CPU
claude -p "Extract key..."   —
```
Load average: **6.32** on a 10-core CPU. Seven parallel headless Claude instances + four mem0-mcp-server.py processes.

### Root Cause: Four Bugs Stacked Together

| Bug | Description |
|---|---|
| **Per-session lock, not global** | `/tmp/claude-mem0-locks/${SESSION_ID}.lock` — each concurrent session had its own lock; no global cap |
| **PreCompact fires frequently** | Registered on both `SessionEnd` and `PreCompact`; PreCompact fires on *every* context compaction, multiple times per long session |
| **No hard timeout** | `timeout: 10` in settings.json only covers the shell wrapper; `nohup ... &` runs forever if stuck |
| **Orphaned MCP servers** | Each spawned `claude -p` started its own `mem0-mcp-server.py`; when extraction hung, Python server hung with it |

### The Fix

1. **Global concurrency cap via `pgrep`** — before spawning, check process table; skip if any extraction already running system-wide
2. **Remove the PreCompact hook entirely** — `SessionEnd` only; PreCompact requires its own throttle
3. **Hard timeout on spawned process** — `gtimeout 300` (from `brew install coreutils`); 5-minute ceiling; OS kills if hung

After fix: load average dropped from 6.32 to 0.87, running instances: 1.

---

## Hook Script Review Checklist

Five things to check in any AI-generated hook script:

1. **Per-session or per-PID locks** — silently fail under parallelism; want: `pgrep -f <pattern>` global check
2. **Hooks on multiple events** — `PreCompact`, `Stop`, `PostToolUse` fire many times per session; same hook on 2+ events = Nx firing frequency
3. **Background processes without hard timeout** — `nohup cmd &` with no timeout wrapper is a liability; want: `gtimeout 300 cmd &`
4. **Recursive or self-invoking `claude` calls** — one bug in a parent session can spawn N children; want: recursion guard via env var or depth cap
5. **No log rotation** — infinite-growing logs fill disk silently; want: bounded file size or date-based suffix

---

## Limitations

- Not a replacement for CLAUDE.md — keep both; CLAUDE.md is deterministic, Mem0 is probabilistic
- Costs tokens — each `mem0_add` calls Anthropic API for extraction; budget for it
- Cold start — first tool call loads embedding model (~3s on M1); subsequent calls instant
- No project isolation by default — use `metadata` field to filter by project
- Will happily overheat your laptop if guardrails are missing

---

## What It Enables (When Working)

After a week of use:
- "What did I decide about auth?" → gets the decision with full context
- "Show me all architecture decisions for [project]" → filtered by project metadata
- "Why did I choose X?" → semantic match even if the keyword was never explicitly stored

Data persists between sessions, projects, and reboots. It's just a SQLite file.

---

## Related Pages

- [[ai-engineering/mcp-architecture]] — MCP concepts and failure modes
- [[ai-engineering/llm-wiki-pattern]] — The Karpathy system this source complements
- [[ai-engineering/ai-agent-governance]] — Broader governance concerns for AI automation
- [[ai-engineering/claude-code-skills]] — Another pattern for Claude Code context management
- [[analyses/session-memory-vs-wiki-synergy]] — Analysis of the architectural tension between these approaches
