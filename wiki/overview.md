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

**Source count:** 10  
**Wiki pages:** 37 (index, log, overview, glossary + 10 sources + 20 concepts)  
**Last ingest:** 2026-04-22 — Palantir Blog (Deploying Full Spectrum AI in Days: How AIP Bootcamps Work)  
**Last lint:** —

---

## What This Wiki Covers

This wiki currently spans **six domains**:

### 1. RAG Retrieval Strategies (LLM / AI)
Contrast between traditional vector-based RAG and reasoning-based (vectorless) RAG. Core framework: PageIndex by VectifyAI.

- **RAG retrieval approaches** — Vector RAG vs. Vectorless RAG, strengths, limitations, when to use each, hybrid strategy [¹](sources/ai-engineering/pageindex-vectorless-rag.md)
- **PageIndex** — Open source vectorless RAG framework; hierarchical tree indexing + LLM-powered reasoning; 98.7% accuracy on FinanceBench [¹](sources/ai-engineering/pageindex-vectorless-rag.md)
- **MCP (Model Context Protocol)** — AI-driven tool orchestration protocol; AI decides which tools to use; tools not services; capability discovery; tool-level permissions; failure modes: tool overload, context drift [⁹](sources/ai-engineering/vidvatta-mcp-vs-api-architecture.md)
- **Palantir AIP** — Enterprise AI platform; Ontology grounds AI in real-world operational events (not just user messages); full spectrum AI from chat → automation → intelligent primitives; empirical AI architecture principle [¹⁰](sources/ai-engineering/palantir-aip-bootcamps.md)
- **Enterprise AI Deployment** — The bootcamp model for rapid value + capability building; the "learn to fish, eat a fish" principle; expert feedback loops as IP compounding; chat-to-automation as the key mindset shift [¹⁰](sources/ai-engineering/palantir-aip-bootcamps.md)

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

### 6. AI Security for GenAI (New)

Gartner research mapping security controls to the six stages of a GenAI workflow. The core claim: GenAI security requires stage-specific tool chains; no single console covers all stages.

