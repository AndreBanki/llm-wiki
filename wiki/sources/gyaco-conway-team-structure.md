---
title: "Como a estrutura de time molda o seu produto"
type: source
created: 2026-04-22
updated: 2026-04-22
sources: []
tags: [product-management, team-topology, conways-law, organization-design, marketplace]
---

# Como a estrutura de time molda o seu produto

Article by Joca Torres (Gyaco), published April 21, 2026.

---

## Metadata

| Field | Value |
|---|---|
| Author | Joca Torres (Gyaco) |
| Published | 2026-04-21 |
| URL | https://www.gyaco.com/pt/2026/04/21/como-a-estrutura-de-time-molda-o-seu-produto |
| Language | Portuguese (BR) |
| Format | Article / blog post |
| Domain | Product management, organizational design |

---

## Summary

Team structure inevitably shapes the product a team builds — a reality described by Conway's Law. The Reverse Conway Maneuver (start with the desired system architecture and organize teams to reflect it) is a valid but incomplete tool: it ignores users and business strategy. The author presents a case study at Lopes (real estate marketplace) where teams organized around technical systems were blind to simpler, more effective solutions because those solutions fell outside their system's scope.

**Central principle:** *"Estrutura deve seguir estratégia e arquitetura, nessa ordem."* (Structure must follow strategy and architecture, in that order.)

---

## Key Facts and Arguments

### Lei de Conway (Conway's Law)
- First published in *Datamation* magazine, April 1968, by Melvin Conway ("How Do Committees Invent?")
- **Definition:** "Organizations that design systems tend to produce systems that mirror the communication structures of those organizations."
- Consequence: separate teams build separate systems; teams that communicate poorly build poorly defined interfaces; teams organized around technologies build products that reflect those technologies rather than customer needs.
- Structure creates incentives and constraints that silently shape decisions.
- When structure is wrong, it works silently against strategy.

### Manobra Reversa de Conway (Reverse Conway Maneuver)
- Proposes inverting the logic: define the desired system architecture first, then organize teams to reflect that desired architecture.
- Team structure becomes a system design decision, not an accidental consequence.
- **Critique:** Valid and powerful, but starts from an incomplete assumption — it answers a technical question ("what architecture do we want?") before answering the more fundamental question: "who are our users, what problems do we need to solve for them, and what are our business objectives?"
- The inverse is also problematic: ignoring system architecture in favor of pure user/business focus will eventually hit hard technical constraints.

### O Problema da Estrutura por Sistema (System-Centric Team Problem)
- When a team is organized around a product/system, the only way it sees to solve problems is by adding features to that product.
- Engineers solve problems within the limits of their domain — not because they lack creativity, but because of structural incentives.
- Teams organized around systems look at their product, not at the users of the product.

### Estudo de Caso: Lopes
- Lopes is a three-sided real estate marketplace: end clients (buyers/renters) ↔ developers/owners (sellers/landlords) ↔ brokers/franchisees (intermediaries).
- **Before:** Three product-oriented teams — Portal de Busca, CRM web, App dos Corretores.
- **Problem:** The main objective was to get leads to brokers as fast as possible (speed = higher conversion). The team's solution: a broker app with push notifications — **58 defined requirements for an MVP, with 90 more queued.**
- **Root cause:** Organized around the app → every solution went through the app. Simpler options (SMS, WhatsApp — far higher penetration in Brazil) were outside the team's field of vision.
- **After:** Reorganized around marketplace actors — time do Cliente Final, time de Incorporadoras e Proprietários, time de Corretores e Franqueados, time de Sistemas Centrais.
- **Result:** Reorganization done in one week. Within one month, each team had clarity on their users, their problems, and the outcomes they should generate. Teams stopped thinking about features to add to existing systems and started thinking about problems to solve for specific users.

### Princípio Final
> "Estrutura deve seguir estratégia e arquitetura, nessa ordem. A arquitetura de sistemas é uma restrição importante. Mas a estratégia define o que precisa ser construído antes de qualquer decisão técnica."

---

## Key Quotes

> "As organizações que projetam sistemas de software tendem a produzir sistemas que espelham as estruturas de comunicação dessas organizações." — Melvin Conway

> "Quando a estrutura está errada, ela trabalha silenciosamente contra a estratégia."

> "Quando o foco é o produto, a única forma de resolver problemas é adicionando funcionalidades ao produto. Quando o foco é o usuário e o resultado esperado, o espaço de soluções se abre."

> "Estrutura deve seguir estratégia e arquitetura, nessa ordem."

---

## Related Pages

- [[conways-law]]
- [[team-topology]]
- [[conversation-design]] — parallel insight: framing the question determines the solution space
