# Wiki Log

## [2026-04-26] ingest | Planejamento da Construção com AltoQi Visus Planning — Objeto de Aprendizagem módulos 1–4 (GT TIC ANTAC / Mariana Farias / MDIC Construa Brasil)
Pages created: `wiki/sources/bim-construction/gt-antac-visus-planning-objeto-aprendizagem.md` — tutorial completo 4 módulos: modelo federado IFC, EAP, cronograma, setorização, simulação 4D, rastreamento planejado vs. executado, relatórios; `wiki/products/altoqi-visus-planning.md` — nova página de produto (primeiro uso do diretório `wiki/products/`)
Pages updated: `wiki/concepts/bim-construction/planejamento-preditivo-obras.md` — nova nota confirmando Frente 4 + links para product page; `wiki/glossary.md` — 8 novos termos (Simulação 4D, EAP, Predecessora, Setorização, Modelo Federado, Curva S, Projeto Construa Brasil; AltoQi Visus Planning expandido); `wiki/index.md` — nova linha de source + nova seção Products; `wiki/overview.md` — contadores atualizados, bullet Frente 4 confirmada + bullet workflow operacional; `mkdocs.yml` — nova linha de source + nova seção Products no nav; `raw/clips/ingested.md` — 4 filenames adicionados
Key additions: Frente 4 (rastreamento planejado vs. executado) confirmada no Visus Planning v2024 — não é mais "potencial futuro". EAP como estrutura unificada (quantitativo + orçamento + planejamento) documentada pela primeira vez. Projeto Construa Brasil (MDIC) adicionado como ator-chave no ecossistema BIM brasileiro. Primeiro uso do diretório `wiki/products/`.


Pages created: `wiki/sources/ai-engineering/how-to-use-graphify-knowledge-graph.md` — source summary: Graphify 3-pass pipeline (AST parsing, transcription, parallel LLM extraction); provenance tagging; subgraph retrieval; 71.5x token reduction claim
Pages updated: `wiki/concepts/ai-engineering/rag-approaches.md` — added Fourth Paradigm: Graph-Based RAG section with full comparison table; `wiki/glossary.md` — added Graphify, Provenance Tagging, Knowledge Graph RAG, AST Parsing, PreToolUse Hook; `wiki/index.md`, `wiki/overview.md`, `mkdocs.yml`, `raw/clips/ingested.md`
Key additions: Graph-based RAG documented as fourth paradigm alongside vector RAG, vectorless RAG, and 1M context. Provenance tagging (EXTRACTED/INFERRED/AMBIGUOUS) introduced as a new concept for epistemic honesty in AI-generated knowledge structures. The deterministic/probabilistic extraction distinction is a design principle applicable beyond Graphify.

## [2026-04-26] ingest | Seamless Content Ingestion for Claude-Obsidian Second Brain (James Wilkins — Medium)
Pages created: `wiki/sources/ai-engineering/james-wilkins-obsidian-web-clipper-ingest.md` — source summary: Obsidian Web Clipper + overnight ingest script pipeline; 5 content-type templates; tiered model routing pattern
Pages updated: `wiki/concepts/ai-engineering/llm-wiki-pattern.md` — added Layer 0 (Content Acquisition) section with automated capture pattern; `wiki/concepts/ai-engineering/llm-model-economics.md` — added Tiered Model Routing by Task Type section; `wiki/glossary.md` — added Obsidian Web Clipper, Content Acquisition Pipeline, Tiered Model Routing, Ollama; `wiki/index.md`, `wiki/overview.md`, `mkdocs.yml`
Key additions: Content acquisition as the upstream gap in the LLM Wiki pattern — the "how does anything get into raw/" question answered. Tiered model routing introduced as a distinct dimension: not just "which model for my app" but "which model for each task in my pipeline". This wiki's `raw/clips/` pattern documented as a parallel implementation of Wilkins' `ingested` checkbox system.


