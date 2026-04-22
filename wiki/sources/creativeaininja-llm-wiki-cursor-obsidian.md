---
title: "I Gave an AI a One-Page Idea and It Built Me an Entire Knowledge Base in 30 Minutes"
type: source
created: 2026-04-22
updated: 2026-04-22
sources: [article.md]
tags: [llm-wiki, ai-tools, knowledge-management, cursor, obsidian, karpathy, rag]
---

# I Gave an AI a One-Page Idea and It Built Me an Entire Knowledge Base in 30 Minutes

*A walkthrough of the LLM Wiki pattern, its implementation with Cursor AI, and Obsidian integration.*

---

## Metadata

| Field | Value |
|---|---|
| Author | Balu Kosuri (@creativeaininja) |
| Publication | Medium |
| Original URL | https://medium.com/@creativeaininja/mempalace-the-viral-ai-memory-system-that-got-22k-stars-in-48-hours-an-honest-look-and-setup-26c234b0a27b |
| Local file | `article.md` |
| Date | April 2026 |

---

## One-line Summary

Practical walkthrough of implementing Andrej Karpathy's LLM Wiki pattern in 30 minutes using Cursor AI (3 prompts) and Obsidian — demonstrates how AI-maintained wikis compound knowledge while eliminating the maintenance burden that kills human-maintained wikis.

---

## Key Facts

- **Origin:** Andrej Karpathy published `llm-wiki.md` in early 2026 — a one-page markdown document describing a pattern for AI-maintained knowledge bases; available at https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285
- **Implementation:** Author used Cursor AI to build the entire infrastructure in 3 prompts from a blank project folder
- **Time:** ~30 minutes from idea to working wiki
- **Core insight:** AI's comparative advantage is bookkeeping — cross-referencing, updating indexes, maintaining glossaries, flagging contradictions. This is exactly the work that causes human-maintained wikis to go stale and be abandoned.

## The Three-Layer Architecture

| Layer | Folder | Owner | Purpose |
|---|---|---|---|
| Raw sources | `raw/` | Human | Immutable originals — PDFs, markdown, transcripts, clippings |
| Wiki | `wiki/` | AI | Structured knowledge base — summary pages, concept pages, glossary, index |
| Schema | `CLAUDE.md` (or `copilot-instructions.md`) | Human (edits) / AI (reads) | Operating manual — entity types, page format, ingest/query/lint workflows |

## Three Operations

**Ingest:** Drop a document in `raw/`, tell the AI. The AI creates a source summary page, updates entity pages across the wiki, adds terms to glossary, updates the index, updates the overview. One source can touch 10–15 wiki pages.

**Query:** Ask a question. The AI reads the wiki (not raw files) to answer. Good answers can be saved back as analysis pages — questions make the knowledge base richer.

**Lint:** "Lint the wiki" triggers a health check: contradictions, stale claims, orphan pages (no inbound links), missing cross-references, inconsistent terminology.

## Why It Works Without Vector Databases

The `index.md` serves as a lightweight navigation map. When queried, the AI reads `index.md` first to identify relevant pages, then drills into them. No embeddings or similarity search needed — works well up to hundreds of pages.

**Connection to [[rag-approaches]]:** The wiki's own index.md is a vectorless navigation mechanism — an instance of the reasoning-based retrieval philosophy documented from the PageIndex source.

## The Schema File as "The Brain"

The schema file (`CLAUDE.md` / `copilot-instructions.md`) defines:
- Entity types (product, feature, persona, concept, style rule, analysis)
- YAML frontmatter format for every page
- Ingest workflow (step-by-step)
- Query workflow
- Lint workflow
- Session-start checklist

Editing this file changes how the AI behaves for your domain. Adding a new entity type (e.g., "API endpoint") instantly teaches the AI to recognize and file that type of knowledge.

## Setup with Cursor AI: The Three Prompts

1. **"What is this and how can I make use of this as a technical writer?"** → Cursor explained the pattern and mapped it to the author's use case
2. **"Can you make a plan and create?"** → Cursor built the full project structure, schema, and starter wiki pages
3. **"Can you set up Obsidian?"** → Cursor installed Obsidian via Homebrew, pre-configured vault with graph view, hotkeys, and sidebar layout

## Obsidian Integration

- Browsing layer: shows wiki pages as a visual graph
- Graph view color-coded by page type (sources = grey, glossary = orange, overview = purple, analyses = blue)
- Obsidian Web Clipper browser extension: clip web articles directly to `raw/`
- Two-window workflow: Cursor (left, talk to AI) + Obsidian (right, browse wiki in real time)

## Use Cases Identified

| Audience | Application |
|---|---|
| Technical writers | Product specs, customer calls, competitor analyses — glossary grows automatically |
| Researchers | Papers and articles cross-referenced; thesis evolves over time |
| Product managers | PRDs, interviews, retros — wiki maintains the big picture |
| Students | Textbook chapters ingested one at a time; study guide builds itself |
| General | Trip planning, hobby research, book clubs, course notes |

## Key Quotes

> "The reason people abandon wikis is not that they stop caring about the knowledge. It is that the maintenance becomes too much."

> "AI never gets tired of maintenance. It can update 15 files in a single pass."

> "Your job becomes the interesting part: finding good sources, asking the right questions, and deciding what matters."

---

## Related Pages

- [[llm-wiki-pattern]] — the LLM Wiki concept in full
- [[rag-approaches]] — vectorless retrieval philosophy; index.md is an instance of this
- [[pageindex]] — another vectorless approach; shares the "no embeddings" philosophy
- [[glossary]] — terms introduced: LLM Wiki, schema file, knowledge compounding, ingest, lint
