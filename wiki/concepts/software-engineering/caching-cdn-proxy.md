---
title: Caching, CDN, and Proxy
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [shivambhadani-system-design-for-beginners]
tags: [caching, redis, cdn, proxy, blob-storage, performance, nginx, cloudfront]
---

Three infrastructure layers that reduce latency and protect backend services: in-memory caching (Redis), content delivery networks, and proxy servers.

## Caching

Caching stores frequently accessed, pre-computed data in a fast-access layer so future requests don't hit the database.

**Typical impact:** Database query: 800 ms → Redis cache: 20 ms

### Cache Hit vs Cache Miss

- **Cache hit** — data found in the cache; served immediately
- **Cache miss** — data not in cache; fetched from the database, then written to cache for future requests

### Cache Invalidation Strategies

1. **TTL (Time to Live)** — data automatically expires after a set duration; next request after expiry triggers a fresh database fetch
2. **Write-through** — when data is written to the DB, simultaneously write to cache; cache always stays current

### Types of Caches

| Type | Location | Examples |
|---|---|---|
| Client-side | User's browser | HTML, CSS, JS files |
| Server-side (in-memory) | Application or dedicated cache server | Redis, Memcached |
| CDN | Edge servers (distributed globally) | AWS CloudFront, Cloudflare |
| Application-level | Within application code | Intermediate computation results |

## Redis Deep Dive

Redis is an **in-memory key-value store**. Reads/writes happen in RAM, making it significantly faster than disk-based databases.

**Limitation:** RAM is expensive and limited — Redis is for hot (frequently accessed) data, not all data.

**Key data types:**

| Type | Key Commands | Use Case |
|---|---|---|
| String | `SET key value`, `GET key`, `MGET k1 k2` | Simple values, counters |
| List | `LPUSH`/`RPUSH` (add), `LPOP`/`RPOP` (remove) | Queue (LPUSH + RPOP = FIFO); Stack (LPUSH + LPOP = LIFO) |
| Hash | `HSET`, `HGET` | Object-like records |
| Set | `SADD`, `SMEMBERS` | Unique collections, tags |
| Sorted Set | `ZADD`, `ZRANGE` | Leaderboards, ranked lists |

**Key naming convention:** `entity:id:field` → e.g., `user:1`, `user:2:email`

**Redis beyond caching:** Redis also supports real-time Pub/Sub for broadcasting messages across WebSocket servers. → [[software-engineering/messaging-and-events]]

## Blob Storage

Binary Large Objects (BLOBs) — video, image, PDF files — cannot be stored efficiently in relational or document databases due to their size and the impact on query performance.

**Solution:** Dedicated blob storage services (managed, auto-scaling):
- **AWS S3** — dominant choice; 11 nines (99.999999999%) durability; pay-as-you-go
- **Cloudflare R2**

**S3 features:** Automatic scaling, encryption at rest and in transit, fine-grained access control (IAM policies, ACLs, pre-signed URLs).

## Content Delivery Network (CDN)

A CDN caches static content (images, video, CSS, JS, PDFs) on **edge servers** distributed globally. Users are served from the nearest edge server rather than the origin server.

**How it works:**
1. User requests a file
2. Request routes to the nearest edge server (via GeoDNS)
3. **Cache hit:** served from edge immediately
4. **Cache miss:** edge fetches from origin server (S3), caches it, returns it to the user
5. Subsequent requests to that edge server: served from cache until TTL expires

**Key concepts:**

| Concept | Definition |
|---|---|
| Edge server | Geographically distributed CDN node |
| Origin server | The authoritative source (typically S3) |
| TTL | How long content stays cached at the edge before refreshing |
| GeoDNS | DNS mechanism that routes requests to the nearest edge server |

**Examples:** AWS CloudFront, Cloudflare CDN

## Proxy

A proxy is an intermediary server that sits between a client and a backend server.

### Forward Proxy

Sits in front of **clients**. Acts on behalf of the client. The backend server sees the proxy's IP, not the client's.

**Use cases:**
- VPN (access geo-blocked content)
- Client-side caching of frequently accessed resources
- Corporate content filtering (blocking certain sites for employees)

### Reverse Proxy

Sits in front of **servers**. Acts on behalf of the server. Clients see the proxy, not the actual backend servers.

**Use cases:**
- Load balancing (clients → reverse proxy → pool of servers)
- SSL termination (proxy decrypts HTTPS; backend communicates in plain HTTP)
- Static content caching
- Security (backend servers not exposed directly to the internet)

**Examples:** Nginx, HAProxy

> A load balancer is an instance of a reverse proxy.

**The key distinction:**
- Forward proxy hides the **client** from the server
- Reverse proxy hides the **server** from the client

## Related Pages

- [[software-engineering/system-design-approach]]
- [[software-engineering/messaging-and-events]]
- [[software-engineering/distributed-systems]]
- [[software-engineering/database-scaling]]
- [[software-engineering/shivambhadani-system-design-for-beginners]] *(source)*
