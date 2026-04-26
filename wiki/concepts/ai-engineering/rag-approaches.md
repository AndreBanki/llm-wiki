---
title: RAG Retrieval Approaches
type: concept
created: 2026-04-22
updated: 2026-04-26
sources: [pageindex-vectorless-rag.md]
tags: [rag, retrieval, vector-rag, vectorless-rag, embeddings, chunking]
---

Overview of Retrieval-Augmented Generation (RAG) retrieval strategies, contrasting the traditional vector-based approach with the emerging reasoning-based (vectorless) approach.

## What Is RAG?

Retrieval-Augmented Generation (RAG) is a pattern where an LLM's response is grounded in retrieved document content rather than relying solely on training data. The core challenge is the **retrieval step** — finding the right piece of content to feed to the LLM.

## Vector RAG (Traditional)

### How it works

1. Document → **Chunking** (split into fixed-size token windows)
2. Chunks → **Embedding model** → dense vectors
3. Vectors stored in a **vector database**
4. Query → embedded → **cosine similarity search** → top-k chunks
5. Chunks → LLM → answer

### Core assumption

> The text most semantically similar to the query is the most relevant.

### Known limitations

| Problem | Description |
|---|---|
| Chunking destroys context | Document structure, cross-references, and logical flow are severed at arbitrary token boundaries |
| Cross-references invisible | Phrases like "see Appendix G" become disconnected fragments with no link to their targets |
| Intent ≠ content | Query vocabulary may differ entirely from answer vocabulary — the LLM is asking *what* it wants, not *how the answer is phrased* |
| Similarity ≠ relevance | Semantically close chunks may not contain the actual answer (e.g., executive summary vs. balance sheet footnote) |

### Best for

- Searching across large collections of documents to identify which ones are relevant
- High-throughput, low-latency requirements
- Short, unstructured, or conversational documents

## Vectorless RAG (Reasoning-Based)

### How it works

1. Document → **Tree Builder (LLM)** → hierarchical node tree (title + summary + key topics per section)
2. Tree stored as JSON
3. Query → **Tree Search Agent (LLM)** reasons over tree → selects relevant branches
4. **Node Expander** drills deeper → **Content Retriever** fetches raw text
5. Raw text → LLM → answer with citations

### Core assumption

> If I were a human expert, where in this document would I look to answer this question?

### Key properties

- No embeddings, no vector database, no chunking
- Retrieval is **explainable** — the reasoning trace shows why sections were chosen
- Preserves document hierarchy and cross-references
- Multiple sequential LLM calls → higher latency and cost per query

### Best for

- Single long structured documents where precision matters (financial filings, legal contracts, technical manuals)
- Regulated industries requiring explainability and auditability
- Queries requiring exact numbers, specific citations, or cross-referenced data

## Comparison Table

| Dimension | Vector RAG | Vectorless RAG (PageIndex) |
|---|---|---|
| Index type | Dense vector embeddings | Hierarchical JSON tree |
| Retrieval mechanism | Cosine similarity | LLM reasoning over tree |
| Chunking | Required | Not used |
| Document structure | Destroyed | Preserved |
| Cross-references | Invisible | Navigable by reasoning |
| Explainability | None | Full reasoning trace |
| Latency | Low | Higher (multiple LLM calls) |
| FinanceBench accuracy | ~50% | 98.7% (PageIndex) |
| Best document type | Collections / short docs | Single long structured docs |

## Hybrid Approach

Use vector search to find the right document from a large collection, then use PageIndex to extract the precise answer from within that document. This combines the scalability of vector search with the precision of reasoning-based retrieval.

## Broader Pattern

The shift from similarity to reasoning in retrieval mirrors a broader trend: when tasks require understanding structure and following logic, reasoning-first approaches outperform similarity-first approaches. Claude Code has reportedly moved away from vector-based code retrieval in favor of reasoning-driven approaches for the same reason.

## Third Paradigm: 1M Context — No Retrieval At All

