---
title: Glossary
type: glossary
created: 2026-04-07
updated: 2026-04-22
sources: [pageindex-vectorless-rag.md]
tags: [terminology, style, glossary]
---

# Glossary

Living reference of terms, definitions, and style conventions. The LLM checks this before using any technical term. Updated on every ingest that introduces new or refined terminology.

---

## How to Read This Glossary

Each entry follows this format:

**Term** *(canonical form)*
: Definition. Usage notes. Related terms.
- Preferred: `term` / Avoid: `deprecated term`
- See also: [[related-page]]

---

## Terminology

**RAG** *(Retrieval-Augmented Generation)*
: A pattern where an LLM's response is grounded in content retrieved from external documents rather than relying solely on training data. The retrieval step is the key engineering challenge.
- See also: [[rag-approaches]]

**Vector RAG** *(traditional RAG)*
: The dominant RAG implementation: documents are chunked, embedded into dense vectors, stored in a vector database, and retrieved via cosine similarity search at query time.
- Preferred: `vector RAG` / Avoid: `standard RAG`, `classic RAG` (ambiguous)
- See also: [[rag-approaches]]

**Vectorless RAG**
: A RAG approach that eliminates embeddings and vector databases entirely. Instead uses LLM reasoning over a structured document index (e.g., hierarchical tree) to identify relevant content.
- Canonical term introduced by VectifyAI for the PageIndex approach.
- See also: [[pageindex]], [[rag-approaches]]

**PageIndex**
: Open source vectorless RAG framework by VectifyAI (introduced September 2025). Builds a hierarchical tree index from a document's natural structure and uses LLM reasoning to navigate to the answer.
- See also: [[pageindex]]

**FinanceBench**
: A benchmark for evaluating RAG systems on financial document Q&A tasks. Used to compare retrieval accuracy. PageIndex scores 98.7%; traditional vector RAG scores ~50%.

**Chunking**
: The process of splitting a document into fixed-size segments (typically measured in tokens) before embedding. A necessary step in vector RAG, but one that destroys document structure and cross-references.
- See also: [[rag-approaches]]

**Tree Index** *(PageIndex tree, hierarchical index)*
: In PageIndex, the structured JSON representation of a document's content. Each node contains: `node_id`, `title`, `pages`, `summary`, `key_topics`. Built once at index time; used for reasoning-based retrieval at query time.
- See also: [[pageindex]]

**Reasoning-Based Retrieval**
: A retrieval strategy where an LLM reasons about *where in a document* an answer is likely located, navigating document structure rather than computing similarity scores. Contrasted with similarity-based retrieval.
- See also: [[rag-approaches]], [[pageindex]]

**FinanceBench** *(benchmark)*
: Financial document Q&A benchmark. PageIndex: 98.7% accuracy. Traditional vector RAG: ~50%.

**Cosine Similarity**
: The standard distance metric used in vector RAG to compare query embeddings against stored document chunk embeddings. Measures semantic similarity, not relevance to user intent.
- See also: [[rag-approaches]]

**VectifyAI**
: The team that built and maintains PageIndex. Also operates the cloud service at pageindex.ai.
- See also: [[pageindex]]

---

## Style Conventions

*(Writing rules and tone guidelines specific to this knowledge base's domain. Will populate as style guides and branded content are ingested.)*

| Convention | Rule | Example |
|---|---|---|
| *(none yet)* | | |

---

## Deprecated / Avoid List

Terms that have been replaced, renamed, or should not be used:

| Avoid | Use Instead | Reason |
|---|---|---|
| *(none yet)* | | |

---

## Regional / Variant Terms

Terms that differ between audiences, teams, or locales:

| Term | Region/Context | Notes |
|---|---|---|
| *(none yet)* | | |

---

## Related Pages

- [[overview]] — big-picture synthesis
- [[index]] — master catalog
