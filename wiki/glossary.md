---
title: Glossary
type: glossary
created: 2026-04-07
updated: 2026-04-22
sources: [pageindex-vectorless-rag.md, francieli-wagner-bim-coordination.md, mbs-performance-vs-development-coaching.md, mbs-two-questions-for-great-conversation.md]
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
- See also: [[rag-approaches]]

**Vector RAG** *(traditional RAG)*
: The dominant RAG implementation: documents are chunked, embedded into dense vectors, stored in a vector database, and retrieved via cosine similarity search at query time.
- Preferred: `vector RAG` / Avoid: `standard RAG`, `classic RAG` (ambiguous)
- See also: [[rag-approaches]]

**Vectorless RAG**
: A RAG approach that eliminates embeddings and vector databases entirely. Instead uses LLM reasoning over a structured document index (e.g., hierarchical tree) to identify relevant content.
- Canonical term introduced by VectifyAI for the PageIndex approach.
- See also: [[pageindex]], [[rag-approaches]]

**PageIndex**
: Open source vectorless RAG framework by VectifyAI (introduced September 2025). Builds a hierarchical tree index from a document's natural structure and uses LLM reasoning to navigate to the answer.
- See also: [[pageindex]]

**FinanceBench**
: A benchmark for evaluating RAG systems on financial document Q&A tasks. Used to compare retrieval accuracy. PageIndex scores 98.7%; traditional vector RAG scores ~50%.

**Chunking**
: The process of splitting a document into fixed-size segments (typically measured in tokens) before embedding. A necessary step in vector RAG, but one that destroys document structure and cross-references.
- See also: [[rag-approaches]]

**Tree Index** *(PageIndex tree, hierarchical index)*
: In PageIndex, the structured JSON representation of a document's content. Each node contains: `node_id`, `title`, `pages`, `summary`, `key_topics`. Built once at index time; used for reasoning-based retrieval at query time.
- See also: [[pageindex]]

**Reasoning-Based Retrieval**
: A retrieval strategy where an LLM reasons about *where in a document* an answer is likely located, navigating document structure rather than computing similarity scores. Contrasted with similarity-based retrieval.
- See also: [[rag-approaches]], [[pageindex]]

**FinanceBench** *(benchmark)*
: Financial document Q&A benchmark. PageIndex: 98.7% accuracy. Traditional vector RAG: ~50%.

**Cosine Similarity**
: The standard distance metric used in vector RAG to compare query embeddings against stored document chunk embeddings. Measures semantic similarity, not relevance to user intent.
- See also: [[rag-approaches]]

**VectifyAI**
: The team that built and maintains PageIndex. Also operates the cloud service at pageindex.ai.
- See also: [[pageindex]]

---

## Coaching / Leadership

**Performance Coaching**
: A mode of coaching focused on the task at hand — getting things done, fixing problems, moving faster. The natural default under pressure. Risk: the coach takes ownership of the thinking, leaving the other person feeling unaccomplished.
- Contrasted with: development coaching
- See also: [[coaching-modes]]

**Development Coaching**
: A mode of coaching focused on the person doing the task — who they are becoming, what they are learning, what capability they are building. Requires staying curious long enough for the other person to grow.
- Not passive or slow by default; it's intentional curiosity
- Contrasted with: performance coaching
- See also: [[coaching-modes]]

**Resisting the Urge to Rescue**
: A key discipline in development coaching. After asking a question, not filling the silence with your own answer. Trusting the other person to do their own thinking even when it feels slow or uncomfortable.
- See also: [[coaching-modes]]

**Holding Space**
: Remaining present and attentive without rushing to fill silence or offer solutions. Allows the other person room to think, process, and arrive at their own conclusions.
- See also: [[coaching-modes]]

---

## BIM / Coordenação de Projetos

**BIM** *(Building Information Modeling / Modelagem da Informação da Construção)*
: Metodologia de trabalho baseada em modelos digitais tridimensionais e inteligentes que integram geometria, dados e informações do ciclo de vida da construção.
- Canonical form for this wiki: `BIM` (sigla em inglês, universalmente adotada no Brasil)
- See also: [[bim-coordination]]

**Coordenação BIM**
: Processo de integração e compatibilização das disciplinas de projeto (estrutural, hidráulica, elétrica, HVAC, incêndio, etc.) dentro de um ambiente BIM, com o objetivo de identificar e resolver conflitos antes da execução em obra.
- See also: [[bim-coordination]]

**Modelo Federado**
: Agregação dos modelos individuais de cada disciplina em um único ambiente de visualização e análise. Condição necessária, mas não suficiente, para coordenação BIM real.
- See also: [[bim-coordination]]

**Compatibilização**
: Processo de identificação e resolução de conflitos físicos, funcionais ou de sequência entre disciplinas de projeto. Pode ser feita via clash detection automatizado ou revisão manual.
- See also: [[bim-coordination]]

**Disciplinas Complementares**
: Conjunto de projetos de engenharia que complementam o projeto arquitetônico: estrutural, hidráulica, elétrica, HVAC (climatização), PPCI (prevenção e combate a incêndio), entre outros.
- Preferred: `disciplinas complementares` / Avoid: `disciplinas` (ambíguo)

**Clash Detection**
: Verificação automatizada de interferências físicas (colisões geométricas) entre elementos de disciplinas distintas dentro do modelo federado.

**PPCI** *(Projeto de Prevenção e Combate a Incêndio)*
: Disciplina complementar responsável pelo sistema de proteção contra incêndio: sprinklers, hidrantes, rotas de fuga, etc.

**HVAC** *(Heating, Ventilation, and Air Conditioning)*
: Disciplina complementar de climatização e ventilação. No contexto brasileiro, inclui ar-condicionado e ventilação mecânica.

**Conversation Design**
: The practice of pre-selecting questions and structuring the opening of a group conversation to invite depth and bypass surface-level exchange. The designer acts as a host, then steps back. Distinct from facilitation (which manages process) and coaching (which is one-on-one).
- See also: [[conversation-design]]

**Good Host**
: A role described by MBS as deliberately curating people and questions to create conditions for meaningful connection and collaboration — not just organizing logistics. A good host wants "great people to know other great people."
- See also: [[conversation-design]]

**The Conspiracy**
: MBS's accountability membership community. Members commit to a Worthy Goal and receive support, focus, and accountability from a "brilliant community of humans."
- See also: [[mbs-two-questions-for-great-conversation]]

**Worthy Goal**
: The declared aspiration a Conspiracy member commits to. The practical answer to the conversation design question "What are you up to?" — what adventure is beckoning, the edge you're stepping toward.
- See also: [[conversation-design]], [[mbs-two-questions-for-great-conversation]]

**"What are you known for?"**
: First question of MBS's two-question dinner format. Invites participants to name their values, elemental parts, and best self as seen by people who care about them — not their public reputation.
- See also: [[conversation-design]]

**"What are you up to?"**
: Second question of MBS's two-question dinner format. Conspiratorial in tone; asks about the adventure beckoning, the edge being stepped toward, and who the person is becoming. Bypasses status updates.
- See also: [[conversation-design]]

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
