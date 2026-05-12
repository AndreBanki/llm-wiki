---
title: "PRDs are Dead"
source: "https://shailesh-sharma.medium.com/spec-driven-development-for-product-managers-8b5231d206b7"
author:
  - "[[Shailesh Sharma]]"
published: 2026-03-29
created: 2026-05-12
description: "Here is what comes next"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Q48ODJjIMT9uMlhklJtZRw.png)

## Here is what comes next

You are a Senior Product Manager at Google Maps.

Your VP walks into your Monday standup and says three words: “Build Ask Maps.”

What is “Ask Maps”: Users can type or speak a natural language query directly into Maps and get intelligent, context-aware answers. “Find me a rooftop restaurant near Koramangala that’s open after 10 PM and has good reviews for cocktails.” No filters. No manual search. Just ask.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*vBvfjaMtb9GaaQh7.gif)

Everyone in the room is excited. The engineers want to start prototyping immediately. Someone has already opened Cursor.

> *And this is exactly where most AI-era product development goes wrong.*

Because what happens next is what the industry has started calling “vibe coding.” Someone fires a prompt into an AI coding tool.

The tool generates a working prototype in 20 minutes. Everyone is impressed. The demo looks great.

*Three sprints later, the codebase is a mess, the AI feature behaves inconsistently across edge cases, and no one can explain why it sometimes returns results in Tamil Nadu when the user is searching in Telangana.*

> Spec-driven development is the structured alternative.

And in this article, I want to walk you through exactly what it looks like: not in abstract terms, but through the Ask Maps feature, end to end.

Before we go deep into Spec Driven Development, you can find out our articles on the following

