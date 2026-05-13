---
title: RAG Retrieval Approaches
type: concept
created: 2026-04-22
updated: 2026-05-13
sources: [pageindex-vectorless-rag.md, gaurav-shrivastav-rag-fundamentally-broken.md, Five LLM concepts I keep explaining to engineers shipping their first agents.md, BIMConverse - GraphRAG for IFC Natural Language Queries - IAAC BLOG.pdf, "The AI Revolution Nobody Saw Coming_ Why Ontology Just Beat Vector Embeddings.md"]
tags: [rag, retrieval, vector-rag, vectorless-rag, embeddings, chunking, gradient-wall, clara, differentiable-retrieval, graphrag, ontology, benchmarks]
---

Overview of Retrieval-Augmented Generation (RAG) retrieval strategies, contrasting the traditional vector-based approach with the emerging reasoning-based (vectorless) approach.

## What Is RAG?

Retrieval-Augmented Generation (RAG) is a pattern where an LLM's response is grounded in retrieved document content rather than relying solely on training data. The core challenge is the **retrieval step** — finding the right piece of content to feed to the LLM.

> "The model is the simple part. Retrieval is the hard job that determines whether your RAG system is embarrassing or helpful." — Harika Yenuga

**Practitioner diagnostic:** if your RAG system is underperforming, the first question to ask is not "which LLM should I use?" but: *"What does my retrieval recall look like at k=10 on a held-out evaluation set?"* Most teams have never measured it. They've been blaming the LLM for documents the retriever never surfaced.

## Two Analytical Frames

This page uses two complementary frames for evaluating RAG approaches:

- **Retrieval mechanism** — how each paradigm finds content (similarity, reasoning, graph, none); the primary organizing frame
- **Gradient wall** — whether the approach enables end-to-end learning between retriever and generator; a secondary frame introduced by Gaurav Shrivastav (2026)

Both frames are kept in tension: the paradigm frame shows best-fit use cases; the gradient wall frame exposes which "improvements" are architectural fixes vs. patches.

## The Gradient Wall: RAG's Structural Flaw

Standard RAG has a deeper architectural problem that chunk size, embedding models, and similarity thresholds cannot fix: **the retrieval step is not differentiable**.

Modern deep learning works via backpropagation: when a neural network makes a mistake, the error travels backward through every layer, adjusting weights proportionally to their contribution. This requires every step to be differentiable — smooth, continuous, mathematically well-behaved.

The top-K document selection step is not. A document is either in the context window or it is not. No fractional document; no smooth transition. So when the retriever surfaces wrong documents and the LLM generates a wrong answer, the error signal **cannot flow backward through the discrete selection step**. The retriever never learns it made a mistake. Next identical query → same mistake.

This is the gradient wall. It permanently decouples the retriever from the generator regardless of which retrieval paradigm is used. Almost all popular RAG improvements work *around* this wall; only CLaRa (see below) attacks it directly.

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

### Process-Level Improvements (gradient wall remains intact)

Two approaches improve Vector RAG accuracy without changing its fundamental architecture:

**Golden Retriever RAG** — An LLM intercepts the raw query before retrieval, expands jargon, resolves abbreviations, and adds contextual detail, then sends the enriched query to the retriever. Retrieval accuracy improves measurably. Cost: one extra LLM call per query (added latency).

**Instructed Retriever (Databricks, January 2026)** — Guides the retriever with structured instructions upfront rather than training it with generator feedback: (1) **Query Decomposition** — breaks multi-part questions into independently searchable components; (2) **Contextual Relevance** — reasons about actual intent, not keyword proximity; (3) **Metadata Reasoning** — converts "last year" into concrete date filters. Results on StaRK-Instruct benchmark: 35–50% recall gains; up to 70% on harder enterprise QA tasks. A genuinely useful system, but the retriever still cannot learn from generator outcomes — the wall is intact.

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

### Enterprise Ontology-Guided GraphRAG Pattern

Recent enterprise-oriented material adds a practical pattern on top of GraphRAG: treat graph retrieval as one component in a hybrid stack where ontology constraints and action semantics shape retrieval and execution together.

- **Vector retrieval** handles broad semantic recall
- **Graph traversal** resolves explicit relationships and multi-hop structure
- **Ontology-guided reasoning** enforces domain constraints and improves context completeness for agent actions

In practice, this pattern is strongest on relational and operational queries, while simple lookup queries may still be served efficiently by vector-centric retrieval alone. Reported numerical gains in this class of source should be treated as directional unless benchmark methodology is independently verified.

### BIM-Specific Execution Pattern (BIMConverse, 2024)

An applied thesis implementation in architecture/construction shows how GraphRAG patterns are operationalized for IFC archives:

- Revit -> IFC -> Neo4j LPG (via IfcOpenShell + TopologicPy + custom extraction)
- Natural language question -> Cypher translation -> graph execution -> JSON -> natural language answer
- Demonstrated over ~60 real residential projects, with strong quantitative and relational querying but noticeable sensitivity to prompt precision, context retention, and parameter naming heterogeneity

