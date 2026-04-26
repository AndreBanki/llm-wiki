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
| [[overview]] | High-level synthesis of the entire knowledge base | 2026-04-24 |
| [[glossary]] | Living terminology, definitions, and style conventions | 2026-04-07 |

---

## Sources

*One entry per raw document ingested. Add entries here after each ingest. Organized by domain category.*

### AI Engineering

| Page | Summary | Updated |
|---|---|---|
| [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]] | Medium article: LLM Wiki pattern by Karpathy, implemented in 30 min with Cursor + Obsidian — origin story of this wiki's architecture | 2026-04-22 |
| [[ai-engineering/pageindex-vectorless-rag]] | Medium article: PageIndex vectorless RAG vs traditional vector RAG — 98.7% FinanceBench accuracy | 2026-04-22 |
| [[ai-engineering/vidvatta-mcp-vs-api-architecture]] | LinkedIn post: MCP vs. Traditional API Architecture — strategic layer-by-layer comparison; client roles, protocol, services, security, scaling, career paths | 2026-04-22 |
| [[ai-engineering/gartner-genai-security-workflow]] | Gartner (Oct 2025): 6-stage GenAI security workflow — data, model, generation, deployment, compliance, feedback — with threat taxonomy and countermeasures | 2026-04-22 |
| [[ai-engineering/palantir-aip-bootcamps]] | Palantir Blog (Oct 2023): AIP Bootcamp model — 1–5 day enterprise AI deployment; Ontology concept; full spectrum AI; empirical architecture principle; 11 use cases | 2026-04-22 |
| [[ai-engineering/eric-luque-claude-code-skills]] | LinkedIn Pulse (Apr 2026): Claude Code Skills — directory-based context packages for AI agents; 9 skill categories; gotcha-driven knowledge capture; Opus 4.7 amplification | 2026-04-22 |
| [[ai-engineering/eric-luque-claude-opus-47-operator-risk]] | LinkedIn Pulse (Apr 2026): Opus 4.7 shifts AI from copilot to operator; four production risks (global errors, silent cost, delegation without governance, pipeline anti-pattern); four-component governance stack | 2026-04-22 |
| [[ai-engineering/balajiBal-palantir-ontologies]] | Medium (Mar 2026): Palantir's ontology-first approach as foundation for agentic AI; schema vs. ontology distinction; "Meaning precedes intelligence"; ontologies as deterministic interface and coordination layer | 2026-04-24 |
| [[ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens]] | Medium/Towards AI (Apr 2026): Qwen 3.6 Plus hits 1T daily tokens on OpenRouter; benchmark comparison vs Claude Opus 4.6 and GPT-5.4; token economics for agent pipelines; agentic architecture decisions | 2026-04-24 |
| [[ai-engineering/tejas-sharma-karpathy-knowledge-system]] | Level Up Coding/Medium (Apr 2026): reframes Karpathy's LLM Wiki as a solution to the synthesis problem; quarriable knowledge; Obsidian as reader not builder; Constella as no-code alternative | 2026-04-24 |
| [[ai-engineering/daniel-rusnok-mem0-mcp-semantic-memory]] | Medium (Apr 2026): adding persistent semantic memory to Claude Code via Mem0 + MCP + ChromaDB; session amnesia problem; 4-bug incident (7 parallel Claude instances); hook review checklist | 2026-04-25 |
| [[ai-engineering/james-wilkins-obsidian-web-clipper-ingest]] | Medium (Apr 2026): 2-click content acquisition pipeline for Claude-Obsidian Second Brain; Obsidian Web Clipper (5 templates); overnight Python script with tiered model routing (Gemini Flash/Ollama for tagging; Claude for synthesis) | 2026-04-26 |
| [[ai-engineering/how-to-use-graphify-knowledge-graph]] | Medium (Apr 2026): Graphify — converts any folder into a persistent knowledge graph; 3-pass pipeline (AST parsing, local transcription, parallel LLM extraction); provenance tagging (EXTRACTED/INFERRED/AMBIGUOUS); 71.5x token reduction via subgraph retrieval | 2026-04-26 |

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
| [[bim-construction/alessandro-lopes-planejamento-obra-40]] | LinkedIn Pulse (Abr 2026): planejamento preditivo de obras; IA como antevisão; frentes de obra; Procore/Autodesk Construction Cloud; Brasil em fase inicial | 2026-04-22 |
| [[bim-construction/jhonatan-lazarin-ia-gestao-obras]] | LinkedIn post (Abr 2026): IA na gestão de obras — dados como diferencial, não a ferramenta; mapa das cinco frentes (planejamento, controle financeiro, equipes, execução, melhoria contínua); pré-condição: processos bem definidos + dados consistentes | 2026-04-25 |
| [[bim-construction/alexander-mattos-contratos-engenharia]] | LinkedIn post (Abr 2026): tipos de contratos em engenharia (Turn-key/EPC, Preço Unitário, Administração, Aliança); contratos como modelos de alocação de risco; implicações para planejamento e AltoQi Visus Planning | 2026-04-25 |
| [[bim-construction/gt-antac-visus-planning-objeto-aprendizagem]] | GT TIC ANTAC / MDIC Construa Brasil (Mai 2025): workflow operacional completo do AltoQi Visus Planning — modelo federado IFC, EAP, cronograma 4D, setorização, simulação, rastreamento planejado vs. executado, relatórios | 2026-04-26 |