1. [Uber’s AI Strategy](https://www.technomanagers.com/p/uber-autonomous-vehicle-strategy)
2. [Memory in AI](https://www.technomanagers.com/p/memory-in-ai-part-1)
3. [Spotify’s AI Strategy](https://www.technomanagers.com/p/spotifys-ai-strategy)

## What Spec-Driven Development Actually Is?

Spec-driven development (SDD) is a methodology where you write a formal, machine-readable specification before any code is generated.

==This specification defines the behaviour, constraints, success criteria, and edge cases for a feature. The AI coding agent then generates code that must satisfy the spec. If the generated code does not meet the spec, the build fails automatically.==

This is different from how most teams use AI tools today.

In the traditional AI-assisted workflow, a developer writes a prompt, the AI generates code, the developer reviews it, finds gaps, re-prompts, and this cycle repeats until something “feels right.”

There is no contract. There is no explicit definition of what the feature must and must not do. The AI guesses. The developer hopes. Technical debt accumulates silently.

SDD flips this. You start with the contract. You define what Ask Maps must do before you decide how it should be built. The code is a downstream artefact of the spec, not a starting point.

Three levels of SDD exist: spec-first (the spec guides the AI workflow), spec-anchored (the spec is continuously updated as the feature evolves), and spec-as-source (only the spec is ever edited by humans, never the code directly). For most product teams, spec-first or spec-anchored is the practical operating mode.

Now, let us apply this to Ask Maps, step by step.

## Phase 1: Strategic Alignment Before Writing Anything

Most PMs think the spec is the first output of the discovery process. It is not. The first output is alignment with what you are actually building.

Before anyone writes a spec for Ask Maps, the product team needs to resolve a set of foundational questions. These are not design questions. These are strategy questions.

### What is the primary job to be done?

Ask Maps could solve multiple problems. It could be a discovery tool (help users find places they did not know existed). It could be a planning tool (help users build a full day itinerary). It could be a real-time assistant (give live, context-aware answers based on current traffic, weather, and availability).

These are three different features. They share a surface but diverge completely in their backend requirements, data dependencies, and success metrics.

At Google Maps, this decision has massive downstream consequences. A discovery-focused Ask Maps integrates deeply with Google’s restaurant and business index. A planning tool needs multi-stop optimisation logic. A real-time assistant needs live data pipelines for weather, traffic, and business hours APIs.

The team needs to pick one primary job. Everything else is scope creep.

### What is the explicit scope boundary?

What will Ask Maps not do? This is equally important as what it will do. Will it handle transactional requests (”book a table at this restaurant”)? Or is it purely informational? Will it work offline? Will it support voice input at launch? What languages will it support on day one?

Scope boundaries are not limitations. They are the spec’s load-bearing walls.

### What are the success metrics?

Before a single line of spec is written, the team defines what success looks like. For Ask Maps, this might be: query satisfaction rate above 80% (user rates the answer as helpful), mean response latency under 2 seconds, and a 15% increase in session length compared to the current Maps search flow.

These numbers are not arbitrary. They will directly inform the non-functional requirements in the spec later.

### Practical SDD tool behaviour at this stage:

In tools like Agent OS, this phase is handled by a “spec researcher” sub-agent. It ingests your product brief and roadmap, then surfaces clarifying questions with suggested default answers.

The PM does not write long paragraphs in response. They respond with “yes” or minor corrections. The agent synthesises the answers into a structured requirements brief.

For Ask Maps, the output of this phase is something like:

- Primary job: Place discovery through natural language
- Scope: Informational only, no transactions, English-first
- Input modes: Text and voice
- Success metric: Query satisfaction above 80%, P99 latency under 2 seconds
- Out of scope for v1: Itinerary building, multi-stop optimisation, transactional bookings

This is not the spec. This is the raw material for the spec.

## Phase 2: Writing the Ask Maps Specification

Now the spec is written. And this is where SDD requires discipline, because the instinct is to write a technical spec. SDD requires a behavioural spec.

A behavioural spec defines what the system must do and how it must behave from the user’s perspective and from a system contract perspective. It does not prescribe the implementation.

Here is what the Ask Maps spec looks like:

### Feature: Ask Maps Version: 1.0 Owner: \[PM Name\] Last updated: \[Date\]

**Goal:** Enable Google Maps users to discover places and get location-aware answers through natural language queries, without using traditional filter-based search.

### User Stories:

1. As a Maps user, I want to ask a natural language question about places near me, so that I can discover options I would not find through manual filters.
2. As a Maps user, I want to ask follow-up questions in the same session without re-entering my original context, so that I can refine my search conversationally.
3. As a Maps user, I want Ask Maps to consider my current location, time of day, and day of week automatically, so that I get contextually relevant answers without explicitly stating these.

### Functional Requirements:

1. FR-01: The system must accept natural language queries of up to 500 characters via text input.
2. FR-02: The system must accept voice input and convert it to text before processing.
3. FR-03: The system must use the user’s current GPS-confirmed location as the default geographic context for all queries.
4. FR-04: The system must return a minimum of 3 and a maximum of 10 place results per query.
5. FR-05: Each result must include: place name, distance from user, rating, a one-line AI-generated reason for the recommendation, and a direct CTA to navigate.
6. FR-06: The system must support follow-up queries within the same session, preserving the context of the initial query.
7. FR-07: If the system cannot find relevant results with confidence above 0.75, it must surface a “limited results” state rather than hallucinating low-quality matches.

### Non-Functional Requirements:

1. NFR-01: P50 response latency must be under 1 second. P99 must be under 2 seconds.
2. NFR-02: The system must handle a minimum of 10,000 concurrent queries.
3. NFR-03: The AI recommendation layer must not surface results from businesses that have a Google rating below 3.5 unless explicitly asked by the user.
4. NFR-04: The system must not store the user’s query text beyond the active session without explicit consent.

### Edge Cases and Failure Modes:

1. EC-01: User is in a location with no GPS signal. The system must prompt the user to manually enter a location rather than defaulting to a stale cached location.
2. EC-02: User queries a category with no matches within a 10km radius. The system must expand the radius to 25km and inform the user of this expansion.
3. EC-03: Query contains a language other than English. V1 must return a graceful “English only” message. V2 will address multi-language support.
4. EC-04: Query is ambiguous (for example, “good food near me”). The system must ask one clarifying question before returning results, not make an assumption.

### Out of Scope:

- Transactional bookings (restaurant reservations, ride bookings)
- Multi-stop itinerary planning
- Queries not related to physical places (for example, “what is the capital of France”)

Notice what this spec does not contain: no database schema, no API structure, no infrastructure decisions. Those are implementation choices. The spec is silent on them intentionally. The AI coding agent gets to make those decisions within the constraints of the spec. The spec defines what must be true. The implementation decides how.

## Phase 3: The Design Document

The spec is human-readable. The design document is agent-readable.

Once the spec is approved (and this approval step is non-negotiable in SDD, the PM and engineering lead both sign off before any code is generated), the AI agent translates the spec into a structured design document.

This document contains:

### API Contract (from FR-01, FR-02, FR-04):

The Ask Maps endpoint accepts POST requests.

Input schema:

- query (string, required, max 500 characters): The natural language query
- location (object, required): Contains lat (float) and lng (float) from GPS
- session\_id (string, optional): For follow-up query context preservation (FR-06)
- input\_mode (enum: “text” | “voice”, required)

Output schema:

- results (array, min 3, max 10): Each object contains place\_id, name, distance\_km, rating, ai\_reason, navigate\_url
- state (enum: “success” | “limited\_results” | “clarification\_needed” | “error”)
- clarification\_question (string, nullable): Populated only when state is “clarification\_needed”

### Confidence Gate (from FR-07):

The AI recommendation layer must include a confidence score per result. Results with confidence below 0.75 are excluded from the final output array. If this exclusion brings the total results below 3, the system sets the state to “limited\_results” and returns whatever results passed the threshold.

### Radius Expansion Logic (from EC-02):

Initial query radius: 10km. If the results count is below 3 after confidence filtering, expand to 25km. Append a `radius_expanded: true` boolean to the response object. The UI layer uses this flag to surface the “We expanded your search area” message.

### Security Constraints (from NFR-04):

Query text must not be written to any persistent store. Session data lives in ephemeral cache only, with a TTL of 30 minutes.

This design document becomes the to-do list for the AI coding agent. Each requirement maps to a specific implementation task. Nothing is left to interpretation.

## Phase 4: Breaking It Into Testable Tasks

In SDD, the design document is decomposed into discrete, independently testable implementation units. This is where the workflow starts looking like traditional engineering project management, except that AI agents are executing the tasks, not humans writing the code from scratch.

For Ask Maps, the task breakdown looks like this:

### Task Group A: Core API Layer

- A1: Implement the POST /ask-maps endpoint with input validation (FR-01, FR-02)
- A2: Implement GPS location ingestion and validation. Fail gracefully if coordinates are malformed (EC-01)
- A3: Implement session management with 30-minute ephemeral TTL (NFR-04, FR-06)

### Task Group B: AI Recommendation Engine

- B1: Integrate with Google Places API for candidate place retrieval
- B2: Implement confidence scoring model with 0.75 threshold gate (FR-07)
- B3: Implement radius expansion logic: 10km base, expand to 25km with flag (EC-02)
- B4: Generate AI-written one-line reasons per result using the LLM layer

### Task Group C: Edge Case Handling

- C1: Implement ambiguity detection. If query is flagged as ambiguous, return clarification question instead of results (EC-04)
- C2: Implement rating filter: exclude results with Google rating below 3.5 from candidate pool (NFR-03)
- C3: Implement “English only” language detection for V1 (EC-03)

### Task Group D: Non-Functional Requirements

- D1: Load test to confirm P99 latency under 2 seconds at 10,000 concurrent queries (NFR-01, NFR-02)
- D2: Security audit on query storage to confirm no persistent writes (NFR-04)

Each task has a direct reference back to a specific requirement in the spec. This is the core discipline of SDD. You can always trace any line of code back to a business requirement. If you cannot, that code should not exist.

## Phase 5: Execution Under Constraints

The AI coding agent now generates code. But this is not vibe coding with a spec document sitting nearby. The spec is an active constraint.

In practice, this means:

The CI/CD pipeline has automated spec validation checks embedded.

If the AI agent generates code for the Ask Maps endpoint that does not include the confidence threshold gate, the build fails. Not a code review comment. A hard build failure.

If the agent generates a response schema that returns results without the ai\_reason field, the build fails. Because FR-05 explicitly mandates it.

If the agent writes query text to a database table (even a logging table), the build fails. Because NFR-04 says it cannot.

This is what “executable specification” means. The spec is not a document someone reads. It is a contract that the system enforces.

One critical challenge at this phase is what practitioners call context fragmentation. Most AI coding tools understand a single repository. But Google Maps is not a single repository.

The Ask Maps feature will touch the core Maps search service, the Places API integration layer, the user session service, the UI component library, and the AI/ML serving infrastructure. These live in different codebases, owned by different teams.

If the AI agent only sees one of these repositories, it will generate code that is locally correct but architecturally inconsistent. It will reinvent session management that already exists in the session service. It will create a new confidence scoring library instead of using the existing ML inference wrapper.

> *This is why enterprise SDD needs a context engine that maps semantic dependencies across repositories.*

For a team without access to enterprise tooling, the practical workaround is explicit cross-repo documentation injected into the AI agent’s context at task time.

## Phase 6: Debugging the Spec, Not Just the Code

This is the phase most PMs never hear about, and it is arguably the most important.

In SDD, when the AI generates code that is wrong, you do not fix the code directly. You fix the specification.

Here is why: AI code generation is non-deterministic. If you fix a bug in the generated code without updating the spec, the next time you regenerate (for a refactor, a new feature, or a regression fix), the AI will reproduce the exact same bug. It is following the spec. The spec said nothing about this case. So the AI guessed.

Concretely: Imagine the Ask Maps agent generates code that sometimes returns results from a different city when the user is near a city boundary. The radius expansion logic triggered, expanded to 25km, and pulled in results from an adjacent city without informing the user.

In vibe coding, a developer patches this edge case in the code and moves on.

In SDD, the PM goes back to the spec, adds a new edge case:

EC-05: When radius expansion crosses an administrative city boundary, the system must segment results by city and surface a separator in the UI indicating “Results from \[adjacent city\]”.

The spec is updated. The design document is updated. The CI/CD validation check is updated. The AI agent regenerates the affected module. The fix propagates correctly and permanently.

This is the compounding benefit of SDD. Every bug you find and fix in the spec makes the entire feature more robust, not just the one line of code that was wrong.

## Why This Matters for Product Managers Specifically

SDD is not just an engineering methodology. It is a PM leverage tool.

In the traditional development model, the PM writes a PRD, hands it to engineering, and then spends the next three sprints in spec review meetings clarifying requirements that were ambiguous in the document. The PM is a translator, repeatedly.

In SDD, the spec is the single source of truth that both the PM and the AI agent operate from. When engineering asks, “Why does the endpoint behave this way?” the answer is always FR-07 or NFR-03. Not “I think I mentioned it in the PRD somewhere.” The spec is precise. The behaviour is traceable.

For PMs building AI-powered features specifically, this precision is not optional. Research shows AI LLMs generate vulnerable code at rates between 9.8% and 42.1%, and a significant fraction of those vulnerabilities are rated Critical severity.

> *A PM who cannot articulate the exact constraints their AI feature must operate within is not doing product management. They are doing product wishful thinking.*

SDD forces PMs to be specific. That specificity is the PM’s highest-leverage contribution in an AI-first development environment.

## The Learning Curve Is Real, But It Pays Off

When I first started working through SDD workflows, the upfront planning phase felt slow. Writing behavioural requirements instead of just describing the feature in prose felt overly formal. Defining edge cases before writing a single line of code felt premature.

Three sprints in, the compounding became obvious. The Ask Maps spec, once written, became the source for the engineering scoping document, the QA test plan, the security review checklist, and the launch readiness criteria. The spec was written once and used six times. Every clarifying question in sprint planning was answerable by pointing to a requirement ID.

The slow part upfront makes everything downstream faster.

## Where to Go From Here

AI Product Management is the future; you can keep ignoring but this will become the baseline in 8 to 14 Months.

You should take action to kill the anxiety — Start today only, Learn about AI Product Management, start from basics to Advance with the Flagship AI PM Course.

You can also check out our **Highest rated AI PM course · 4.9/5 · 500+ enrollments →** [**See testimonials and course details**](https://topmate.io/technomanagers/1861184)

## About Author

[*Shailesh Sharma*](https://www.linkedin.com/in/shailesh-sharma/)*! I help PMs and business leaders excel in Product, Strategy, and AI using First Principles Thinking. For more, check out my* [*AI Product Management Course*](https://topmate.io/technomanagers/1861184)*,* [*PM Interview Mastery Course*](https://topmate.io/technomanagers/1470531)*,* [*Cracking Strategy*](https://topmate.io/technomanagers/1472775)*, and* [*other Resources*](https://topmate.io/technomanagers)