This case reinforces a practical distinction: many production "GraphRAG" implementations in domain systems behave as NL-to-graph-query mediators over explicit graph databases. They can provide strong grounding and low hallucination risk without necessarily implementing the full graph-community summarization pipeline associated with some Microsoft GraphRAG variants.

### Best for

- Large codebases with complex dependency graphs
- Mixed-media corpora (code + PDFs + video transcripts)
- Teams that need explainability about *why* a relationship was identified
- Scenarios where raw files cannot fit in context even with 1M-window models

### GraphRAG Performance Benchmarks (MDPI KA-RAG Study)

*Source: Aftab, "The AI Revolution Nobody Saw Coming" (Apr 2026) — [[ai-engineering/aftab-ontology-beat-vector-embeddings]]*

Study comparing vector RAG vs. ontology-guided GraphRAG on 20 complex enterprise queries over grant application documents:

| Metric | Vector RAG | GraphRAG (Ontology-Guided) |
|---|---|---|
| Retrieval Accuracy | 68% | **91.4%** |
| Complete Answers | 45% | **80%** |
| Hallucination Rate | 22% | **8%** |
| Multi-Hop Success | 30% | **85%** |

**Why the gap is largest on multi-hop queries:** vector similarity scores individual chunks independently — it cannot follow a chain `Shipment→Orders→Customers→Regions`. GraphRAG traverses that chain through explicit relationship edges. Where the answer requires connecting three or more entities, the structural advantage compounds.

**Caveat:** N=20 on a specific document type (grant applications). The numbers are directionally representative for relational enterprise queries, but should not be treated as universal baselines.

**Cost implication:** the higher retrieval precision of GraphRAG reduces token waste (fewer wrong chunks in context, fewer LLM retries), with an estimated 30–50% inference cost reduction vs. pure vector RAG for relational-heavy workloads. Offset by an upfront ontology construction cost of ~$50–200 (from an existing DB schema) to ~$500–2000/month (ongoing LLM extraction from unstructured text).

### Comparison with other paradigms

| Dimension | Vector RAG | Vectorless RAG | 1M Context | Graph RAG (Graphify) | CLaRa |
|---|---|---|---|---|---|
| Index type | Dense vectors | Hierarchical JSON tree | None | Knowledge graph | Memory tokens |
| Retrieval | Cosine similarity | LLM tree reasoning | None | Subgraph extraction | Differentiable top-k |
| Structure preserved | No (chunked) | Yes (tree) | Yes (full) | Yes (graph topology) | Semantic compression |
| Multi-hop reasoning | No | Limited | Yes | Yes | Via Query Reasoner |
| Provenance tracking | No | No | No | Yes (EXTRACTED/INFERRED) | No |
| End-to-end learning | No (gradient wall) | No (gradient wall) | N/A | No (gradient wall) | **Yes** |
| Best for | Large collections | Single long docs | Fits-in-context | Code + mixed corpora | Research / E2E training |

See [[ai-engineering/how-to-use-graphify-knowledge-graph]] for full Graphify implementation details.

## Fifth Paradigm: Differentiable Retrieval (CLaRa)

Published December 2025 by researchers from Apple and the University of Edinburgh. The only RAG approach that attacks the gradient wall directly rather than working around it.

Standard RAG compresses documents into text chunks and retrieves by vector similarity. CLaRa replaces this entirely:

- **Memory tokens** — compressed representations of document content. Not text chunks; not embeddings of text. Small sets of continuous, learned tokens encoding semantic meaning at **16x to 128x compression**, stripped of syntax noise and filler words.
- **Query Reasoner** — generates a hypothetical ideal answer first, then searches for memory tokens that would *support* that hypothetical. Inverse of standard retrieval: searching for what *should* be there, not what *looks similar*.
- **Differentiable top-k estimator** — makes the retrieval selection step mathematically smooth enough for gradients to flow backward from answer generation, through the retrieval step, into the Query Reasoner.

**The retriever can now learn from the generator's mistakes.** End-to-end training is possible for the first time.

**Released models (Hugging Face):** CLaRa-7B-Base, CLaRa-7B-Instruct, CLaRa-7B-E2E. The E2E variant uses the full differentiable retrieval loop.

**Status as of early 2026:** Research release. Production maturity to be established.

See [[ai-engineering/gaurav-shrivastav-rag-fundamentally-broken]] for the full source analysis including the gradient wall explanation and all five evaluated approaches.

---

## Related Pages

- [[ai-engineering/pageindex]]
- [[ai-engineering/pageindex-vectorless-rag]] (source article)
- [[ai-engineering/how-to-use-graphify-knowledge-graph]] (source article)
- [[bim-construction/bimconverse-graphrag-ifc-natural-language-queries]] (source article — BIM GraphRAG implementation)
- [[ai-engineering/gaurav-shrivastav-rag-fundamentally-broken]] (source article — gradient wall, CLaRa)
- [[ai-engineering/harika-yenuga-five-llm-concepts-first-agents]] (source article — practitioner framing, recall@k=10 diagnostic)
- [[ai-engineering/aftab-ontology-beat-vector-embeddings]] (source article — GraphRAG benchmarks, enterprise migration roadmap)
- [[ai-engineering/llm-model-economics]]
- [[ai-engineering/llm-hallucination]]
- [[ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens]] (source article)
