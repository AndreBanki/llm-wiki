---
title: Spec-Driven Development (SDD)
type: concept
created: 2026-05-12
updated: 2026-05-12
sources: ["PRDs are Dead.md"]
tags: [product-management, ai-product-management, spec-driven-development, vibe-coding, behavioral-spec, executable-specification, ai-engineering]
---

A development methodology where a formal, machine-readable specification is written and approved before any code is generated; the spec functions as an executable contract enforced by CI/CD, not as a document.

---

## Core Idea

SDD flips the traditional sequence:

| Traditional | SDD |
|---|---|
| Write product intent → generate code → infer what constraints exist | Write formal spec (constraints, behavior, success criteria) → code is derived as a downstream artefact |
| PM clarifies ambiguity in sprint review meetings | Ambiguity resolved in the spec before generation starts |
| Bug fix patches the code | Bug fix patches the spec; AI regenerates correctly on next run |

The spec is **not** a document people read. It is a contract the build system enforces. Code that violates the spec cannot merge.

---

## The Vibe Coding Alternative (and Why It Fails)

**Vibe coding**: fire a prompt into an AI coding tool, review output, re-prompt until something "feels right." No contract. No explicit definition of what the feature must and must not do.

Failure modes:
- Inconsistent edge case behavior (e.g., Tamil Nadu results when user is in Telangana)
- Technical debt that accumulates silently because there's no spec to flag violations
- Every refactor or regression fix reproduces the same bugs (AI follows the implicit spec — which had no constraint on the problem)

---

## Three Maturity Levels

| Level | Definition | Practical Mode |
|---|---|---|
| **Spec-first** | Spec guides the AI workflow before code generation | Default for most teams |
| **Spec-anchored** | Spec is continuously updated as the feature evolves | Mature teams |
| **Spec-as-source** | Only the spec is ever edited by humans; code is never touched directly | Advanced / aspirational |

Most product teams operate at spec-first or spec-anchored.

---

## What a Behavioural Spec Contains

A behavioural spec defines *what* the system must do from the user's perspective and from a system-contract perspective. It does **not** prescribe implementation.

Required sections:
- **Goal statement** — one-paragraph feature objective
- **User stories** — actor + action + motivation
- **Functional requirements (FR-xx)** — numbered, traceable, testable
- **Non-functional requirements (NFR-xx)** — latency, concurrency, data retention
- **Edge cases (EC-xx)** — failure modes and required system behavior
- **Out-of-scope** — explicit exclusions

What it omits intentionally: database schema, API structure, infrastructure decisions. The AI coding agent makes those choices within the spec's constraints.

---

## The Six-Phase SDD Workflow

### 1. Strategic Alignment (Before the Spec)

Resolve: primary JTBD (pick one — they diverge in backend requirements), explicit scope boundary (what will NOT be built), success metrics (these directly inform NFRs). Output is a requirements brief, not the spec.

### 2. Write the Behavioural Spec

Requires approval from both PM and engineering lead before generation starts. This approval gate is non-negotiable.

### 3. Translate to a Design Document (Agent-Readable)

The approved spec is translated by an AI agent into a structured design document: API contracts, data schemas, confidence gates, security constraints. Every item references a spec requirement ID. Nothing left to interpretation.

### 4. Decompose into Testable Tasks

Design document → discrete, independently testable implementation units. Each task references its requirement ID. Code without a traceable requirement should not exist.

### 5. Execute Under Constraints

CI/CD embeds automated spec validation:
- Missing required field in response → hard build failure (not a code review comment)
- Query text written to a database → hard build failure
- Confidence threshold gate omitted → hard build failure

**Context fragmentation problem**: AI agents see one repository. Enterprise features span multiple repos. Workaround: inject explicit cross-repo documentation into the AI agent's context at task time.

### 6. Debug the Spec, Not the Code

When generated code is wrong, fix the specification first. Patching the code without updating the spec means the bug is reproduced on the next AI-assisted regeneration, refactor, or regression fix.

Spec-fix process:
1. Identify edge case
2. Add EC-xx (or update FR-xx) in the spec
3. Update design document
4. Update CI/CD validation check
5. AI agent regenerates affected module

---

## SDD as PM Leverage

In the traditional model, the PM writes a PRD and then spends three sprints in clarifying meetings. In SDD, the spec is the single source of truth: "Why does this behave this way?" → point to FR-07. The spec written once becomes:
- Engineering scoping document
- QA test plan
- Security review checklist
- Launch readiness criteria

The key data point: AI LLMs generate vulnerable code at rates between 9.8% and 42.1%, with a significant fraction rated Critical severity. A PM who cannot articulate exact constraints is not doing product management — they're doing product wishful thinking.

---

## Relationship to Adjacent Concepts

### SDD + AI-Native Product Orchestration

[[product-org-design/ai-native-product-orchestration]] describes the PM's workflow (Product Note → context files → generated spec → review gate → autonomous PR). SDD is the engineering discipline that makes "generated spec → autonomous PR" safe:

- Product Note + context files provide the *intent*
- The behavioural spec translates intent into *enforceable constraints*
- The executable specification makes constraint enforcement *automatic*

Together they form the complete loop: orchestration model (what the PM does) + spec discipline (how the AI operates safely).

### SDD + AI Agent Governance

[[ai-engineering/ai-agent-governance]] frames governance as "architecture of decision" — where human judgment gates remain mandatory. SDD provides a concrete governance mechanism for the code generation layer: every generated artifact is validated against a human-approved spec. The spec IS the governance artifact.

### SDD + Ontology-Driven Architecture

Both SDD and [[ai-engineering/ontology-driven-architecture]] follow the same structural principle: make semantics and constraints explicit before execution. An ontology makes domain meaning explicit for AI agents operating on data; a spec makes behavioral meaning explicit for AI agents operating on code.

### SDD + GenAI Security Workflow

[[ai-engineering/genai-security-workflow]] addresses AI security at the model/generation/deployment layer. SDD adds a pre-generation security layer: NFRs and EC-xx entries in the spec can encode security constraints (data retention, confidence thresholds, scope boundaries) that become CI/CD build failures rather than post-hoc review findings.

---

## Related Pages

- [[product-org-design/shailesh-sharma-prds-are-dead]]
- [[product-org-design/ai-native-product-orchestration]]
- [[product-org-design/shailesh-sharma-anthropic-pm-execution-collapse]]
- [[ai-engineering/ai-agent-governance]]
- [[ai-engineering/genai-security-workflow]]
- [[ai-engineering/ontology-driven-architecture]]
