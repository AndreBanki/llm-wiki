---
title: CAP Theorem and Consistency
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [shivambhadani-system-design-for-beginners]
tags: [distributed-systems, cap-theorem, consistency, availability, partition-tolerance, quorum, consistent-hashing]
---

The foundational tradeoff theorem for distributed systems, plus the two consistency models (strong and eventual) and the methods for achieving each.

## CAP Theorem

A distributed system can guarantee at most **two** of these three properties simultaneously:

- **Consistency (C)** — Every read returns the most recent write, regardless of which node serves it. All nodes have identical data at all times.
- **Availability (A)** — The system always responds to requests, even if some nodes have failed.
- **Partition Tolerance (P)** — The system continues operating even if network partitions occur (some nodes can't communicate with others).

**In practice**: Network partitions are inevitable in distributed systems. Therefore **P is always required**. The real tradeoff is between **CP** and **AP**.

| Choice | Guarantees | Sacrifices | Use Cases |
|---|---|---|---|
| **CP** | Consistency + Partition Tolerance | Availability during partitions | Banking, payments, stock trading — stale data is unacceptable |
| **AP** | Availability + Partition Tolerance | Consistency during partitions | Social media, product catalogs — stale data is acceptable |

> CA (no partition tolerance) is only theoretically possible in a non-distributed single-node system — irrelevant in production.

## Consistency Deep Dive

### Strong Consistency

- Every read after a write returns the latest value
- All replicas agree before acknowledging a write
- The system behaves as if there is only one copy of the data

**Methods to achieve:**

1. **Synchronous replication** — all replicas updated before write is acknowledged. Example: Google Spanner
2. **Quorum-based protocols** — `W + R > N` (write quorum + read quorum > total nodes). Used by DynamoDB, Cassandra in strong mode
3. **Consensus algorithms** (Raft, etc.) — write/read succeeds only when >50% of nodes acknowledge. Used by Docker Swarm

### Eventual Consistency

- Writes are acknowledged immediately; replicas sync in the background
- There may be a period where different nodes return different values
- Eventually, all nodes converge to the same value

**Methods to achieve:**

1. **Asynchronous replication** — common default in Cassandra, MongoDB, DynamoDB
2. **Relaxed quorum** — `W + R ≤ N`
3. **Gossip protocol** — nodes exchange heartbeats with a subset of peers, propagating updates through the system. Used by DynamoDB, Cassandra

### When to Choose Which

| Choose Strong Consistency | Choose Eventual Consistency |
|---|---|
| Banking / payment systems | Social media like/share counts |
| Trading platforms (stock prices) | Product catalogs in e-commerce |
| Any scenario where incorrect data causes real harm | Any scenario where temporary staleness is acceptable |

## Consistent Hashing

An algorithm for assigning data to nodes in a distributed system that minimizes data movement when nodes are added or removed.

### Why It Exists

With simple modulo-based assignment (`hash(key) % N`), adding or removing one node changes the assignment of almost all keys, forcing massive data migration. Consistent hashing limits disruption to only the keys adjacent to the changed node.

### How It Works

1. Hash each node (by IP or ID) to a position on a conceptual ring of size [0, 2¹²⁸)
2. Hash each data key to a position on the same ring
3. Each key belongs to its nearest **clockwise** node

When a node is removed, only the keys it owned move to the next clockwise node. All other keys are unaffected.

> Consistent hashing tells you which key belongs to which node. The actual data migration is your responsibility.

**Used by:** AWS DynamoDB, Apache Cassandra, Riak, Redis Cluster

### Cross-Domain Connection

Consistent hashing uses ring-based, structure-aware routing — not a brute-force scan of all nodes. This parallels PageIndex's approach of reasoning about document structure rather than similarity-matching chunks. Both trade brute-force retrieval for structure-aware navigation. → [[ai-engineering/rag-approaches]], [[ai-engineering/pageindex]]

## Related Pages

- [[software-engineering/distributed-systems]]
- [[software-engineering/database-scaling]]
- [[software-engineering/system-design-approach]]
- [[ai-engineering/rag-approaches]]
- [[ai-engineering/pageindex]]
- [[software-engineering/shivambhadani-system-design-for-beginners]] *(source)*
