---
title: "I Stopped Using Vector Databases for RAG: PageIndex Vectorless RAG"
type: source
created: 2026-04-22
updated: 2026-04-22
sources: [pageindex-vectorless-rag.md]
tags: [rag, pageindex, vectorless-rag, vector-database, llm, retrieval]
---

Medium article by Sweety Tripathi (Apr 13, 2026) arguing that vectorless RAG via PageIndex outperforms traditional vector RAG for structured, complex documents.

## Metadata

| Field | Value |
|---|---|
| Author | Sweety Tripathi |
| Published | April 13, 2026 |
| Platform | Medium — Generative AI publication |
| URL | https://medium.com/generative-ai/i-stopped-using-vector-databases-for-rag-pageindex-vectorless-rag-e54dedbe364e |
| Reading time | 10 min |
| Raw file | `raw/pageindex-vectorless-rag.md` |

## Key Claims

- Vector RAG conflates "similar" with "relevant" — a fundamental flaw for precise fact retrieval in structured documents.
- PageIndex (by VectifyAI) achieves **98.7% accuracy on FinanceBench** vs ~50% for traditional vector RAG.
- PageIndex uses **no embeddings, no vector database, no chunking** — only hierarchical tree indexing + LLM reasoning.
- The approach is especially suited to single long structured documents (financial filings, legal contracts, technical manuals).
- A **hybrid approach** — vector search to find the document, PageIndex to extract the answer — is the recommended "best of both worlds."

## Three Problems with Vector RAG (per article)

1. **Chunking destroys context** — document structure, cross-references, and flow are lost
2. **Cross-references invisible** — "see Appendix G" becomes a dead fragment
3. **Queries express intent, not content** — query vocabulary may not match answer vocabulary

## PageIndex Architecture (Two Phases)

1. **Index phase:** LLM reads document → builds hierarchical JSON tree (node = section title + summary + key topics)
2. **Query phase:** LLM reasons over tree → navigates to relevant branch → retrieves raw text → generates answer with citations

## Implementation Notes

- Python implementation using PyMuPDF + Google Gemini 2.0 Flash
- Retrieval decision is fully explainable via `reasoning` field
- Sections grouped by page boundaries (not arbitrary token count)

## Quotes

> "What PageIndex is really doing is treating retrieval as a reasoning problem instead of a similarity problem."

> "No embeddings. No vector database. No chunking."

## Related Pages

- [[pageindex]]
- [[rag-approaches]]
