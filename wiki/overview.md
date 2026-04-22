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

**Source count:** 5  
**Wiki pages:** 17 (index, log, overview, glossary + 5 sources + 7 concepts)  
**Last ingest:** 2026-04-22 — Gyaco article (Como a estrutura de time molda o seu produto)  
**Last lint:** —

---

## What This Wiki Covers

This wiki currently spans three domains:

### 1. RAG Retrieval Strategies (LLM / AI)
Contrast between traditional vector-based RAG and reasoning-based (vectorless) RAG. Core framework: PageIndex by VectifyAI.

- **RAG retrieval approaches** — Vector RAG vs. Vectorless RAG, strengths, limitations, when to use each, hybrid strategy [¹](sources/pageindex-vectorless-rag.md)
- **PageIndex** — Open source vectorless RAG framework; hierarchical tree indexing + LLM-powered reasoning; 98.7% accuracy on FinanceBench [¹](sources/pageindex-vectorless-rag.md)

### 2. Coordenação de Projetos BIM (Construção Civil)
Integração de disciplinas complementares em projetos BIM. Foco no problema cultural/processual (não apenas ferramental) da coordenação.

- **Coordenação BIM** — Modelo federado vs. cultura de responsabilidade sequencial; o princípio "não interessa quem chegou primeiro" [²](sources/francieli-wagner-bim-coordination.md)
- **Pares de conflito** — Matrix de risco entre disciplinas: Estrutural×HVAC, Hidro×Elétrico, Estrutural×Hidro (ALTO); HVAC×Incêndio, Elétrico×Estrutural (MÉDIO) [²](sources/francieli-wagner-bim-coordination.md)

### 3. Coaching and Leadership (Personal Development)

Two MBS Works newsletters covering the art of coaching and intentional conversation. Source: Michael Bungay Stanier (MBS Works).

- **Coaching modes** — Two modes on a spectrum; performance is the default under pressure; development requires intentional curiosity [³](sources/mbs-performance-vs-development-coaching.md)
- **Practical technique** — "What have you already considered?" as a minimal intervention to shift from solution mode to development mode [³](sources/mbs-performance-vs-development-coaching.md)
- **Conversation design** — Intentional group hosting via pre-selected questions; the "good host" role; the two-question dinner format ("What are you known for?" / "What are you up to?") [⁴](sources/mbs-two-questions-for-great-conversation.md)

### 4. Product Management and Organizational Design

One Gyaco article by Joca Torres covering the relationship between team structure and system architecture.

- **Conway's Law** — Organizations produce systems that mirror their communication structures; structure works silently against strategy when wrong [⁵](sources/gyaco-conway-team-structure.md)
- **Reverse Conway Maneuver** — Valid but incomplete tool; must be preceded by strategy (users + business objectives) [⁵](sources/gyaco-conway-team-structure.md)
- **Team topology** — System-centric vs. user-centric organizing; Lopes three-sided marketplace case study [⁵](sources/gyaco-conway-team-structure.md)
- **Principle:** "Estrutura deve seguir estratégia e arquitetura, nessa ordem" [⁵](sources/gyaco-conway-team-structure.md)

## Key Insights (as of last ingest)

**RAG domain:** The shift from *similarity-based retrieval* to *reasoning-based retrieval* is a meaningful architectural evolution for structured document Q&A. When tasks require understanding document structure and following logical references, reasoning beats similarity. [¹](sources/pageindex-vectorless-rag.md)

**BIM domain:** Coordenação BIM efetiva é um problema cultural e processual, não apenas tecnológico. Modelo federado é condição necessária, não suficiente. O critério correto para sequênciar decisões entre disciplinas é o menor custo total para o cliente, não quem chegou primeiro. [²](sources/francieli-wagner-bim-coordination.md)

**Coaching domain:** The default mode under pressure is performance coaching. Development coaching requires a deliberate choice to stay curious. A single well-placed question — "What have you already considered?" — can shift the dynamic without sacrificing momentum. The same philosophy extends to group settings: pre-designed questions ("What are you known for?" / "What are you up to?") act as containers that invite depth without requiring a structured agenda. [³](sources/mbs-performance-vs-development-coaching.md) [⁴](sources/mbs-two-questions-for-great-conversation.md)

**Product management domain:** The framing of a team's scope determines what solutions it can see. A team organized around a system can only solve problems by adding features to that system. A team organized around a user segment can draw from any channel, tool, or approach. This is a structural phenomenon, not a creativity problem — and it connects to the broader wiki theme: *the right framing unlocks a wider solution space* (echoed in coaching, conversation design, and BIM sequencing decisions). [⁵](sources/gyaco-conway-team-structure.md)
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
