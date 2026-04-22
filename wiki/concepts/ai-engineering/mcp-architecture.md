---
title: MCP Architecture (Model Context Protocol)
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [vidvatta-mcp-vs-api-architecture.md]
tags: [mcp, agent-architecture, tool-orchestration, ai-engineering, capability-discovery]
---

MCP (Model Context Protocol) is a protocol layer that enables AI agents to discover and invoke tools based on context and reasoning, replacing the human-decides-which-endpoint model of traditional REST APIs.

## What is MCP?

MCP is a protocol for AI-to-tool communication. Rather than a developer writing code that calls a specific API endpoint, an AI agent receives a set of available tools and *reasons* about which ones to invoke, in what order, and with what inputs — based on the current task context.

**Fundamental shift:**
- **Traditional API:** human (or deterministic code) decides which endpoint to call
- **MCP:** the AI model decides which tool to use, based on context + capability discovery

---

## Architecture Layers

### Client Layer

The MCP client is an AI Agent or Copilot. Its interface is *Context + Tools* — it receives available tool definitions and task context, then reasons about what to do.

Contrasted with an API client (app or human user) whose interface is a list of endpoints it must explicitly call.

### Protocol Layer

The MCP protocol is:
- **Context-aware**: the model's state informs what tools it calls
- **Capability discovery**: the client learns what tools exist dynamically, rather than having endpoints hardcoded
- **Permission-scoped execution**: each tool invocation operates within declared permission scopes

This contrasts with HTTP requests, which are stateless and require explicit, fixed inputs.

### Service Layer (MCP Servers)

MCP servers expose **tools, not services**. Key distinctions:
- No strict endpoint contracts
- Capabilities are AI-facing, not human-facing
- The server does not assume a specific calling sequence

**Failure modes unique to MCP:**
- **Tool overload** — too many tools available confuses the model; it may choose the wrong one or fail to converge
- **Context drift** — the model loses track of what the current task requires across a multi-step tool chain

### Data / Resource Layer

MCP can access: local files, IDE context, Cloud APIs.
- Fewer network hops than traditional architectures
- Lower marginal cost per operation (compute shifts to edge)

### Security Model

| MCP | Traditional API |
|---|---|
| Tool-level permissions | Network perimeter |
| Context isolation | Token-based auth |
| Local trust zone | Service-level access |

MCP's security model is granular at the *tool level*, not the service level. Each tool has its own permission scope, and the trust boundary is local (the agent environment) rather than network-wide.

---

## Scaling Properties

- Scales by **capability reuse**: adding a new tool to the MCP server immediately makes it available to all agents
- Intelligence scales faster than infrastructure: as models improve, the same tools produce better outcomes without re-engineering
- Compute shifts toward the edge: local resources (files, IDE state) reduce reliance on remote service calls

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Too many tools | Fewer, well-scoped tools — each tool should have a clear, distinct purpose |
| No permission scopes | Explicit scopes for each tool — limit what each tool can access |

---

## MCP vs. Traditional API: Summary Table

| Dimension | MCP | Traditional API |
|---|---|---|
| Decision maker | AI model | Human / code |
| Interface | Context + tools | Endpoints |
| Protocol | Context-aware, capability discovery | Stateless, fixed schema |
| Service nature | Tools (AI-facing) | Services (contract-driven) |
| Security | Tool-level permissions, context isolation | Network perimeter, token auth |
| Scaling | Capability reuse, edge compute | Infrastructure capacity |
| Failure modes | Tool overload, context drift | Cascading failures, gateway bottlenecks |

---

## Learning Sequence

> Start with APIs → Move to MCP.  
> APIs build system thinking. MCP builds AI orchestration thinking.

Understanding REST API design (stateless contracts, explicit inputs, auth) is prerequisite knowledge for understanding *why* MCP makes different tradeoffs.

---

## Career Path (MCP Track)

AI Engineer → Agent Platform Engineer → AI Architect

---

## Relationship to Other AI Engineering Concepts

| Concept | Relationship to MCP |
|---|---|
| RAG (retrieval) | RAG retrieves *context*; MCP orchestrates *actions*. Complementary layers in an AI agent stack. |
| LLM Wiki pattern | The wiki's schema file is an MCP-like construct: it defines what the AI can do and what constraints apply. |
| Vectorless RAG | Both MCP and vectorless RAG rely on *LLM reasoning* to navigate structure, rather than fixed lookup. |

---

## Related Pages

- [[ai-engineering/vidvatta-mcp-vs-api-architecture]] — source post with full layer-by-layer comparison table
- [[ai-engineering/rag-approaches]] — RAG as the retrieval layer; MCP as the action/orchestration layer
- [[ai-engineering/llm-wiki-pattern]] — meta-level orchestration; the schema file as a tool contract analog
- [[ai-engineering/pageindex]] — vectorless RAG; reasoning-based navigation (parallel philosophy to MCP's reasoning-based tool selection)
