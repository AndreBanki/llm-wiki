---
title: System Design Approach
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [shivambhadani-system-design-for-beginners]
tags: [system-design, software-engineering, interviews, scaling, microservices, load-balancer]
---

A framework for decomposing and solving system design problems, plus the foundational scaling concepts that apply to nearly every architecture decision.

## Problem-Solving Framework

When given any system design problem:

1. **Understand the problem statement** — what features, what scale, what constraints?
2. **Decompose into sub-problems** — e.g., an e-commerce app → product listing + search + ordering + payment
3. **For each sub-problem, decide across 4 dimensions:**
   - **Database** — which type? which scaling approach?
   - **Caching** — where? what TTL? what invalidation strategy?
   - **Scaling & Fault Tolerance** — vertical, horizontal, auto-scaling, redundancy
   - **Communication** — synchronous (REST/API) or asynchronous (message broker)?

> Only create sub-sub-problems when genuinely needed. Over-decomposition adds complexity without value.

## Back-of-the-Envelope Estimation

Spend ~5 minutes at the start of any design to estimate:

- **Load estimation**: DAU × reads per user = read RPS; DAU × writes per user = write RPS
- **Storage estimation**: (size per record × write volume) + (size per media item × fraction with media)
- **Resource estimation**: (RPS × processing time per request) / (processing capacity per core) = cores needed → servers needed

**Key powers of 2 / 10:**

| Short | Value | Power of 2 | Power of 10 |
|---|---|---|---|
| 1 KB | 1 Thousand bytes | 2¹⁰ | 10³ |
| 1 MB | 1 Million bytes | 2²⁰ | 10⁶ |
| 1 GB | 1 Billion bytes | 2³⁰ | 10⁹ |
| 1 TB | 1 Trillion bytes | 2⁴⁰ | 10¹² |
| 1 PB | 1 Quadrillion bytes | 2⁵⁰ | 10¹⁵ |

## Scaling Fundamentals

**Vertical scaling** — increase specs (RAM, CPU, storage) of a single machine. Simple; preferred for SQL databases and stateful apps. Hits a hardware ceiling.

**Horizontal scaling** — add more machines; distribute load via a load balancer. Used in most production systems. Requires stateless application servers.

**Auto-scaling** — dynamically adjust instance count based on a CPU/load threshold. Avoids over-provisioning during low-traffic periods.

## Load Balancer Algorithms

| Algorithm | How It Works | Best For |
|---|---|---|
| Round Robin | Requests distributed sequentially in order | Servers with equal capacity |
| Weighted Round Robin | Servers get more/fewer requests based on their weight | Servers with unequal capacity |
| Least Connections | Route to the server with fewest active connections | Variable-duration requests |
| Hash-Based | Hash client IP or user ID → consistent server assignment | Session persistence |

## Microservices vs Monolith

| Aspect | Monolith | Microservices |
|---|---|---|
| Team size | Small (2–3 engineers) | Multiple teams |
| Independent scaling | No — whole app scales together | Yes — per service |
| Tech stack flexibility | No — one language/framework | Yes — per service |
| Failure isolation | No — one crash affects all | Yes — one service down, others unaffected |
| When to start | Early-stage startups | When team count / complexity grows |

**Microservices + API Gateway**: All client requests go to a single API Gateway endpoint, which routes to the appropriate microservice. The gateway also handles rate limiting, caching, auth, and SSL termination.

> "Microservices of any startup defines its internal team structure." — directly mirrors Conway's Law. → [[product-org-design/conways-law]]

## Related Pages

- [[software-engineering/cap-theorem-and-consistency]]
- [[software-engineering/database-scaling]]
- [[software-engineering/messaging-and-events]]
- [[software-engineering/caching-cdn-proxy]]
- [[software-engineering/distributed-systems]]
- [[product-org-design/conways-law]]
- [[software-engineering/shivambhadani-system-design-for-beginners]] *(source)*
