---
title: "BIMConverse - GraphRAG for IFC Natural Language Queries"
type: source
created: 2026-05-04
updated: 2026-05-04
sources: [BIMConverse - GraphRAG for IFC Natural Language Queries - IAAC BLOG.pdf]
tags: [bim, ifc, graphrag, neo4j, cypher, openai, ifcopenshell, topologicpy, natural-language-query, design-intelligence, knowledge-graph, openbim]
---

IAAC/MaCAD final thesis project (Libny Pacheco, Christoph Berkmiller) describing a practical pipeline to query IFC BIM archives in natural language by converting models into a Neo4j labeled property graph and translating questions into Cypher.

---

## Metadata

| Field | Value |
|---|---|
| Authors | Libny Pacheco, Christoph Berkmiller |
| Institution | IAAC - Institute for Advanced Architecture of Catalonia |
| Program | Master in Advanced Computation for Architecture and Design (MaCAD 23/24 Final Thesis) |
| Source Type | IAAC Blog thesis report |
| Date (article updated) | 2024-09-25 |
| Original URL | https://blog.iaac.net/bimconverse-graphrag-for-ifc-natural-language-queries/ |
| Core stack | Revit -> IFC -> IfcOpenShell + TopologicPy -> Neo4j (LPG) -> NeoConverse/BIMConverse -> GPT-4o |
| Query language | Cypher |
| Corpus | ~60 residential BIM projects (White Arkitekter, 2016-2022) |

---

## Core Question

How can data, information, and knowledge embedded in BIM models become accessible via natural language, without requiring users to write technical query code?

The source uses Ackoff's pyramid (data -> information -> knowledge) as the evaluation frame for query quality.

---

## State Of The Art Framing

The source maps prior IFC-querying approaches and their limits:

- RDF/SPARQL lineage: RDF, BIMSPARQL, NLQL4BIM, GSP4BIM
- LPG lineage: IFC-GRAPH + Cypher traversal
- Main critique: even "natural language" wrappers still end up generating technical queries and require precise, domain-aware interpretation

The proposed direction is GraphRAG over IFC-derived LPGs, with a chat interface mediating natural-language intent and graph query execution.

---

## Architecture And Method

### 1. BIM To Graph Conversion

- Revit models are exported to IFC for standardization and compatibility
- IfcOpenShell extracts explicit entities, attributes, and relations
- TopologicPy derives implicit spatial/topological relations
- Custom code handles heterogeneous modeling edge cases, including wall-layer material mapping and order reconstruction
- Graph is materialized in Neo4j with nodes (rooms, walls, doors, windows, etc.) and explicit + implicit relations

### 2. NL Querying Workflow (BIMConverse)

- UI is a customized NeoConverse single-page app (local)
- User configures Bolt connection, OpenAI key/model, graph schema context, and few-shot examples
- LLM translates NL prompt to Cypher
- Query-cleaning step post-processes Cypher before execution
- Neo4j returns JSON result
- A second prompt converts JSON answer into human-readable natural language
- Chat history is reused to reduce friction in follow-up questions

### 3. Reliability Position

The source claims reduced hallucination risk versus standalone chat because the LLM translates between representation layers (NL <-> Cypher <-> NL) while factual answers come from graph database execution.

---

## Reported Results

### Data Querying

- Strong performance for counts and attribute retrieval across project-specific and cross-project scopes
- Response quality described as high and often table-structured

### Information Querying

- Supports contextual/relational queries (comparisons, ratios, element distributions, relation-aware queries)
- Demonstrates interpretation with explicit uncertainty boundaries when data is incomplete

### Knowledge Querying

- Early capability for synthesis and comparative reasoning across model aspects
- Current ceiling constrained by graph coverage (missing classes/attributes limit deeper reasoning)

### Practical Scale Notes

- Corpus scale: ~60 real projects
- Processing time scales with project size: under 2 minutes (small) to ~50 minutes per floor (large)
- No full conversion failures, but many heterogeneity adjustments were needed

---

## Limitations Identified By Authors

- Context retention inconsistencies in multi-turn dialogue
- High prompt precision requirement (term choice and disambiguation strongly affect output)
- Query interpretation edge cases (directionality, double-counting behavior)
- Pathfinding realism constraints in some spatial routing results
- Parameter naming heterogeneity across project families (e.g., windows/doors)

---

## Outlook And Extensions

- Expand graph schema coverage (IfcBeam, IfcColumn, IfcSlab, stronger vertical links)
- Add code and regulation documents into retrieval context for compliance and quality-control queries
- Explore open alternatives to proprietary dependencies (Neo4j/OpenAI)
- Potential CI/CD pipeline: trigger graph regeneration via webhooks from APS or Speckle
- Mentions IFC5 + ECS direction and cross-database graph unification paths (JSON-LD/RDF variants)

---

## Why This Matters For The Wiki

This source adds a concrete BIM-domain GraphRAG implementation pattern that complements existing conceptual pages:

- It operationalizes graph-based retrieval with explicit IFC tooling choices
- It grounds anti-hallucination claims in DB-backed execution rather than prompt-only controls
- It links openBIM interoperability (IFC) to natural-language analytics workflows in production-like archives

---

## Related Pages

- [[bim-construction/openbim-standards]]
- [[bim-construction/bim-coordination]]
- [[bim-construction/construcao-40]]
- [[ai-engineering/rag-approaches]]
- [[ai-engineering/how-to-use-graphify-knowledge-graph]]
- [[glossary]]
