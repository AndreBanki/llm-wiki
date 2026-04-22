# I Stopped Using Vector Databases for RAG: PageIndex Vectorless RAG

**Author:** Sweety Tripathi  
**Published:** April 13, 2026  
**Source:** Medium — Generative AI publication  
**Tags:** Vectorless RAG, Vector Database, LLM, AI  
**URL:** https://medium.com/generative-ai/i-stopped-using-vector-databases-for-rag-pageindex-vectorless-rag

---

## Introduction

If you have been building RAG systems for a while, you know the frustration. You spend hours setting up embeddings, tuning chunk sizes, picking the right vector database, and then your system still returns the wrong answer. Not because it could not find something similar. But because "similar" and "relevant" are just not the same thing.

The author encountered this problem working with a 120-page 10-K financial filing. The vector RAG system kept pulling chunks from the executive summary when the actual answer was buried in a footnote on page 87. Both sections had similar keywords and similar semantic meaning, but only one had the actual number needed.

That is when the author found PageIndex.

---

## What Is PageIndex?

PageIndex is an open source RAG framework built by the team at VectifyAI. The core idea is simple but genuinely different: instead of converting documents into vectors and doing a nearest neighbor search, PageIndex builds a hierarchical tree structure from the document and then uses an LLM to reason its way to the right answer.

**No embeddings. No vector database. No chunking.**

They call it "vectorless RAG."

The project was introduced in September 2025. Benchmark: **98.7% accuracy on FinanceBench**. Traditional vector RAG systems score around 50% on the same benchmark.

---

## The Problem with Vector RAG

The fundamental assumption of vector RAG: the text most semantically similar to your query is also the most relevant. That assumption breaks constantly in the real world.

**Three core problems:**

1. **Chunking destroys context.** Splitting a 100-page document into 500-token chunks throws away the document's natural structure. Cross-references like "as mentioned in Table 3.2" become disconnected from their targets. The document has a logic and a flow. Chunking ignores all of that.

2. **Cross-references are invisible to vectors.** Documents often say things like "see Appendix G" or "refer to the prior year figures in Section 4." Vector similarity has no way to follow those references — it treats them as text fragments with no connection to where they point.

3. **Queries express intent, not content.** When a user asks a question, they are expressing what they want to know, not what the answer looks like. The answer might use completely different vocabulary than the question. Vector retrieval struggles here because it is matching question text against answer text.

---

## How PageIndex Works

PageIndex works in two main phases.

### Phase 1: Building the Index (Table of Contents Tree)

When you feed a document into PageIndex, it does not chunk it. Instead, it reads the document and builds a hierarchical tree that mirrors the document's natural structure — think of it like an intelligent, deeply nested table of contents.

Each node in the tree:
- Represents a section or subsection
- Has a title
- Has a summary (written by the LLM during indexing — this becomes the retrieval signal)
- Has key topics

Example tree for a 10-K filing:
```
Annual Report 2023
├── Business Overview
│   ├── Products and Services
│   └── Market Position
├── Risk Factors
│   ├── Financial Risks
│   └── Operational Risks
├── Financial Statements
│   ├── Balance Sheet
│   │   ├── Assets
│   │   └── Liabilities
│   └── Income Statement
└── Notes to Financial Statements
    ├── Note 1: Accounting Policies
    └── Note 12: Long-term Debt
```

### Phase 2: Reasoning-Based Tree Search

When a query comes in, PageIndex does NOT search a vector database. It gives the LLM the query and the top-level structure of the tree and asks it to reason about where the answer might be.

The LLM navigates the tree, drilling down level by level, until it reaches the content that answers the question. This is how a human analyst works — checking the table of contents, finding the right section, and going straight there.

---

## Architecture

Pipeline (index time):
1. Input Document (PDF, HTML, Markdown)
2. Document Parser (OCR or Markdown)
3. Tree Builder (LLM-powered) — generates hierarchical node tree with titles and section summaries
4. PageIndex Store (JSON Tree)

Pipeline (query time):
1. User Query
2. Tree Search Agent (LLM) — reads tree structure, selects most relevant branch
3. Node Expander — drills deeper into selected branch
4. Content Retriever — fetches raw text of relevant nodes
5. Answer Generator (LLM) — synthesizes answer with citations
6. Final Answer + Source References

Key insight: **every step except the final content fetch is a reasoning step**. The LLM is actively thinking about where to look, not matching vectors.

---

## Code Implementation (Python)

Uses: PyMuPDF (`fitz`) for PDF parsing, Google Gemini 2.0 Flash as LLM.

### Step 1: Parse Document
```python
import fitz  # pip install pymupdf

def parse_pdf(pdf_path: str) -> list[dict]:
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            pages.append({"page_num": i + 1, "text": text})
    doc.close()
    return pages
```

### Step 2: Group Pages into Sections
```python
def group_pages_into_sections(pages, per_section=3):
    sections = []
    for i in range(0, len(pages), per_section):
        batch = pages[i : i + per_section]
        section_id = f"S{str(i // per_section + 1).zfill(3)}"
        combined_text = "\n\n".join(p["text"] for p in batch)
        sections.append({
            "section_id": section_id,
            "start_page": batch[0]["page_num"],
            "end_page": batch[-1]["page_num"],
            "text": combined_text,
        })
    return sections
```

### Step 3: Build Tree Index (LLM-Powered)
LLM reads each section preview and generates: title, summary (2-3 sentences), key_topics. Result is a JSON tree stored to disk.

### Step 4: Tree Search (Reasoning)
LLM receives the full tree + query and returns: reasoning (step-by-step), selected_ids, confidence level.

The `reasoning` field is not decoration — it provides full explainability of the retrieval decision.

### Step 5: Content Retrieval
Simple dictionary lookup on parsed sections — no vector lookup, no embedding computation.

### Step 6: Answer Generation
Retrieved text + original question → Gemini → precise answer with page-level citations.

---

## When to Use PageIndex vs. Vector RAG

| Scenario | Use |
|---|---|
| Single long structured document, precision required | PageIndex |
| Need full reasoning trace / explainability | PageIndex |
| Regulated industries (finance, legal, healthcare) | PageIndex |
| Searching across large document collections | Vector RAG |
| High throughput, low latency required | Vector RAG |
| Short, unstructured, conversational documents | Vector RAG |
| Find document from collection + extract precise answer | Hybrid (both) |

**Best of both worlds:** Use vector search to find the right document from a collection, then use PageIndex to extract the precise answer from within that document.

---

## Getting Started

- GitHub: https://github.com/VectifyAI/PageIndex
- Cloud API: https://pageindex.ai
- MCP server available for direct integration with Claude and other agentic workflows
- Official cookbook examples get you to a working system in ~30 minutes

---

## Key Quote

> "What PageIndex is really doing is treating retrieval as a reasoning problem instead of a similarity problem."
