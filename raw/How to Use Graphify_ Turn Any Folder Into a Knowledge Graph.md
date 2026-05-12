---
title: "How to Use Graphify: Turn Any Folder Into a Knowledge Graph"
source: "https://medium.com/agentic-builders/how-to-use-graphify-turn-any-folder-into-a-knowledge-graph-d51b38eb60b6"
author:
  - "[[Ana Bildea]]"
  - "[[PhD]]"
published: 2026-04-11
created: 2026-04-26
description: "How to Use Graphify: Turn Any Folder Into a Knowledge Graph A step-by-step guide to using Graphify, the open-source tool that builds a queryable knowledge graph Every developer working with LLMs on …"
tags:
  - "clippings"
---
## A step-by-step guide to using Graphify, the open-source tool that builds a queryable knowledge graph

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*LOtskpRjqIxDelqR)

Every developer working with LLMs on large codebases eventually hits the same wall: context windows are finite, but codebases are not. The standard approach — dumping raw files into the prompt and hoping for the best — scales linearly in tokens and sub-linearly in actual understanding.

Andrej Karpathy recently described his personal knowledge workflow: dumping papers, screenshots, and tweets into a raw folder, then using an LLM to compile everything into a wiki and navigating it with `Obsidian`.

> He ended his description with a challenge: “I think there is room here for an incredible new product instead of a hacky collection of scripts.”

`**Graphify**` is that product. It takes a fundamentally different approach to context. Instead of feeding raw files to your AI assistant, it builds a persistent, queryable knowledge graph from your code, docs, papers, images, and video. It then serves compressed subgraphs to your AI assistant.

Here is a step-by-step guide on how Graphify works under the hood, and how you can use it to reduce your token usage by up to **71.5x.**

## Step 1: Install and Point at a Folder

Getting started with Graphify requires zero configuration. It is not a wrapper around a vector database, and it does not require you to set up complex embedding pipelines.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*p9he7ArP3kyQv_HO)

You simply install the package via `pip (pip install graphifyy)` and run a single command `(graphify .)` inside your project directory. Graphify immediately begins scanning your files — whether they are code, PDFs, images, or videos — and starts building the graph.

## Step 2: Pass 1 — Deterministic AST Parsing

The first pass of the Graphify pipeline is entirely deterministic and runs locally on your machine. No code is sent to any LLM API during this phase.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*9zy5EDAMPjywJ3y0)

Graphify uses `tree-sitter` to parse code across 20 different languages. It extracts classes, functions, imports, call graphs, docstrings, and rationale comments. Because this extraction is deterministic, every edge created in this pass is tagged with a provenance label of **EXTRACTED** and a confidence score of 1.0. You always know that these relationships are factual representations of your codebase.

## Step 3: Pass 2 — Local Transcription

If your folder contains audio or video files (like recorded lectures or meeting MP4s), Graphify handles them in a second local pass.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ja0wUGNvd5XQF2e6)

Using **faster-whisper**, Graphify transcribes these media files directly on your device. The audio never leaves your machine. Furthermore, the transcripts are SHA256-cached, meaning that if you run Graphify again, the transcription step is instant unless the media file has changed. These transcripts are then fed into the final extraction pass.

## Step 4: Pass 3 — Parallel LLM Extraction

For unstructured semantic content — such as documentation, PDFs, images, and the transcripts generated in Pass 2 — deterministic parsing is not possible. This is where Graphify leverages LLMs.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*j0wTR4JZ6s-1HO70)

It is important to note that Graphify itself is a skill, not a standalone orchestrator. Claude or other coding CLI is the runtime. Meaning that your coding assistant (Claude/Codex, etc) uses the Graphify skill to dispatch subagents in parallel. Each subagent reads the content and extracts concepts, relationships, and design rationale. The output from these subagents is strictly validated against a schema before being merged into the main graph. Because these relationships are deduced by an AI, they are tagged with a provenance label of `INFERRED` along with a confidence score.

## Step 5: The Knowledge Graph Output

Once the three passes are complete, Graphify outputs a structured, persistent knowledge graph.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*2GMTmKLsqOoGiE_a)

The output takes three forms:

- **GRAPH\_REPORT.md**: A human-readable audit report that summarizes the graph and surfaces any edges for human review.
- **graph.json:** A machine-readable file designed for AI assistants to query.
- **graph.html**: An interactive graph viewer that lets you click nodes, search, and filter by community.

You can also opt-in to generate an **Obsidian Vault** (using the — obsidian flag), which creates a ready-to-use wiki with backlinks, allowing you to navigate the graph visually and textually just like Karpathy’s workflow.

Every edge in the graph carries its provenance tag (`EXTRACTED`, `INFERRED,` or `AMBIGUOUS`), ensuring epistemic honesty. You always know what the system found versus what it guessed.

## Step 6: Querying the Graph

The true power of Graphify is realized when you integrate it with your AI coding assistant. It currently supports 10 platforms: Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, Aider, OpenClaw, Factory Droid, and Trae.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ea9mDXKwU-_kBtaH)

Graphify ships with a `PreToolUse` hook. When you ask your assistant a question like “how does the auth flow work?”, the hook fires before the assistant starts grepping through raw files. The assistant reads the graph map first, identifies the relevant nodes, and retrieves a focused subgraph.

Instead of dumping 52 files into the context window, the assistant receives a highly relevant subgraph of perhaps 300 tokens. This structural context allows the AI to provide accurate answers while using drastically fewer tokens.

## Take aways

When you put it all together, Graphify represents a step forward in how AI assistants consume information. And yes it is linked to `context graph` the next shift in agentic AI.

The principle is simple: structured, compressed, provenance-tagged knowledge graphs are a better input representation than raw files. By separating deterministic extraction from probabilistic inference, and by clustering based on topology rather than embeddings, Graphify ensures that the structural relationships within your project are preserved and queryable.

The graph is the context window. Everything else is just search.

The next generation of developer tooling will not be about feeding more context to models — it will be about feeding better context. Tools that separate what is known from what is inferred, and that compress structure rather than raw text, will define how serious teams work with AI at scale.

To try it today, run `pip install graphifyy && graphify .` inside any project folder. Start with a codebase you already know well — the graph it produces will surprise you.

Thank you for reading. See you in the next one.