Pages created:
- `wiki/sources/ai-engineering/daniel-rusnok-mem0-mcp-semantic-memory.md` — session amnesia problem; Mem0 + MCP + ChromaDB architecture; 4-tool MCP interface; the Incident (7 parallel Claude instances); four root-cause bugs; fix with global pgrep cap + gtimeout; hook review checklist
- `wiki/concepts/ai-engineering/ai-session-memory.md` — new concept: three-tier memory model (context/session/domain), Mem0 MCP pattern, vectorless vs. semantic retrieval tension, production hook hazards
- `wiki/analyses/session-memory-vs-wiki-synergy.md` — synergy analysis: how Mem0 session memory and the Karpathy LLM Wiki operate as complementary tiers; combined architecture; knowledge promotion workflow; the vectorless/semantic tension resolved by knowledge type

Pages updated:
- `wiki/glossary.md` — added: AI Session Memory, AI Amnesia, Mem0, ChromaDB, Claude Code Hook; updated frontmatter sources
- `wiki/index.md` — added source entry, concept entry (ai-session-memory), new Analyses section with synergy page
- `wiki/overview.md` — updated source count (19→20), page count (49→52); added 3 bullets to domain 6 (AI Knowledge Management): session memory tier, knowledge promotion workflow, hook production hazards; updated last ingest
- `mkdocs.yml` — added AI Session Memory to Concepts nav; added Rusnok source to Sources nav; added Analyses section with synergy page
- `raw/ingested.md` — added entry for Rusnok article

Key additions: The distinction between *what I know* (wiki) and *what I decided* (Mem0) is now a first-class concept in the wiki. The synergy analysis surfaces the most actionable cross-domain insight: these two memory systems are not alternatives but complementary tiers, each optimized for its knowledge type. The hook incident provides a concrete production case study reinforcing the AI Agent Governance concept.

---

## [2026-04-25] ingest | IA na Gestão de Obras: dados como diferencial (Jhonatan Lazarin — LinkedIn)
Pages created:
- `wiki/sources/bim-construction/jhonatan-lazarin-ia-gestao-obras.md` — tese: o diferencial não é a ferramenta, mas como os dados são usados; mapa das cinco frentes de IA na gestão de obras; pré-condição: processos bem definidos + dados consistentes; relevância para Visus Planning

Pages updated:
- `wiki/concepts/bim-construction/planejamento-preditivo-obras.md` — adicionadas duas seções: "As Cinco Frentes de IA na Gestão de Obras" (tabela com maturidade por frente + posicionamento do Visus Planning) e "Dados como Diferencial, Não a Ferramenta" (com conexões cross-wiki a ontology-driven-architecture e Alessandro Lopes); atualizado frontmatter (sources, tags, updated)
- `wiki/glossary.md` — atualizado "AltoQi Visus Planning" (expandido com Cinco Frentes e framing Lazarin); adicionados: "Cinco Frentes de IA na Gestão de Obras", "Dados como Diferencial"
- `wiki/index.md` — adicionada nova source entry; atualizado summary de planejamento-preditivo-obras
- `wiki/overview.md` — atualizado source count (19); adicionados dois novos bullets à seção BIM; atualizado key insight BIM+AI com framing Lazarin
- `mkdocs.yml` — adicionado Jhonatan Lazarin à nav BIM sources
- `raw/ingested.md` — adicionada entrada para linkedin-post-jhonatan-lazarin-ia-gestao-obras

Key additions: O mapa das cinco frentes de IA na gestão de obras é agora um conceito de primeira classe no wiki — e um instrumento de posicionamento direto para o Visus Planning. A convergência entre "dados como diferencial" (Lazarin) e "meaning precedes intelligence" (Palantir Ontology) reforça um tema transversal emergente: sem substrato de dados bem estruturado, ferramentas de IA amplificam ruído, não insight.

---

## [2026-04-25] ingest | Tipos de Contratos em Engenharia: Riscos, Vulnerabilidades e Potencial de Perdas (Alexander Mattos — LinkedIn)
Pages created:
- `wiki/sources/bim-construction/alexander-mattos-contratos-engenharia.md` — tese central: problemas em projetos de engenharia nascem na estrutura do contrato; análise de Turn-key/EPC, Preço Unitário, Administração, Aliança/IPD; implicações para AltoQi Visus Planning
- `wiki/concepts/bim-construction/tipos-contrato-engenharia.md` — conceito completo: modelos contratuais em engenharia; matriz de risco por tipo; implicações para planejamento por stakeholder; vocabulário de claim management; FIDIC; dimensão AltoQi Visus Planning

