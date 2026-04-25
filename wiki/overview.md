---
title: Overview
type: overview
created: 2026-04-07
updated: 2026-04-25
sources: []
tags: [overview, synthesis]
---

# Knowledge Base Overview

*This page is the LLM's working synthesis of everything in the wiki. It updates after every ingest that shifts the big picture.*

---

## Current State

**Source count:** 20  
**Wiki pages:** 52 (index, log, overview, glossary + 20 sources + 26 concepts + 1 analysis)  
**Last ingest:** 2026-04-25 — Daniel Rusnok / Medium (How I Added Persistent Semantic Memory to Claude Code in 15 Minutes)  
**Last lint:** 2026-04-24

---

## What This Wiki Covers

This wiki currently spans **six domains**:

### 1. RAG Retrieval Strategies (LLM / AI)
Contrast between traditional vector-based RAG and reasoning-based (vectorless) RAG. Core framework: PageIndex by VectifyAI.

- **RAG retrieval approaches** — Vector RAG vs. Vectorless RAG, strengths, limitations, when to use each, hybrid strategy [¹](sources/ai-engineering/pageindex-vectorless-rag.md)
- **PageIndex** — Open source vectorless RAG framework; hierarchical tree indexing + LLM-powered reasoning; 98.7% accuracy on FinanceBench [¹](sources/ai-engineering/pageindex-vectorless-rag.md)
- **MCP (Model Context Protocol)** — AI-driven tool orchestration protocol; AI decides which tools to use; tools not services; capability discovery; tool-level permissions; failure modes: tool overload, context drift [⁹](sources/ai-engineering/vidvatta-mcp-vs-api-architecture.md)
- **Claude Code Skills** — Directory-based context packages for AI coding agents; a skill is a folder (not a file): entry-point .md + config.json + scripts + templates + references + examples; 9 categories from library reference to infrastructure runbooks; the *gotchas section* is the most valuable content; folder structure enables progressive disclosure as context engineering; Opus 4.7 makes well-written skills dramatically more effective [¹¹](sources/ai-engineering/eric-luque-claude-code-skills.md)
- **AI as Operator** — Claude Opus 4.7 marks the transition from copilot (AI suggests, human validates) to operator (AI interprets, decides, executes — human arrives after); long context enables systemic visibility, meaning errors cascade globally not locally [¹²](sources/ai-engineering/eric-luque-claude-opus-47-operator-risk.md)
- **AI Agent Governance** — The new CTO/Principal responsibility: architecture of decision (where AI can/cannot decide); four-component production stack: real guardrails (executable policy), agent observability (what, why, cost), AI FinOps (budget control), execution control (suggest everything; execute within bounds) [¹²](sources/ai-engineering/eric-luque-claude-opus-47-operator-risk.md)
- **LLM Model Economics** — As of early 2026, the gap between frontier closed models and top open-weight models is now primarily economic rather than qualitative; Qwen 3.6 Plus (78.8% SWE-bench) is available at $0.28/M input tokens vs. $5.00/M for Claude Opus 4.6 (80.8%) — a 17x cost differential that is business-critical at agent pipeline scale [¹⁴](sources/ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens.md)
- **OpenRouter** — Inference routing platform aggregating open-weight and closed models under a single OpenAI-compatible API; enables per-task model routing (open-weight for volume, frontier for hard tasks) without infrastructure changes [¹⁴](sources/ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens.md)
- **1M Context vs. RAG** — Long-context windows (1M tokens) can replace chunking-based RAG pipelines for entire codebases or document corpora; eliminates vector DB infrastructure for single-document use cases; does not replace RAG for multi-document corpora larger than the context window [¹⁴](sources/ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens.md) [¹](sources/ai-engineering/pageindex-vectorless-rag.md)
- **Palantir AIP** — Enterprise AI platform; Ontology grounds AI in real-world operational events (not just user messages); full spectrum AI from chat → automation → intelligent primitives; empirical AI architecture principle [¹⁰](sources/ai-engineering/palantir-aip-bootcamps.md)
- **Ontology-Driven Architecture** — Schemas describe data; ontologies describe reality. An ontology defines entities, relationships, constraints, and valid state transitions — making it the operational core of the system, not a metadata layer. Big data worked without ontologies because intelligence was external (humans interpreted results). Agentic systems require ontologies because the system itself must act. Without ontologies, agents hallucinate actions, misuse tools, and produce unenforceable safety boundaries [¹⁵](sources/ai-engineering/balajiBal-palantir-ontologies.md)
- **Ontologies as Coordination Layer** — A shared ontology provides the deterministic interface that allows humans, services, and AI agents to operate together: a common model of what exists, what can change, who can change it. Governance alone (ownership, access control, compliance) is insufficient — "governance without ontology is bureaucracy without physics" [¹⁵](sources/ai-engineering/balajiBal-palantir-ontologies.md)
- **Enterprise AI Deployment** — The bootcamp model for rapid value + capability building; the "learn to fish, eat a fish" principle; expert feedback loops as IP compounding; chat-to-automation as the key mindset shift [¹⁰](sources/ai-engineering/palantir-aip-bootcamps.md)

