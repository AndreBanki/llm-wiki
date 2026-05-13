---
title: "Topologia de Times (Team Topology)"
type: concept
created: 2026-04-22
updated: 2026-05-13
sources: [gyaco-conway-team-structure.md, How Anthropic PMs Ship Features in 45 Minutes (Without Writing PRDs).md, The Best Product Managers Don’t Talk to Customers.md]
tags: [product-management, organization-design, team-topology, marketplace]
---

# Topologia de Times (Team Topology)

How teams are structured relative to systems, users, and business strategy — and the practical consequences of each structural choice.

---

## Core Idea

Team topology is the deliberate arrangement of teams around a specific organizing principle. The choice of organizing principle (system, technology, user segment, business capability) is itself a product and strategy decision — because team structure shapes what solutions teams can see and build. See [[product-org-design/conways-law]].

---

## Organizing Principles

### System/Product-Centric (organized around a technical artifact)
- Each team "owns" a system, platform, or application.
- Teams develop deep expertise in their system.
- **Risk:** Teams solve problems within the limits of their system. Solutions outside the system's scope become invisible.
- **Common symptom:** Feature accumulation — growing backlogs of requirements that all route through one system, even when simpler cross-channel solutions exist.

### User/Actor-Centric (organized around a user segment or marketplace actor)
- Each team "owns" the experience of a specific user type.
- Teams develop deep understanding of their users' problems and goals.
- **Benefit:** Solution space is open — any channel, system, or approach that solves the user's problem qualifies.
- **Risk:** Without attention to system architecture, teams may create technical debt or overlapping systems over time.

### Capability/Outcome-Centric
- Teams organized around a business capability or outcome (e.g., "conversion," "onboarding," "retention").
- Closely related to user-centric; differs in that it explicitly ties team scope to a measurable business objective.

---

## Three-Sided Marketplace Structure (Caso Lopes)

The Lopes real estate marketplace reorganization (documented in [[product-org-design/gyaco-conway-team-structure]]) is a practical example of shifting from system-centric to user-centric topology.

### Before (System-Centric)
| Team | System Owned |
|---|---|
| Time do Portal | Property search portal |
| Time do CRM | CRM web for franchisees and brokers |
| Time do App | Broker mobile app |

**Problem:** Each team looked at its product, not at the users of the product. Lead delivery speed problem → only solution visible was a broker app with push notifications (58-requirement MVP, 90 more queued). SMS and WhatsApp were invisible.

### After (User/Actor-Centric)
| Team | User Segment Owned |
|---|---|
| Time do Cliente Final | End clients (buyers/renters) |
| Time de Incorporadoras e Proprietários | Developers and property owners |
| Time de Corretores e Franqueados | Brokers and franchisees |
| Time de Sistemas Centrais | Shared infrastructure |

**Outcome:** Reorganization completed in one week. Within one month, each team had clarity on users, problems to solve, and outcomes to generate. Teams shifted from "what feature can we add?" to "what is the best way to solve this user's problem?"

---

## Design Principles for Team Topology

1. **Strategy before architecture.** Define what needs to be built (who are the users, what problems to solve, what business outcomes to achieve) before making team structure decisions.
2. **Architecture as constraint.** System architecture is a real and important constraint — it must be considered, not ignored.
3. **Structure follows strategy and architecture, in that order.** See [[product-org-design/conways-law]] for the full principle.
4. **Cognitive load matters.** Teams must have a scope narrow enough to develop genuine expertise about their users or domain.
5. **Shared infrastructure is a valid team.** A "central systems" or platform team handles the shared technical foundation without forcing product teams to own it.

---

## AI-Native Delivery Implication

When execution latency drops (idea -> spec -> PR in under an hour), team topology still matters, but the bottleneck moves:

- From coordination overhead (handoffs, ticket decomposition, PRD rituals)
- To orchestration quality (context files, constraints, human review gates)

This raises the leverage of user-centric and outcome-centric teams. With faster implementation loops, structure quality and framing quality have even greater impact on what gets built.

Signal quality becomes a first-class constraint: user-centric teams still need disciplined synthesis of requests, behavior data, and market signals to avoid request-driven roadmap drift. See [[product-org-design/customer-signal-synthesis]].

See [[product-org-design/ai-native-product-orchestration]].

---

## Related Pages

- [[product-org-design/conways-law]]
- [[product-org-design/gyaco-conway-team-structure]]
- [[product-org-design/ai-native-product-orchestration]]
- [[product-org-design/customer-signal-synthesis]]
