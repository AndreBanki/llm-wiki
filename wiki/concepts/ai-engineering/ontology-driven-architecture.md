---
title: Ontology-Driven Architecture
type: concept
created: 2026-04-24
updated: 2026-05-03
sources: [balajiBal-palantir-ontologies, palantir-aip-bootcamps, nfigay-ontology-marketing-vs-formal, How to Develop An Open Source Ontology & AI Pipeline.md, Building Your First Ontology_ A Hands-On Tutorial.md, You Don't Need a PhD to Build an Ontology.md]
tags: [ontology, agentic-ai, schema, world-modeling, data-governance, coordination, deterministic-interface, formal-semantics, semantic-cartography, semantic-layer, open-source, skos, protege, orionbelt, tools]
---

# Ontology-Driven Architecture

An architectural approach in which a formal ontology — an explicit, shared model of real-world entities, relationships, constraints, and state transitions — serves as the operational core of a software system, rather than being a downstream analytical layer or metadata glossary.

Pioneered at scale by Palantir. Increasingly recognized as the foundational requirement for reliable agentic AI systems.

---

## The Core Distinction: Schema vs. Ontology

The most important conceptual line in this domain:

| | Schema | Ontology |
|---|---|---|
| **Describes** | Data | Reality |
| **Example** | A table has a `status` column | Status can be `PENDING`, `ACTIVE`, or `CLOSED`; moving from `ACTIVE` to `CLOSED` requires a manager role; being in `CLOSED` prohibits re-assignment |
| **Answers** | What does the database look like? | What states exist? How do you transition between them? What actions are valid right now? |
| **Era** | Big Data (retrospective) | Agentic AI (operational) |
| **Where intelligence lives** | Outside the system (analysts, humans) | Encoded in the system |

> "Schemas describe data. Ontologies describe reality." — balaji bal

---

## Four Components of an Ontology

A complete operational ontology defines:

1. **Entities** — the real-world things the system operates on (people, accounts, vehicles, facilities, transactions)
2. **Relationships** — how entities connect and interact (ownership, movement, dependency, authorization)
3. **Constraints** — what is allowed and what is forbidden
4. **State transitions** — how entities change over time and what actions those changes enable or prohibit

This is what separates an ontology from a schema, a data catalog, or a metadata glossary. The ontology isn't a layer on top of the system — it *is* the system.

---

## Why Big Data Worked Without Ontologies

Early big data systems (Hadoop, Spark, data lakes) succeeded without ontologies because they were optimized for a specific mode:
- **Retrospective analysis** — looking backward at what happened
- **Batch processing** — not real-time, not event-driven
- **Human-in-the-loop interpretation** — meaning lived in analysts' heads, not in the system

In this mode, the system produced insight; humans supplied judgment. Ontologies were optional because *intelligence was external*.

Data governance (ownership, access control, lineage, compliance) filled gaps that could be tolerated in a system that never acted autonomously.

---

## The Breaking Point: Why Agentic Systems Require Ontologies

Agentic systems don't just analyze data — they **take actions**: calling tools, triggering workflows, allocating resources at machine speed. The moment you move from *insight to action*, implicit meaning becomes a liability.

**Without ontologies, agentic systems fail in predictable ways:**
- Agents hallucinate actions that don't map to real-world state
- Tools are misused because their effects and preconditions aren't defined
- Safety boundaries become probabilistic (policy-based) instead of deterministic (physics-based)
- Coordination between agents collapses into prompt spaghetti

> "This is why so many 'AI agents' today look impressive in demos and fail in production. They are reasoning over text and schemas, not over a shared model of reality."

Palantir's agents avoid this because they are *constrained by the ontology*: actions are only valid if they correspond to legitimate state transitions on real entities.

---

## Ontologies as the Coordination Layer

Ontologies are not just technical infrastructure — they are a **coordination layer** for any system in which multiple humans, services, and agents must operate together.

Without a shared model of reality, coordination requires:
- Constantly negotiated contracts between services
- Human interpretation to bridge semantic gaps
- Governance policy to fill the gaps the system can't enforce itself

With a shared ontology, every participant has a common answer to:
- What exists
- What can change
- Who is allowed to change it
- What the consequences are

> "Ontologies make systems composable. They turn APIs into contracts about reality, not just function signatures."

This is why Palantir deployments scale across organizations and years — the ontology becomes the stable interface between people, software, and agents.

**In modern terms: ontologies are the deterministic interface that agentic systems desperately need.**

---

## Why Data Governance Alone Is Not Enough

Data governance addresses:
- Who owns a dataset?
- Who can access it?
- Is it compliant?

These are necessary but not sufficient. Ontologies answer a different class of questions:
- What *is* this thing?
- What can happen to it?
- What actions are valid right now?

> "Governance without ontology is bureaucracy without physics."

You can regulate access to data perfectly and still have a system that doesn't understand the domain it's operating in. Governance is policy; ontology is physics. In Palantir's implementation, governance is inseparable from the ontology — enforced through meaning, not bolted on with policy.

---

## Palantir's Approach: World-Modeling as Core Strategy

Palantir was a *world-modeling company* from the beginning — not a dashboards company, a data lake company, or an analytics company. While the big data industry raced to ingest more data faster, Palantir consistently asked:

> "What are the actual entities in this domain, and how do they relate?"

This was unfashionable for most of the 2010s. In hindsight, it was prescient. The bet:

> "Meaning had to be encoded up front, explicitly, and shared across the system."

Core principle: **Meaning precedes intelligence.**

---

---

## A Critical View: The Formal Semantics Gap

*Source: Dr Nicolas Figay, "Everyone Has an Ontology Now. Almost Nobody Has an Ontology." (2026) — [[ai-engineering/nfigay-ontology-marketing-vs-formal]]*

The framing above reflects the view advanced by balaji bal and Palantir. A second, complementary view holds that vendor "ontologies" — including Palantir's — do not qualify as formal ontologies in the logical sense, and that this distinction matters when AI agents must reason autonomously in high-stakes domains.

A **formal ontology** provides:

| Property | What it means |
|---|---|
| **Formal semantics** | Axioms with a well-defined model-theoretic interpretation |
| **Description logic** | A decidable fragment of first-order logic for class relationships and constraints |
| **Open World Assumption** | Absence of a fact = unknown, not false; inference can derive what was not explicitly stated |
| **Inference** | A reasoner derives conclusions from axioms; the system can *prove* things |
| **Decidability** | The inference procedure terminates in bounded time |
| **Auditability** | Every derived conclusion traces back to the axioms that produced it |

Figay's assessment of the vendor landscape:

- **Palantir Ontology** — "the most sophisticated of the vendor offerings" (object types, link types, action types) — but no description logic, no inference, no formal epistemological commitment. A well-governed conceptual map, not semantic reasoning.
- **Microsoft Fabric IQ** — bootstrapped from Power BI semantic models by business users via no-code tools. No formal semantics.

The stakes are not low: Palantir runs systems supporting defence operations; Microsoft positions Fabric IQ for autonomous AI decision-making. When an agent acts on an informal semantic layer, its reasoning is only as good as the completeness of what domain experts manually constructed — not what an inference engine derived.

**The key question:** *What exactly can your system prove?*

### Holding Both Views in Tension

| Dimension | balaji bal (2026) | Dr Nicolas Figay (2026) |
|---|---|---|
| **Palantir Ontology** | Deterministic interface in practice | Most sophisticated vendor offering, still lacks formal semantics |
| **What you get** | Valid state transitions that constrain agent actions | Well-governed conceptual map with no inference engine |
| **The bet** | Convergence on meaning is achievable and sufficient | Convergence is a structural impossibility |
| **Failure mode** | Agents hallucinate when the ontology has gaps | Agents have no formal proof — informal gaps fail silently |

The resolution: Palantir's Ontology is more powerful than a schema and more useful than a data catalog. Whether the formal/informal distinction matters depends on what the system must *prove*. For operational coordination within a governed domain, informal ontologies may be sufficient. For formal certification of autonomous behavior in safety-critical systems, they are not.

---

## A Competing Paradigm: Semantic Cartography

*Source: Dr Nicolas Figay — CAISE 2025 / I-ESA 2026*

Semantic Cartography starts from the opposite epistemological premise: **universal semantic representation is not a problem waiting to be solved — it is a structural impossibility.**

Enterprise systems inevitably involve representations that are:
- **Legitimate:** each valid within its own frame of reference
- **Incompatible:** cannot be merged without losing information from at least one frame
- **Necessary:** the incompatibility reflects genuine differences in how different actors model the world

The appropriate response is not to build a better unified ontology. It is to build tools that *navigate plurality*: mapping the semantic landscape — where representations align, where they diverge, and what the interoperability consequences of each divergence are.

**The architectural contrast:**

| | Ontology-Driven Architecture | Semantic Cartography |
|---|---|---|
| **Core bet** | Convergence is achievable — build toward unified meaning | Convergence is impossible — navigate plurality |
| **Primary artifact** | Ontology (unified model) | Map (representation landscape) |
| **Agent stance** | Agents constrained by valid ontology state transitions | Agents navigating explicit representation divergences |
| **Failure mode** | Brittle when model is incomplete | Requires ongoing cartographic maintenance |
| **Scope** | Single domain or enterprise | Multi-domain, multi-organization interoperability |

**Both paradigms agree:** agentic systems need semantic grounding. **They disagree:** on whether to achieve it by converging on a shared model or by building navigation tools for irreducible plurality.

Figay's argument: a platform betting on convergence creates brittle, opaque, non-auditable semantic infrastructure that fails quietly until it fails catastrophically. Two decades of industrial evidence support the plurality view.

---

## Open-Source Implementation Pathway

*Source: Dhiraj Patra, "How to Develop An Open Source Ontology & AI Pipeline" (2026) — [[ai-engineering/dhiraj-patra-open-source-ontology-pipeline]]*

The Palantir Ontology's capabilities can be approximated with open-source tools. The key architectural mapping:

| Palantir Capability | Open-Source Equivalent | Role |
|---|---|---|
| Data Integration (Magritte) | Airbyte + dbt | Ingest → Bronze/Silver/Gold medallion layers |
| Ontology Objects & Links | Neo4j (Knowledge Graph) | Entities as nodes, relationships as edges |
| Semantic Layer | Cube.js / dbt Semantic Layer | Map technical tables to business terms via YAML |
| Actions (Write-back) | Retool / Streamlit | UI buttons that trigger database mutations |
| AI/ML Integration | MLflow + Neo4j GDS | Graph algorithms feed ML models; predictions become object properties |

**The Semantic Layer** is the critical middle tier: it translates raw database artifacts (tables, columns, joins) into business-meaningful terms — so a user queries "Revenue" not `SUM(orders.price)`. Tools like Cube.js and dbt Semantic Layer achieve this via YAML configuration rather than a full ontological commitment.

**Critical assessment:** This approach gives total ownership and flexibility at the cost of integration effort. However, per the Formal Semantics Gap section above, an open-source stack built this way still lacks formal inference, the Open World Assumption, and provable reasoning — it replicates Palantir's practical capabilities without addressing Figay's deeper critique. The term "ontology" here refers to a well-organized semantic layer with entity relationships, not a formal ontology in the logical sense.

---

## Practitioner Tooling: Building Ontologies

*Sources: [[ai-engineering/pankaj-kumar-building-first-ontology-tutorial]], [[ai-engineering/ralfo-becher-you-dont-need-phd-ontology]]*

The formal/informal spectrum described above is reflected in the available tooling. Two primary tools exist for practitioners who need to build ontologies without full-time ontology engineering backgrounds.

### The Design Process: Paper Before Software

Regardless of tool, the recommended methodology (Pankaj Kumar) starts before any software:

1. **List classes** — the 5–10 "things" that exist in the domain (entities)
2. **Draw relationships** — labeled arrows between concepts (object properties)
3. **List attributes** — what information describes each class (data properties)
4. **Articulate rules** — what logical constraints and state transitions exist (axioms)

> "If you can explain your domain to another person, you can model it in an ontology. The formal languages just give structure to knowledge you already have."

This maps directly to the four ontology components: entities → classes; relationships → object properties; constraints/state transitions → axioms and restrictions.

### Tool Comparison

| Dimension | Protégé | OrionBelt |
|---|---|---|
| **Created by** | Stanford University | Ralfo Becher (open-source) |
| **Interface** | Desktop application | Browser-based (Streamlit) |
| **Reasoner** | Pellet / HermiT (full OWL DL) | OWL-RL (built in) |
| **Formal semantics** | Full Description Logic ✅ | OWL-RL (subset of OWL DL) ⚠️ |
| **SWRL / complex axioms** | Supported | Not supported |
| **SKOS support** | Via plugins | Dedicated SKOS page ✅ |
| **Bulk operations** | Manual one-by-one | Paste names (one per line or CSV) ✅ |
| **Undo** | Limited | Checkpointed; bulk rolls back as single step ✅ |
| **Import diff** | No | Shows new/conflicts/prefix changes before applying ✅ |
| **Best for** | Formal ontology engineering; full DL inference | Practical domain modeling; fast iteration; SKOS vocabulary |
| **Install** | Download from protege.stanford.edu | `pip install orionbelt-ontology-builder` |

**Formal semantics position:** Protégé + Pellet/HermiT operates fully in OWL DL — this is the real formal inference that Figay says almost nobody achieves. OrionBelt with OWL-RL is a meaningful step above vendor "ontologies" (which have no inference at all), but still not full DL. The practical choice: start with OrionBelt for speed and accessibility; migrate to Protégé when formal provability is required.

### The Inference Demonstration

The canonical proof of formal inference in Protégé:
1. Define a class: `VegetarianDish` ≡ `Dish and (isVegetarian value true)`
2. Create individual: `MargheritaPizza` as a `Dish` with `isVegetarian = true`
3. Run reasoner (Pellet/HermiT)
4. Result: `MargheritaPizza` is **automatically classified** as a `VegetarianDish` — never stated explicitly

This is the mechanistic difference between an informal ontology (a labeled property graph) and a formal one (a system that can prove new facts). The Palantir Ontology would require an action rule to be manually written; a formal ontology derives the classification.

### Common Design Mistakes

| Mistake | Wrong approach | Right approach |
|---|---|---|
| Too many classes | `ItalianRestaurant`, `ChineseRestaurant`… | One `Restaurant` + `specializesIn` → `CuisineType` |
| Class vs. individual | `Restaurant` as individual | `Restaurant` as class, `MamasTrattoria` as individual |
| Overly complex properties | `serves_spicy_vegetarian_dishes` | Combine simple: `serves` + `hasSpiciness` + `isVegetarian` |
| Reinventing the wheel | Custom `hasName` | Import Schema.org, FOAF, or Dublin Core |

### Standard Ontology Reuse Libraries

Before defining custom properties, check established vocabularies:
- **Schema.org** — general web content: names, addresses, organizations, events
- **FOAF (Friend of a Friend)** — people, identities, social relationships
- **Dublin Core** — document metadata: title, creator, subject, description

---

## SKOS: Controlled Vocabularies

*Source: [[ai-engineering/ralfo-becher-you-dont-need-phd-ontology]]*

**SKOS (Simple Knowledge Organization System)** is a W3C standard for representing controlled vocabularies, taxonomies, and thesauri in RDF. It is conceptually distinct from OWL class hierarchies:

| | OWL Class Hierarchy | SKOS Concept Scheme |
|---|---|---|
| **Models** | Logical types and individuals | Vocabulary terms and their semantic relationships |
| **Relationship** | `rdfs:subClassOf` (logical subsumption) | `skos:broader` / `skos:narrower` (hierarchical navigation) |
| **Use case** | Domain ontology (what exists, what can change) | Controlled vocabulary (authorized terminology, thesaurus) |
| **Inference** | Reasoner derives new class memberships | Validates cycles, missing labels, hierarchy consistency |
| **Examples** | "A VegetarianDish is a Dish where isVegetarian=true" | UNESCO Thesaurus, medical subject headings, classification systems |

SKOS is directly relevant to the Axis project: material types, activity categories, contract types, and regulatory classifications are all natural SKOS concept schemes — structured vocabularies that don't need full OWL inference but need consistent, navigable, interoperable terminology.

**Key SKOS relationships:**
- `skos:Concept` — a unit of thought (a term)
- `skos:ConceptScheme` — a collection of concepts
- `skos:broader` / `skos:narrower` — hierarchical; inverses automatically maintained
- `skos:related` — associative (not hierarchical)
- `skos:prefLabel` / `skos:altLabel` — preferred and alternate terms (multilingual support)

---

## Connections to Other Concepts

- **[[ai-engineering/aip-platform]]** — Palantir AIP uses the Ontology to ground AI in real-world operational events; this page deepens and critiques the ontology layer of that concept
- **[[ai-engineering/nfigay-ontology-marketing-vs-formal]]** — primary source for the Formal Semantics Gap and Semantic Cartography sections above
- **[[ai-engineering/dhiraj-patra-open-source-ontology-pipeline]]** — primary source for the Open-Source Implementation Pathway section
- **[[ai-engineering/pankaj-kumar-building-first-ontology-tutorial]]** — primary source for the Practitioner Tooling and paper exercise sections above; Protégé workflow
- **[[ai-engineering/ralfo-becher-you-dont-need-phd-ontology]]** — primary source for OrionBelt and SKOS sections above
- **[[ai-engineering/mcp-architecture]]** — MCP (Model Context Protocol) is a complementary deterministic interface: MCP defines what *tools* an agent can call; an ontology defines what *reality states* are valid. Both move AI from text-reasoning to structured-world-reasoning
- **[[ai-engineering/ai-agent-governance]]** — Ontologies are the enforcement mechanism that makes guardrails deterministic; the four-component governance stack (guardrails, observability, FinOps, execution control) is structurally stronger when built on an ontology — and weaker when the ontology lacks formal semantics
- **[[ai-engineering/genai-security-workflow]]** — The Gartner framework's data governance stage is necessary but, per both sources, insufficient; formal ontologies would complete what governance alone cannot enforce
- **[[product-org-design/conways-law]]** — "Meaning must be encoded upfront" mirrors "strategy must precede structure"; both reject emergent, unplanned design in favor of deliberate upfront modeling
