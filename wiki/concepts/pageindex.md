---
title: PageIndex
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [pageindex-vectorless-rag.md]
tags: [pageindex, vectorless-rag, rag, retrieval, vectifyai, llm-reasoning]
---

Open source vectorless RAG framework by VectifyAI that replaces embedding-based similarity search with LLM-powered hierarchical tree navigation for precise document retrieval.

## What It Is

PageIndex is an open source RAG framework that eliminates the need for vector databases entirely. Built by VectifyAI and introduced in September 2025.

**Core approach:** Build a hierarchical tree index from a document's natural structure, then use an LLM to *reason* its way to the relevant section — the same way a human analyst reads a table of contents.

**Tagline:** "Vectorless RAG" — no embeddings, no vector database, no chunking.

## Performance

| Benchmark | PageIndex | Traditional Vector RAG |
|---|---|---|
| FinanceBench accuracy | **98.7%** | ~50% |

## How It Works

### Phase 1 — Building the Index

1. Document is parsed page by page (PDF, HTML, Markdown)
2. Pages are grouped into sections by natural page boundaries
3. LLM reads each section and generates a structured node: `title`, `summary`, `key_topics`
4. Result: a hierarchical JSON tree stored to disk (the "PageIndex Store")

Each tree node mirrors the document's natural structure — effectively an intelligent, deeply nested table of contents.

### Phase 2 — Reasoning-Based Tree Search

1. Query arrives
2. LLM receives the full tree + query → reasons about which branch to explore
3. LLM drills down level by level (Node Expander) until reaching relevant content
4. Content Retriever fetches raw text of the selected nodes
5. Answer Generator synthesizes a precise answer with page-level citations

Every step except the final content fetch is a reasoning step. The LLM is actively thinking about where to look, not computing similarity.

## Architecture Components

| Component | Role |
|---|---|
| Document Parser | Extracts text via OCR or Markdown parsing |
| Tree Builder (LLM) | Generates hierarchical node tree with titles and summaries |
| PageIndex Store | Persisted JSON tree file |
| Tree Search Agent (LLM) | Selects most relevant branch for a given query |
| Node Expander | Drills into the selected branch |
| Content Retriever | Fetches raw section text |
| Answer Generator (LLM) | Produces final answer with citations |

## Key Differentiators

- **Explainability:** Every retrieval decision includes a `reasoning` field — you can see exactly why a section was chosen. Vector search cannot provide this.
- **Structure preservation:** Sections grouped by page boundaries, not arbitrary token counts.
- **Intent-aware:** LLM reasons about where an expert would look, rather than matching query vocabulary to answer vocabulary.

## When to Use PageIndex

**Good fit:**
- Single long structured documents (financial filings, legal contracts, technical manuals, academic papers)
- Situations where precision matters more than speed
- Regulated industries: finance, legal, healthcare
- When stakeholders need a full audit trail of where answers came from

**Not a good fit:**
- Searching across large document collections to find which document is relevant
- High throughput / low latency requirements (multiple sequential LLM calls add latency and cost)
- Short, unstructured, or conversational documents with no meaningful hierarchy

**Hybrid approach:** Use vector search to find the right document from a collection, then use PageIndex to extract the precise answer within that document.

## Getting Started

- GitHub: https://github.com/VectifyAI/PageIndex
- Cloud API + MCP server: https://pageindex.ai
- Reference implementation: Python + PyMuPDF + Google Gemini 2.0 Flash

## Related Pages

- [[pageindex-vectorless-rag]] (source article)
- [[rag-approaches]]
