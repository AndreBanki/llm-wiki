---
title: "How to Build the Knowledge System Andrej Karpathy Uses (And What It's Actually For)"
type: source
created: 2026-04-24
updated: 2026-04-24
sources: []
tags: [llm-wiki, knowledge-management, karpathy, pkm, synthesis, obsidian, constella]
---

# How to Build the Knowledge System Andrej Karpathy Uses (And What It's Actually For)

*A reframe of Karpathy's LLM Wiki system — not as a workflow but as a fundamentally different relationship with knowledge, and who does the connecting.*

---

## Metadata

| Field | Value |
|---|---|
| Author | Tejas Sharma |
| Publication | Level Up Coding (Medium) |
| Original URL | https://levelup.gitconnected.com/how-to-build-the-knowledge-system-andrej-karpathy-uses-and-what-its-actually-for-cf45dea0b277 |
| Date | April 10, 2026 |

---

## One-line Summary

Reframes Karpathy's LLM Wiki system as a solution to the synthesis problem — not the retrieval problem — and articulates why knowledge without connection is just storage.

---

## Core Thesis

Most readers of Karpathy's original post focused on the tools: markdown, scripts, Obsidian. They missed the actual shift. What Karpathy built inverts **who does the connecting**. Every prior PKM system — folders, apps, note vaults — assumes the human makes the links. Karpathy's system delegates that entirely to the AI.

> *"Knowledge without connection is just storage. And storage doesn't make you think better. It just makes you feel like you're on top of things."*

---

## The Synthesis Problem

The article names a diagnosis: professionals at the top of their fields don't have information problems. They have **synthesis problems**.

| Archetype | What they have | What they lack |
|---|---|---|
| Lawyer with 10 years of case notes | Deep information | A way to reason across all of it at once |
| Consultant who advised 30 companies | Domain knowledge | The pattern that connects the cases |
| Researcher who read 500 papers | Data | The connection that makes it cohere |

This framing extends the value proposition of the LLM Wiki pattern beyond note-taking productivity into professional leverage.

---

## The Six Implementation Steps

As described in this article (aligns with [[ai-engineering/llm-wiki-pattern]]):

1. **Raw directory** — everything goes in: clipped articles, downloaded papers, bookmarked repos, images that matter. Point: one place the AI can read from. Karpathy uses Obsidian Web Clipper to convert web articles to markdown.
2. **Compile step** — the AI reads raw/ and builds the wiki: identifies concepts, writes articles, links related ideas, adds backlinks, organizes into a directory structure. You don't write this. The AI does.
3. **IDE layer** — Obsidian as a *reader*, not a builder. You navigate what the AI built; you don't create notes inside it. This distinction matters: Obsidian here is a viewer.
4. **Q&A against the wiki** — once large enough, you ask complex questions. Answers are drawn from your own accumulated knowledge — no hallucinations from the open web.
5. **Filing outputs back in** — when the AI gives you an answer, generates a visualization, or writes a summary, you file it back into the wiki. Every query enriches the base. This is where compounding starts.
6. **Linting / health checks** — periodically the LLM scans the wiki for inconsistencies, fills gaps using web search, finds interesting connections that could become new articles. AI does the maintenance; you review what it surfaces.

---

## Key Distinctions

### Obsidian as Reader, Not Builder
> *"You're not creating notes inside it. You're using it to navigate what the AI built."*

This makes explicit what the [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]] source implied: Obsidian's role is a browsing/navigation layer, not an authoring layer.

### Quarriable Knowledge
Once the wiki is large enough, you can *quarry* it — ask complex questions that draw on your entire accumulated reading, synthesized on demand. The wiki transforms from a passive archive into an active reasoning substrate.

### Karpathy's Own Words
> *"A hacky collection of scripts."*

Karpathy himself described his implementation this way. The article uses this to argue that the gap between what the system does and what it takes to build it is precisely the problem Constella was designed to solve.

---

## Constella

The author, Tejas Sharma, built [Constella](https://constella.app) as a no-code implementation of the same pattern. Sources go in; AI builds the connections; you ask questions against everything you've accumulated. No terminal, no scripts, no configuration.

Mentioned here as a market signal: the LLM Wiki pattern is generating demand for productized, accessible implementations.

---

## Delta vs. Existing Wiki

| Aspect | This Source | Existing Coverage |
|---|---|---|
| Synthesis problem framing | Named explicitly; three archetypes | Not previously named |
| Quarriable knowledge | Introduced as term | Not in glossary |
| Obsidian as reader (not builder) | Made explicit | Implicit in existing coverage |
| Filing outputs back in | Explicit step 5 | Implicit in query workflow |
| Karpathy's "hacky scripts" quote | Documented | Not previously captured |
| Constella | Mentioned | Not mentioned |

---

## Related Pages

- [[ai-engineering/llm-wiki-pattern]]
- [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]]
- [[ai-engineering/rag-approaches]]
- [[glossary]]
