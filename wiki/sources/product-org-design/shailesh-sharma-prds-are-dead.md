---
title: "PRDs are Dead — Spec-Driven Development for Product Managers"
type: source
created: 2026-05-12
updated: 2026-05-12
sources: ["PRDs are Dead.md"]
tags: [product-management, ai-product-management, spec-driven-development, vibe-coding, behavioral-spec, executable-specification]
---

A practitioner walkthrough of Spec-Driven Development (SDD) applied end-to-end to the "Ask Maps" feature for Google Maps — the structured alternative to vibe coding in the AI era.

---

## Metadata

| Field | Value |
|---|---|
| Author | Shailesh Sharma |
| Published | 2026-03-29 |
| URL | https://shailesh-sharma.medium.com/spec-driven-development-for-product-managers-8b5231d206b7 |
| Language | English |
| Format | Web clip / Medium article |
| Domain | Product management, AI-enabled delivery |

---

## Summary

The article diagnoses "vibe coding" — firing prompts into AI coding tools without formal specifications — as the primary failure mode of AI-era product development. The proposed alternative is Spec-Driven Development: write a formal, machine-readable specification *before* any code is generated, and embed it as an executable contract in the CI/CD pipeline.

The full argument is illustrated through a fictional but detailed "Ask Maps" feature build, walking through six phases from strategic alignment to spec debugging. The author's central claim: in an AI-first development environment, the PM's highest-leverage contribution is precise specification — not documentation, not sprint choreography.

---

## The Vibe Coding Problem

Without a spec contract:
- AI coding tools generate plausible code in minutes
- No definition of what the feature must and must not do
- Technical debt accumulates silently
- Bugs regenerated on every AI-assisted refactor (AI "follows the spec; the spec said nothing about this case")

---

## The Three Levels of SDD

| Level | Definition | Practical Mode |
|---|---|---|
| Spec-first | Spec guides the AI workflow | Yes (default for most teams) |
| Spec-anchored | Spec continuously updated as feature evolves | Yes (mature teams) |
| Spec-as-source | Only spec is ever edited by humans; code is never touched directly | Advanced/aspirational |

---

## Six Phases (Applied to "Ask Maps")

### Phase 1: Strategic Alignment Before Writing Anything

Resolve foundational strategy questions before the spec:
- **Primary JTBD**: pick one (discovery vs. planning vs. real-time assistant — each has different backend dependencies)
- **Explicit scope boundary**: what will it NOT do?
- **Success metrics**: numbers that will directly inform non-functional requirements

Tool behaviour: a "spec researcher" sub-agent ingests the product brief and surfaces clarifying questions. PM responds with yes/corrections. Output is a requirements brief, not the spec.

### Phase 2: Writing the Behavioural Spec

Key discipline: write a **behavioural spec**, not a technical spec.
- Defines what the system must do and how it must behave from user and system-contract perspectives
- Does NOT prescribe database schema, API structure, or infrastructure decisions
- AI coding agent makes implementation choices *within* the spec's constraints

Example Ask Maps spec structure:
- Goal statement
- User stories (3 actors)
- Functional requirements (FR-01 to FR-07) — numbered for traceability
- Non-functional requirements (NFR-01 to NFR-04)
- Edge cases (EC-01 to EC-04)
- Out-of-scope list

**Approval is non-negotiable**: PM and engineering lead both sign off before any code is generated.

### Phase 3: The Design Document

Agent-readable translation of the human-readable spec.

Contains:
- API contract (derived from FR references)
- Data schemas (input/output)
- Confidence gate implementation (from FR-07)
- Radius expansion logic (from EC-02)
- Security constraints (from NFR-04)

Each requirement maps to a specific implementation task. Nothing left to interpretation.

### Phase 4: Breaking Into Testable Tasks

Design document → discrete, independently testable implementation units.

Four task groups for Ask Maps:
- **A (Core API Layer)**: endpoint, GPS validation, session management
- **B (AI Recommendation Engine)**: Places API, confidence scoring, radius expansion, one-line reasons
- **C (Edge Case Handling)**: ambiguity detection, rating filter, language detection
- **D (Non-Functional)**: load test, security audit

Every task references the specific requirement ID it satisfies. Code without a traceable requirement should not exist.

### Phase 5: Execution Under Constraints

CI/CD pipeline has automated spec validation checks:
- Missing confidence threshold gate → build fails (not a code review comment)
- Response schema without required field → build fails (per FR-05)
- Query text written to any persistent store → build fails (per NFR-04)

**Context fragmentation challenge**: AI agents only see one repository; enterprise features span multiple repos (Maps search, Places API, session service, UI library, ML serving). Workaround: explicit cross-repo documentation injected into the AI agent's context at task time.

### Phase 6: Debugging the Spec, Not the Code

When AI-generated code is wrong, fix the specification, not the code.

**Why**: AI code generation is non-deterministic. Patching the code directly means the same bug is reproduced on the next AI regeneration. Patching the spec propagates the fix permanently.

Process:
1. Find the edge case
2. Add it to the spec (e.g., EC-05: radius expansion across city boundaries)
3. Update design document and CI/CD validation
4. AI agent regenerates affected module

Compounding benefit: every spec fix makes the entire feature more robust, not just the one line.

---

## Why This Matters for PMs Specifically

- In traditional development: PM writes PRD, then spends three sprints clarifying ambiguities
- In SDD: spec is single source of truth; "Why does the endpoint behave this way?" answered by requirement ID, not "I think I mentioned it in the PRD somewhere"
- PM precision is not optional when AI generates vulnerable code at 9.8–42.1% rates (with a significant Critical severity fraction)
- The spec written once is used as: engineering scoping document, QA test plan, security review checklist, and launch readiness criteria

> "A PM who cannot articulate the exact constraints their AI feature must operate within is not doing product management. They are doing product wishful thinking."

---

## Key Terms Introduced

- **Spec-Driven Development (SDD)** — see [[product-org-design/spec-driven-development]]
- **Vibe Coding** — AI-assisted dev without a formal spec; see [[glossary]]
- **Behavioural Spec** — what the system must do, not how; see [[glossary]]
- **Executable Specification** — spec enforced as CI/CD hard failures; see [[glossary]]
- **Context Fragmentation** — AI agent sees only one repo in multi-repo enterprise; see [[glossary]]

---

## What This Adds to the Wiki

- Provides the engineering methodology that makes [[product-org-design/ai-native-product-orchestration]] robust and repeatable
- Fills the "how do you generate a reliable spec" gap in the orchestration model
- Adds a concrete governance mechanism for AI code quality — complementing [[ai-engineering/ai-agent-governance]] and [[ai-engineering/genai-security-workflow]]
- Forms a pair with [[product-org-design/shailesh-sharma-anthropic-pm-execution-collapse]]: that article describes the PM's orchestration workflow; this describes the spec discipline that makes autonomous execution safe

---

## Related Pages

- [[product-org-design/spec-driven-development]]
- [[product-org-design/ai-native-product-orchestration]]
- [[product-org-design/shailesh-sharma-anthropic-pm-execution-collapse]]
- [[ai-engineering/ai-agent-governance]]
- [[ai-engineering/genai-security-workflow]]