Pages updated:
- `wiki/concepts/bim-construction/planejamento-preditivo-obras.md` — added "Contrato como Variável de Configuração" section com tabela: tipo de contrato → stakeholder → alertas críticos
- `wiki/glossary.md` — added: EPC, Turn-key/Empreitada Integral, Alocação de Risco, Claim, Claim Management, FIDIC, AltoQi Visus Planning
- `wiki/index.md` — added new source and concept entries for BIM & Construction
- `wiki/overview.md` — updated source count (17→18), page count (46→48), last ingest; extended BIM section with 2 new bullets (tipos de contrato + Visus Planning); updated section description
- `mkdocs.yml` — added Tipos de Contrato em Engenharia to concepts nav; added Alexander Mattos source to BIM sources nav

Key additions: A dimensão contratual é agora um conceito de primeira classe no wiki. A conexão mais importante: o tipo de contrato determina quem tem risco → o que precisa de visibilidade → requisito de produto para AltoQi Visus Planning. Isso transforma a análise de contratos de um tema de infraestrutura/óleo&gás em um insumo direto para o design de produto da AltoQi.

Note: source provided as a LinkedIn post screenshot in chat — no PDF file in raw/; ingested.md not updated.

---

## [2026-04-24] lint
Issues found: 6
- `overview.md` frontmatter `updated` stale (2026-04-22 → 2026-04-24)
- `index.md` overview entry date stale (2026-04-07 → 2026-04-24)
- `overview.md` duplicate section `### 6.` and out-of-order numbering (AI Security was 6, Knowledge Mgmt was 5, Software Eng was also 6) → renumbered to 5, 6, 7
- `overview.md` duplicate footnote `[⁸]` used by both Gartner GenAI Security and Shivambhadani → Shivambhadani reassigned to `[¹⁷]` (6 occurrences fixed)
- `glossary.md` line 455: `[[sources/ai-engineering/balajiBal-palantir-ontologies]]` used non-standard `sources/` prefix → fixed to `[[ai-engineering/balajiBal-palantir-ontologies]]`
- `overview.md` `Source count` stale (16 → 17) and `Wiki pages` count inflated with phantom "updated pages" language (54 → 46)
Fixes applied: all 6
No orphan pages. No contradictions.

Append-only chronological record of all activity: ingests, queries, and lint passes.

To view recent activity: `grep "^## \[" log.md | tail -10`

---

## [2026-04-24] ingest | How to Build the Knowledge System Andrej Karpathy Uses (Tejas Sharma — Level Up Coding / Medium)
Pages created:
- `wiki/sources/ai-engineering/tejas-sharma-karpathy-knowledge-system.md` — reframes LLM Wiki as a solution to the synthesis problem; quarriable knowledge; Obsidian as reader not builder; Constella reference; Karpathy's "hacky scripts" quote

Pages updated:
- `wiki/concepts/ai-engineering/llm-wiki-pattern.md` — added synthesis problem section with three-archetype table; added quarriable knowledge and "filing outputs back in" to query operation; updated Obsidian toolchain description to reader-not-builder
- `wiki/glossary.md` — added: PKM, Synthesis Problem, Quarriable Knowledge, Constella; updated Andrej Karpathy entry with "hacky scripts" quote
- `wiki/index.md` — added new source entry; updated llm-wiki-pattern concept summary
- `wiki/overview.md` — updated source count (16); added Synthesis Problem, Quarriable Knowledge, and Obsidian-as-reader bullets to AI Knowledge Management section
- `mkdocs.yml` — added LLM Wiki (Tejas Sharma) to AI Engineering sources nav

Key additions: The synthesis problem framing is now a first-class concept in the wiki — extending the LLM Wiki's value proposition from productivity (faster retrieval) to professional leverage (cross-domain synthesis). The "quarriable knowledge" vocabulary is a useful handle for conversations about when an LLM Wiki becomes genuinely powerful.

---

