---
title: "Seamless Content Ingestion for Claude-Obsidian Second Brain"
type: source
created: 2026-04-26
updated: 2026-04-26
sources: [Seamless Content Ingestion for Claude-Obsidian Second Brain.md]
tags: [llm-wiki, obsidian, content-acquisition, web-clipper, ingest-pipeline, tiered-model-routing, gemini-flash, ollama, knowledge-management]
---

How to build a low-friction, automated content acquisition pipeline feeding into a Claude-Obsidian Second Brain. Addresses the gap in the LLM Wiki conversation: not the architecture of the wiki itself, but how documents actually get *into* `raw/` in the first place.

---

## Metadata

| Field | Value |
|---|---|
| **Author** | James Wilkins |
| **Published** | 2026-04-22 |
| **Platform** | Medium / Generative AI |
| **URL** | https://generativeai.pub/seamless-content-ingestion-for-claude-obsidian-second-brain-865ae7fd8aa3 |
| **Source file** | `raw/clips/Seamless Content Ingestion for Claude-Obsidian Second Brain.md` |

---

## Core Claim

> The best system is one you actually use. If capture requires too much manual effort, it won't survive contact with real browsing habits.

Two guiding design principles:
- **Robustness** — must work for any content format without breaking on edge cases
- **Minimal Effort** — as few steps as possible between "interesting article" and "saved to knowledge base"

The full capture-to-knowledge cycle is **2 clicks** (Web Clipper) + overnight automated processing.

---

## Component 1: Obsidian Web Clipper

A browser extension that converts any web page into a structured markdown note with YAML frontmatter, deposited directly into an Obsidian Inbox folder.

### Frontmatter fields populated automatically:
- `title` — page title
- `source` — original URL
- `author` — page author
- `published` — publication date
- `created` — clip date
- `description` — meta description
- `tags` — initial tags (can include `clippings`)
- `type` — content type (article, video, pdf, github, social)
- `ingested` — checkbox (false until the overnight script processes it)
- `read` — checkbox (for manual reading list management)

### Five content-type templates:

| Template | Trigger | Key difference |
|---|---|---|
| **Article** (default) | Any page not matching others | Standard frontmatter; full article body |
| **PDF/Paper** | arXiv, PubMed, Semantic Scholar | Captures abstract + `pdf_url` for later download |
| **Video** | YouTube URLs | Pulls full transcript via `{{transcript}}` |
| **GitHub** | github.com repos/gists | Captures README; extracts repo owner from URL |
| **Social** | X, Twitter, Reddit, LinkedIn | Captures post content |

The default Article template acts as fallback — it handles any page that doesn't match a specific trigger.

---

## Component 2: Automated Overnight Ingest Script (Python)

Runs in the background (scheduled overnight, or triggered manually). Processes everything in the Obsidian Inbox folder.

### Processing loop per file:
1. **PDF handling** — if `type: pdf`, download the full document from `pdf_url` and convert; append below clipped abstract
2. **Length check** — short posts used as-is; long content sent to LLM
3. **LLM call** — returns ~100-word summary + tag list in one API call
4. **Tag normalization** — new tags merged with existing, deduplicated, lowercased, hyphenated
5. **Frontmatter update** — writes `summary`, updated `tags`, `ingested: true`
6. **File move** — Inbox/ → Wiki/ via Obsidian CLI (preserves all wikilinks)

### Model choice rationale:
Using Gemini Flash (or a local Ollama model) rather than Claude for this routine layer:
- Tagging and summarization is a simple, structured task — overkill for frontier models
- "Using a nuclear reactor to toast a slice of bread"
- Preserves Claude quota for synthesis, reasoning, and Q&A tasks
- Local Ollama is free and privacy-preserving for sensitive content

### Obsidian CLI:
A command-line tool that interfaces with a running Obsidian instance. Used instead of direct filesystem operations because it:
- Preserves wikilinks when moving files between folders
- Is more reliable than raw file manipulation
- Requires Obsidian to be running in the background

---

## Recommended Obsidian Plugins

| Plugin | Purpose |
|---|---|
| **Templater** | Applies a default frontmatter template to all manually-created notes, keeping them in sync with clipped content |
| **Local Image Plus** | Downloads images from remote URLs into local vault storage — enables offline access and AI agent visibility of images |

---

## Relationship to This Wiki

This wiki implements a structurally identical pattern:
- `raw/clips/` is the Inbox equivalent
- Clips are moved from `raw/clips/` to `raw/` after ingestion, so inbox contents always represent pending clips
- The Copilot agent fills the role of the overnight Python script — performing tagging, summarization, and wiki page generation
- The `copilot-instructions.md` schema file is the equivalent of Wilkins' "ingest routine brief"

The key difference: this wiki's ingest is human-triggered per source (for quality and deliberateness), whereas Wilkins' system processes everything automatically overnight (optimized for volume and zero friction).

---

## Related Pages

- [[ai-engineering/llm-wiki-pattern]]
- [[ai-engineering/llm-model-economics]]
- [[ai-engineering/ai-session-memory]]
- [[ai-engineering/creativeaininja-llm-wiki-cursor-obsidian]]
- [[ai-engineering/tejas-sharma-karpathy-knowledge-system]]
