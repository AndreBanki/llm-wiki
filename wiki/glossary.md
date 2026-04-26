---
title: Glossary
type: glossary
created: 2026-04-07
updated: 2026-04-26
sources: [pageindex-vectorless-rag.md, francieli-wagner-bim-coordination.md, mbs-performance-vs-development-coaching.md, mbs-two-questions-for-great-conversation.md, gyaco-conway-team-structure.md, mbs-paradoxes-of-being-a-coach.md, article.md, gartner-genai-security-workflow, vidvatta-mcp-vs-api-architecture.md, palantir-aip-bootcamps.md, eric-luque-claude-code-skills.md, Planejamento de obra 4.0_ algoritmos que otimizam cronogramas e antecipam gargalos _ LinkedIn.pdf, Qwen 3.6 Plus Just Hit 1 Trillion Daily Tokens — Here's Why Developers Are Ditching $5M Claude for a $0.28 Alternative.pdf, balajiBal-palantir-ontologies.md, tejas-sharma-karpathy-knowledge-system.md, linkedin-post-jhonatan-lazarin-ia-gestao-obras, daniel-rusnok-mem0-mcp-semantic-memory.md, Seamless Content Ingestion for Claude-Obsidian Second Brain.md, How to Use Graphify_ Turn Any Folder Into a Knowledge Graph.md]
tags: [terminology, style, glossary]
---

# Glossary

Living reference of terms, definitions, and style conventions. The LLM checks this before using any technical term. Updated on every ingest that introduces new or refined terminology.

---

## How to Read This Glossary

Each entry follows this format:

**Term** *(canonical form)*
: Definition. Usage notes. Related terms.
- Preferred: `term` / Avoid: `deprecated term`
- See also: [[related-page]]

---

## Terminology

**RAG** *(Retrieval-Augmented Generation)*
: A pattern where an LLM's response is grounded in content retrieved from external documents rather than relying solely on training data. The retrieval step is the key engineering challenge.
- See also: [[ai-engineering/rag-approaches]]

**Vector RAG** *(traditional RAG)*
: The dominant RAG implementation: documents are chunked, embedded into dense vectors, stored in a vector database, and retrieved via cosine similarity search at query time.
- Preferred: `vector RAG` / Avoid: `standard RAG`, `classic RAG` (ambiguous)
- See also: [[ai-engineering/rag-approaches]]

**Vectorless RAG**
: A RAG approach that eliminates embeddings and vector databases entirely. Instead uses LLM reasoning over a structured document index (e.g., hierarchical tree) to identify relevant content.
- Canonical term introduced by VectifyAI for the PageIndex approach.
- See also: [[ai-engineering/pageindex]], [[ai-engineering/rag-approaches]]

**PageIndex**
: Open source vectorless RAG framework by VectifyAI (introduced September 2025). Builds a hierarchical tree index from a document's natural structure and uses LLM reasoning to navigate to the answer.
- See also: [[ai-engineering/pageindex]]

**FinanceBench**
: A benchmark for evaluating RAG systems on financial document Q&A tasks. Used to compare retrieval accuracy. PageIndex scores 98.7%; traditional vector RAG scores ~50%.

**Chunking**
: The process of splitting a document into fixed-size segments (typically measured in tokens) before embedding. A necessary step in vector RAG, but one that destroys document structure and cross-references.
- See also: [[ai-engineering/rag-approaches]]

**Tree Index** *(PageIndex tree, hierarchical index)*
: In PageIndex, the structured JSON representation of a document's content. Each node contains: `node_id`, `title`, `pages`, `summary`, `key_topics`. Built once at index time; used for reasoning-based retrieval at query time.
- See also: [[ai-engineering/pageindex]]

**Reasoning-Based Retrieval**
: A retrieval strategy where an LLM reasons about *where in a document* an answer is likely located, navigating document structure rather than computing similarity scores. Contrasted with similarity-based retrieval.
- See also: [[ai-engineering/rag-approaches]], [[ai-engineering/pageindex]]

**FinanceBench** *(benchmark)*
: Financial document Q&A benchmark. PageIndex: 98.7% accuracy. Traditional vector RAG: ~50%.

**Cosine Similarity**
: The standard distance metric used in vector RAG to compare query embeddings against stored document chunk embeddings. Measures semantic similarity, not relevance to user intent.
- See also: [[ai-engineering/rag-approaches]]

**VectifyAI**
: The team that built and maintains PageIndex. Also operates the cloud service at pageindex.ai.
- See also: [[ai-engineering/pageindex]]

**SWE-bench Verified**
: The canonical benchmark for evaluating software engineering capability in LLMs. Tests models against real GitHub issues from production repositories — requires the model to actually understand and fix bugs, not just recognize patterns. As of early 2026, top scores: Claude Opus 4.6 at 80.8%, Qwen 3.6 Plus at 78.8%.
- See also: [[ai-engineering/llm-model-economics]]

**Open-Weight Model**
: An LLM whose model weights are publicly available (downloadable and self-hostable), as opposed to closed/proprietary models where weights are kept private by the vendor. Open-weight models can be run locally, fine-tuned, and accessed via inference providers like OpenRouter. Note: "open-weight" is more precise than "open-source" (which implies training code and data are also public).
- Contrasted with: closed model, proprietary model (e.g., Claude, GPT)
- See also: [[ai-engineering/llm-model-economics]]

**OpenRouter**
: An inference routing platform that aggregates multiple LLM providers (open-weight and proprietary) through a single OpenAI-compatible API endpoint. Enables developers to switch between models by changing only the `model` string. Key for cost-performance arbitrage: run Qwen 3.6 Plus at $0.28/M for high-volume tasks; route to Claude/GPT for hard tasks. No waitlist as of April 2026.
- See also: [[ai-engineering/llm-model-economics]], [[ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens]]

**Token Economics**
: The analysis of LLM token consumption and cost as a first-class architectural and business decision. Especially important for agentic pipelines: each agent loop re-sends accumulating context, so cost compounds. A 17x token cost differential between models translates to 17x operational cost difference at scale.
- See also: [[ai-engineering/llm-model-economics]], [[ai-engineering/ai-agent-governance]]

**Linear Attention**
: An attention mechanism that approximates standard (quadratic) transformer attention with $O(n)$ cost scaling instead of $O(n^2)$ — making it dramatically cheaper for long-context inference. Used in Qwen 3.6 Plus for bulk context processing, enabling its 1M-token context window at competitive inference speeds.
- Contrasted with: standard quadratic attention (cost scales with sequence length squared)
- See also: [[ai-engineering/llm-model-economics]]

**Mixture-of-Experts (MoE)**
: A neural network architecture where a large number of "expert" subnetworks exist, but only a sparse subset activates per forward pass (selected by a gating mechanism based on input). Enables scaling total model parameters without proportionally scaling compute. Used in Qwen 3.6 Plus (sparse MoE + linear attention hybrid).
- See also: [[ai-engineering/llm-model-economics]]

**Qwen 3.6 Plus**
: Alibaba's flagship agentic coding model released April 2, 2026. Open-weight; hybrid linear attention + sparse MoE architecture; 1M-token context window; $0.28/M input tokens; 78.8% SWE-bench Verified; 158 tok/s inference speed. First model to process 1 trillion tokens in a single day on OpenRouter. Designed as an agentic-first model: tool use as first-class primitive, dual orchestrator/subagent support, always-on chain-of-thought.
- See also: [[ai-engineering/llm-model-economics]], [[ai-engineering/chew-loong-nian-qwen36plus-trilhao-tokens]]

**AI Session Memory** *(persistent semantic memory, Mem0 memory)*
: The capability for an AI coding agent to retain and retrieve decisions, preferences, and architectural choices across sessions — solving the problem that every new session starts from scratch. Implemented via Mem0 + ChromaDB + MCP. Distinct from domain knowledge (LLM Wiki) and static context (CLAUDE.md); operates at the project-decision tier.
- Contrasted with: LLM Wiki (synthesized domain knowledge), CLAUDE.md (deterministic static context)
- See also: [[ai-engineering/ai-session-memory]]

**AI Amnesia**
: The condition where an AI coding assistant has no memory of past sessions. Each session restarts from zero; decisions made in prior sessions are permanently lost unless manually re-explained. The core problem that session memory tools like Mem0 address.
- See also: [[ai-engineering/ai-session-memory]]

**Mem0 (mem0ai)**
: A Python library for AI memory management. Takes text, extracts key facts using an LLM, stores them as vector embeddings in a vector database (e.g., ChromaDB), and enables semantic search retrieval. Used to add persistent session memory to Claude Code via an MCP server.
- See also: [[ai-engineering/ai-session-memory]]

**ChromaDB**
: A local, SQLite-backed vector database. Stores vector embeddings on disk with no infrastructure requirements (no Docker, no server process). Used as the storage backend for Mem0 in session memory setups. Data persists across reboots.
- See also: [[ai-engineering/ai-session-memory]], [[ai-engineering/rag-approaches]]

**Claude Code Hook**
: A script registered with Claude Code to fire automatically on specific lifecycle events: `SessionEnd`, `PreCompact`, `Stop`, `PostToolUse`. Hooks enable automated workflows (e.g., memory extraction) but carry production risks: PreCompact fires on every context compaction (not just session end), unbounded background processes cause runaway CPU, per-session locks fail under concurrent sessions.
- Key rule: register on `SessionEnd` only; use a global `pgrep`-based concurrency cap; add `gtimeout 300` wrapper
- See also: [[ai-engineering/ai-session-memory]], [[ai-engineering/ai-agent-governance]]

**Obsidian Web Clipper**
: A browser extension that converts any web page into a structured markdown note with auto-populated YAML frontmatter and deposits it into an Obsidian folder in 2 clicks. Supports 5 content-type templates (Article, PDF/Paper, Video, GitHub, Social) with URL-based auto-selection. The frontmatter includes `title`, `source` (URL), `author`, `published`, `created`, `description`, `tags`, `type`, and status checkboxes (`ingested`, `read`).
- See also: [[ai-engineering/llm-wiki-pattern]], [[ai-engineering/james-wilkins-obsidian-web-clipper-ingest]]

**Content Acquisition Pipeline** *(clip pipeline, ingest pipeline)*
: The upstream workflow that gets raw documents into `raw/` before the wiki ingest process begins. Two patterns: (1) *Manual curation* — human deposits files deliberately, high quality per source, higher friction; (2) *Automated capture* — browser extension + overnight script processes everything, near-zero friction, lower curation per source. The `ingested` checkbox / tracking file pattern bridges capture and wiki ingest in both variants.
- See also: [[ai-engineering/llm-wiki-pattern]], [[ai-engineering/james-wilkins-obsidian-web-clipper-ingest]]

**Tiered Model Routing**
: An architecture pattern that assigns different LLM tiers to tasks of different complexity within the same pipeline. Routine tasks (tagging, summarization, classification) route to cheap/local models (Gemini Flash, Ollama); complex reasoning and synthesis route to frontier models (Claude). Principle: *don't use a nuclear reactor to toast bread* — save frontier quota for tasks where the capability gap is material. Extends the cost-quality tradeoff framework from "which model for my app" to "which model for each task in my pipeline."
- See also: [[ai-engineering/llm-model-economics]], [[ai-engineering/james-wilkins-obsidian-web-clipper-ingest]]

**Ollama**
: A free, open-source tool for running AI language models locally on your own machine without sending data to any external API. Suitable for batch processing tasks (tagging, summarization) where privacy, cost, or quota conservation matters. RAM-intensive — best scheduled for overnight runs to avoid degrading the development environment during work hours.
- See also: [[ai-engineering/llm-model-economics]]

**Graphify**
: An open-source Python tool (`pip install graphifyy`) that converts any local folder — code, PDFs, images, audio, video — into a persistent, queryable knowledge graph. Uses a three-pass pipeline: deterministic AST parsing (Pass 1), local audio/video transcription (Pass 2), and parallel LLM extraction (Pass 3). Serves compressed subgraphs to AI assistants instead of raw files. Claimed 71.5x token reduction. Graphify is a *skill*, not an orchestrator; the user's coding assistant (Claude Code, Cursor, etc.) is the runtime that dispatches subagents.
- See also: [[ai-engineering/rag-approaches]], [[ai-engineering/how-to-use-graphify-knowledge-graph]]

**Provenance Tagging** *(graph edge provenance)*
: A labeling convention for edges in a knowledge graph that makes explicit whether a relationship was deterministically extracted or probabilistically inferred. Graphify uses three labels: `EXTRACTED` (from AST/structured source, confidence 1.0), `INFERRED` (from LLM reasoning over unstructured content, confidence < 1.0), `AMBIGUOUS` (low-confidence, flagged for human review). Core principle: epistemic honesty — you always know what the system *found* vs. what it *guessed*.
- See also: [[ai-engineering/how-to-use-graphify-knowledge-graph]]

**Knowledge Graph RAG** *(graph-based RAG)*
: A RAG paradigm where retrieval is performed by extracting a topology-clustered **subgraph** from a persistent knowledge graph, rather than retrieving vector-similarity chunks or reasoning over a document tree. Enables multi-hop relational queries and preserves cross-file dependency structure. Contrasted with Vector RAG (similarity-based), Vectorless RAG (tree traversal), and 1M Context (no retrieval). See Graphify.
- See also: [[ai-engineering/rag-approaches]]

**AST Parsing** *(Abstract Syntax Tree parsing)*
: Deterministic structural analysis of source code that extracts classes, functions, imports, call graphs, and docstrings by parsing the code's syntax tree — not by reading it as text. Used in Graphify's Pass 1. Because AST parsing is rule-based, all edges it produces carry confidence 1.0 (`EXTRACTED`). `tree-sitter` is the library used by Graphify for cross-language AST parsing (20 languages).
- Contrasted with: LLM-based code understanding (probabilistic, confidence < 1.0)
- See also: [[ai-engineering/how-to-use-graphify-knowledge-graph]]

**PreToolUse Hook** *(Graphify hook)*
: A lifecycle hook that fires before an AI assistant uses any file-reading or search tool. Graphify installs a PreToolUse hook so the assistant reads the knowledge graph map *first*, identifies relevant nodes, and retrieves a focused subgraph — rather than grepping through raw files.
- See also: [[ai-engineering/how-to-use-graphify-knowledge-graph]], [[ai-engineering/claude-code-skills]]

---

## Coaching / Leadership

**Performance Coaching**
: A mode of coaching focused on the task at hand — getting things done, fixing problems, moving faster. The natural default under pressure. Risk: the coach takes ownership of the thinking, leaving the other person feeling unaccomplished.
- Contrasted with: development coaching
- See also: [[coaching-leadership/coaching-modes]]

**Development Coaching**
: A mode of coaching focused on the person doing the task — who they are becoming, what they are learning, what capability they are building. Requires staying curious long enough for the other person to grow.
- Not passive or slow by default; it's intentional curiosity
- Contrasted with: performance coaching
- See also: [[coaching-leadership/coaching-modes]]

**Resisting the Urge to Rescue**
: A key discipline in development coaching. After asking a question, not filling the silence with your own answer. Trusting the other person to do their own thinking even when it feels slow or uncomfortable.
- See also: [[coaching-leadership/coaching-modes]]

**Holding Space**
: Remaining present and attentive without rushing to fill silence or offer solutions. Allows the other person room to think, process, and arrive at their own conclusions.
- See also: [[coaching-leadership/coaching-modes]]

**Being of Coaching** *(being vs. doing)*
: The embodied way a coach shows up — the quality of presence, relationship, process management, and outcome relationship — as distinct from the techniques and questions used (the "doing"). MBS's argument: AI can replicate coaching questions; it cannot replicate the being.
- See also: [[coaching-leadership/coaching-paradoxes]]

**Humble Confidence**
: The first coaching paradox (MBS). Confidence to step forward and contribute, paired with genuine humility about where you're still learning — held with lightness, not defensiveness. Synthesizes to: grounded but not timid; confident but not arrogant.
- See also: [[coaching-leadership/coaching-paradoxes]]

**Fierce Love**
: The second coaching paradox (MBS). Genuine care for the other person's growth (love) combined with the willingness to ask uncomfortable questions, name avoided patterns, and invite them beyond what currently feels doable (fierce). Support and challenge held together.
- See also: [[coaching-leadership/coaching-paradoxes]]

**Light and Grounded**
: The third coaching paradox (MBS). Shaping the conversation process (grounded) without controlling the thinking (light). Enough structure to keep the conversation purposeful; enough freedom for insight to emerge. Avoids "disguised advice" on one end and "unproductive wandering" on the other.
- See also: [[coaching-leadership/coaching-paradoxes]], [[coaching-leadership/conversation-design]]

**Care and Don't Care**
: The fourth coaching paradox (MBS). Caring about the coachee's progress while holding that outcome lightly enough that curiosity doesn't shrink and ownership remains with the coachee. The coach creates conditions for better thinking; what the coachee does with it is theirs.
- See also: [[coaching-leadership/coaching-paradoxes]]

---

## BIM / Coordenação de Projetos

**BIM** *(Building Information Modeling / Modelagem da Informação da Construção)*
: Metodologia de trabalho baseada em modelos digitais tridimensionais e inteligentes que integram geometria, dados e informações do ciclo de vida da construção.
- Canonical form for this wiki: `BIM` (sigla em inglês, universalmente adotada no Brasil)
- See also: [[bim-construction/bim-coordination]]

**Coordenação BIM**
: Processo de integração e compatibilização das disciplinas de projeto (estrutural, hidráulica, elétrica, HVAC, incêndio, etc.) dentro de um ambiente BIM, com o objetivo de identificar e resolver conflitos antes da execução em obra.
- See also: [[bim-construction/bim-coordination]]

**Modelo Federado**
: Agregação dos modelos individuais de cada disciplina em um único ambiente de visualização e análise. Condição necessária, mas não suficiente, para coordenação BIM real.
- See also: [[bim-construction/bim-coordination]]

**Compatibilização**
: Processo de identificação e resolução de conflitos físicos, funcionais ou de sequência entre disciplinas de projeto. Pode ser feita via clash detection automatizado ou revisão manual.
- See also: [[bim-construction/bim-coordination]]

**Disciplinas Complementares**
: Conjunto de projetos de engenharia que complementam o projeto arquitetônico: estrutural, hidráulica, elétrica, HVAC (climatização), PPCI (prevenção e combate a incêndio), entre outros.
- Preferred: `disciplinas complementares` / Avoid: `disciplinas` (ambíguo)

**Clash Detection**
: Verificação automatizada de interferências físicas (colisões geométricas) entre elementos de disciplinas distintas dentro do modelo federado.

**PPCI** *(Projeto de Prevenção e Combate a Incêndio)*
: Disciplina complementar responsável pelo sistema de proteção contra incêndio: sprinklers, hidrantes, rotas de fuga, etc.

**HVAC** *(Heating, Ventilation, and Air Conditioning)*
: Disciplina complementar de climatização e ventilação. No contexto brasileiro, inclui ar-condicionado e ventilação mecânica.

**Planejamento Preditivo de Obras**
: Uso de algoritmos e IA para transformar o planejamento de construção de um processo reativo em um processo de antevisão — alimentando sistemas com dados reais de execução para identificar padrões de risco antes que se materializem em atrasos.
- See also: [[bim-construction/planejamento-preditivo-obras]]

**Frente de Obra**
: Unidade básica de análise no planejamento de construção. Cada frente corresponde a um conjunto de atividades realizadas em paralelo ou sequência, com sua própria produtividade, dependências de material e vulnerabilidades de atraso.
- See also: [[bim-construction/planejamento-preditivo-obras]]

**Cronograma Inteligente**
: Sistema de planejamento de obras que aprende com dados de cada obra executada e sugere sequências ótimas de frentes com base em disponibilidade de equipe, lead times de material e dependências de projeto. Visão de futuro proposta por Alessandro Lopes (Athié Wohnrath).
- See also: [[bim-construction/planejamento-preditivo-obras]]

**Antevisão** *(foresight, no contexto de obras)*
: Capacidade de identificar e endereçar riscos de execução antes que se materializem como surpresas no cronograma. Contrastada com o modo reativo (reagir ao problema quando aparece). Principal promessa da IA preditiva no planejamento de obras.
- See also: [[bim-construction/planejamento-preditivo-obras]]

**Lead Time** *(no contexto de construção civil)*
: Prazo entre o pedido de um material/serviço e sua efetiva disponibilidade em obra. Um dos principais dados de entrada para sistemas preditivos de cronograma.
- Note: o mesmo termo aparece em supply chain / product management com sentido similar, mas o contexto de obras tem particularidades (fornecedores especializados, itens sob medida, logística de canteiro).

**EPC** *(Engineering, Procurement and Construction)*
: Modalidade contratual em que uma única contratada é responsável pelo projeto executivo (Engineering), suprimento de materiais e equipamentos (Procurement) e execução da obra (Construction). Equivalente funcional do Turn-key. Todo o risco de custo e prazo fica com a contratada.
- See also: [[bim-construction/tipos-contrato-engenharia]]

**Turn-key / Empreitada Integral**
: Modalidade contratual em que a contratada entrega a obra "pronta para funcionar" — responsabilidade total sobre escopo, prazo e custo. Terminologia brasileira equivalente: empreitada integral. Alta vulnerabilidade a mudanças de escopo; risco muito alto para a contratada.
- Canonical form for this wiki: `Turn-key / EPC` when referring to the model in general; `Empreitada Integral` when specifically referencing a contrato no Brasil
- See also: [[bim-construction/tipos-contrato-engenharia]]

**Alocação de Risco** *(risk allocation)*
: Distribuição contratual de quem absorve o impacto financeiro de eventos imprevistos em um projeto. O tipo de contrato é o principal mecanismo de alocação de risco. Determina os incentivos de cada parte e o que cada stakeholder precisa monitorar no planejamento.
- See also: [[bim-construction/tipos-contrato-engenharia]]

**Claim** *(reivindicação contratual)*
: Solicitação formal de compensação (financeira ou de prazo) por uma parte do contrato em função de eventos não previstos ou de responsabilidade da outra parte. Frequência e tipologia de claims variam com o tipo de contrato.
- Preferred: `claim` (anglicismo universalmente adotado na indústria brasileira de infraestrutura)
- See also: [[bim-construction/tipos-contrato-engenharia]]

**Claim Management**
: Disciplina especializada em identificar, quantificar, documentar e negociar reivindicações contratuais (claims) em projetos de engenharia e construção. Mais relevante em contratos Turn-key/EPC devido ao alto risco da contratada.
- See also: [[bim-construction/tipos-contrato-engenharia]]

**FIDIC** *(Fédération Internationale des Ingénieurs-Conseils)*
: Organização internacional que publica os contratos-padrão mais adotados em projetos de engenharia civil internacionais. Principais livros: Yellow Book (EPC/Plant), Red Book (Preço Unitário/Construction), Silver Book (Turn-key mais rígido/EPC Turnkey).

**AltoQi Visus Planning**
: Produto de planejamento de obras em concepção pela AltoQi. Encaixa-se na **Frente 1 (Planejamento e previsão)** do mapa de IA na gestão de obras — estimativa de prazos, custos e riscos com base em dados históricos. Contexto estratégico: o tipo contratual determina quais métricas são destacadas e para quais stakeholders; o framing "dados como diferencial, não a ferramenta" (Lazarin) posiciona o produto como amplificador da capacidade de antevisão do gestor.
- See also: [[bim-construction/tipos-contrato-engenharia]], [[bim-construction/planejamento-preditivo-obras]], [[bim-construction/jhonatan-lazarin-ia-gestao-obras]]

**Cinco Frentes de IA na Gestão de Obras**
: Framework de posicionamento para soluções de IA em construção: (1) Planejamento e previsão, (2) Controle financeiro em tempo real, (3) Gestão de equipes e produtividade, (4) Execução e monitoramento, (5) Análise e melhoria contínua. Útil para mapear onde um produto ou funcionalidade se encaixa no contexto mais amplo da transformação digital de obras.
- See also: [[bim-construction/jhonatan-lazarin-ia-gestao-obras]], [[bim-construction/planejamento-preditivo-obras]]

**Dados como Diferencial** *(data as differentiator)*
: Framing proposto por Jhonatan Lazarin: o que impacta o resultado de uma obra não é a ferramenta de IA em si, mas como os dados são usados ao longo do processo. A IA só amplifica análise e controle quando aplicada sobre processos bem definidos e dados consistentes. Paralelo no wiki: "meaning precedes intelligence" (Palantir Ontology) — inteligência sem substrato semântico produz ruído, não insight.
- See also: [[bim-construction/jhonatan-lazarin-ia-gestao-obras]], [[ai-engineering/ontology-driven-architecture]]

---

## Product Management / Organizational Design

**Lei de Conway** *(Conway's Law)*
: "Organizations that design systems tend to produce systems that mirror the communication structures of those organizations." (Melvin Conway, 1968.) Team structure shapes product structure — when structure is wrong, it works silently against strategy.
- See also: [[product-org-design/conways-law]]

**Manobra Reversa de Conway** *(Reverse Conway Maneuver)*
: The practice of defining the desired system architecture first, then organizing teams to reflect that architecture. Valid and powerful, but incomplete: ignores users and business strategy, which must be defined before any architectural decision.
- See also: [[product-org-design/conways-law]]

**Times Orientados a Produto** *(Product/System-Centric Teams)*
: Teams organized around a specific system or technology artifact. Risk: can only see solutions within their system's scope, leading to feature accumulation and blind spots for cross-channel solutions.
- Contrasted with: times orientados a usuário
- See also: [[product-org-design/team-topology]]

**Times Orientados a Usuário** *(User-Centric Teams)*
: Teams organized around a user segment or marketplace actor. Benefit: the solution space is open — any channel or approach that solves the user's problem qualifies.
- Contrasted with: times orientados a produto
- See also: [[product-org-design/team-topology]]

**Topologia de Times** *(Team Topology)*
: The deliberate arrangement of teams around a specific organizing principle (system, user, capability). The choice of organizing principle is itself a product and strategy decision.
- See also: [[product-org-design/team-topology]]

**Marketplace de Três Pontas** *(Three-Sided Marketplace)*
: A marketplace with three distinct actor types, each with different goals and requiring dedicated value creation. Example (Lopes): end clients (buyers/renters) + developers/owners (sellers) + brokers/franchisees (intermediaries).
- See also: [[product-org-design/gyaco-conway-team-structure]], [[product-org-design/team-topology]]

---

## Coaching / Leadership

**Conversation Design**
: The practice of pre-selecting questions and structuring the opening of a group conversation to invite depth and bypass surface-level exchange. The designer acts as a host, then steps back. Distinct from facilitation (which manages process) and coaching (which is one-on-one).
- See also: [[coaching-leadership/conversation-design]]

**Good Host**
: A role described by MBS as deliberately curating people and questions to create conditions for meaningful connection and collaboration — not just organizing logistics. A good host wants "great people to know other great people."
- See also: [[coaching-leadership/conversation-design]]

**The Conspiracy**
: MBS's accountability membership community. Members commit to a Worthy Goal and receive support, focus, and accountability from a "brilliant community of humans."
- See also: [[coaching-leadership/mbs-two-questions-for-great-conversation]]

**Worthy Goal**
: The declared aspiration a Conspiracy member commits to. The practical answer to the conversation design question "What are you up to?" — what adventure is beckoning, the edge you're stepping toward.
- See also: [[coaching-leadership/conversation-design]], [[coaching-leadership/mbs-two-questions-for-great-conversation]]

**"What are you known for?"**
: First question of MBS's two-question dinner format. Invites participants to name their values, elemental parts, and best self as seen by people who care about them — not their public reputation.
- See also: [[coaching-leadership/conversation-design]]

**"What are you up to?"**
: Second question of MBS's two-question dinner format. Conspiratorial in tone; asks about the adventure beckoning, the edge being stepped toward, and who the person is becoming. Bypasses status updates.
- See also: [[coaching-leadership/conversation-design]]

---

## AI Knowledge Management

**LLM Wiki** *(LLM Wiki pattern)*
: A pattern for AI-maintained personal knowledge bases, introduced by Andrej Karpathy in early 2026. The AI reads source documents once and builds a structured, interlinked wiki — then updates it incrementally as new sources are added. Key insight: AI handles bookkeeping (the work that kills human-maintained wikis) while humans focus on sourcing and questioning.
- See also: [[ai-engineering/llm-wiki-pattern]]

**PKM** *(Personal Knowledge Management)*
: The broad category of tools and practices for individuals to capture, organize, and retrieve knowledge. Examples: Obsidian, Roam Research, Notion, Logseq. The LLM Wiki pattern is distinguished from traditional PKM by delegating the connecting/linking work to AI rather than the human.
- See also: [[ai-engineering/llm-wiki-pattern]]

**Synthesis Problem**
: The challenge faced by experienced professionals who have accumulated large amounts of domain knowledge but lack a mechanism to reason across all of it at once. Distinct from an *information problem* (not enough data) or a *retrieval problem* (can't find the data). The LLM Wiki pattern's primary value proposition at professional scale. Three canonical archetypes: lawyer with 10 years of case notes, consultant who advised 30 companies, researcher who read 500 papers.
- See also: [[ai-engineering/llm-wiki-pattern]], [[ai-engineering/tejas-sharma-karpathy-knowledge-system]]

**Quarriable Knowledge**
: A property of a knowledge base that is large and well-connected enough to be *queried like a mine* — complex questions can be answered on demand, drawn entirely from accumulated sources, without hallucination from the open web. Term introduced by Tejas Sharma to describe the end state of a mature LLM Wiki.
- See also: [[ai-engineering/llm-wiki-pattern]], [[ai-engineering/tejas-sharma-karpathy-knowledge-system]]

**Constella**
: A no-code personal knowledge tool (constella.app) built by Tejas Sharma implementing the same pattern as Karpathy's LLM Wiki: sources go in, AI builds the connections, you ask questions against everything you've accumulated. Designed to remove the setup complexity Karpathy called "a hacky collection of scripts."
- See also: [[ai-engineering/tejas-sharma-karpathy-knowledge-system]]

**Schema File** *(CLAUDE.md, copilot-instructions.md)*
: The operating manual for the AI agent in an LLM Wiki. Defines entity types, page YAML format, ingest/query/lint workflows, and session-start checklist. Editing it changes how the AI behaves for a specific domain.
- Canonical reference in this repo: `.github/copilot-instructions.md`
- See also: [[ai-engineering/llm-wiki-pattern]]

**Knowledge Compounding**
: The accumulation effect in an LLM Wiki where each new source makes the wiki richer, more cross-referenced, and more useful — as opposed to chat-based AI which forgets everything between sessions.
- See also: [[ai-engineering/llm-wiki-pattern]]

**Ingest** *(wiki operation)*
: The workflow of processing a new source document into the wiki: creating a source summary page, updating affected entity pages, updating glossary and index, and logging the activity. One ingest typically touches 10–15 wiki pages.
- Contrasted with: query, lint
- See also: [[ai-engineering/llm-wiki-pattern]]

**Lint** *(wiki operation)*
: The health-check workflow for an LLM Wiki: scanning for contradictions between pages, stale claims, orphan pages (no inbound links), concepts missing their own page, and inconsistent terminology.
- Contrasted with: ingest, query
- See also: [[ai-engineering/llm-wiki-pattern]]

**Cursor AI**
: An AI-powered code editor that reads project files (including schema/instruction files) and operates as an AI agent within the project. Primary recommended tool for running LLM Wiki workflows.
- See also: [[ai-engineering/llm-wiki-pattern]]

**Obsidian**
: A free markdown-based note-taking app with a visual graph view of page connections. Recommended browsing layer for LLM Wiki — shows wiki pages and their links as an interactive graph. Pre-configurable via `.obsidian/` vault settings.
- See also: [[ai-engineering/llm-wiki-pattern]]

**Andrej Karpathy**
: AI researcher; founding member at OpenAI, former head of AI/Autopilot at Tesla. Originator of the LLM Wiki pattern (`llm-wiki.md`, early 2026). Known for making deep technical AI concepts accessible. Self-described his LLM Wiki implementation as "a hacky collection of scripts."
- See also: [[ai-engineering/llm-wiki-pattern]], [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]], [[ai-engineering/tejas-sharma-karpathy-knowledge-system]]

---

## AI Security / GenAI Governance

**3H Principles** *(Helpful, Honest, Harmless)*
: The three required properties of trustworthy GenAI output, popularized by Anthropic. **Helpful** = serves the user's legitimate needs; **Honest** = does not mislead or fabricate; **Harmless** = does not harm the user or third parties. Primary output quality standard at the generation stage of the GenAI workflow.
- See also: [[ai-engineering/constitutional-ai]], [[ai-engineering/genai-security-workflow]]

**Constitutional AI**
: A formalized set of high-level directives or principles that govern the output and behavior of an AI system. Implemented by the CISO/developer or encoded so the AI governs itself. Ensures outputs consistently align with 3H principles. Organizations may have multiple constitutions for different use cases.
- See also: [[ai-engineering/constitutional-ai]], [[ai-engineering/genai-security-workflow]]

**TRiSM** *(Trust, Risk, and Security Management)*
: Gartner's meta-framework for AI governance. Addresses trust (helpful, honest), risk (harmless), and security (hardened deployment). Combined with 3H principles via a Constitutional AI workflow.
- See also: [[ai-engineering/genai-security-workflow]]

**Data Security Debt**
: Technical and governance debt related to data security that accumulates when unstructured data receives lower priority. GenAI adoption exposes this debt sharply: missing data classification, sensitivity labeling, and access controls block secure AI deployment. Must be addressed before or early in the GenAI workflow.
- See also: [[ai-engineering/genai-security-workflow]]

**Human in the Loop**
: The design principle of maintaining human oversight at every stage of the GenAI workflow. Humans validate outputs, interpret regulatory requirements, and provide nuanced judgment that automated systems cannot replicate. A required architectural element, not optional.
- Preferred: `human in the loop` / Note: distinct from human-in-the-loop in control systems (different domain)
- See also: [[ai-engineering/genai-security-workflow]]

**Data Poisoning**
: An attack where a malicious actor intentionally introduces corrupted or misleading data into a training dataset, manipulating the model's behavior — typically causing it to perform incorrectly or act in biased ways.
- See also: [[ai-engineering/genai-security-workflow]]

**Model Evasion**
: An attack where adversarial inputs that look normal to humans cause an AI model to make mistakes — misclassifying dangerous content as safe, or allowing malicious behavior to go undetected.
- See also: [[ai-engineering/genai-security-workflow]]

**Model Tampering**
: An attack where an adversary gains access to a trained model and modifies its weights, introducing unintended biases or unauthorized behavioral changes.
- See also: [[ai-engineering/genai-security-workflow]]

**Model Leakage / Model Inversion**
: A threat where the trained model inadvertently leaks parts of its proprietary training data to unauthorized users through query responses. Model inversion is the technique of reconstructing training data by querying the model.
- See also: [[ai-engineering/genai-security-workflow]]

**DSPM** *(Data Security Posture Management)*
: Tools designed to provide visibility into data security posture — particularly for unstructured data. Used at the data acquisition stage of the GenAI workflow for data discovery, classification, and flow mapping.
- See also: [[ai-engineering/genai-security-workflow]]

**Guardrails** *(AI)*
: Security controls that span multiple stages of the GenAI workflow (generation, deployment, feedback). Implement content moderation, data leakage prevention, and output safety constraints as a unified enforcement layer.
- Tools: NVIDIA NeMo Guardrails, OpenAI Moderation API
- See also: [[ai-engineering/genai-security-workflow]], [[ai-engineering/constitutional-ai]]

**Feedback Poisoning**
: An attack where malicious actors submit fake feedback or reports to corrupt model retraining or overwhelm feedback triage systems. Particularly dangerous because it degrades model quality over time.
- See also: [[ai-engineering/genai-security-workflow]]

---

## AI Agent Governance

**AI Operator** *(operator model)*
: A mode in which an AI model does not just suggest actions but interprets context, makes decisions, and executes them autonomously — with the human arriving after the fact to review results. Contrasted with the copilot model. Enabled by effective long-context reasoning (e.g., Claude Opus 4.7).
- Contrasted with: copilot (AI suggests, human validates, system executes)
- See also: [[ai-engineering/ai-agent-governance]], [[ai-engineering/eric-luque-claude-opus-47-operator-risk]]

**Architecture of Decision**
: The structural design of where, under what conditions, and with what safeguards an AI agent is permitted to make autonomous decisions within an organization. The primary governance responsibility for CTOs and Principal Engineers as AI transitions from copilot to operator.
- Key questions: where can AI decide? where can it not? how do we audit, limit, and shut it down?
- See also: [[ai-engineering/ai-agent-governance]]

**Delegation (AI)**
: The transfer of decision authority to an AI agent — as distinct from automation (where a rule determines execution). Delegation is unpredictable without governance scaffolding; automating a decision is not the same as delegating it.
- Contrasted with: automation (rule → system executes, predictable)
- See also: [[ai-engineering/ai-agent-governance]]

**Agent Observability**
: The ability to inspect what decision an AI agent made, why it made that decision (reasoning trace), and how much it cost (token consumption per task). A required component of any production agentic system; without it, debugging, auditing, and improvement are impossible.
- See also: [[ai-engineering/ai-agent-governance]], [[ai-engineering/mcp-architecture]]

**AI FinOps**
: The discipline of managing and controlling the financial cost of running AI models in production. Includes budget limits per task, per team, and per operation class. Critical when newer model generations consume more tokens per request by default — without FinOps, costs rise silently.
- See also: [[ai-engineering/ai-agent-governance]]

**Silent Cost Creep**
: A failure mode in AI production deployments where model upgrades or tokenizer changes increase token consumption per request without any visible product change — resulting in unexpected cost increases with no obvious trigger.
- See also: [[ai-engineering/ai-agent-governance]]

**Execution Control**
: A governance mechanism that separates the AI's suggestion scope (unlimited) from its execution scope (explicitly constrained). The principle: AI can suggest everything; it executes only within approved boundaries. Requires defined action limits, decision scope, rollback automation, and human checkpoints for irreversible actions.
- See also: [[ai-engineering/ai-agent-governance]]

---

## MCP / Agent Architecture

**MCP** *(Model Context Protocol)*
: A protocol layer that enables AI agents to discover and invoke tools based on context and reasoning. The AI model decides which tool to use; the server exposes capabilities rather than endpoints. Contrasted with traditional REST APIs where a human or deterministic code explicitly calls a known endpoint.
- See also: [[ai-engineering/mcp-architecture]]

**MCP Server**
: In MCP architecture, a server that exposes *tools* (AI-facing capabilities) rather than *services* (business logic contracts). No strict endpoint schema; the AI navigates its capabilities through reasoning and capability discovery.
- Contrasted with: traditional service / REST API service
- See also: [[ai-engineering/mcp-architecture]]

**Capability Discovery**
: A protocol-level mechanism in MCP where an AI client dynamically learns what tools are available from an MCP server at runtime — rather than having endpoints hardcoded. Enables flexible, model-driven orchestration.
- See also: [[ai-engineering/mcp-architecture]]

**Tool Overload**
: An MCP-specific failure mode where too many tools are exposed to the agent, causing the model to choose incorrectly, hallucinate a tool call, or fail to converge on the right action. Fix: expose fewer, well-scoped tools with explicit permission scopes.
- See also: [[ai-engineering/mcp-architecture]]

**Context Drift**
: An MCP-specific failure mode where an AI agent loses coherence about what the current task requires across a multi-step tool chain. The model's context window no longer reflects the task state correctly.
- See also: [[ai-engineering/mcp-architecture]]

**Tool-Level Permissions**
: The MCP security model where each exposed tool has its own permission scope, limiting what it can access or modify. Contrasted with the network-perimeter and service-level access model of traditional API security.
- See also: [[ai-engineering/mcp-architecture]]

**Context Isolation**
: In MCP security, the principle that each agent's execution context is isolated — preventing one tool invocation from leaking context to another, and bounding the blast radius of a compromised tool.
- See also: [[ai-engineering/mcp-architecture]]

---

## Enterprise AI Deployment / AIP

**AIP** *(Palantir Artificial Intelligence Platform)*
: Palantir's enterprise AI platform that integrates foundation models with live operational data through the Ontology. Enables organizations to move from chat-based AI to event-driven AI automation across any business function.
- See also: [[ai-engineering/aip-platform]]

**Ontology** *(operational ontology, Palantir Ontology)*
: A formal, explicit model of reality that defines the entities, relationships, constraints, and valid state transitions in a domain. In Palantir's implementation: a live semantic data model that grounds AI actions in real-world operational state. The critical distinction — *schemas describe data; ontologies describe reality*. A schema tells you a table has a `status` column; an ontology tells you what states are possible, how you move between them, and what actions are enabled or prohibited at each state.
- The ontology is not a layer on top of the system — it *is* the system
- Enables reliable agentic action: agents can only perform operations that correspond to legitimate state transitions on real entities
- See also: [[ai-engineering/ontology-driven-architecture]], [[ai-engineering/aip-platform]]

**Schema vs. Ontology**
: The foundational architectural distinction between describing data structure (schema) and describing operational reality (ontology). Schemas define what a database looks like; ontologies define what the domain means. Big data systems worked without ontologies because intelligence was external (analysts interpreted the data). Agentic systems require ontologies because the system itself must act reliably.
- See also: [[ai-engineering/ontology-driven-architecture]]

**Meaning Precedes Intelligence**
: Core design principle articulated by balaji bal as Palantir's foundational belief: before a system can act intelligently, it must have an explicit, shared model of what the entities in its domain are, how they relate, and what can happen to them. Intelligence built on top of implicit meaning (schemas, governance policies, analyst interpretation) fails when the system is expected to act autonomously.
- See also: [[ai-engineering/ontology-driven-architecture]], [[ai-engineering/balajiBal-palantir-ontologies]]

**World-Modeling**
: The practice of building software systems whose primary purpose is to represent and reason over a domain's entities, relationships, and dynamics — as opposed to systems optimized for data processing, analytics, or reporting. Palantir was a world-modeling company from the beginning. The ontology is the technical implementation of the world model.
- See also: [[ai-engineering/ontology-driven-architecture]]

**Deterministic Interface**
: An interface whose behavior is fully specified by explicit, computable rules rather than probabilistic model outputs. Ontologies serve as deterministic interfaces for agentic systems: an agent cannot take an action unless it corresponds to a valid state transition defined in the ontology. Contrasted with probabilistic guardrails (which constrain through model behavior, not hard rules).
- Related term: MCP tools also act as deterministic interfaces at the tool-call level
- See also: [[ai-engineering/ontology-driven-architecture]], [[ai-engineering/mcp-architecture]]

**Governance without Ontology**
: A system in which data access, ownership, and compliance are enforced through policy, but the system itself has no model of the domain's real-world entities and valid operations. Per balaji bal: "Governance without ontology is bureaucracy without physics." Policy can regulate access; only an ontology can enforce what actions are *meaningful and valid*.
- See also: [[ai-engineering/ontology-driven-architecture]], [[ai-engineering/genai-security-workflow]]

**Full Spectrum AI**
: Palantir's term for the maturity spectrum of enterprise AI deployment, from chat-style interaction at one end to fully automated, event-driven intelligent primitives embedded in business applications at the other. Most enterprises start at the chat end and must be guided toward automation.
- See also: [[ai-engineering/aip-platform]], [[ai-engineering/enterprise-ai-deployment]]

**AIP Bootcamp**
: Palantir's 1–5 day immersive hands-on engagement format for enterprise AI deployment. Participants build real production use cases (not demos) while simultaneously developing team capability. Core principle: "learn to fish, eat a fish" — deliver value today and build skills for tomorrow.
- See also: [[ai-engineering/enterprise-ai-deployment]], [[ai-engineering/aip-platform]]

**Empirical AI Architecture**
: The principle that AI architecture decisions (number of LLMs, fine-tuning vs. prompting, commercial vs. open source, learning loop design) must be discovered through real production use cases rather than decided upfront based on theoretical preferences. Contrasted with "theological" AI architecture (upfront doctrine).
- Related: parallels "structure follows strategy" in product org design — both reject premature architectural commitment
- See also: [[ai-engineering/enterprise-ai-deployment]], [[ai-engineering/aip-platform]]

**Expert Feedback Loop**
: A mechanism where domain experts validate, correct, or augment AI outputs in the flow of their normal work — and those corrections are captured to improve the model over time. Key source of proprietary competitive advantage in enterprise AI.
- See also: [[ai-engineering/enterprise-ai-deployment]]

---

## Claude Code / Agentic Coding

**Claude Code**
: Anthropic's agentic coding tool — an AI agent that reads project files, executes commands, and operates autonomously within a software project. Runs as an MCP client; extensible via Skills. Distinct from Claude (the general-purpose LLM): Claude Code is the agent environment, Claude is the model powering it.
- See also: [[ai-engineering/claude-code-skills]], [[ai-engineering/mcp-architecture]]

**Skill (Claude Code)**
: A directory-based context package for Claude Code that gives the agent specialized knowledge, tools, and operational patterns for a specific task domain. Not a single Markdown file — a folder containing the entry-point `skill.md`, `config.json`, reference docs, scripts, templates, and examples. Located at `.claude/skills/<name>/`.
- Preferred: *skill* (lower case when used generically) / *Skill* (proper noun in Claude Code context)
- See also: [[ai-engineering/claude-code-skills]]

**Gotcha (skills)**
: A production-discovered pitfall that an AI model repeatedly falls into without explicit correction. The most valuable content of a skill's documentation. Examples: deprecated method signatures, schema mismatches between database and API, test isolation requirements. Skills should grow their gotchas section organically as errors are observed.
- Not to be confused with: general programming gotchas (the meaning is similar but context-specific here)
- See also: [[ai-engineering/claude-code-skills]]

**Context Engineering**
: The practice of deliberately structuring information sources — their content, format, and organization — to maximize the quality of an AI model's reasoning. In Claude Code Skills, this includes folder structure as progressive disclosure (detailed docs in subfolders, loaded on demand). Broader than prompt engineering: involves data architecture, not just text composition.
- Related: progressive disclosure, skill folder structure
- See also: [[ai-engineering/claude-code-skills]]

**Progressive Disclosure (prompts)**
: The application of the UI/UX principle of progressive disclosure to AI prompt design: the entry-point file gives the model the high-level overview and rules; detailed reference material lives in subfolders that the model navigates on demand. Preserves context budget while making full detail available.
- Related: context engineering, skill folder structure
- See also: [[ai-engineering/claude-code-skills]], [[ai-engineering/rag-approaches]]

**Skill Description (trigger conditions)**
: The `description` field of a Claude Code Skill — specifies *when the model should consider invoking the skill*, written as trigger conditions (verbs, task types, keywords) rather than as a human-readable summary. A vague description results in a skill that is never invoked at the right moment.
- Contrast: human-readable description ("skill for deploying AWS services") vs. trigger description ("use when user asks to deploy, publish, push, or mentions staging, canary, rollback")
- See also: [[ai-engineering/claude-code-skills]]

**CLAUDE_PLUGIN_DATA**
: An environment variable pointing to a stable per-plugin data directory that persists across skill updates. Used to store state (logs, history, preferences) that would be lost if written to the skill's own directory (which may be overwritten during updates).
- See also: [[ai-engineering/claude-code-skills]]

**Task Budget (Opus 4.7)**
: A beta feature in Claude Opus 4.7 that lets the caller specify a token budget for a complete agentic loop (including reasoning, tool calls, results, and output). Enables calibrating computational effort per skill: critical skills at `xhigh` effort, routine skills at `high`.
- See also: [[ai-engineering/claude-code-skills]]

---

## Style Conventions

*(Writing rules and tone guidelines specific to this knowledge base's domain. Will populate as style guides and branded content are ingested.)*

| Convention | Rule | Example |
|---|---|---|
| *(none yet)* | | |

---

## Deprecated / Avoid List

Terms that have been replaced, renamed, or should not be used:

| Avoid | Use Instead | Reason |
|---|---|---|
| *(none yet)* | | |

---

## Regional / Variant Terms

Terms that differ between audiences, teams, or locales:

| Term | Region/Context | Notes |
|---|---|---|
| *(none yet)* | | |

---

## Related Pages

- [[overview]] — big-picture synthesis
- [[index]] — master catalog