- **GenAI workflow stages** — Data, Model, Generation, Deployment, Compliance/Monitoring, Feedback Loops; each stage has a distinct threat profile and security controls [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **Data security debt** — accumulated unaddressed governance work (classification, sensitivity labels, data catalogs) that GenAI adoption exposes; must be addressed early or blocks deployment [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **3H principles** — Helpful, Honest, Harmless (Anthropic); the evaluative standard for GenAI output quality and safety at the generation stage [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **Constitutional AI** — formalized governance directives embedded in the AI system to enforce 3H; cross-cutting: applies to training data selection, output filtering, and feedback correction [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **Human in the loop** — required architectural element at every stage, not optional; validates outputs, interprets compliance, provides judgment automated systems cannot [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **TRiSM** — Gartner's Trust, Risk, and Security Management meta-framework for AI governance [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)

### 5. AI Knowledge Management (Meta-domain)

This wiki's own architecture and methodology, traced back to Andrej Karpathy's `llm-wiki.md` pattern.

- **LLM Wiki pattern** — Three-layer architecture (raw/ + wiki/ + schema); three operations (ingest/query/lint); AI handles bookkeeping while humans focus on sourcing and questioning [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Knowledge compounding** — Each ingest makes the wiki richer; cross-references multiply; connections surface automatically; contrasted with chat-based AI that resets every session [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Index-based navigation** — `index.md` as a vectorless navigation map; the AI reads it first on every query to find relevant pages — no embeddings needed [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Schema as brain** — The schema/instruction file converts a general-purpose AI into a disciplined wiki maintainer; editing it adapts AI behavior to any domain [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)

### 6. Software Engineering / System Design

A comprehensive survey of distributed systems, scaling patterns, database strategies, and system design interview frameworks. Source: Shivam Bhadani (@shivambhadani_).

- **System design fundamentals** — Servers, DNS, latency, throughput, vertical vs horizontal scaling, auto-scaling, and back-of-the-envelope estimation as the entry point to any architecture decision [⁸](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **CAP theorem** — Foundational distributed systems tradeoff: in practice always CP or AP (never CAP); strong consistency for banking/payments; eventual consistency for social/catalog use cases [⁸](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **Database scaling ladder** — Progressive approach: index → vertical scale → partitioning → master-slave → multi-master → sharding; advance only when the previous step hits its limit [⁸](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **Messaging taxonomy** — Message queue (single consumer type, message deleted) vs message stream (multiple consumer groups, message persists); Kafka for high-throughput streams; Redis Pub/Sub for real-time push [⁸](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **Problem-solving framework** — Decompose into sub-problems; for each: database, caching, scaling/fault tolerance, communication (sync vs async) [⁸](sources/software-engineering/shivambhadani-system-design-for-beginners.md)

## Key Insights (as of last ingest)

**RAG domain:** The shift from *similarity-based retrieval* to *reasoning-based retrieval* is a meaningful architectural evolution for structured document Q&A. When tasks require understanding document structure and following logical references, reasoning beats similarity. [¹](sources/ai-engineering/pageindex-vectorless-rag.md)

**BIM domain:** Coordenação BIM efetiva é um problema cultural e processual, não apenas tecnológico. Modelo federado é condição necessária, não suficiente. O critério correto para sequênciar decisões entre disciplinas é o menor custo total para o cliente, não quem chegou primeiro. [²](sources/bim-construction/francieli-wagner-bim-coordination.md)

**Coaching domain:** The default mode under pressure is performance coaching. Development coaching requires a deliberate choice to stay curious. A single well-placed question — “What have you already considered?” — can shift the dynamic without sacrificing momentum. The same philosophy extends to group settings: pre-designed questions act as containers that invite depth without requiring a structured agenda. Beneath all of this sits the “being of coaching”: four paradoxes (Humble Confidence, Fierce Love, Light and Grounded, Care and Don’t Care) that AI cannot replicate — the embodied presence that makes questions land differently. [³](sources/coaching-leadership/mbs-performance-vs-development-coaching.md) [⁴](sources/coaching-leadership/mbs-two-questions-for-great-conversation.md) [⁶](sources/coaching-leadership/mbs-paradoxes-of-being-a-coach.md)

**Product management domain:** The framing of a team's scope determines what solutions it can see. A team organized around a system can only solve problems by adding features to that system. A team organized around a user segment can draw from any channel, tool, or approach. This is a structural phenomenon, not a creativity problem — and it connects to the broader wiki theme: *the right framing unlocks a wider solution space* (echoed in coaching, conversation design, and BIM sequencing decisions). [⁵](sources/product-org-design/gyaco-conway-team-structure.md)
**AI security domain:** The security of GenAI systems is a stage-specific problem: data quality threats (poisoning, leakage, polymorphism) precede model attacks (evasion, tampering), which precede generation risks (non-3H outputs), which precede deployment exploits (API hijacking, DoS), which precede compliance gaps, which precede feedback manipulation. Each layer must be solved in sequence. The cross-cutting insight: a human in the loop at every stage is the only safeguard against the failure modes that automated tools miss — not a luxury but a structural requirement. [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)

**AI knowledge management domain (meta):** This wiki is itself an instance of the LLM Wiki pattern. The same insight that makes vectorless RAG effective — reasoning about document structure rather than similarity-matching chunks — applies to wiki navigation: `index.md` is a structured navigation map, not a vector index. The maintenance cost argument is the key architectural claim: AI’s comparative advantage is exactly the bookkeeping that makes human-maintained wikis fail. This connects the meta-domain to all others: every insight ingested here is only as useful as the system’s ability to surface it later. [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
**Software engineering domain:** System design is fundamentally a framework for making principled tradeoffs under constraints. The 4-dimension decomposition (database, caching, scaling, communication) provides a repeatable structure for any problem. The CAP theorem names the irreducible tradeoff in distributed systems. The database scaling ladder names the right order of interventions. Crucially, this domain reinforces two existing wiki themes: (1) microservice boundaries mirror team communication structures — Conway's Law in software form; (2) consistent hashing uses structure-aware routing rather than brute-force search, directly paralleling PageIndex's vectorless RAG approach. [⁸](sources/software-engineering/shivambhadani-system-design-for-beginners.md)**AI agent architecture domain (MCP):** MCP represents the *action layer* of AI agents — complementing RAG (the retrieval layer) and LLM reasoning (the processing layer). The core architectural shift: decision-making about which tool to call moves from deterministic code into the model itself. This has direct security implications (tool-level permissions replace network-perimeter auth) and novel failure modes (tool overload, context drift) that have no traditional API analogs. Practical principle: expose fewer, well-scoped tools rather than comprehensive capability sets. [⁹](sources/ai-engineering/vidvatta-mcp-vs-api-architecture.md)

**Enterprise AI deployment domain (AIP):** The most important insight from Palantir's AIP Bootcamp model is the same insight that runs through the coaching, product, and system design domains of this wiki: *upfront architectural decisions made without empirical evidence are dangerous*. In AI deployment, this means: don't decide how many LLMs to use, whether to fine-tune, or what your learning loop looks like before you have a production use case to learn from. The enabling technology is the Ontology — a semantic data model that bridges operational reality and AI prompts, unlocking event-driven automation rather than just chat. This connects directly to MCP (both replace user-prompt-driven with event-driven AI) and to Conway's Law (both reject theological structure in favor of strategy-led, empirically-validated design). [¹⁰](sources/ai-engineering/palantir-aip-bootcamps.md)
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
