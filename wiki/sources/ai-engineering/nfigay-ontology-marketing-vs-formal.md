---
title: "Everyone Has an Ontology Now. Almost Nobody Has an Ontology."
type: source
created: 2026-04-27
updated: 2026-04-27
sources: ["Everyone Has an Ontology Now. Almost Nobody Has an Ontology..md"]
tags: [ontology, formal-semantics, description-logic, semantic-cartography, agentic-ai, vendor-critique, enterprise-ai, microsoft-fabric, palantir]
---

# Everyone Has an Ontology Now. Almost Nobody Has an Ontology.

Medium article by Dr Nicolas Figay (April 16, 2026) arguing that "ontology" has become a marketing term — stripped of its formal meaning and applied to governed property graphs, business glossaries, and typed schemas that share the name but none of the logical guarantees.

---

## Metadata

| Field | Value |
|---|---|
| Author | Dr Nicolas Figay |
| Published | 2026-04-16 |
| Source URL | https://medium.com/@nfigay/everyone-has-an-ontology-now-almost-nobody-has-an-ontology-4032a0e02f40 |
| Format | Medium article |
| Tags | ontology, formal semantics, agentic AI, Semantic Cartography, enterprise AI |

---

## Core Thesis

The word "ontology" has escaped its technical meaning and become a marketing asset. Microsoft (Fabric IQ), Palantir, SAP, Salesforce, and AWS each have a version of the same story: an "ontology" that signals rigor, structure, and shared understanding — the claim that the platform knows what your business *means*, not just what your data says.

The problem: most of what is being sold under that label is a governed property graph, a business glossary with relationship types, or a typed schema with constraints. These are not worthless, but they are not ontologies in any formal sense. And the distinction matters enormously the moment you ask an AI agent to reason on top of them.

**The key question:** *What exactly can your system prove?*

---

## What a Formal Ontology Actually Requires

A formal ontology — in the logical sense — provides:

| Property | What it means |
|---|---|
| **Formal semantics** | Axioms with a well-defined model-theoretic interpretation |
| **Description logic** | A decidable fragment of first-order logic for expressing class relationships and constraints |
| **Open World Assumption (OWA)** | Absence of a fact does not mean it is false — it means it is unknown |
| **Inference** | From what you have asserted, a reasoner derives what you have not explicitly stated |
| **Decidability** | The inference procedure terminates in bounded time in defined fragments |
| **Auditability** | Every derived conclusion can be traced to the axioms that produced it |

None of the vendor "ontologies" examined by Figay commit to any of this.

---

## The Vendor Landscape

### Microsoft Fabric IQ
Bootstrapped from Power BI semantic models by business experts using no-code visual tools. No formal semantics. No inference engine. Marketed as the foundation for agentic AI making autonomous operational decisions. Kyndryl cites "trust" as their reason for adoption; ENMAX Power connects transmission and distribution grid data to it.

### Palantir Ontology
Defines object types, link types, and action types — "the most sophisticated of the vendor offerings." But: no description logic underneath, no inference, no formal commitment to an epistemological regime.

> "What you get is a well-governed conceptual map. What you are promised is semantic reasoning. These are not the same thing."

### The Pattern

> "Everyone has an ontology now. Almost nobody has an ontology."

---

## Why the Stakes Are High

The gap between claim and reality is not academic. When an AI agent acts autonomously on the basis of an informal "semantic layer," the relevant question is: *what guarantees does that layer actually provide?*

Without formal semantics: no inference, no formal constraint validation, no decidability. The agent's reasoning is only as good as the completeness and consistency of the model as manually constructed by domain experts. That is operational context dressed in the language of logic — useful, but not what is being claimed.

The systems in question are not low-stakes: Palantir runs defence operations and critical infrastructure. Microsoft positions Fabric IQ for autonomous operational AI.

---

## Figay's Alternative: Semantic Cartography

The author's position starts from the opposite epistemological premise: **universal semantic representation is not a problem waiting to be solved — it is a structural impossibility.**

The appropriate response is not to build a better unified ontology. It is to build tools that navigate plurality: that make the coexistence of multiple, legitimate, incompatible representations visible, governable, and traversable.

**Semantic Cartography** (presented at CAISE 2025; underlying the I-ESA 2026 paper on Enterprise Interoperability in Funchal) is a tool for mapping the semantic landscape: showing where representations align, where they diverge, and what the consequences of that divergence are for interoperability.

Related projects: *Inhabiting Babel*; ArchiCG experiment with "futur supported Knowledge cartography."

**The architectural bet:** A platform promising unified ontological grounding for agents bets that convergence is achievable. Figay argues — with formal backing and two decades of industrial evidence — that building on that bet creates brittle, opaque, non-auditable semantic infrastructure that fails quietly until it fails catastrophically.

---

## Relation to Existing Wiki — Both Views Held in Tension

This source is in productive tension with [[ai-engineering/balajiBal-palantir-ontologies]], which presents Palantir's Ontology positively as a "deterministic interface." The wiki holds both views:

| | balaji bal (2026) | Dr Nicolas Figay (2026) |
|---|---|---|
| **Palantir Ontology** | The most sophisticated vendor offering; deterministic in practice | The most sophisticated vendor offering; still lacks formal semantics |
| **Core claim** | It defines valid state transitions → constrains agent actions | It defines valid state transitions → but with no formal inference or proof |
| **What you get** | Deterministic interface for agentic AI | Well-governed conceptual map |
| **The bet** | Convergence is achievable and sufficient | Convergence is a structural impossibility |

The resolution: Palantir's Ontology is more powerful than a database schema and more useful than a data catalog. Whether the formal/informal distinction matters depends on what you need the system to *prove*. For operational coordination of agents within a governed domain, it may be sufficient. For formal certification of autonomous behavior in safety-critical systems, it is not.

---

## Related Pages

- [[ai-engineering/ontology-driven-architecture]] — concept page holding both views in tension; includes Semantic Cartography as a competing paradigm
- [[ai-engineering/balajiBal-palantir-ontologies]] — the Palantir-positive view; complement to this source
- [[ai-engineering/aip-platform]] — Palantir AIP: the concrete deployment context for the ontology
- [[ai-engineering/ai-agent-governance]] — governance gap when the semantic layer lacks formal proof guarantees
- [[ai-engineering/enterprise-ai-deployment]] — vendor enterprise AI deployment context
