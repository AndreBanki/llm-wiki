---
title: "System Design For Beginners: Everything You Need in One Article"
type: source
created: 2026-04-22
updated: 2026-04-22
sources: [shivambhadani-system-design-for-beginners]
tags: [system-design, software-engineering, distributed-systems, databases, caching, messaging, scalability, interviews]
---

A comprehensive beginner-to-intermediate survey of 26 system design concepts by Shivam Bhadani, structured for software engineering interview preparation. Theory is paired with practical implementation exercises (NodeJS code, AWS labs).

## Metadata

| Field | Value |
|---|---|
| Author | Shivam Bhadani (@shivambhadani_) |
| Published | December 21, 2024 |
| URL | https://medium.com/@shivambhadani_/system-design-for-beginners-everything-you-need-in-one-article-c74eb702540b |
| Format | Medium article (~60 min read) |
| Domain | Software Engineering / System Design |

## Core Thesis

Any system design problem can be decomposed into sub-problems. For each sub-problem, make decisions across four dimensions:

1. **Database** — which type, which scaling approach
2. **Caching** — where, how, with what invalidation strategy
3. **Scaling & Fault Tolerance** — vertical, horizontal, auto, redundancy
4. **Communication** — synchronous (REST) vs asynchronous (message broker)

## Topics Covered

| # | Topic | Key Concept |
|---|---|---|
| 1 | Servers & DNS | IP → port → deployment → cloud providers (EC2) |
| 2 | Latency & Throughput | RTT; requests/sec; optimize both |
| 3 | Scaling | Vertical (specs ↑) vs horizontal (machines ↑) |
| 4 | Auto Scaling | Dynamic instance count based on CPU threshold |
| 5 | Back-of-the-envelope | Load, storage, resource estimation |
| 6 | CAP Theorem | C/A/P; always choose CP or AP (not CAP) |
| 7 | Database Scaling | Indexing → partitioning → master-slave → sharding |
| 8 | SQL vs NoSQL | ACID vs flexible schema; vertical vs horizontal scale |
| 9 | Microservices | Independent services + API Gateway |
| 10 | Load Balancer | Round Robin, Weighted, Least Connections, Hash-Based |
| 11 | Caching | Redis deep dive; TTL; cache hit/miss; invalidation |
| 12 | Blob Storage | AWS S3; binary large objects; managed storage |
| 13 | CDN | Edge servers; GeoDNS; origin vs edge; TTL |
| 14 | Message Broker | Queue vs stream; producer/consumer; retry/decoupling |
| 15 | Apache Kafka | Topics, partitions, consumer groups, rebalancing |
| 16 | Realtime Pub/Sub | Push model (vs broker pull); Redis Pub/Sub |
| 17 | Event-Driven Architecture | Simple notification vs event-carried state transfer |
| 18 | Distributed Systems | Coordinator/worker; leader election; client sees one machine |
| 19 | Auto-Recoverable Systems | Orchestrator + leader election; no human intervention |
| 20 | Big Data Tools | Apache Spark; distributed computation |
| 21 | Consistency Deep Dive | Strong vs eventual; quorum (W+R>N); gossip protocol |
| 22 | Consistent Hashing | Ring-based key routing; minimal data movement on resize |
| 23 | Data Redundancy | Main + replica; continuous replication; failover |
| 24 | Proxy | Forward (hides client) vs reverse (hides server) |
| 25 | Problem-Solving Framework | Decompose → 4 dimensions per sub-problem |

## Key Quotes

> "Most startups start with a monolith because, at the starting point, only 2–3 people work on the tech side, but it eventually moves to microservice when no. of teams increases."

> "Consistent hashing is just an algorithm that tells which key belongs to which node."

> "The most challenging part of a distributed system is how multiple machines coordinate with each other to do the task."

> "Sharding is a very complex thing. Try to avoid this in practical life and only do this when all the above things are not sufficient."

## Cross-Domain Connections

- **Conway's Law**: "Microservices of any startup defines its internal team structure." — directly reinforces [[product-org-design/conways-law]]
- **Vectorless RAG / PageIndex**: Consistent hashing uses a hash ring to route keys without brute-force search — structurally similar to how PageIndex uses document structure to navigate without vector similarity. Reinforces [[ai-engineering/rag-approaches]]
- **"Right framing unlocks a wider solution space"**: CP vs AP choice, SQL vs NoSQL choice, queue vs stream choice — all depend on correctly framing the problem requirements. Reinforces the wiki's central cross-domain theme.

## Related Pages

- [[ai-engineering/rag-approaches]]
- [[ai-engineering/pageindex]]
- [[product-org-design/conways-law]]
- [[software-engineering/cap-theorem-and-consistency]]
- [[software-engineering/database-scaling]]
- [[software-engineering/distributed-systems]]
- [[software-engineering/messaging-and-events]]
- [[software-engineering/caching-cdn-proxy]]
- [[software-engineering/system-design-approach]]
