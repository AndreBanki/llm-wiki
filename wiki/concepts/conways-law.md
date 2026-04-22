---
title: "Lei de Conway e Manobra Reversa de Conway"
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [gyaco-conway-team-structure.md]
tags: [product-management, organization-design, team-topology, conways-law, system-architecture]
---

# Lei de Conway e Manobra Reversa de Conway

Team communication structure and system architecture are mirror images of each other — understanding this relationship is the basis of intentional organizational design for product teams.

---

## Lei de Conway (Conway's Law)

**Origin:** Melvin Conway, "How Do Committees Invent?", *Datamation* magazine, April 1968.

**Definition:**
> "Organizations that design systems tend to produce systems that mirror the communication structures of those organizations."

In plain terms: the way you organize your teams determines the way your product will be built.

### Consequences
- Separate teams build separate systems.
- Teams with poor communication build poorly defined interfaces between their systems.
- Teams organized around technologies build products that reflect those technologies, not customer needs.
- Structure creates incentives and constraints that silently shape decisions — often without anyone noticing.
- **When structure is wrong, it works silently against strategy.**

### The Visibility Problem
A team organized around a specific product or system can only see solutions within that system's scope. An engineer on a broker app team will naturally solve problems by adding features to the broker app — not because they lack creativity, but because that's what falls within their operational boundaries.

**The Lopes case:** A team tasked with getting leads to brokers faster built an MVP with 58 requirements for a broker app (with 90 more queued). SMS and WhatsApp — simpler, faster, and with far higher penetration in Brazil — were invisible because they fell outside the app team's scope. See [[gyaco-conway-team-structure]].

---

## Manobra Reversa de Conway (Reverse Conway Maneuver)

**Concept:** If Conway's Law describes how structure shapes the product, the Reverse Conway Maneuver proposes inverting the logic. Instead of letting team structure emerge organically and observing what product it produces, you:
1. Define the desired system architecture first.
2. Organize teams to reflect that desired architecture.

Team structure becomes a **system design decision**, not an accidental consequence.

**Example application:** If you want well-defined microservices, create teams that correspond to those services. If you want certain parts of the system to evolve independently, create teams that can work independently.

### The Limitation
The Reverse Conway Maneuver starts from an incomplete assumption: **system architecture is important, but it is not the only factor that should determine how teams organize.**

The question "what system architecture do we want?" is a legitimate technical question — but it can only be answered well *after* answering the more fundamental question:

> "Who are our users, what problems do we need to solve for them, and what are our business objectives?"

The inverse is also problematic: organizing purely around users and business objectives while ignoring system architecture will eventually hit hard technical constraints that are difficult to overcome.

---

## The Synthesis: Structure Must Follow Strategy and Architecture

**Principle:** *"Estrutura deve seguir estratégia e arquitetura, nessa ordem."*
(Structure must follow strategy and architecture, in that order.)

- Team structure must reflect **both** the desired system architecture **and** the logic of value creation for users and the business.
- When both factors are aligned, structure works in favor of strategy.
- When only one is considered, structure continues working silently against strategy.

### Product-Centric vs. User-Centric Teams

| Dimension | Product/System-Centric | User-Centric |
|---|---|---|
| Team organized around | A system or technology | A user segment or marketplace actor |
| Problem-solving reflex | Add features to the existing system | Find the best way to solve the user's problem |
| Solution space | Bounded by the system's scope | Open — any channel or approach qualifies |
| Risk | Builds technically elegant solutions that miss user needs | May accumulate technical debt if architecture is ignored |

**Key insight:** When the focus is the product, the only way to solve problems is by adding features to the product. When the focus is the user and the expected outcome, the solution space opens up.

---

## Related Pages

- [[gyaco-conway-team-structure]]
- [[team-topology]]
- [[conversation-design]] — parallel insight: the framing of the question determines the solution space
