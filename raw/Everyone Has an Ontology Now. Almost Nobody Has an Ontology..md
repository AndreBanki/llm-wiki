---
title: "Everyone Has an Ontology Now. Almost Nobody Has an Ontology."
source: "https://medium.com/@nfigay/everyone-has-an-ontology-now-almost-nobody-has-an-ontology-4032a0e02f40"
author:
  - "[[Dr Nicolas Figay]]"
published: 2026-04-16
created: 2026-04-27
description: "Everyone Has an Ontology Now. Almost Nobody Has an Ontology. Microsoft just announced Fabric IQ. At its core: an “Ontology item.” Palantir has been selling its “Ontology” as the backbone of …"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SK0Ai7r0UobGvCyIpEh-NA.png)

Microsoft just announced Fabric IQ. At its core: an “Ontology item.” Palantir has been selling its “Ontology” as the backbone of enterprise AI for years. SAP, Salesforce, AWS — each has a version of the same story.

There is a pattern here worth naming.

The word “ontology” has escaped its technical meaning and become a marketing asset. It signals rigor, structure, shared understanding. It implies that the platform knows what your business means — not just what your data says. In the age of agentic AI, that is an enormously valuable claim.

The problem is that most of what is being sold under that label is something else: a governed property graph. A business glossary with relationship types. A typed schema with some constraints layered on top. These are not worthless — they are genuinely useful artefacts. But they are not ontologies in any formal sense, and the distinction matters enormously the moment you ask an AI agent to reason on top of them.

Let me be precise about what a formal ontology actually implies.

An ontology, in the logical sense, provides a formal semantics — axioms, description logic, an explicit stance on the Open World Assumption. It distinguishes individuals from classes. It allows inference: from what you have asserted, a reasoner can derive what you have not explicitly stated. That derivation is bounded, decidable in defined fragments, and auditable.

None of the vendor “ontologies” I have examined commit to any of this. Microsoft’s Fabric IQ ontology is bootstrapped from Power BI semantic models by business experts using no-code visual tools. Palantir’s Ontology defines object types, link types, action types — a rich operational model, the most sophisticated of the vendor offerings — but with no description logic underneath, no inference, no formal commitment to an epistemological regime. What you get is a well-governed conceptual map. What you are promised is semantic reasoning. These are not the same thing.

This would be a merely academic distinction if the stakes were low. They are not.

Microsoft explicitly positions Fabric IQ as the foundation for agentic AI that makes autonomous operational decisions. Kyndryl cites “trust” as the reason they are adopting it. ENMAX Power is connecting transmission and distribution grid data to it. Palantir runs systems supporting Defence operations and critical infrastructure.

When an AI agent acts autonomously on the basis of a “semantic layer,” the question that matters is: what guarantees does that layer actually provide? If the ontology is informal — if it is a business glossary with governance tooling — then the agent’s reasoning is only as good as the completeness and consistency of the model as manually constructed by domain experts. There is no inference. There is no formal constraint validation. There is no decidability. There is operational context, curated by humans, dressed in the language of logic.

That is not nothing. But it is not what is being claimed.

I have spent the last several years building something that starts from the opposite epistemological position.

The foundational claim of my wor, elaborated in *Inhabiting Babel* and experimented as a futur supported Knowledge cartography with next version of ArchiCG, is that universal semantic representation is not a problem waiting to be solved. It is a structural impossibility. The appropriate response is not to build a better ontology-as-single-source-of-truth. It is to build tools that navigate plurality: that make the coexistence of multiple, legitimate, incompatible representations visible, governable, and traversable.

The Semantic Cartography I presented at CAISE 2025 is underlying the paper about Enterprise Interoperability I will present this week at I-ESA 2026 in Funchal. This is not about asserting a unified model of the enterprise. It is a tool for cartographying the semantic landscape — showing where representations align, where they diverge, and what the consequences of that divergence are for interoperability.

The difference is not stylistic. It is architectural. A platform that promises unified ontological grounding for agents is making a bet that convergence is achievable. I am arguing — with formal backing and two decades of industrial evidence — that it is not, and that building on that bet creates exactly the kind of brittle, opaque, non-auditable semantic infrastructure that fails quietly until it fails catastrophically.

The vendors are not wrong that the problem is real. Data without meaning is noise. Agents without semantic grounding make confident mistakes. The push toward ontological infrastructure is a legitimate response to a genuine crisis in enterprise AI.

But the solution being offered, centralized, informal, democratized ontology construction, reproduces the problem it claims to solve. You cannot ground reasoning in a model that has no formal semantics. You cannot certify agent behavior against constraints that were never formally specified.

Everyone has an ontology now.

Almost nobody has an ontology.

The question worth asking your vendor: what exactly can your system prove?