## [2026-04-24] ingest | Palantir's Real Secret Sauce — Ontologies (balaji bal — Medium)
Pages created:
- `wiki/sources/ai-engineering/balajiBal-palantir-ontologies.md` — schema vs. ontology distinction; why agentic systems require ontologies; ontologies as coordination layer and deterministic interface; "meaning precedes intelligence"
- `wiki/concepts/ai-engineering/ontology-driven-architecture.md` — deep concept page on operational ontologies; four components; schema/ontology contrast; big data era vs. agentic era; coordination layer; governance vs. ontology

Pages updated:
- `wiki/concepts/ai-engineering/aip-platform.md` — expanded Ontology section with schema/ontology distinction and link to ontology-driven-architecture concept
- `wiki/glossary.md` — updated Ontology entry; added: Schema vs. Ontology, Meaning Precedes Intelligence, World-Modeling, Deterministic Interface, Governance without Ontology
- `wiki/index.md` — added new source and concept entries
- `wiki/overview.md` — updated source count (15); added Ontology-Driven Architecture and Coordination Layer bullets; added ontology key insight paragraph
- `mkdocs.yml` — added Ontology-Driven Architecture to concepts nav; added Palantir Ontologies source to nav

Key additions: The schema vs. ontology distinction is now a first-class concept in the wiki. Directly deepens existing Palantir AIP coverage and connects to AI agent governance (deterministic guardrails), MCP (deterministic tool interfaces), and Conway's Law (explicit upfront structure vs. emergent design).

---

## [2026-04-24] ingest | Qwen 3.6 Plus Just Hit 1 Trillion Daily Tokens (Chew Loong Nian — Towards AI / Medium)
Pages created:
- `wiki/sources/ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens.md` — benchmark comparison, architecture specs, cost math, agentic design decisions, OpenRouter access guide
- `wiki/concepts/ai-engineering/llm-model-economics.md` — decision framework for model selection; token economics; open-weight vs. frontier; OpenRouter; linear attention + MoE; tiered agent architecture

Pages updated:
- `wiki/concepts/ai-engineering/rag-approaches.md` — added third paradigm: 1M context window as alternative to RAG chunking
- `wiki/concepts/ai-engineering/ai-agent-governance.md` — added model selection as AI FinOps dimension; linked to llm-model-economics
- `wiki/glossary.md` — added: SWE-bench Verified, Open-Weight Model, OpenRouter, Token Economics, Linear Attention, MoE, Qwen 3.6 Plus
- `wiki/index.md` — added new source and concept entries
- `wiki/overview.md` — updated source count (14); added LLM Model Economics, OpenRouter, and 1M Context vs. RAG bullets
- `mkdocs.yml` — added LLM Model Economics to concepts nav; added Qwen source to sources nav
- `raw/ingested.md` — added PDF to ingested list

Key additions: The 17x token cost differential between open-weight and frontier models is now documented as a business-critical agent architecture decision. OpenRouter is flagged as an infrastructure tool to investigate for agent pipelines.

---

## [2026-04-22] ingest | Planejamento de obra 4.0: algoritmos que otimizam cronogramas e antecipam gargalos (Alessandro Lopes)

**Source:** LinkedIn Pulse article by Alessandro Lopes (Sócio/Diretor de Inovação, Athié Wohnrath), April 22, 2026  
**URL:** https://www.linkedin.com/pulse/planejamento-de-obra-40-algoritmos-que-otimizam-e-antecipam-lopes-f8s9f/

Pages created:
- `wiki/sources/bim-construction/alessandro-lopes-planejamento-obra-40.md` — source summary: IA como antevisão no planejamento de obras; frentes de obra; cronograma inteligente; Procore/Autodesk Construction Cloud; MIT/PMI/ASCE references; Brazil as early-stage market
- `wiki/concepts/bim-construction/planejamento-preditivo-obras.md` — new concept page: planejamento preditivo, loop de dados históricos, frente de obra como unidade de análise, cronograma inteligente, tabela reagir→prever, knowledge gaps

