# Wiki Log

Append-only chronological record of all activity: ingests, queries, and lint passes.

To view recent activity: `grep "^## \[" log.md | tail -10`

---

## [2026-04-22] ingest | I Gave an AI a One-Page Idea and It Built Me an Entire Knowledge Base in 30 Minutes

**Source:** `article.md` (Medium article by Balu Kosuri / @creativeaininja)
**URL:** https://medium.com/@creativeaininja/mempalace-the-viral-ai-memory-system-that-got-22k-stars-in-48-hours-an-honest-look-and-setup-26c234b0a27b

Pages created:
- `wiki/sources/creativeaininja-llm-wiki-cursor-obsidian.md`
- `wiki/concepts/llm-wiki-pattern.md`

Pages updated:
- `wiki/glossary.md` — added 8 new terms in new section "AI Knowledge Management": LLM Wiki, Schema File, Knowledge Compounding, Ingest, Lint, Cursor AI, Obsidian, Andrej Karpathy
- `wiki/index.md` — added 1 source entry and 1 concept entry
- `wiki/overview.md` — added 5th domain (AI Knowledge Management — meta-domain); added key insight for meta-domain; updated source count (6) and page count (20)

Key additions:
- This article is the **origin story** of this wiki's own architecture — traces the LLM Wiki pattern back to Karpathy's `llm-wiki.md` gist (early 2026)
- Core concept: three-layer architecture (raw/ + wiki/ + schema); schema file = "the brain" that converts a general-purpose AI into a disciplined wiki maintainer
- Core argument: AI's comparative advantage is bookkeeping — the work that kills human-maintained wikis; maintenance cost drops to nearly zero
- Knowledge compounding: the wiki grows richer with each ingest, unlike chat-based AI which resets every session
- Index-based navigation: `index.md` as a vectorless navigation map — cross-domain connection to PageIndex / vectorless RAG concepts already in the wiki
- Implementation: Cursor AI + Obsidian toolchain; full infrastructure buildable in 30 min from 3 prompts
- Cross-domain connection: `index.md` navigation IS an instance of reasoning-based retrieval (PageIndex domain); reinforces the wiki's recurring theme that *the right framing unlocks a wider solution space*

---

## [2026-04-22] ingest | MBS Works — The paradoxes of being a coach

**Source:** MBS Works newsletter by Michael Bungay Stanier, March 10, 2026  
**URL:** https://mail.google.com/mail/u/0/#snoozed/FMfcgzQfCMqcqBmFlkdsBJnkkpppPBjv

Pages created:
- `raw/mbs-paradoxes-of-being-a-coach.md`
- `wiki/sources/mbs-paradoxes-of-being-a-coach.md`
- `wiki/concepts/coaching-paradoxes.md`

Pages updated:
- `wiki/concepts/coaching-modes.md` — added cross-references to coaching-paradoxes and new source
- `wiki/glossary.md` — added 6 new terms: Being of Coaching, Humble Confidence, Fierce Love, Light and Grounded, Care and Don't Care; updated sources frontmatter
- `wiki/index.md` — added 1 source entry and 1 concept entry
- `wiki/overview.md` — added 2 new coaching domain bullets; updated coaching key insight to include being-of-coaching layer and ⁶ citation; updated source count (6) and page count (19)

Key additions:
- "Being of coaching" concept — coaching effectiveness lives in how you show up, not just what questions you ask
- Four paradoxes framework: Humble Confidence, Fierce Love, Light and Grounded, Care and Don't Care
- AI contrast: questions are replicable; the being is not — a new cross-domain connection between coaching and AI domains
- Outcome-ownership principle: coach creates conditions for better thinking; coachee owns the results
- Fierce Love connects to and extends the support/challenge axis in coaching-modes
- Light and Grounded reinforces the structure-vs-freedom balance in conversation-design

---

## [2026-04-22] ingest | Gyaco — Como a estrutura de time molda o seu produto

**Source:** Article by Joca Torres (Gyaco), published 2026-04-21
**URL:** https://www.gyaco.com/pt/2026/04/21/como-a-estrutura-de-time-molda-o-seu-produto

Pages created:
- `wiki/sources/gyaco-conway-team-structure.md`
- `wiki/concepts/conways-law.md`
- `wiki/concepts/team-topology.md`

Pages updated:
- `wiki/glossary.md` — added 6 new terms: Lei de Conway, Manobra Reversa de Conway, Times Orientados a Produto, Times Orientados a Usuário, Topologia de Times, Marketplace de Três Pontas; added new section "Product Management / Organizational Design"
- `wiki/index.md` — added 1 source and 2 concept entries
- `wiki/overview.md` — added 4th domain (Product Management and Organizational Design); updated source count (5) and page count (17); added key insight connecting product framing to the broader wiki theme of "right framing unlocks wider solution space"

Key additions:
- Core concept: Lei de Conway — structure silently shapes product; when wrong, works against strategy
- Critique: Manobra Reversa de Conway is valid but incomplete — must be preceded by strategy (who are users, what problems, what business objectives)
- Principle: "Estrutura deve seguir estratégia e arquitetura, nessa ordem"
- Lopes case study: teams organized around systems (portal, CRM, app) were blind to SMS/WhatsApp as lead delivery solutions; reorganized around marketplace actors (Cliente Final, Incorporadoras/Proprietários, Corretores/Franqueados, Sistemas Centrais) in one week
- Cross-domain insight: framing determines solution space — echoes coaching ("What have you already considered?") and conversation design (pre-selected questions open depth)

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

---

## [2026-04-22] ingest | MBS Newsletter — Two questions for a great conversation

**Source:** Email newsletter by Michael Bungay Stanier (MBS Works), March 31, 2026
**URL:** https://mail.google.com/mail/u/0/#snoozed/FMfcgzQgLFgnpdHzDmgxdtxGsGKNqsWT

Pages created:
- `raw/mbs-two-questions-for-great-conversation.md`
- `wiki/sources/mbs-two-questions-for-great-conversation.md`
- `wiki/concepts/conversation-design.md`

Pages updated:
- `wiki/concepts/coaching-modes.md` — added cross-reference to conversation-design
- `wiki/glossary.md` — added 6 new terms: Conversation Design, Good Host, The Conspiracy, Worthy Goal, "What are you known for?", "What are you up to?"
- `wiki/index.md` — added new source and concept entries
- `wiki/overview.md` — expanded coaching domain, updated source count and key insights

Key additions:
- New concept: conversation design — intentional pre-selection of questions to invite depth in a group setting
- Two-question dinner format: "What are you known for?" (values/best self) + "What are you up to?" (adventure/becoming)
- "Good host" as a role: curating people and questions to create conditions for meaningful connection
- The Conspiracy: MBS's accountability membership community; Worthy Goal as the member's declared aspiration
- Reinforces the MBS core philosophy: the right question unlocks more than advice or information