### 2. Coordenação de Projetos BIM (Construção Civil)
Integração de disciplinas complementares em projetos BIM. Foco no problema cultural/processual (não apenas ferramental) da coordenação. Expansão para planejamento preditivo de execução de obras via IA e para a dimensão contratual como variável de configuração do planejamento.

- **Coordenação BIM** — Modelo federado vs. cultura de responsabilidade sequencial; o princípio “não interessa quem chegou primeiro” [²](sources/bim-construction/francieli-wagner-bim-coordination.md)
- **Pares de conflito** — Matrix de risco entre disciplinas: Estrutural×HVAC, Hidro×Elétrico, Estrutural×Hidro (ALTO); HVAC×Incêndio, Elétrico×Estrutural (MÉDIO) [²](sources/bim-construction/francieli-wagner-bim-coordination.md)
- **Planejamento preditivo de obras** — IA como antevisão: alimentar sistemas com dados reais (produtividade por frente, lead times de fornecedores, histórico de atrasos) para emitir alertas preditivos como “70% de chance de atrasar se o material não chegar até quinta” [¹³](sources/bim-construction/alessandro-lopes-planejamento-obra-40.md)
- **Cronograma inteligente** — visão de futuro: cronograma que aprende com cada obra executada e sugere sequência ótima de frentes; Brasil ainda dá os primeiros passos; ferramentas: Procore, Autodesk Construction Cloud [¹³](sources/bim-construction/alessandro-lopes-planejamento-obra-40.md)- **Dados como diferencial, não a ferramenta** — o que impacta o resultado de uma obra não é a ferramenta, mas como os dados são usados ao longo do processo; pré-condição: processos bem definidos + dados consistentes; ecoa "meaning precedes intelligence" do domínio de ontologias [¹⁹](sources/bim-construction/jhonatan-lazarin-ia-gestao-obras.md)
- **Cinco frentes de IA na gestão de obras** — mapa de posicionamento: (1) Planejamento e previsão, (2) Controle financeiro em tempo real, (3) Gestão de equipes/produtividade, (4) Execução e monitoramento, (5) Análise e melhoria contínua; Visus Planning na Frente 1 com potencial para Frente 4 [¹⁹](sources/bim-construction/jhonatan-lazarin-ia-gestao-obras.md)- **Tipos de Contrato em Engenharia** — O tipo de contrato define como o risco é alocado e o que cada stakeholder precisa monitorar. Turn-key/EPC: contratada absorve todo o risco → planejamento voltado para a gestão da contratada. Preço Unitário → medições e produtividade centrais. Administração/Cost Plus → custos e eficiência. Aliança/IPD → painel unificado. Princípio: "Grande parte dos problemas não nasce na execução — nasce na forma como o contrato foi estruturado" [¹⁸](sources/bim-construction/alexander-mattos-contratos-engenharia.md)
- **AltoQi Visus Planning (dimensão contratual)** — Para AltoQi Visus Planning, o tipo de contrato é uma variável de configuração: dashboards, alertas e stakeholder primário mudam conforme o modelo contratual do projeto [¹⁸](sources/bim-construction/alexander-mattos-contratos-engenharia.md)

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

### 5. AI Security for GenAI

Gartner research mapping security controls to the six stages of a GenAI workflow. The core claim: GenAI security requires stage-specific tool chains; no single console covers all stages.

