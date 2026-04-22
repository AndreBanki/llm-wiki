# Wiki Log

Append-only chronological record of all activity: ingests, queries, and lint passes.

To view recent activity: `grep "^## \[" log.md | tail -10`

---

## [2026-04-07] init | Wiki created

Wiki initialized for a technical writer's personal knowledge base.

Structure created:
- `raw/` — source documents folder
- `wiki/` — LLM-maintained knowledge base
- `wiki/sources/` — per-source summary pages
- `CLAUDE.md` — schema and operating instructions

Core pages created:
- `wiki/index.md`
- `wiki/log.md`
- `wiki/overview.md`
- `wiki/glossary.md`

Next step: Drop your first source into `raw/` and say **"ingest [filename]"**.

---

## [2026-04-22] ingest | I Stopped Using Vector Databases for RAG: PageIndex Vectorless RAG

**Source:** `raw/pageindex-vectorless-rag.md` (Medium article by Sweety Tripathi, Apr 13, 2026)

Pages created:
- `wiki/sources/pageindex-vectorless-rag.md`
- `wiki/concepts/pageindex.md`
- `wiki/concepts/rag-approaches.md`

Pages updated:
- `wiki/glossary.md` — added 9 new terms: RAG, Vector RAG, Vectorless RAG, PageIndex, FinanceBench, Chunking, Tree Index, Reasoning-Based Retrieval, VectifyAI
- `wiki/index.md` — added Sources and Concepts sections
- `wiki/overview.md` — updated state and domain coverage

Key additions:
- PageIndex by VectifyAI: vectorless RAG via hierarchical tree + LLM reasoning; 98.7% FinanceBench accuracy vs ~50% for vector RAG
- Core concept: "retrieval as a reasoning problem, not a similarity problem"
- Documented three canonical failures of vector RAG: chunking destroys context, cross-references invisible, queries express intent not content
- Documented hybrid strategy: vector search for document discovery + PageIndex for precise in-document extraction

---

## [2026-04-22] ingest | Francieli Wagner — BIM Coordination LinkedIn Post

**Source:** LinkedIn post by Francieli Wagner (PROJETSE Engenharia e Arquitetura), ~2026-04-22
**URL:** https://www.linkedin.com/posts/francieli-wagner_engenharia-incorporaaexaeto-bim-activity-7452373067118600192-EUlE

Pages created:
- `wiki/sources/francieli-wagner-bim-coordination.md`
- `wiki/concepts/bim-coordination.md`

Pages updated:
- `wiki/glossary.md` — added 8 new terms: BIM, Coordenação BIM, Modelo Federado, Compatibilização, Disciplinas Complementares, Clash Detection, PPCI, HVAC
- `wiki/index.md` — added new source and concept entries
- `wiki/overview.md` — added second domain (Coordenação de Projetos BIM), updated source count and key insights

Key additions:
- Core argument: coordenação BIM efetiva é um problema cultural/processual, não apenas tecnológico — modelo federado é necessário mas insuficiente
- Princípio: "Não interessa quem chegou primeiro. Interessa o que sai mais barato para o cliente."
- Matrix de risco de conflito entre disciplinas (F2-C): 3 pares ALTO (Estrutural×HVAC, Hidro×Elétrico, Estrutural×Hidro), 2 pares MÉDIO (HVAC×Incêndio, Elétrico×Estrutural)

---

## [2026-04-22] ingest | MBS Newsletter — Do you focus on the task or the person?

**Source:** Email newsletter by Michael Bungay Stanier (MBS Works), March 5, 2026
**URL:** https://mail.google.com/mail/u/0/#snoozed/FMfcgzQfCDWTHlVshvtMSDBxbHgmZrhL
**Purpose:** Writing and documenting coaching concepts for work

Pages created:
- `raw/mbs-performance-vs-development-coaching.md`
- `wiki/sources/mbs-performance-vs-development-coaching.md`
- `wiki/concepts/coaching-modes.md`

Pages updated:
- `wiki/glossary.md` — added 4 new terms: Performance Coaching, Development Coaching, Resisting the Urge to Rescue, Holding Space
- `wiki/index.md` — added new source and concept entries
- `wiki/overview.md` — added third domain (Coaching and Leadership), updated source count and key insights

Key additions:
- Core distinction: performance coaching (task-focused, default under pressure) vs. development coaching (person-focused, requires intentional curiosity)
- Risk of defaulting to performance: coach takes ownership of thinking, leaving the other person unaccomplished
- Practical technique: "What have you already considered?" — one question that shifts dynamic from solution mode to development mode