Pages updated:
- `wiki/concepts/bim-construction/bim-coordination.md` — filled knowledge gap "ferramentas de coordenação BIM"; added Procore/Autodesk Construction Cloud table; added link to planejamento-preditivo-obras; updated related pages
- `wiki/glossary.md` — added 5 new terms under BIM section: Planejamento Preditivo de Obras, Frente de Obra, Cronograma Inteligente, Antevisão, Lead Time (construção)
- `wiki/index.md` — added source entry (Alessandro Lopes) and concept entry (Planejamento Preditivo de Obras) under BIM & Construction; updated bim-coordination summary
- `wiki/overview.md` — updated source count (12→13), page count (44→46), last ingest; extended BIM section with 2 new bullets (planejamento preditivo + cronograma inteligente); added BIM+AI cross-domain insight to Key Insights
- `mkdocs.yml` — added Planejamento Preditivo de Obras to concepts nav; added Alessandro Lopes source to sources nav
- `raw/ingested.md` — added PDF to ingested list

Key additions:
- First wiki coverage of construction execution planning as distinct from project coordination (Francieli Wagner covers design phase; this covers execution phase)
- Establishes "antevisão" as a named concept and the data loop (produtividade + lead times + histórico de atrasos) as the core mechanism
- Creates a meaningful cross-domain connection: the feedback loop principle is identical between Palantir AIP (operational data → better AI decisions) and construction predictive planning (historical execution data → better scheduling)
- Alessandro Lopes and Francieli Wagner now form a complementary pair covering the full lifecycle: design coordination + execution planning

---

## [2026-04-22] ingest | O Claude Opus 4.7 não é um upgrade. É o começo de um problema que você ainda não viu (Eric Luque)

**Source:** LinkedIn Pulse article by Eric Luque (Co-founder Ecotrace), April 16, 2026  
**URL:** https://www.linkedin.com/pulse/o-claude-opus-47-n%C3%A3o-%C3%A9-um-upgrade-come%C3%A7o-de-problema-que-eric-luque-zxgvf/

Pages created:
- `wiki/sources/ai-engineering/eric-luque-claude-opus-47-operator-risk.md` — source summary covering copilot→operator shift, four risks (global errors, silent cost, delegation without governance, pipeline anti-pattern), four-component stack, architecture of decision
- `wiki/concepts/ai-engineering/ai-agent-governance.md` — new concept page: delegation vs automation, long-context as operational risk, four-component production stack, architecture of decision

Pages updated:
- `wiki/concepts/ai-engineering/enterprise-ai-deployment.md` — added AI in Production: The Governance Gap section; new related pages
- `wiki/concepts/ai-engineering/mcp-architecture.md` — added execution limits and observability rows to common mistakes table
- `wiki/glossary.md` — added new section "AI Agent Governance" with 7 terms: AI Operator, Architecture of Decision, Delegation (AI), Agent Observability, AI FinOps, Silent Cost Creep, Execution Control
- `wiki/overview.md` — added AI as Operator and AI Agent Governance bullets to domain 1; updated source count (11→12) and page count
- `wiki/index.md` — added source entry and updated enterprise-ai-deployment + ai-agent-governance concept entries
- `mkdocs.yml` — added AI Agent Governance to concepts nav; added new source to AI Engineering sources nav
- `raw/ingested.md` — added PDF to ingested list

Key additions:
- First wiki coverage of AI governance as a discipline distinct from AI security (Gartner) — focuses on organizational architecture of decision rather than threat mitigation
- Establishes the copilot→operator shift as a named concept in the wiki
- Creates the AI FinOps and Agent Observability terms as first-class glossary entries
- Eric Luque's two articles (Skills + Operator Risk) now form a recognized pair: interface (Skills) + governance (Operator Risk)

---

## [2026-04-22] ingest | Skills no Claude Code: O Guia Definitivo (Eric Luque)

**Source:** LinkedIn Pulse article by Eric Luque (Co-founder Ecotrace), April 18, 2026  
**URL:** https://www.linkedin.com/pulse/skills-claude-code-o-guia-definitivo-para-quem-quer-parar-eric-luque-kosuf/

