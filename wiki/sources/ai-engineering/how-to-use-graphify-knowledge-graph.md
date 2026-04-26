---
title: "How to Use Graphify: Turn Any Folder Into a Knowledge Graph"
type: source
created: 2026-04-26
updated: 2026-04-26
sources: [How to Use Graphify_ Turn Any Folder Into a Knowledge Graph.md]
tags: [graphify, knowledge-graph, rag, context-engineering, ast-parsing, provenance-tagging, claude-code, obsidian, karpathy]
---

Step-by-step guide to Graphify — an open-source tool that converts any folder into a persistent, queryable knowledge graph to reduce AI token consumption by up to 71.5x.

## Metadata

| Field | Value |
|---|---|
| **URL** | https://medium.com/agentic-builders/how-to-use-graphify-turn-any-folder-into-a-knowledge-graph-d51b38eb60b6 |
| **Author** | Ana Bildea, PhD |
| **Published** | 2026-04-11 |
| **Publication** | Agentic Builders (Medium) |

---

## Core Claim

> "The graph is the context window. Everything else is just search."

Structured, compressed, provenance-tagged knowledge graphs are a better input representation for AI assistants than raw files. The core mechanism: instead of dumping raw files into a context window, Graphify builds a graph and serves a focused **subgraph** — reducing from 52 files to ~300 tokens for a typical query.

---

## The Problem It Solves

Every developer working with LLMs on large codebases hits the same wall: context windows are finite, but codebases are not. Dumping raw files scales **linearly in tokens** but **sub-linearly in understanding**. Graphify frames itself as a direct response to Karpathy's 2026 challenge:

> "I think there is room here for an incredible new product instead of a hacky collection of scripts."

---

## The Three-Pass Pipeline

### Pass 1 — Deterministic AST Parsing (local, no LLM)

- Uses `tree-sitter` to parse code across **20 languages**
- Extracts: classes, functions, imports, call graphs, docstrings, rationale comments
- Fully deterministic — no code sent to any LLM API
- All edges tagged: `EXTRACTED` with confidence score `1.0`

### Pass 2 — Local Transcription (local, no LLM)

- Uses `faster-whisper` for audio/video files (MP4s, recordings)
- Audio never leaves the machine
- SHA256-cached: re-runs are instant unless the media file changes
- Transcripts fed into Pass 3 as unstructured text

### Pass 3 — Parallel LLM Extraction

- Handles unstructured content: documentation, PDFs, images, transcripts from Pass 2
- Claude Code (or another coding assistant) acts as **the runtime**; Graphify is a **skill**, not a standalone orchestrator
- The assistant dispatches **parallel subagents** that each extract concepts and relationships
- Output is strictly schema-validated before merging into the main graph
- All edges tagged: `INFERRED` with a confidence score

---

## Provenance Tagging

Every edge in the graph carries a provenance label:

| Label | Meaning | Confidence |
|---|---|---|
| `EXTRACTED` | Deterministically derived from AST or structured source | 1.0 |
| `INFERRED` | Deduced by an LLM from unstructured content | < 1.0 (varies) |
| `AMBIGUOUS` | System is uncertain; flagged for human review | low |

This is the key epistemic guarantee: you always know **what the system found** vs. **what it guessed**. `GRAPH_REPORT.md` surfaces all `AMBIGUOUS` edges for human review.

---

## Outputs

| File | Description |
|---|---|
| `GRAPH_REPORT.md` | Human-readable audit report; surfaces AMBIGUOUS edges |
| `graph.json` | Machine-readable graph; consumed by AI assistants |
| `graph.html` | Interactive viewer: click nodes, search, filter by community |
| Obsidian Vault (`--obsidian`) | Optional: ready-to-use wiki with backlinks for human navigation |

---

## Query Integration via PreToolUse Hook

Graphify ships a `PreToolUse` hook. When an assistant receives a question like "how does the auth flow work?", the hook fires **before** the assistant starts grepping files:

1. Assistant reads `graph.json` first
2. Identifies relevant nodes
3. Retrieves a focused **subgraph** (~300 tokens)
4. Answers from structure — not raw file search

Supported platforms: **Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, Aider, OpenClaw, Factory Droid, Trae** (10 total).

---

## Getting Started

```bash
pip install graphifyy
graphify .          # inside any project directory
graphify . --obsidian  # also generate an Obsidian vault
```

Zero configuration required.

---

## Key Design Principles

1. **Separation of deterministic and probabilistic extraction** — Pass 1/2 run locally with no LLM; only Pass 3 involves inference, and its outputs are explicitly labeled as such.
2. **Graph is the context window** — topology-clustered subgraphs replace raw files as the AI's primary context input.
3. **Epistemic honesty via provenance** — every relationship carries a confidence score and provenance tag.
4. **Skill, not orchestrator** — Graphify delegates to the user's existing coding assistant rather than replacing it.

---

## Related Pages

- [[ai-engineering/rag-approaches]]
- [[ai-engineering/llm-wiki-pattern]]
- [[ai-engineering/claude-code-skills]]
- [[ai-engineering/ai-agent-governance]]