- **GenAI workflow stages** — Data, Model, Generation, Deployment, Compliance/Monitoring, Feedback Loops; each stage has a distinct threat profile and security controls [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **Data security debt** — accumulated unaddressed governance work (classification, sensitivity labels, data catalogs) that GenAI adoption exposes; must be addressed early or blocks deployment [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **3H principles** — Helpful, Honest, Harmless (Anthropic); the evaluative standard for GenAI output quality and safety at the generation stage [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **Constitutional AI** — formalized governance directives embedded in the AI system to enforce 3H; cross-cutting: applies to training data selection, output filtering, and feedback correction [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **Human in the loop** — required architectural element at every stage, not optional; validates outputs, interprets compliance, provides judgment automated systems cannot [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)
- **TRiSM** — Gartner's Trust, Risk, and Security Management meta-framework for AI governance [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)

### 6. AI Knowledge Management (Meta-domain)

This wiki's own architecture and methodology, traced back to Andrej Karpathy's `llm-wiki.md` pattern.

- **LLM Wiki pattern** — Three-layer architecture (raw/ + wiki/ + schema); three operations (ingest/query/lint); AI handles bookkeeping while humans focus on sourcing and questioning [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Knowledge compounding** — Each ingest makes the wiki richer; cross-references multiply; connections surface automatically; contrasted with chat-based AI that resets every session [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Index-based navigation** — `index.md` as a vectorless navigation map; the AI reads it first on every query to find relevant pages — no embeddings needed [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Schema as brain** — The schema/instruction file converts a general-purpose AI into a disciplined wiki maintainer; editing it adapts AI behavior to any domain [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
- **Synthesis problem** — Experienced professionals don't have information problems; they have synthesis problems. The LLM Wiki's deepest value is not faster retrieval but surfacing connections across everything accumulated — showing what you don't know yet, and where two ideas almost touch but don't [¹⁶](sources/ai-engineering/tejas-sharma-karpathy-knowledge-system.md)
- **Quarriable knowledge** — Once the wiki is large enough, your own accumulated reading becomes answerable on demand, without hallucination from the open web [¹⁶](sources/ai-engineering/tejas-sharma-karpathy-knowledge-system.md)
- **Obsidian as reader, not builder** — Karpathy uses Obsidian only for navigation (browsing what the AI built), not for note creation; the distinction matters: the IDE layer is a viewer [¹⁶](sources/ai-engineering/tejas-sharma-karpathy-knowledge-system.md)

- **Session memory vs. domain knowledge** — Two complementary memory tiers for AI coding assistants: the LLM Wiki handles synthesized domain knowledge (curated sources, stable, cross-referenced); Mem0/ChromaDB handles episodic project decisions (automatic, ephemeral, per-project). Neither replaces the other. CLAUDE.md is a third tier (deterministic, always loaded). Together they give an AI assistant the full context a senior developer carries in their head [²⁰](sources/ai-engineering/daniel-rusnok-mem0-mcp-semantic-memory.md)
- **Knowledge promotion workflow** — Mem0 memories can graduate into wiki knowledge: when a project-specific decision reveals a generalizable pattern, it belongs in the wiki; the specific decision stays in Mem0. The wiki's glossary and concept pages provide the ontological backbone that makes Mem0 queries more precise [²⁰](sources/ai-engineering/daniel-rusnok-mem0-mcp-semantic-memory.md)
- **Hook production hazards** — AI-generated automation code passes a dry-run and fails under real-world concurrency. Four stacked failure modes documented: per-session locks (allow N concurrent extractions), PreCompact hook frequency, unbounded background processes, orphaned MCP servers. Meta-lesson: *"It generated a working script in 30 seconds" is not the same as "it generated a safe script."* [²⁰](sources/ai-engineering/daniel-rusnok-mem0-mcp-semantic-memory.md)

### 7. Software Engineering / System Design

A comprehensive survey of distributed systems, scaling patterns, database strategies, and system design interview frameworks. Source: Shivam Bhadani (@shivambhadani_).

- **System design fundamentals** — Servers, DNS, latency, throughput, vertical vs horizontal scaling, auto-scaling, and back-of-the-envelope estimation as the entry point to any architecture decision [¹⁷](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **CAP theorem** — Foundational distributed systems tradeoff: in practice always CP or AP (never CAP); strong consistency for banking/payments; eventual consistency for social/catalog use cases [¹⁷](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **Database scaling ladder** — Progressive approach: index → vertical scale → partitioning → master-slave → multi-master → sharding; advance only when the previous step hits its limit [¹⁷](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **Messaging taxonomy** — Message queue (single consumer type, message deleted) vs message stream (multiple consumer groups, message persists); Kafka for high-throughput streams; Redis Pub/Sub for real-time push [¹⁷](sources/software-engineering/shivambhadani-system-design-for-beginners.md)
- **Problem-solving framework** — Decompose into sub-problems; for each: database, caching, scaling/fault tolerance, communication (sync vs async) [¹⁷](sources/software-engineering/shivambhadani-system-design-for-beginners.md)

## Key Insights (as of last ingest)

**RAG domain:** The shift from *similarity-based retrieval* to *reasoning-based retrieval* is a meaningful architectural evolution for structured document Q&A. When tasks require understanding document structure and following logical references, reasoning beats similarity. [¹](sources/ai-engineering/pageindex-vectorless-rag.md)

**BIM domain:** Coordenação BIM efetiva é um problema cultural e processual, não apenas tecnológico. Modelo federado é condição necessária, não suficiente. O critério correto para sequênciar decisões entre disciplinas é o menor custo total para o cliente, não quem chegou primeiro. [²](sources/bim-construction/francieli-wagner-bim-coordination.md)

**BIM + AI cross-domain:** O maior inimigo de uma obra não é a dificuldade técnica — é a surpresa. A IA não substitui o gestor: ela fornece antevisão, cruzando dados reais de execução (produtividade por frente, lead times, histórico de atrasos) para prever riscos antes que se materializem. O que impacta o resultado, porém, não é a ferramenta — é como os dados são usados: IA amplifica apenas quando aplicada sobre processos bem definidos e dados consistentes (paralelo direto com "meaning precedes intelligence" do domínio de ontologias). O mapa completo das cinco frentes (planejamento, controle financeiro, equipes, execução, melhoria contínua) posiciona o Visus Planning primariamente na Frente 1, com dados do campo como caminho para a Frente 4. [¹³](sources/bim-construction/alessandro-lopes-planejamento-obra-40.md) [¹⁹](sources/bim-construction/jhonatan-lazarin-ia-gestao-obras.md)

**Coaching domain:** The default mode under pressure is performance coaching. Development coaching requires a deliberate choice to stay curious. A single well-placed question — “What have you already considered?” — can shift the dynamic without sacrificing momentum. The same philosophy extends to group settings: pre-designed questions act as containers that invite depth without requiring a structured agenda. Beneath all of this sits the “being of coaching”: four paradoxes (Humble Confidence, Fierce Love, Light and Grounded, Care and Don’t Care) that AI cannot replicate — the embodied presence that makes questions land differently. [³](sources/coaching-leadership/mbs-performance-vs-development-coaching.md) [⁴](sources/coaching-leadership/mbs-two-questions-for-great-conversation.md) [⁶](sources/coaching-leadership/mbs-paradoxes-of-being-a-coach.md)

**Product management domain:** The framing of a team's scope determines what solutions it can see. A team organized around a system can only solve problems by adding features to that system. A team organized around a user segment can draw from any channel, tool, or approach. This is a structural phenomenon, not a creativity problem — and it connects to the broader wiki theme: *the right framing unlocks a wider solution space* (echoed in coaching, conversation design, and BIM sequencing decisions). [⁵](sources/product-org-design/gyaco-conway-team-structure.md)
**AI security domain:** The security of GenAI systems is a stage-specific problem: data quality threats (poisoning, leakage, polymorphism) precede model attacks (evasion, tampering), which precede generation risks (non-3H outputs), which precede deployment exploits (API hijacking, DoS), which precede compliance gaps, which precede feedback manipulation. Each layer must be solved in sequence. The cross-cutting insight: a human in the loop at every stage is the only safeguard against the failure modes that automated tools miss — not a luxury but a structural requirement. [⁸](sources/ai-engineering/gartner-genai-security-workflow.md)

**AI knowledge management domain (meta):** This wiki is itself an instance of the LLM Wiki pattern. The same insight that makes vectorless RAG effective — reasoning about document structure rather than similarity-matching chunks — applies to wiki navigation: `index.md` is a structured navigation map, not a vector index. The maintenance cost argument is the key architectural claim: AI’s comparative advantage is exactly the bookkeeping that makes human-maintained wikis fail. This connects the meta-domain to all others: every insight ingested here is only as useful as the system’s ability to surface it later. [⁷](sources/ai-engineering/creativeaininja-llm-wiki-cursor-obsidian.md)
**Software engineering domain:** System design is fundamentally a framework for making principled tradeoffs under constraints. The 4-dimension decomposition (database, caching, scaling, communication) provides a repeatable structure for any problem. The CAP theorem names the irreducible tradeoff in distributed systems. The database scaling ladder names the right order of interventions. Crucially, this domain reinforces two existing wiki themes: (1) microservice boundaries mirror team communication structures — Conway's Law in software form; (2) consistent hashing uses structure-aware routing rather than brute-force search, directly paralleling PageIndex's vectorless RAG approach. [¹⁷](sources/software-engineering/shivambhadani-system-design-for-beginners.md)**AI agent architecture domain (MCP):** MCP represents the *action layer* of AI agents — complementing RAG (the retrieval layer) and LLM reasoning (the processing layer). The core architectural shift: decision-making about which tool to call moves from deterministic code into the model itself. This has direct security implications (tool-level permissions replace network-perimeter auth) and novel failure modes (tool overload, context drift) that have no traditional API analogs. Practical principle: expose fewer, well-scoped tools rather than comprehensive capability sets. [⁹](sources/ai-engineering/vidvatta-mcp-vs-api-architecture.md)

**Claude Code Skills domain:** The key insight from this article is a reframing: a skill is a *folder*, not a file. It is a complete context-delivery package — documentation, scripts, templates, examples, config — that transforms a general model into a domain specialist. The highest-value element of any skill is the *gotchas section*: production-discovered pitfalls the model repeatedly falls into. Skills should start minimal and grow organically. The folder structure itself is a context engineering tool (progressive disclosure). With Opus 4.7's more literal instruction-following, a well-written skill has proportionally higher ROI — and a vague description or missing gotchas is proportionally more costly. This connects directly to the LLM Wiki pattern: both are about accumulating non-obvious knowledge in structured, navigable form, compounding value over time. [¹¹](sources/ai-engineering/eric-luque-claude-code-skills.md)

**Enterprise AI deployment domain (AIP):** The most important insight from Palantir's AIP Bootcamp model is the same insight that runs through the coaching, product, and system design domains of this wiki: *upfront architectural decisions made without empirical evidence are dangerous*. In AI deployment, this means: don't decide how many LLMs to use, whether to fine-tune, or what your learning loop looks like before you have a production use case to learn from. The enabling technology is the Ontology — a semantic data model that bridges operational reality and AI prompts, unlocking event-driven automation rather than just chat. This connects directly to MCP (both replace user-prompt-driven with event-driven AI) and to Conway's Law (both reject theological structure in favor of strategy-led, empirically-validated design). [¹⁰](sources/ai-engineering/palantir-aip-bootcamps.md)

**Ontology-driven architecture domain:** The deepest insight from Palantir's ontology-first bet is a single principle: *meaning precedes intelligence*. Big data systems could work without ontologies because intelligence was external — analysts supplied judgment, governance supplied policy. Agentic systems cannot work without ontologies because the system itself must act at machine speed. The schema vs. ontology distinction is foundational: a schema tells you what a database looks like; an ontology tells you what the domain means — what states exist, what transitions are valid, what actions are permitted. Without this, agents don't fail loudly (hallucinations, policy violations, prompt spaghetti); they fail silently in production. The cross-domain connection: ontologies are the AI equivalent of a deliberate team topology — both reject emergent, unplanned design in favor of explicit upfront modeling that makes the system composable and reliable over time. [¹⁵](sources/ai-engineering/balajiBal-palantir-ontologies.md)
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

### 🔴 PRIORIDADE CRÍTICA — Ontologia como Camada Operacional

O wiki tem cobertura inicial do conceito de ontologia (via Palantir/balaji bal e AIP Bootcamps), mas ela é **superficial em relação à profundidade que o tema merece**. Ontologia é o mecanismo que transforma sistemas de IA em agentes confiáveis — e o wiki ainda não cobre:

- **Implementação prática de ontologias** — como se constrói uma ontologia operacional para um domínio real? Quais ferramentas (SPARQL, OWL, Property Graph, RDF)? Quais padrões de modelagem?
- **Ontologia vs. Knowledge Graph** — qual a diferença entre um ontology-driven system e um knowledge graph? Quando usar cada abordagem?
- **Ontologias em sistemas não-Palantir** — como empresas que não usam AIP implementam camadas semânticas equivalentes? Existem padrões open-source?
- **Ontologia e RAG** — qual a relação entre um ontology-driven retrieval e as abordagens de RAG já documentadas no wiki (vectorless, vector)? Uma ontologia pode substituir o índice?
- **Ontologia como interface de segurança** — a ligação entre ontologias e o GenAI Security Workflow (Gartner) ainda está subdesenvolvida. Como as constraints e state transitions da ontologia se mapeiam para os controles de segurança nos 6 estágios?
- **Ontologia em domínios específicos deste wiki** — BIM já tem um modelo de dados rico (IFC/BIM 360) — qual a relação com ontologias? Existe uma ontologia de construção civil?

**Fontes sugeridas para ingestão:**
- Documentação oficial do Palantir Ontology / Foundry
- Artigos sobre ontologia e agentic AI além da visão Palantir
- Casos de uso de knowledge graphs em enterprise AI (ex: AWS Neptune, Neo4j, Stardog)
- Especificação IFC como ontologia de construção

---

## Related Pages

- [[index]] — full catalog of all wiki pages
- [[glossary]] — terminology and style conventions