Pages created:
- `raw/eric-luque-claude-code-skills.md` — full article content in Markdown
- `wiki/sources/ai-engineering/eric-luque-claude-code-skills.md` — source summary with 9-category table, best practices, Opus 4.7 impact, and breaking changes
- `wiki/concepts/ai-engineering/claude-code-skills.md` — concept page for Claude Code Skills: what they are, folder structure, 9 categories, best practices, Opus 4.7 impact, relationship to MCP/RAG/LLM Wiki

Pages updated:
- `wiki/concepts/ai-engineering/mcp-architecture.md` — added Claude Code Skills row to relationship table; added to Related Pages; updated sources frontmatter
- `wiki/glossary.md` — added new section "Claude Code / Agentic Coding" with 7 new terms: Claude Code, Skill (Claude Code), Gotcha (skills), Context Engineering, Progressive Disclosure (prompts), Skill Description (trigger conditions), CLAUDE_PLUGIN_DATA, Task Budget (Opus 4.7)
- `wiki/index.md` — added 1 source entry and 1 concept entry; corrected domain count to 5
- `wiki/overview.md` — added Claude Code Skills bullet to AI Engineering domain (source ¹¹); added key insight paragraph for Skills domain; updated source count (11) and page count (40)

Key additions:
- Introduces **Claude Code Skills** as a structured, directory-based context-delivery mechanism for AI agents — a major new concept in the ai-engineering domain
- Core insight: the *gotchas section* is the most valuable part of any skill — production-discovered pitfalls that compound over time, directly paralleling this wiki's own knowledge-capture philosophy
- **Context engineering via folder structure**: progressive disclosure applied to LLM prompting — main file gives overview, subfolders are retrieved on demand to preserve context budget
- **Opus 4.7 impact**: more literal instruction following means descriptions and gotchas matter more than ever; the model rewards well-written skills disproportionately
- Cross-domain: Skills as client-side specialization above MCP extends the MCP concept from protocol to full workflow tooling; "start with one gotcha" mirrors "start with one use case" from enterprise AI deployment

---

## [2026-04-22] ingest | Deploying Full Spectrum AI in Days: How AIP Bootcamps Work

**Source:** Palantir Blog post, October 12, 2023  
**URL:** https://blog.palantir.com/deploying-full-spectrum-ai-in-days-how-aip-bootcamps-work-21829ec8d560

Pages created:
- `wiki/sources/ai-engineering/palantir-aip-bootcamps.md` — source summary with five "why it works" principles, 11 enterprise use cases, Ontology concept, and customer testimonials
- `wiki/concepts/ai-engineering/aip-platform.md` — concept page for Palantir AIP: Ontology, full spectrum AI maturity model, empirical AI architecture principle, bootcamp methodology, connections to MCP and Conway's Law
- `wiki/concepts/ai-engineering/enterprise-ai-deployment.md` — concept page for enterprise AI deployment: bootcamp model, chat-to-automation shift, expert feedback loops, empirical architecture, use case categories

Pages updated:
- `wiki/concepts/ai-engineering/mcp-architecture.md` — added AIP/Ontology as a cross-reference in the "Relationship to Other AI Engineering Concepts" table; added to Related Pages
- `wiki/glossary.md` — added new section "Enterprise AI Deployment / AIP" with 6 new terms: AIP, Ontology (Palantir), Full Spectrum AI, AIP Bootcamp, Empirical AI Architecture, Expert Feedback Loop; updated sources frontmatter
- `wiki/index.md` — added 1 source entry and 2 concept entries
- `wiki/overview.md` — added AIP and Enterprise AI Deployment bullets to RAG/AI domain section; added enterprise AI deployment key insight paragraph; updated source count (10) and page count (37); assigned source number ¹⁰

Key additions:
- Introduces **Enterprise AI Deployment** as a concrete, platform-specific domain in the wiki
- Core concept: the **Palantir Ontology** as the enabling layer that shifts AI from user-prompt-driven to event-driven (the operational bridge between real-world events and AI actions)
- **Empirical AI architecture** principle: architecture decisions must emerge from production experience, not upfront doctrine — the most important cross-domain insight of this ingest
- Cross-domain connections: (1) Ontology grounds AI in operational reality, parallel to MCP's event-driven tool orchestration; (2) "empirical not theological" mirrors Joca Torres's "structure follows strategy" principle
- **AIP Bootcamp model** as a repeatable methodology for rapid enterprise AI adoption: delivers working use case + team capability simultaneously

