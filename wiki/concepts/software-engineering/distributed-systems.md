---
title: Distributed Systems
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [shivambhadani-system-design-for-beginners]
tags: [distributed-systems, leader-election, orchestration, big-data, fault-tolerance, coordinator-worker]
---

Core concepts for systems where multiple machines coordinate to perform work that a single machine cannot handle.

## What Is a Distributed System?

A system where **work is performed by a set of multiple machines** acting as one. From the client's perspective, a distributed system looks like a single machine — the distribution is transparent.

Key properties:
- Work is divided and distributed across nodes (worker machines)
- A coordinator/leader assigns work and aggregates results
- The system must handle node failures gracefully
- All distributed **stateful** systems must address the CAP theorem tradeoffs → [[software-engineering/cap-theorem-and-consistency]]

**Examples:** Apache Cassandra, AWS DynamoDB, MongoDB, Google Spanner, Redis Cluster, horizontal scaling clusters.

## Coordinator / Worker Pattern

The most common distributed systems pattern:

```
Client → Leader (Coordinator)
           ├── Worker 1
           ├── Worker 2
           └── Worker 3
```

1. Client makes a request to the leader
2. Leader divides the task and assigns sub-tasks to workers
3. Workers complete sub-tasks and return results to the leader
4. Leader aggregates and returns the final result to the client

**Coordinator responsibilities:**
- Divide work and distribute it evenly
- Handle worker failures (detect and reassign work)
- Aggregate partial results
- Logging and monitoring

## Leader Election

When a leader fails, the cluster must automatically elect a new one without human intervention.

**Triggers for election:**
1. System startup — which server becomes the initial leader?
2. Leader failure — a follower detects the crash and triggers a new election

**Leader election algorithms:**

| Algorithm | Time Complexity | Notes |
|---|---|---|
| LCR | O(N²) | Simple ring-based algorithm |
| HS | O(N log N) | More efficient |
| Bully | O(N) | Highest-ID node takes over |
| Gossip Protocol | O(log N) | Used in production (DynamoDB, Cassandra) |

> Treat leader election as a black box for system design purposes. What matters: when the leader goes down, one follower automatically becomes the new leader.

## Auto-Recoverable Systems

A pattern for zero-human-intervention system recovery using nested orchestration + leader election:

```
Leader Orchestrator (elected by leader election)
    ├── Worker Orchestrator 1 → monitors servers
    ├── Worker Orchestrator 2 → monitors servers
    └── Worker Orchestrator 3 → monitors servers
              ↓
         Server pool (application/database servers)
```

Recovery chain:
- A server goes down → the monitoring worker orchestrator restarts it
- A worker orchestrator goes down → the leader orchestrator restarts it
- The leader orchestrator goes down → worker orchestrators run leader election; new leader takes over

This is the conceptual pattern behind managed container orchestration tools like Kubernetes.

## Big Data Tools

When a dataset is too large to process on one machine, use distributed computation tools that implement the coordinator/worker pattern.

- **Apache Spark** — the dominant open-source distributed computation framework
- Write business logic as jobs (in Python, Java, or Scala); Spark handles distribution, fault tolerance, and result aggregation

**When to use:**
- Training ML models at scale
- Large ETL data pipelines
- Social network analysis
- Recommendation systems

> For system design interviews, knowing *when* to reach for a big data tool matters more than knowing its internals.

## Stateful vs Stateless Systems

| Type | Definition | Examples |
|---|---|---|
| Stateless | Machines don't store data between requests | Application servers |
| Stateful | Machines hold data for future use | Databases, caches |

Consistency (CAP theorem) only applies to **distributed stateful systems** — typically databases. Application servers are generally stateless and do not require consistency coordination.

## Related Pages

- [[software-engineering/cap-theorem-and-consistency]]
- [[software-engineering/database-scaling]]
- [[software-engineering/messaging-and-events]]
- [[software-engineering/system-design-approach]]
- [[software-engineering/shivambhadani-system-design-for-beginners]] *(source)*
