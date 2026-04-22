---
title: Glossary
type: glossary
created: 2026-04-07
updated: 2026-04-22
sources: [pageindex-vectorless-rag.md, francieli-wagner-bim-coordination.md, mbs-performance-vs-development-coaching.md, mbs-two-questions-for-great-conversation.md, gyaco-conway-team-structure.md, mbs-paradoxes-of-being-a-coach.md, article.md, gartner-genai-security-workflow, vidvatta-mcp-vs-api-architecture.md, palantir-aip-bootcamps.md, eric-luque-claude-code-skills.md]
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
: AI researcher; founding member at OpenAI, former head of AI/Autopilot at Tesla. Originator of the LLM Wiki pattern (`llm-wiki.md`, early 2026). Known for making deep technical AI concepts accessible.
- See also: [[ai-engineering/llm-wiki-pattern]], [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]]

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

**Ontology** *(Palantir)*
: Palantir's semantic data model that represents an organization's real-world entities and events in a structured, live format. Grounds AI prompts in operational reality rather than just user input — enabling event-driven automation (e.g., a supply disruption triggers AI analysis without a human typing a prompt).
- Note: Palantir-specific term; not to be confused with the general concept of ontology in knowledge representation
- See also: [[ai-engineering/aip-platform]]

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
