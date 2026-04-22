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

**Source count:** 6  
**Wiki pages:** 20 (index, log, overview, glossary + 6 sources + 9 concepts)  
**Last ingest:** 2026-04-22 — Medium article (LLM Wiki pattern: Cursor + Obsidian setup)  
**Last lint:** —

---

## What This Wiki Covers

This wiki currently spans **five domains**:

### 1. RAG Retrieval Strategies (LLM / AI)
Contrast between traditional vector-based RAG and reasoning-based (vectorless) RAG. Core framework: PageIndex by VectifyAI.

- **RAG retrieval approaches** — Vector RAG vs. Vectorless RAG, strengths, limitations, when to use each, hybrid strategy [¹](sources/ai-engineering/pageindex-vectorless-rag.md)
- **PageIndex** — Open source vectorless RAG framework; hierarchical tree indexing + LLM-powered reasoning; 98.7% accuracy on FinanceBench [¹](sources/ai-engineering/pageindex-vectorless-rag.md)

### 2. Coordenação de Projetos BIM (Construção Civil)
Integração de disciplinas complementares em projetos BIM. Foco no problema cultural/processual (não apenas ferramental) da coordenação.

- **Coordenação BIM** — Modelo federado vs. cultura de responsabilidade sequencial; o princípio "não interessa quem chegou primeiro" [²](sources/bim-construction/francieli-wagner-bim-coordination.md)
- **Pares de conflito** — Matrix de risco entre disciplinas: Estrutural×HVAC, Hidro×Elétrico, Estrutural×Hidro (ALTO); HVAC×Incêndio, Elétrico×Estrutural (MÉDIO) [²](sources/bim-construction/francieli-wagner-bim-coordination.md)

### 3. Coaching and Leadership (Personal Development)

Two MBS Works newsletters covering the art of coaching and intentional conversation. Source: Michael Bungay Stanier (MBS Works).

- **Coaching modes** — Two modes on a spectrum; performance is the default under pressure; development requires intentional curiosity [³](sources/coaching-leadership/mbs-performance-vs-development-coaching.md)
- **Practical technique** — "What have you already considered?" as a minimal intervention to shift from solution mode to development mode [³](sources/coaching-leadership/mbs-performance-vs-development-coaching.md)
- **Conversation design** — Intentional group hosting via pre-selected questions; the "good host" role; the two-question dinner format ("What are you known for?" / "What are you up to?") [⁴](sources/coaching-leadership/mbs-two-questions-for-great-conversation.md)- **Being of coaching** — What differentiates coach-like people is not their questions (AI can replicate those) but their embodied presence: four paradoxes each skilled coach must hold [⁶](sources/coaching-leadership/mbs-paradoxes-of-being-a-coach.md)
- **Four paradoxes** — Humble Confidence (you), Fierce Love (relationship), Light and Grounded (process), Care and Don't Care (outcome) [⁶](sources/coaching-leadership/mbs-paradoxes-of-being-a-coach.md)
### 4. Product Management and Organizational Design

One Gyaco article by Joca Torres covering the relationship between team structure and system architecture.

- **Conway's Law** — Organizations produce systems that mirror their communication structures; structure works silently against strategy when wrong [⁵](sources/product-org-design/gyaco-conway-team-structure.md)
- **Reverse Conway Maneuver** — Valid but incomplete tool; must be preceded by strategy (users + business objectives) [⁵](sources/product-org-design/gyaco-conway-team-structure.md)
- **Team topology** — System-centric vs. user-centric organizing; Lopes three-sided marketplace case study [⁵](sources/product-org-design/gyaco-conway-team-structure.md)
- **Principle:** "Estrutura deve seguir estratégia e arquitetura, nessa ordem" [⁵](sources/product-org-design/gyaco-conway-team-structure.md)

### 5. AI Knowledge Management (Meta-domain)

This wiki's own architecture and methodology, traced back to Andrej Karpathy's `llm-wiki.md` pattern.

- **LLM Wiki pattern** — Three-layer architecture (raw/ + wiki/ + schema); three operations (ingest/query/lint); AI handles bookkeeping while humans focus on sourcing and questioning [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Knowledge compounding** — Each ingest makes the wiki richer; cross-references multiply; connections surface automatically; contrasted with chat-based AI that resets every session [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Index-based navigation** — `index.md` as a vectorless navigation map; the AI reads it first on every query to find relevant pages — no embeddings needed [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Schema as brain** — The schema/instruction file converts a general-purpose AI into a disciplined wiki maintainer; editing it adapts AI behavior to any domain [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)

## Key Insights (as of last ingest)

**RAG domain:** The shift from *similarity-based retrieval* to *reasoning-based retrieval* is a meaningful architectural evolution for structured document Q&A. When tasks require understanding document structure and following logical references, reasoning beats similarity. [¹](sources/ai-engineering/pageindex-vectorless-rag.md)

**BIM domain:** Coordenação BIM efetiva é um problema cultural e processual, não apenas tecnológico. Modelo federado é condição necessária, não suficiente. O critério correto para sequênciar decisões entre disciplinas é o menor custo total para o cliente, não quem chegou primeiro. [²](sources/bim-construction/francieli-wagner-bim-coordination.md)

**Coaching domain:** The default mode under pressure is performance coaching. Development coaching requires a deliberate choice to stay curious. A single well-placed question — “What have you already considered?” — can shift the dynamic without sacrificing momentum. The same philosophy extends to group settings: pre-designed questions act as containers that invite depth without requiring a structured agenda. Beneath all of this sits the “being of coaching”: four paradoxes (Humble Confidence, Fierce Love, Light and Grounded, Care and Don’t Care) that AI cannot replicate — the embodied presence that makes questions land differently. [³](sources/coaching-leadership/mbs-performance-vs-development-coaching.md) [⁴](sources/coaching-leadership/mbs-two-questions-for-great-conversation.md) [⁶](sources/coaching-leadership/mbs-paradoxes-of-being-a-coach.md)

**Product management domain:** The framing of a team's scope determines what solutions it can see. A team organized around a system can only solve problems by adding features to that system. A team organized around a user segment can draw from any channel, tool, or approach. This is a structural phenomenon, not a creativity problem — and it connects to the broader wiki theme: *the right framing unlocks a wider solution space* (echoed in coaching, conversation design, and BIM sequencing decisions). [⁵](sources/product-org-design/gyaco-conway-team-structure.md)
**AI knowledge management domain (meta):** This wiki is itself an instance of the LLM Wiki pattern. The same insight that makes vectorless RAG effective — reasoning about document structure rather than similarity-matching chunks — applies to wiki navigation: `index.md` is a structured navigation map, not a vector index. The maintenance cost argument is the key architectural claim: AI’s comparative advantage is exactly the bookkeeping that makes human-maintained wikis fail. This connects the meta-domain to all others: every insight ingested here is only as useful as the system’s ability to surface it later. [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)

---

## Key Themes

*(Will populate after first few ingests. Expect themes like: product areas, user personas, documentation gaps, terminology decisions, style conventions.)*

---

## Open Questions

*(Questions that came up during ingests or queries but haven't been resolved yet. The LLM will maintain this list.)*

- What product or domain is this wiki primarily covering?
- Who are the primary user personas to document for?
- Is there an existing style guide to ingest as a baseline?
- Como estruturar protocolo de sequência de entregas entre disciplinas BIM?

---

## Knowledge Gaps

*(Areas where more sources are needed. The LLM will flag these during ingests and lint passes.)*

---

## Related Pages

- [[index]] — full catalog of all wiki pages
- [[glossary]] — terminology and style conventions