### Software Engineering

| Page | Summary | Updated |
|---|---|---|
| [[software-engineering/shivambhadani-system-design-for-beginners]] | Medium article: comprehensive system design survey (26 topics) for beginners — CAP theorem, database scaling, Kafka, EDA, consistent hashing, distributed systems | 2026-04-22 |

---

## Concepts

*One entry per core domain concept. Organized by domain category.*

### AI Engineering

| Page | Summary | Updated |
|---|---|---|
| [[ai-engineering/llm-wiki-pattern]] | The LLM Wiki pattern: three-layer architecture (raw/ + wiki/ + schema), three operations (ingest/query/lint), knowledge compounding — synthesis problem, quarriable knowledge, and why it works without vector databases; content acquisition layer (Layer 0) via Obsidian Web Clipper | 2026-04-26 |
| [[ai-engineering/ai-session-memory]] | AI session memory: three-tier memory model (context/session/domain), Mem0 + ChromaDB MCP pattern, hook production hazards, vectorless vs. semantic retrieval tension | 2026-04-25 |
| [[ai-engineering/pageindex]] | Open source vectorless RAG framework by VectifyAI — hierarchical tree + LLM reasoning | 2026-04-22 |
| [[ai-engineering/rag-approaches]] | Comparison of vector RAG vs vectorless RAG vs graph-based RAG (Graphify) vs 1M context — strengths, limitations, and hybrid strategy | 2026-04-26 |
| [[ai-engineering/mcp-architecture]] | MCP (Model Context Protocol) — AI-driven tool orchestration; tools not services; capability discovery; security model; failure modes; comparison with traditional REST APIs | 2026-04-22 |
| [[ai-engineering/genai-security-workflow]] | 6-stage GenAI security workflow model (Gartner): each stage's threat profile, countermeasures, and cross-cutting principles (Human in the Loop, Guardrails, TRiSM) | 2026-04-22 |
| [[ai-engineering/constitutional-ai]] | Constitutional AI and 3H principles (Helpful, Honest, Harmless) — the standard for governing GenAI output quality and safety | 2026-04-22 |
| [[ai-engineering/aip-platform]] | Palantir AIP: enterprise AI platform; Ontology as semantic data model; full spectrum AI from chat to automation; empirical AI architecture; AIP Bootcamp format | 2026-04-22 |
| [[ai-engineering/enterprise-ai-deployment]] | How enterprises adopt and operationalize AI: the bootcamp model, empirical architecture, chat-to-automation shift, expert feedback loops, governance gap | 2026-04-22 |
| [[ai-engineering/claude-code-skills]] | Claude Code Skills — directory-based context packages for AI coding agents; 9 categories; gotcha-driven knowledge capture; context engineering via folder structure | 2026-04-22 |
| [[ai-engineering/ai-agent-governance]] | AI agent governance: copilot→operator shift, delegation vs automation, architecture of decision, four-component production stack (guardrails, observability, FinOps, execution control) | 2026-04-24 || [[ai-engineering/ontology-driven-architecture]] | Ontology-driven architecture: schema vs. ontology distinction; why agentic systems require ontologies; ontologies as coordination layer and deterministic interface; "meaning precedes intelligence" | 2026-04-24 || [[ai-engineering/llm-model-economics]] | LLM model selection decision framework: cost-quality tradeoff, token economics for agent pipelines, open-weight vs. frontier closed models, OpenRouter as inference gateway; tiered model routing by task type | 2026-04-26 |

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
| [[bim-construction/bim-coordination]] | Coordenação BIM como problema cultural/processual; pares de maior risco de conflito entre disciplinas complementares; ferramentas Procore e Autodesk Construction Cloud | 2026-04-22 |
| [[bim-construction/planejamento-preditivo-obras]] | Planejamento preditivo de obras: IA como antevisão; frente de obra como unidade de análise; cronograma inteligente; mapa das cinco frentes de IA na gestão de obras; "dados como diferencial, não a ferramenta"; Frente 4 confirmada no Visus Planning 2024 | 2026-04-26 |
| [[bim-construction/tipos-contrato-engenharia]] | Tipos de contrato em engenharia: Turn-key/EPC, Preço Unitário, Administração, Aliança; alocação de risco por modelo; implicações para planejamento e stakeholders (AltoQi Visus Planning) | 2026-04-25 |

