# Wiki Index

Master catalog of all pages. The LLM reads this first when answering queries to find relevant pages. Updated on every ingest.

---

## How to Read This Index

Each entry follows this format:
```
- [[filename]] — one-line summary | type | last updated
```

---

## Core Files

| Page | Summary | Updated |
|---|---|---|
| [[overview]] | High-level synthesis of the entire knowledge base | 2026-04-07 |
| [[glossary]] | Living terminology, definitions, and style conventions | 2026-04-07 |

---

## Sources

*One entry per raw document ingested. Add entries here after each ingest. Organized by domain category.*

### AI Engineering

| Page | Summary | Updated |
|---|---|---|
| [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]] | Medium article: LLM Wiki pattern by Karpathy, implemented in 30 min with Cursor + Obsidian — origin story of this wiki's architecture | 2026-04-22 |
| [[ai-engineering/pageindex-vectorless-rag]] | Medium article: PageIndex vectorless RAG vs traditional vector RAG — 98.7% FinanceBench accuracy | 2026-04-22 |

### Coaching & Leadership

| Page | Summary | Updated |
|---|---|---|
| [[coaching-leadership/mbs-performance-vs-development-coaching]] | MBS email newsletter: performance vs development coaching; practical technique "What have you already considered?" | 2026-04-22 |
| [[coaching-leadership/mbs-two-questions-for-great-conversation]] | MBS email newsletter: two questions for deep group conversation; "good host" role; conversation design as intentional hosting | 2026-04-22 |
| [[coaching-leadership/mbs-paradoxes-of-being-a-coach]] | MBS email newsletter: four paradoxes of coaching (Humble Confidence, Fierce Love, Light and Grounded, Care and Don't Care) — the "being" vs. "doing" of coaching | 2026-04-22 |

### Product & Org Design

| Page | Summary | Updated |
|---|---|---|
| [[product-org-design/gyaco-conway-team-structure]] | Gyaco article (Joca Torres): Conway's Law, Reverse Conway Maneuver critique, Lopes case study — structure must follow strategy and architecture | 2026-04-22 |

### BIM & Construction

| Page | Summary | Updated |
|---|---|---|
| [[bim-construction/francieli-wagner-bim-coordination]] | LinkedIn post: coordenação BIM como problema cultural/processual, não apenas de ferramentas; matrix de conflitos entre disciplinas | 2026-04-22 |

---

## Concepts

*One entry per core domain concept. Organized by domain category.*

### AI Engineering

| Page | Summary | Updated |
|---|---|---|
| [[ai-engineering/llm-wiki-pattern]] | The LLM Wiki pattern: three-layer architecture (raw/ + wiki/ + schema), three operations (ingest/query/lint), knowledge compounding — and why it works without vector databases | 2026-04-22 |
| [[ai-engineering/pageindex]] | Open source vectorless RAG framework by VectifyAI — hierarchical tree + LLM reasoning | 2026-04-22 |
| [[ai-engineering/rag-approaches]] | Comparison of vector RAG vs vectorless RAG — strengths, limitations, and hybrid strategy | 2026-04-22 |

### Coaching & Leadership

| Page | Summary | Updated |
|---|---|---|
| [[coaching-leadership/coaching-modes]] | Performance vs. development coaching — the two modes, the default problem, and the "What have you already considered?" technique | 2026-04-22 |
| [[coaching-leadership/conversation-design]] | Intentional conversation hosting: pre-selected questions to invite depth; the two-question dinner format; the "good host" role | 2026-04-22 |
| [[coaching-leadership/coaching-paradoxes]] | Four paradoxes of the "being of coaching" (MBS): Humble Confidence, Fierce Love, Light and Grounded, Care and Don't Care | 2026-04-22 |

### Product & Org Design

| Page | Summary | Updated |
|---|---|---|
| [[product-org-design/conways-law]] | Lei de Conway + Manobra Reversa de Conway — team structure shapes product; reverse maneuver is valid but incomplete without strategy | 2026-04-22 |
| [[product-org-design/team-topology]] | Organizing principles for product teams: system-centric vs. user-centric vs. capability-centric; Lopes three-sided marketplace case | 2026-04-22 |

### BIM & Construction

| Page | Summary | Updated |
|---|---|---|
| [[bim-construction/bim-coordination]] | Coordenação BIM como problema cultural/processual; pares de maior risco de conflito entre disciplinas complementares | 2026-04-22 |

---

## Style Rules

*One entry per writing convention or style guideline.*

*(Empty — will populate as sources are ingested.)*

---

## Analyses

*One entry per synthesized output: comparison tables, gap analyses, outlines.*

*(Empty — file your first query answer here to start compounding.)*

---

## Index Maintenance Notes

- Add new pages immediately after creation
- Update the "last updated" date when a page changes substantially
- Mark orphan pages with `⚠️ orphan` until they gain inbound links
- If a category grows beyond 10 pages, consider adding sub-sections
- Pages are organized into 4 domain categories: `ai-engineering`, `coaching-leadership`, `product-org-design`, `bim-construction`
- Internal links use the format `[[category/filename]]` (e.g., `[[coaching-leadership/coaching-modes]]`)
