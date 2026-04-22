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

**Source count:** 3  
**Wiki pages:** 12 (index, log, overview, glossary + 3 sources + 4 concepts)  
**Last ingest:** 2026-04-22 — MBS Newsletter (Performance vs. Development Coaching)  
**Last lint:** —

---

## What This Wiki Covers

This wiki currently spans three domains:

### 1. RAG Retrieval Strategies (LLM / AI)
Contrast between traditional vector-based RAG and reasoning-based (vectorless) RAG. Core framework: PageIndex by VectifyAI.

- **RAG retrieval approaches** — Vector RAG vs. Vectorless RAG, strengths, limitations, when to use each, hybrid strategy
- **PageIndex** — Open source vectorless RAG framework; hierarchical tree indexing + LLM-powered reasoning; 98.7% accuracy on FinanceBench

### 2. Coordenação de Projetos BIM (Construção Civil)
Integração de disciplinas complementares em projetos BIM. Foco no problema cultural/processual (não apenas ferramental) da coordenação.

- **Coordenação BIM** — Modelo federado vs. cultura de responsabilidade sequencial; o princípio "não interessa quem chegou primeiro"
- **Pares de conflito** — Matrix de risco entre disciplinas: Estrutural×HVAC, Hidro×Elétrico, Estrutural×Hidro (ALTO); HVAC×Incêndio, Elétrico×Estrutural (MÉDIO)

### 3. Coaching and Leadership (Personal Development)

Distinction between performance coaching (task-focused) and development coaching (person-focused). Source: Michael Bungay Stanier (MBS Works).

- **Coaching modes** — Two modes on a spectrum; performance is the default under pressure; development requires intentional curiosity
- **Practical technique** — "What have you already considered?" as a minimal intervention to shift from solution mode to development mode

## Key Insights (as of last ingest)

**RAG domain:** The shift from *similarity-based retrieval* to *reasoning-based retrieval* is a meaningful architectural evolution for structured document Q&A. When tasks require understanding document structure and following logical references, reasoning beats similarity.

**BIM domain:** Coordenação BIM efetiva é um problema cultural e processual, não apenas tecnológico. Modelo federado é condição necessária, não suficiente. O critério correto para sequênciar decisões entre disciplinas é o menor custo total para o cliente, não quem chegou primeiro.

**Coaching domain:** The default mode under pressure is performance coaching. Development coaching requires a deliberate choice to stay curious. A single well-placed question — "What have you already considered?" — can shift the dynamic without sacrificing momentum.
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
