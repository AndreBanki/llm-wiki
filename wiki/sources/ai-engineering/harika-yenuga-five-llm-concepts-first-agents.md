---
title: "Five LLM concepts I keep explaining to engineers shipping their first agents"
type: source
created: 2026-05-01
updated: 2026-05-01
sources: [Five LLM concepts I keep explaining to engineers shipping their first agents.md]
tags: [llm, context-window, tokens, temperature, hallucination, rag, ai-engineering, practitioners]
---

Practitioner-level article by an ML engineer who has shipped LLM-based products. The central thesis: the model is the simple part. Five operating characteristics cause teams to burn out, and most are learned by getting burned.

## Metadata

| Field | Value |
|---|---|
| Author | Harika Yenuga |
| Published | 2026-04-17 |
| URL | [generativeai.pub](https://generativeai.pub/five-llm-concepts-i-keep-explaining-to-engineers-shipping-their-first-agents-87c502f3c378) |
| Source type | Medium article |
| Domain | AI Engineering — LLM fundamentals for practitioners |

---

## Core Claim

> "The model is simple. It is in these five operating characteristics that teams truly burn out."

The author's vantage point: ML engineer who builds on LLMs for a living, including a coding agent used daily. The concepts are not research-grade — they are the five things that cost teams a week of confused debugging if not internalized early.

---

## The Five Concepts

### 1. Context Window — Treat It as RAM

**The mistake:** engineers confuse "the model has a 200K context" with "I can use 200K."

**The correct mental model:** the context window is a bounded RAM buffer containing everything the model can see at a given moment — system prompt, conversation history, tool schemas, every tool output, every prior response. There is no helpful error when you exceed it. Content silently truncates from the back.

**The concrete consequence:** a modest coding agent task — reading three medium files plus a few tool responses — can consume 30–50K tokens before the model has done any significant work.

**The design implication:** the majority of agent architecture is about one choice: *what does the model truly need to see vs. what can it retrieve on demand?* Teams that answer this well build systems that scale beyond toy demos. Teams that don't build agents that perform well on toy tasks but deteriorate under real workloads.

---

### 2. Tokens — The Unit That Actually Drives Cost

Tokens are sub-word fragments produced by the model's tokenizer. The count deviates from character or word intuition in ways that matter at scale.

**Three non-obvious facts:**

| Insight | Detail |
|---|---|
| Code tokenizes worse than prose | 200-line Python ≈ 3K tokens (not 2K). Brackets, underscores, indentation, identifiers all consume tokens. |
| Non-English text is 2–4x more expensive | Most production tokenizers are trained on English-heavy corpora. Japanese, Arabic, Hindi = 2–4x the token count for the same semantic content. Breaks naive cost models built on English benchmarks. |
| Structured output costs more | JSON, XML schema enforcement is not free — structured output consumes more tokens than equivalent prose. |

**Measurement approach:** run a representative sample of the actual workload through the specific model's tokenizer before shipping anything that scales. Word count estimates are inaccurate, systematically in the direction of *under*-counting, and often wrong by a significant margin.

---

### 3. Temperature — Tail Risk and Reproducibility, Not Creativity

**The standard framing (misleading):** temperature is a "creativity dial."

**The author's production framing:** temperature regulates **tail risk** and **reproducibility**.

| Use case | Temperature recommendation | Rationale |
|---|---|---|
| Tool-calling agents | Near zero | Same call, same input → same decision; debugging requires reproducibility |
| Structured extraction | Near zero | Correctness > variety |
| Classification | Near zero | Deterministic labeling |
| Code generation against spec | Near zero | Spec adherence matters more than variety |
| Diverse sample generation | Higher | When you want 10 variants and will pick the best |
| Brainstorming, creative copy | Higher | Answer space is large; no single correct answer |

**Critical production nuance:** temperature=0 is **not actually deterministic** in hosted APIs. Routing decisions, mixed-precision math, and inference batching all introduce nondeterminism. True reproducibility requires seeded inference on controlled infrastructure — and even then, guarantees are weaker than most engineers expect.

**The typical failure mode:** engineers raise temperature to "help the model be more creative," then can't reproduce a bug, then learn the lesson the hard way.

---

### 4. Hallucination — A Feature, Not a Bug (at the System Level)

**The incorrect mental model:** hallucination is a fault that needs to be fixed in the model.

**The author's framing:** LLMs are **pattern continuation engines, not knowledge bases**. When the model lacks a strong pattern for the actual answer, it generates a confident, fluent pattern for what an answer *looks like*. These two output types are indistinguishable to the user. The model provides no reliable internal signal to tell them apart.

**The key reframe:** hallucinations are better understood as a *feature* of these systems than a fault to be patched. They are controlled at the **system layer**, not the model layer.

**Three system-layer controls:**

1. **Ground in retrieved source material** — instead of asking the model to recall, provide the relevant content and ask the model to reason over it
2. **Constrain the output space** — use function signatures, schemas, or controlled generation to limit what the model can produce
3. **Verify before acting** — especially for irreversible actions, validate outputs before execution

**Specific coding agent hazard:** the model will confidently call APIs that do not exist — with correct-looking argument syntax and naming conventions. The fix is not better prompting; it's feedback in the agent loop.

---

### 5. RAG — Retrieval Is the Hard Part

**The common misconception:** RAG is a model technique.

**The correct framing:** RAG is a **system**, not a technique. The LLM is the simple part. The pipeline — chunking strategy, embedding model choice, hybrid search, reranking, query rewriting, evaluation methodology — determines whether the system is embarrassing or helpful.

**Diagnostic question for underperforming RAG teams:** "What does your retrieval recall look like at k=10 on a held-out evaluation set?"

Most teams have never measured it. They've been blaming the LLM for documents the retriever never surfaced.

---

## Author's Priority Recommendation

> "If you're newer to building on LLMs and you only internalize one of these, make it the context window. Every architectural choice you make is shaped by this limitation, which also happens to be the one that breaks most gradually. Everything else eventually announces itself. Context budgets just cause your system to become less effective until you question why it stopped working."

---

## Delta vs. Existing Wiki Knowledge

| Concept | Wiki status before this ingest |
|---|---|
| Context window as RAM | Discussed tangentially in claude-code-skills and ai-session-memory; no dedicated concept page |
| Token measurement methodology | llm-model-economics covers cost-at-scale; measurement approach (workload sampling, multilingual penalty) was new |
| Temperature as tail risk regulator | No wiki entry; entirely new concept page warranted |
| Hallucination as system-controlled feature | Touched in rag-approaches (grounding); no dedicated concept page |
| RAG — retrieval is the hard part | Reinforced by existing rag-approaches page; recall@k=10 diagnostic is new |

---

## Related Pages

- [[ai-engineering/llm-context-window]]
- [[ai-engineering/temperature]]
- [[ai-engineering/llm-hallucination]]
- [[ai-engineering/rag-approaches]]
- [[ai-engineering/llm-model-economics]]
- [[ai-engineering/claude-code-skills]]
- [[ai-engineering/ai-session-memory]]
