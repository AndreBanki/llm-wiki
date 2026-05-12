---
title: LLM Wiki Pattern
type: concept
created: 2026-04-22
updated: 2026-05-01
sources: [article.md, tejas-sharma-karpathy-knowledge-system.md, Seamless Content Ingestion for Claude-Obsidian Second Brain.md, Your Obsidian Vault Is a Knowledge Graph. Here's How to Make It Think (quickly)..md]
tags: [llm-wiki, knowledge-management, ai-tools, rag, karpathy, cursor, obsidian, synthesis, pkm, content-acquisition, web-clipper, knowledge-graph]
---

# LLM Wiki Pattern

A pattern for AI-maintained personal knowledge bases: the AI reads source documents once and builds a structured, interlinked wiki — then updates that wiki incrementally as new sources are added — rather than re-reading raw files on every query.

---

## Origin

Introduced by **Andrej Karpathy** in early 2026 as a one-page markdown document (`llm-wiki.md`), designed to be copy-pasted into any AI agent as a working specification.

- Original gist: https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285
- Popularized via the article "I Gave an AI a One-Page Idea and It Built Me an Entire Knowledge Base in 30 Minutes" (Balu Kosuri / @creativeaininja, Medium, April 2026)

---

## The Core Problem It Solves

### The Maintenance Problem
Traditional knowledge management fails because of **maintenance cost**:
- Updating cross-references when a page changes
- Keeping summaries current as new information arrives
- Ensuring page A doesn't contradict page B
- Adding new terms to the glossary
- Linking new pages to old ones

This work is boring, repetitive, and never-ending. So wikis go stale, trust erodes, and nobody opens them.

**LLM Wiki's insight:** AI has a comparative advantage in exactly this type of work. It never gets tired. It can update 15 files in a single pass. It notices contradictions. The maintenance cost drops to nearly zero.

### The Synthesis Problem
Separately, even professionals with large, well-maintained archives face a deeper issue: **knowledge without connection is just storage**. The problem isn't retrieval — it's synthesis. Three archetypes (Tejas Sharma):

| Archetype | What they have | What they lack |
|---|---|---|
| Lawyer with 10 years of case notes | Deep information | A way to reason across all of it at once |
| Consultant who advised 30 companies | Domain knowledge | The pattern that connects the cases |
| Researcher who read 500 papers | Data | The connection that makes it cohere |

The LLM Wiki pattern addresses both problems: the AI handles maintenance *and* builds the connections that surface synthesis-level insights.

---

## The Three-Layer Architecture

### Layer 0 — Content Acquisition (upstream of raw/)
The pipeline that gets documents *into* `raw/` in the first place. Often the invisible prerequisite that determines whether the system actually gets used. Two patterns:

**Manual curation (this wiki's approach):** Human deposits files directly into `raw/` — PDFs, copied markdown, web-clipped `.md` files. Each source is deliberate. The tradeoff: higher friction, higher quality per source.

**Automated capture (Wilkins / Obsidian Web Clipper approach):**
- Browser extension converts any page to a structured markdown note with YAML frontmatter in 2 clicks
- Five content-type templates auto-selected by URL trigger: Article, PDF/Paper (arXiv etc.), Video (YouTube transcript), GitHub (README), Social Post
- Frontmatter populated automatically: `title`, `source` (URL), `author`, `published`, `created`, `description`, `tags`, `type`, `ingested`, `read`
- Notes land in an Obsidian Inbox folder overnight processing handles the rest
- Overnight Python script (Gemini Flash or local Ollama) tags and summarizes each note, then moves it from Inbox → Wiki via Obsidian CLI (preserving wikilinks)

**Key design insight (Wilkins):** *The best system is one you actually use.* Automation lowers the capture barrier to near zero; the tradeoff is less curation per source. In this wiki, `raw/clips/` is treated as an inbox: clips are ingested and then moved to `raw/`, so inbox contents always represent pending clips.

See [[ai-engineering/james-wilkins-obsidian-web-clipper-ingest]] for full implementation details.

### Layer 1 — Raw Sources (`raw/`)
- Immutable originals: PDFs, markdown files, web clips, transcripts, meeting notes, style guides
- AI reads from here; never writes here
- Human owns this folder

### Layer 2 — Wiki (`wiki/`)
- AI-generated and AI-maintained knowledge base
- Contains: summary pages, concept pages, product pages, persona pages, analysis pages, glossary, index, overview, log
- Human reads and browses; AI writes and maintains

### Layer 3 — Schema File (`CLAUDE.md` / `copilot-instructions.md`)
- The operating manual for the AI agent
- Defines: entity types, page YAML format, ingest/query/lint workflows, session-start checklist
- Human can edit to adapt the wiki to their domain
- Editing this file changes how the AI behaves — adding a new entity type instantly teaches the AI to recognize and file that knowledge type

---

## Three Operations

### Ingest
1. Drop a document in `raw/`
2. Tell the AI: "Ingest [filename]"
3. AI creates a source summary page, identifies and updates affected entity pages, adds terms to glossary, updates index, updates overview, appends to log
4. One source typically touches 10–15 wiki pages

### Query
1. Ask a question in natural language
2. AI reads `index.md` first (as navigation map), then reads relevant pages
3. AI synthesizes an answer with citations to wiki pages
4. AI offers to save the answer as an analysis page — questions compound the knowledge base

Once the wiki is large enough, it becomes **quarriable**: your own accumulated knowledge becomes answerable on demand, drawn entirely from what you've already read — no hallucinations from the open web.

**Step 5 — Filing outputs back in:** When the AI gives you an answer, generates a visualization, or writes a summary, file it back into the wiki. Every query enriches the base. This is the mechanism by which knowledge compounds — the wiki doesn't just reflect what you've read; over time it reflects what you've *thought*.

### Lint
1. Tell the AI: "Lint the wiki"
2. AI checks for: contradictions between pages, stale claims superseded by newer sources, orphan pages (no inbound links), concepts mentioned but lacking a page, missing cross-references, inconsistent terminology
3. AI proposes fixes; human approves

---

## Why It Works Without Vector Databases

The `index.md` acts as a lightweight navigation map. On every query, the AI reads `index.md` first to identify relevant pages, then reads only those pages. No embeddings, no cosine similarity, no vector database required.

This is functionally an instance of **reasoning-based retrieval** — the AI reasons about *where in the wiki* an answer lives, rather than computing similarity scores across all content. See [[ai-engineering/rag-approaches]] and [[ai-engineering/pageindex]] for the broader pattern.

**Practical limit:** Works well up to hundreds of pages. Beyond that, hierarchical indexing (as in PageIndex) or a two-level index would be needed.

---

## Knowledge Compounding

The central value proposition: **the wiki grows richer and more connected with each ingest**.

- After 3–5 sources: pages exist but connections are sparse
- After 10–15 sources: cross-references multiply; patterns across sources become visible in the overview; the AI starts surfacing connections you hadn't noticed
- After 20+ sources: the overview becomes a genuine synthesis; the glossary enforces consistent terminology across all writing

Compare to chat-based AI, which forgets everything after each session and re-derives answers from scratch every time.

---

## Recommended Toolchain

| Tool | Role |
|---|---|
| **Cursor AI** | Primary interface for talking to the AI agent; reads schema, runs ingest/query/lint |
| **Obsidian** | Browser/viewer for the wiki — a *reader*, not a builder. You navigate what the AI built; you don't create notes inside it. Graph view shows knowledge connections visually. **Complementary perspective (Shereshevsky):** Obsidian can also be the *builder* — a 5-year, 5,000-note vault is itself a knowledge graph that benefits from AI-assisted maintenance. The reader-vs-builder distinction depends on the layer: in the LLM Wiki pattern, Obsidian reads the AI-built wiki; in a personal vault, the human builds and the AI maintains. See [[ai-engineering/obsidian-knowledge-graph]]. |
| **Obsidian Web Clipper** | Browser extension to clip web articles directly to `raw/clips/` — 2-click capture with auto-populated YAML frontmatter; 5 content-type templates |
| Any AI agent | Claude, ChatGPT, Codex, etc. — paste `CLAUDE.md` into context if not using Cursor |

**Two-window workflow:** Cursor on the left (talk to AI), Obsidian on the right (watch wiki pages appear in real time).

---

## Use Cases

- **Technical writers:** Specs, customer calls, competitor analyses — glossary grows automatically; no re-researching what you already know
- **Researchers:** Papers cross-referenced; thesis evolves; connections between papers surfaces automatically
- **Product managers:** PRDs, interviews, retros — big picture stays coherent
- **Students:** Textbook chapters ingested sequentially; study guide builds itself
- **General:** Any domain where knowledge compounds over time from multiple sources

---

## Tips from Practice

1. **Ingest one source at a time** — stay involved; guide emphasis; ask follow-up questions
2. **Save good query answers** — tell the AI to file them as analysis pages; explorations should compound
3. **Check graph view often** — shows which pages are hubs, which are isolated
4. **Edit the schema for your domain** — add entity types specific to your work
5. **Never write wiki pages yourself** — your job is sources and questions; AI's job is filing and bookkeeping
6. **Check glossary before writing** — it has the right terms, the wrong terms, and the reasons

---

## Related Pages

- [[ai-engineering/rag-approaches]] — vectorless retrieval; index.md navigation is an instance of reasoning-based retrieval
- [[ai-engineering/pageindex]] — another vectorless RAG approach sharing the "no embeddings" philosophy
- [[glossary]] — canonical terms: LLM Wiki, schema file, knowledge compounding, ingest, lint, quarriable knowledge, synthesis problem
- [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]] — source article (Balu Kosuri; implementation walkthrough)
- [[ai-engineering/tejas-sharma-karpathy-knowledge-system]] — source article (Tejas Sharma; synthesis problem framing, quarriable knowledge)
- [[ai-engineering/shereshevsky-obsidian-vault-knowledge-graph]] — source article (Shereshevsky; vault-as-graph, compound maintenance, Obsidian-as-builder perspective)
- [[ai-engineering/obsidian-knowledge-graph]] — concept: Obsidian vault as implicit knowledge graph; graph metrics for PKM
