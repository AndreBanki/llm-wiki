---
title: LLM Context Window
type: concept
created: 2026-05-01
updated: 2026-05-01
sources: [Five LLM concepts I keep explaining to engineers shipping their first agents.md]
tags: [context-window, context-budget, agent-architecture, llm, ai-engineering]
---

The context window is the bounded buffer that holds everything an LLM can see at a given moment. Most agent architecture problems are downstream of not managing it explicitly.

## The Core Mental Model

**Wrong:** "The model has a 200K context, so I can use 200K."

**Right:** The context window is **RAM** — a bounded buffer that contains, at any moment:
- System prompt
- Conversation history (all prior turns)
- Tool schemas and definitions
- Tool call results
- Every intermediate response

There is no helpful error when the budget is exceeded. Content truncates silently from the back, and the model loses access to whatever fell off — without telling you.

---

## What Eats the Budget

The context budget is consumed by every component simultaneously:

| Component | Typical consumption |
|---|---|
| System prompt + persona | 500–5,000 tokens depending on complexity |
| Tool schemas (all tools defined) | 500–3,000 tokens per tool set |
| Conversation history | Grows unboundedly with turn count |
| Retrieved documents (RAG) | Per chunk, compounding with retrieval strategy |
| Tool call results | Per tool invocation, compounding with agent loops |
| The model's own prior responses | Included in history |

**Practical example:** a modest coding agent task — reading three medium files plus a few tool responses — can consume 30–50K tokens before the model has done any significant reasoning.

---

## The Architectural Decision This Forces

The context window is not a setting to tune — it is a **design constraint that determines agent architecture**. Every architectural decision in a well-designed agent traces back to one core question:

> *What does the model truly need to see in the context window vs. what can it retrieve on demand?*

Teams that answer this explicitly build systems that scale. Teams that don't build agents that perform on toy tasks and degrade under real workloads.

**Answering the question means deciding:**
- Which parts of the system prompt can be split off into on-demand loaded skills
- How much conversation history to retain vs. summarize vs. drop
- When to retrieve chunks vs. when to load full documents
- Whether tool schemas should all be pre-loaded or registered dynamically

---

## Context Window vs. Context Budget

The **context window** is the model's technical limit (e.g., 200K tokens for Claude Opus 4.7).

The **context budget** is what you actually have available for content after system overhead. They are not the same number — and budget ≠ window even when system overhead is 0.

A useful framing: budget accounting works like memory management in systems programming. You know the total RAM; you plan allocations for each component; you track consumption; you optimize when you run out. You don't treat "total RAM" as available RAM.

---

## Failure Modes

| Failure | What happens | Why it's hard to diagnose |
|---|---|---|
| Context truncation | Model loses track of earlier content; earlier instructions drop off | No error raised; behavior degrades gradually |
| Tool schema inflation | Too many registered tools eat budget before content reaches the model | Tool count seems harmless; cost is invisible |
| History bloat | Long conversations push the system prompt out of the effective window | Works fine for first 10 turns, breaks at turn 50 |
| Retrieval amplification | Each tool call result compounds context consumption across the agent loop | Appears fine at demo scale, fails at production scale |

---

## Relationship to Other Concepts

- **RAG** — the architectural response to limited context: retrieve on demand rather than loading everything upfront. See [[ai-engineering/rag-approaches]]
- **Claude Code Skills** — Skills use progressive disclosure as a context engineering technique: load detailed reference on demand, not upfront. See [[ai-engineering/claude-code-skills]]
- **1M Context** — long-context models (e.g., Qwen 3.6 Plus at 1M tokens) push this constraint further but do not eliminate it; cost scales with consumed tokens. See [[ai-engineering/llm-model-economics]]
- **AI Session Memory** — session memory tools (Mem0) address the history side: store prior decisions externally and retrieve on demand rather than accumulating in-window. See [[ai-engineering/ai-session-memory]]
- **Temperature** — a different operating characteristic; temperature governs output distribution, not context. See [[ai-engineering/temperature]]

---

## Related Pages

- [[ai-engineering/rag-approaches]]
- [[ai-engineering/claude-code-skills]]
- [[ai-engineering/llm-model-economics]]
- [[ai-engineering/ai-session-memory]]
- [[ai-engineering/temperature]]
- [[ai-engineering/llm-hallucination]]
- [[ai-engineering/harika-yenuga-five-llm-concepts-first-agents]] (source article)
