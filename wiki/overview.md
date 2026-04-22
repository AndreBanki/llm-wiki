---
title: Overview
type: overview
created: 2026-04-07
updated: 2026-04-22
sources: []
tags: [overview, synthesis]
---

# Knowledge Base Overview

*This page is the LLM's working synthesis of everything in the wiki. It updates after every ingest that shifts the big picture.*

---

## Current State

**Source count:** 1  
**Wiki pages:** 7 (index, log, overview, glossary + 1 source + 2 concepts)  
**Last ingest:** 2026-04-22 — "I Stopped Using Vector Databases for RAG: PageIndex Vectorless RAG"  
**Last lint:** —

---

## What This Wiki Covers

This wiki currently focuses on **RAG (Retrieval-Augmented Generation) retrieval strategies**, specifically the contrast between traditional vector-based RAG and the emerging reasoning-based (vectorless) approach pioneered by PageIndex.

### Core Topics

- **RAG retrieval approaches** — Vector RAG vs. Vectorless RAG, strengths, limitations, when to use each, hybrid strategy
- **PageIndex** — Open source vectorless RAG framework by VectifyAI; hierarchical tree indexing + LLM-powered tree search; 98.7% accuracy on FinanceBench

### Key Insight (as of last ingest)

The shift from *similarity-based retrieval* to *reasoning-based retrieval* is a meaningful architectural evolution for structured document Q&A. When tasks require understanding document structure and following logical references, reasoning beats similarity. PageIndex is the leading open source implementation of this pattern.

---

## Key Themes

*(Will populate after first few ingests. Expect themes like: product areas, user personas, documentation gaps, terminology decisions, style conventions.)*

---

## Open Questions

*(Questions that came up during ingests or queries but haven't been resolved yet. The LLM will maintain this list.)*

- What product or domain is this wiki primarily covering?
- Who are the primary user personas to document for?
- Is there an existing style guide to ingest as a baseline?

---

## Knowledge Gaps

*(Areas where more sources are needed. The LLM will flag these during ingests and lint passes.)*

---

## Related Pages

- [[index]] — full catalog of all wiki pages
- [[glossary]] — terminology and style conventions