### Software Engineering

| Page | Summary | Updated |
|---|---|---|
| [[software-engineering/system-design-approach]] | Problem-solving framework (decompose → 4 dimensions); scaling fundamentals; load balancer algorithms; microservices vs monolith | 2026-04-22 |
| [[software-engineering/cap-theorem-and-consistency]] | CAP theorem (CP vs AP); strong vs eventual consistency; quorum protocols; consistent hashing ring algorithm | 2026-04-22 |
| [[software-engineering/database-scaling]] | Progressive scaling ladder: indexing → partitioning → master-slave → multi-master → sharding; SQL vs NoSQL decision framework | 2026-04-22 |
| [[software-engineering/distributed-systems]] | Coordinator/worker pattern; leader election algorithms; auto-recoverable systems; big data tools (Spark) | 2026-04-22 |
| [[software-engineering/messaging-and-events]] | Message queue vs stream; Kafka internals; real-time pub/sub; event-driven architecture (EDA) patterns | 2026-04-22 |
| [[software-engineering/caching-cdn-proxy]] | Caching strategies; Redis deep dive; blob storage (S3); CDN edge servers; forward vs reverse proxy | 2026-04-22 |

---

## Analyses

*Synthesized outputs: comparisons, gap analyses, synergy evaluations.*

| Page | Summary | Updated |
|---|---|---|
| [[session-memory-vs-wiki-synergy]] | Synergy analysis: how Mem0/session memory and the Karpathy LLM Wiki operate as complementary tiers; vectorless vs. semantic retrieval; knowledge promotion workflow; combined architecture | 2026-04-25 |

---

## Products

*One entry per product or tool documented.*

| Page | Summary | Updated |
|---|---|---|
| [[products/altoqi-visus-planning]] | AltoQi Visus Planning: plataforma BIM de planejamento 4D; workflow operacional completo (8 etapas); posicionamento nas 5 frentes de IA; dimensão contratual como variável de configuração | 2026-04-26 |

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
- Pages are organized into 5 domain categories: `ai-engineering`, `coaching-leadership`, `product-org-design`, `bim-construction`, `software-engineering`
- Internal links use the format `[[category/filename]]` (e.g., `[[coaching-leadership/coaching-modes]]`)
