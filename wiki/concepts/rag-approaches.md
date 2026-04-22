---
title: RAG Retrieval Approaches
type: concept
created: 2026-04-22
updated: 2026-04-22
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

## Related Pages

- [[pageindex]]
- [[pageindex-vectorless-rag]] (source article)