As of early 2026, a third option has emerged: **skip retrieval entirely**.

Models like Qwen 3.6 Plus (1M-token context window, linear attention architecture) can load an entire codebase or document corpus in a single inference call — including distant function definitions, cross-file dependencies, and historical context — with no retrieval pipeline.

| Paradigm | Retrieval mechanism | Structure preserved | Latency | Cost |
|---|---|---|---|---|
| Vector RAG | Cosine similarity | Destroyed by chunking | Low | Low (after index build) |
| Vectorless RAG | LLM tree reasoning | Preserved | High | High per query |
| 1M context | None | Fully preserved | Low | Depends on model pricing |

**When 1M context replaces RAG:**
- Single long document that fits in context (legal contracts, financial filings, entire codebases)
- Agents needing full session coherence (tool call history + plan traces stay in-window)
- Teams wanting to eliminate vector DB infrastructure entirely

**When 1M context is not enough:**
- Corpus larger than 1M tokens (then RAG is still needed)
- Cost sensitivity at scale (1M-context tier pricing is 3-4x standard tier)

See [[ai-engineering/llm-model-economics]] for the cost tradeoff analysis.

## Fourth Paradigm: Graph-Based RAG (Graphify)

A fourth retrieval approach where the document corpus is represented as a **persistent knowledge graph** rather than a vector index or a tree. Introduced by Graphify (2026).

### How it works

1. **Pass 1 — Deterministic AST Parsing** (local, no LLM): `tree-sitter` extracts code structure across 20 languages. Edges tagged `EXTRACTED`, confidence 1.0.
2. **Pass 2 — Local Transcription** (local, no LLM): `faster-whisper` transcribes audio/video.
3. **Pass 3 — Parallel LLM Extraction**: subagents process unstructured content (PDFs, docs, images) and infer relationships. Edges tagged `INFERRED` with a confidence score.
4. A `PreToolUse` hook intercepts queries before file-grepping — the assistant reads the graph first, retrieves a focused **subgraph**, and answers from structure.

### Key properties

- **Provenance tagging**: every edge is labeled `EXTRACTED`, `INFERRED`, or `AMBIGUOUS` — epistemic honesty about what was found vs. what was guessed
- **Deterministic + probabilistic separation**: rule-based extraction runs locally with confidence 1.0; LLM inference is explicitly labeled as probabilistic
- **Token compression**: serves ~300-token subgraphs instead of full raw files — claimed 71.5x reduction
- **Multi-hop**: topology-clustered graph enables following chains of relationships, not just single-document traversal

### Best for

- Large codebases with complex dependency graphs
- Mixed-media corpora (code + PDFs + video transcripts)
- Teams that need explainability about *why* a relationship was identified
- Scenarios where raw files cannot fit in context even with 1M-window models

### Comparison with other paradigms

| Dimension | Vector RAG | Vectorless RAG | 1M Context | Graph RAG (Graphify) |
|---|---|---|---|---|
| Index type | Dense vectors | Hierarchical JSON tree | None | Knowledge graph |
| Retrieval | Cosine similarity | LLM tree reasoning | None | Subgraph extraction |
| Structure preserved | No (chunked) | Yes (tree) | Yes (full) | Yes (graph topology) |
| Multi-hop reasoning | No | Limited | Yes | Yes |
| Provenance tracking | No | No | No | Yes (EXTRACTED/INFERRED) |
| Local/private pass | No | No | N/A | Yes (Pass 1 + 2) |
| Best for | Large collections | Single long docs | Fits-in-context | Code + mixed corpora |

See [[ai-engineering/how-to-use-graphify-knowledge-graph]] for full implementation details.

---

## Related Pages

- [[ai-engineering/pageindex]]
- [[ai-engineering/pageindex-vectorless-rag]] (source article)
- [[ai-engineering/how-to-use-graphify-knowledge-graph]] (source article)
- [[ai-engineering/llm-model-economics]]
- [[ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens]] (source article)