---

## [2026-04-22] ingest | System Design For Beginners: Everything You Need in One Article

**Source:** Medium article by Shivam Bhadani (@shivambhadani_), December 21, 2024  
**URL:** https://medium.com/@shivambhadani_/system-design-for-beginners-everything-you-need-in-one-article-c74eb702540b

Pages created:
- `wiki/sources/software-engineering/shivambhadani-system-design-for-beginners.md` — source summary with all 26 topics, key quotes, cross-domain connections
- `wiki/concepts/software-engineering/system-design-approach.md` — problem-solving framework (4-dimension decomposition), scaling fundamentals, load balancer algorithms, microservices vs monolith
- `wiki/concepts/software-engineering/cap-theorem-and-consistency.md` — CAP theorem (CP vs AP), strong/eventual consistency, quorum protocols (W+R>N), gossip protocol, consistent hashing ring algorithm
- `wiki/concepts/software-engineering/database-scaling.md` — progressive scaling ladder (indexing → partitioning → master-slave → multi-master → sharding), SQL vs NoSQL decision framework
- `wiki/concepts/software-engineering/distributed-systems.md` — coordinator/worker pattern, leader election algorithms, auto-recoverable systems, big data tools (Spark)
- `wiki/concepts/software-engineering/messaging-and-events.md` — message queue vs stream, Kafka internals (topics/partitions/consumer groups), real-time pub/sub, EDA patterns
- `wiki/concepts/software-engineering/caching-cdn-proxy.md` — caching strategies, Redis deep dive, blob storage (S3), CDN edge architecture, forward vs reverse proxy

Pages updated:
- `wiki/glossary.md` — added 14 new terms in new section "Software Engineering / System Design": CAP Theorem, Consistency, Eventual Consistency, Consistent Hashing, Sharding, Quorum, Message Queue, Message Stream, Event-Driven Architecture, Redis, CDN, Reverse Proxy, Leader Election, Microservices; updated sources frontmatter
- `wiki/index.md` — added software-engineering source entry and 6 concept entries; added Software Engineering sections
- `wiki/overview.md` — fixed section 6 content; updated source count (9) and page count (32); SE key insight already present

