---
title: Database Scaling
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [shivambhadani-system-design-for-beginners]
tags: [database, scaling, sql, nosql, sharding, replication, indexing, partitioning]
---

A progressive ladder for scaling a database from single-server to globally distributed, plus a decision framework for choosing SQL vs NoSQL.

## The Scaling Ladder

Apply each technique in order. Only advance to the next level when the current level hits its limit.

### Step 1: Indexing

- Without an index: full table scan O(N) to find a row
- With an index: database creates a B-tree copy of the indexed column; search becomes O(log N)
- Apply to frequently queried columns; the database manages the B-tree automatically — no custom code needed

### Step 2: Vertical Scaling

Increase RAM, CPU, and storage on the single database server. Simple, requires no application changes. Hits a hardware ceiling.

> **Rule**: Always prefer vertical scaling first. Only proceed to the steps below when you've hit the hardware limit.

### Step 3: Partitioning (same server)

Break a large table into smaller tables kept on the **same** database server. Each partition has its own index, making queries on the smaller table faster. The database (e.g., PostgreSQL) transparently routes queries to the correct partition — no application code change needed.

### Step 4: Master-Slave Architecture

**When:** Read-heavy traffic that a single server can't handle.

- **Master node** — handles all writes (INSERT, UPDATE, DELETE)
- **Slave nodes** — handle read requests (SELECT); data replicates from master asynchronously (or synchronously)
- Load balancer routes reads to the least-busy slave

**Limitation:** Write throughput is still bottlenecked by the single master.

### Step 5: Multi-Master

**When:** Write-heavy traffic that a single master can't handle.

- Multiple masters, each handling writes from a geographic region (e.g., North India DB + South India DB)
- Periodic synchronization between masters
- **Challenge:** conflict resolution — when two masters write different values for the same key, the application must decide how to reconcile (accept both, take the latest, concatenate, etc.)

### Step 6: Database Sharding

**When:** Total data volume exceeds what can fit on any single server. Use as a last resort — complexity is high.

- Split the table across multiple independent database servers (shards), each holding a subset of rows
- Application code must determine which shard to query/write — unlike partitioning, the database does not handle this automatically

**Sharding strategies:**

| Strategy | Mechanism | Pros | Cons |
|---|---|---|---|
| Range-based | Shard by value ranges (IDs 1–1000, 1001–2000…) | Simple | Uneven distribution if data is skewed |
| Hash-based | `hash(sharding_key) % num_shards` | Even distribution | Rebalancing is painful when shard count changes |
| Geographic | Shard by user region | Low latency per region | Hotspot risk in popular regions |
| Directory-based | Lookup table maps keys to shards | Flexible reassignment | Lookup directory becomes a bottleneck |

**Disadvantages of sharding:**
1. Application code must manage shard routing
2. Cross-shard JOINs are expensive (data lives on different servers)
3. Consistency is harder to maintain across shards

> Sharding is a last resort. The complexity cost is high.

## SQL vs NoSQL Decision Framework

| Criterion | Choose SQL | Choose NoSQL |
|---|---|---|
| Schema | Fixed, predefined | Flexible, evolving |
| Data integrity | Critical (financial, transactional) | Acceptable inconsistency |
| Query complexity | Complex joins, aggregations, analytics | Simple key-value / document lookups |
| Scaling preference | Vertical preferred | Horizontal (sharding is the default) |
| Use cases | Banking, payments, orders, analytics | Social media posts, real-time data, product catalogs |

**SQL scaling note:** SQL databases can be sharded, but ACID guarantees become hard to maintain across shards and JOINs become cross-server operations. Prefer NoSQL when horizontal scale is the primary requirement.

**NoSQL types:**

| Type | Examples | Best For |
|---|---|---|
| Document | MongoDB | Flexible-schema records (JSON/BSON) |
| Key-value | Redis, AWS DynamoDB | Ultra-fast lookups; simple structure |
| Column-family | Apache Cassandra | Time-series, write-heavy workloads |
| Graph | Neo4j | Social networks, recommendation engines |

## Summary Decision Rules

1. Start with indexing and vertical scaling
2. Read-heavy traffic → add master-slave replication
3. Write-heavy traffic → consider multi-master or sharding
4. Large, unstructured data needing horizontal scale → NoSQL
5. Need ACID + complex queries → SQL
6. Sharding is a last resort; only when all else fails

## Related Pages

- [[software-engineering/cap-theorem-and-consistency]]
- [[software-engineering/system-design-approach]]
- [[software-engineering/distributed-systems]]
- [[software-engineering/caching-cdn-proxy]]
- [[software-engineering/shivambhadani-system-design-for-beginners]] *(source)*
