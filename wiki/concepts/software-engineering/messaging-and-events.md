---
title: Messaging and Event-Driven Architecture
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [shivambhadani-system-design-for-beginners]
tags: [messaging, kafka, message-broker, pubsub, event-driven, async, eda, rabbitmq]
---

Asynchronous communication patterns: message queues, message streams (Kafka), real-time pub/sub, and event-driven architecture (EDA).

## Synchronous vs Asynchronous Communication

| Model | How It Works | When to Use |
|---|---|---|
| Synchronous | Client sends request, waits for response | Short-lived tasks, real-time responses required |
| Asynchronous | Client gets "processing" acknowledgment; result delivered later | Long-running tasks, non-critical tasks (email), decoupling services |

## Message Brokers

A message broker sits between the **producer** (server that creates work) and the **consumer** (server that processes work).

**Why use a broker instead of direct service-to-service calls?**
1. **Reliability** — if the producer goes down, consumers continue processing from the queue
2. **Retry** — if a consumer fails mid-processing, the message remains in the broker for retry
3. **Decoupling** — producer and consumer work at their own pace, independently

### Message Queue

- Messages are pulled by a **single consumer type**
- Once a consumer processes a message, it is **deleted** from the queue
- Multiple consumer instances can share a queue for parallel processing (each message goes to exactly one instance)
- Examples: **RabbitMQ**, **AWS SQS**

**Use when:** One downstream system needs to process each message.

### Message Stream

- Messages are **not deleted** — they persist (until expiry or manual deletion)
- Multiple consumer groups can each independently read all messages
- Consumers iterate through messages sequentially; they don't claim/delete them
- Examples: **Apache Kafka**, **AWS Kinesis**

**Use when:** Multiple different downstream systems need to process the same message ("write once, read by many").

**The key distinction:** If you add a second service that needs to react to the same events, a queue requires a second separate queue (with the risk of producer failure leaving one queue unpopulated). A stream allows any number of consumer groups to independently read the same stream.

## Apache Kafka Internals

Kafka is a high-throughput message stream, suited for scenarios where many writes happen simultaneously (e.g., tracking millions of driver locations every 2 seconds, buffering writes before flushing to a slower database).

**Key concepts:**

| Concept | Kafka | Database Analogy |
|---|---|---|
| Broker | Kafka server instance | Database server |
| Topic | Named category of messages | Table |
| Partition | Division of a topic for parallelism | Shard |
| Producer | Publishes messages to a topic | INSERT |
| Consumer | Reads from a topic | SELECT |
| Consumer Group | Logical grouping of consumer instances | — |

**Partition rules:**
- One partition can be read by only **one consumer per consumer group**
- Different consumer groups can each read all partitions independently
- **To scale consumers horizontally, you need at least as many partitions as consumers**
- Kafka automatically rebalances partition assignments when consumers are added/removed

**Example (video platform):**
- Topic: `video-uploaded` with 4 partitions
- Consumer Group 1: Video Transcoding service (3 consumers → Kafka assigns 3 partitions)
- Consumer Group 2: Caption Generator service (4 consumers → 1 partition per consumer)

## Real-Time Pub/Sub

| Feature | Message Broker | Pub/Sub |
|---|---|---|
| Message delivery | Consumer **pulls** from broker | Broker **pushes** to subscribers |
| Message storage | Messages stored until consumed | Messages not stored — ephemeral |
| Latency | Higher (polling interval) | Very low (immediate push) |
| Examples | RabbitMQ, Kafka | Redis Pub/Sub |

**Use case:** Real-time chat across horizontally scaled WebSocket servers. Server-1 publishes a message to a Redis Pub/Sub channel; all other servers subscribed to that channel immediately receive and relay it to their connected clients.

## Event-Driven Architecture (EDA)

EDA uses a message broker to decouple producers from consumers in a microservices system.

**When to use:** Non-critical side effects that don't affect the user's immediate response — e.g., sending a confirmation email, updating inventory count, logging analytics.

### Two EDA Patterns

**Simple Event Notification:**
- Producer sends a lightweight event with minimal data (e.g., just the `order_id`)
- Consumers query the database for full details if needed
- Pros: small event size, low broker storage costs
- Cons: consumers make extra database calls

**Event-Carried State Transfer:**
- Producer sends a complete event with all necessary data
- Consumers don't need to query the database
- Pros: reduced latency, no extra network calls
- Cons: larger event payloads, higher broker storage costs

**Why EDA improves resilience:**
1. **Decoupling** — Order Service doesn't directly call Inventory Service; a failure in Inventory Service doesn't break checkout
2. **Resilience** — If Inventory Service is down, the message waits in the broker for when it recovers
3. **Independent scalability** — each consumer service scales horizontally without affecting others

## When to Use Each Pattern

| Scenario | Pattern |
|---|---|
| Long-running task (video transcoding) | Message queue |
| Same event consumed by multiple services | Message stream (Kafka) |
| Real-time notification across servers | Pub/Sub (Redis) |
| Decoupling microservice side effects | EDA (message broker) |
| Buffering high-write-rate data (location tracking) | Kafka (high throughput) |

## Related Pages

- [[software-engineering/distributed-systems]]
- [[software-engineering/system-design-approach]]
- [[software-engineering/cap-theorem-and-consistency]]
- [[software-engineering/caching-cdn-proxy]]
- [[software-engineering/shivambhadani-system-design-for-beginners]] *(source)*