Key additions:
- Introduces **Software Engineering / System Design** as a new sixth domain
- Core framework: decompose any system design problem into sub-problems; for each decide database, caching, scaling/fault tolerance, and communication
- CAP theorem names the irreducible tradeoff in all distributed systems
- Database scaling ladder provides a principled, cost-ordered sequence of interventions
- Messaging taxonomy clarifies when to use queues vs streams vs pub/sub
- Consistent hashing connects cross-domain: ring-based structure-aware routing parallels PageIndex vectorless RAG (reason about structure, don't brute-force search)
- Microservices cross-domain connection: team structure mirrors service boundaries — directly reinforces Conway's Law in `product-org-design/conways-law.md`

---

## [2026-04-22] ingest | MCP vs. Traditional API Architecture: A Strategic Comparison (Vidvatta / LinkedIn)

**Source:** LinkedIn post by Vidvatta  
**URL:** https://www.linkedin.com/posts/vidvatta_%F0%9D%90%8C%F0%9D%90%82%F0%9D%90%8F-%F0%9D%90%AF%F0%9D%90%AC-%F0%9D%90%93%F0%9D%90%AB%F0%9D%90%9A%F0%9D%90%9D%F0%9D%90%A2%F0%9D%90%AD%F0%9D%90%A2%F0%9D%90%A8%F0%9D%90%A7%F0%9D%90%9A%F0%9D%90%A5-%F0%9D%90%80%F0%9D%90%8F%F0%9D%90%88-activity-7447139471264788480-ZpgD

Pages created:
- `raw/vidvatta-mcp-vs-api-architecture.md` — raw source content
- `wiki/sources/ai-engineering/vidvatta-mcp-vs-api-architecture.md` — source summary page with full layer-by-layer comparison tables
- `wiki/concepts/ai-engineering/mcp-architecture.md` — concept page for MCP: architecture layers, security model, failure modes, comparison with REST APIs, learning sequence

Pages updated:
- `wiki/glossary.md` — added 7 new terms in new section "MCP / Agent Architecture": MCP, MCP Server, Capability Discovery, Tool Overload, Context Drift, Tool-Level Permissions, Context Isolation; updated sources frontmatter
- `wiki/index.md` — added 1 source entry and 1 concept entry
- `wiki/overview.md` — added MCP bullet to RAG/AI domain; added key insight for MCP domain; updated source count (8) and page count (25); assigned source number ⁹

Key additions:
- MCP is entirely new to the wiki — introduces the *action/orchestration layer* of AI agents (complementing the existing retrieval layer: RAG/PageIndex)
- Core concept: the decision-making about which tool to invoke moves from deterministic code into the AI model itself — fundamental architectural shift
- Novel failure modes: tool overload and context drift have no traditional API analogs — important for practitioners designing agent systems
- Security model shift: tool-level permissions + context isolation replaces network-perimeter + token auth
- Learning guidance: Start with APIs → Move to MCP (APIs build system thinking; MCP builds AI orchestration thinking)
- Cross-domain connection: MCP's reasoning-based tool selection parallels vectorless RAG's reasoning-based document navigation — both reflect the same architectural philosophy of using LLM reasoning to navigate structured capability spaces

---

## [2026-04-22] ingest | Implement AI Security in the Generative AI Workflow (Gartner)

**Source:** Gartner research note, Joerg Fritsch, Marissa Schmidt et al.
**URL:** https://www.gartner.com/doc/reprints?id=1-2MS6Q352&ct=260129&st=sb
**Gartner ID:** G00832004 | October 2025

Pages created:
- `wiki/sources/ai-engineering/gartner-genai-security-workflow.md`
- `wiki/concepts/ai-engineering/genai-security-workflow.md`
- `wiki/concepts/ai-engineering/constitutional-ai.md`

Pages updated:
- `wiki/glossary.md` — added 12 new terms in new section "AI Security / GenAI Governance": 3H Principles, Constitutional AI, TRiSM, Data Security Debt, Human in the Loop, Data Poisoning, Model Evasion, Model Tampering, Model Leakage/Inversion, DSPM, Guardrails, Feedback Poisoning
- `wiki/index.md` — added 1 source entry and 2 concept entries
- `wiki/overview.md` — added 6th domain (AI Security for GenAI); updated source count (7) and page count (23); added key insight for AI security domain

Key additions:
- New domain: AI security for GenAI — no prior wiki pages covered this
- 6-stage GenAI workflow model (data, model, generation, deployment, compliance, feedback) as canonical framework for security governance
- 3H principles (Helpful, Honest, Harmless) — Anthropic's output quality standard
- Constitutional AI — formalized governance directives enforcing 3H across training, generation, and feedback stages
- Data security debt — the governance time-bomb most orgs face when deploying GenAI
- Human in the loop as a formal architectural requirement, not a nice-to-have
- TRiSM meta-framework for AI governance
- Full threat taxonomy: data polymorphism/poisoning/leakage, model evasion/tampering/leakage, API hijacking, DoS/cost exhaustion, feedback poisoning, sensor spoofing

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

## [2026-04-22] restructure | Reorganiza��o por categorias de dom�nio

Pages moved:
- wiki/sources/ ? 4 subcategories: i-engineering/ (2), coaching-leadership/ (3), product-org-design/ (1), im-construction/ (1)
- wiki/concepts/ ? 4 subcategories: i-engineering/ (3), coaching-leadership/ (3), product-org-design/ (2), im-construction/ (1)

Files updated:
- wiki/index.md � Sources and Concepts sections reorganized with category headers; maintenance notes updated
- wiki/overview.md � All (sources/filename.md) footnote links updated to include category subpath
- wiki/glossary.md � All [[wikilinks]] updated to [[category/filename]] format
- All 16 concept and source pages � [[wikilinks]] updated to [[category/filename]] format

Key changes:
- Domain categories established: i-engineering, coaching-leadership, product-org-design, im-construction
- Linking convention updated to [[category/filename]] across the entire wiki
- Schema unchanged � categories are a structural convention, not a new entity type
