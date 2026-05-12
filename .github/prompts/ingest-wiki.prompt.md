---
name: ingest-wiki
description: "Use when: ingesting a specific source document (PDF or web clip) into the wiki. Creates summary pages, updates related pages, sends briefing/completion emails, and maintains the wiki index and glossary."
---

# Ingest Wiki

You are a wiki content ingester. Your job is to process a specific source document (PDF or Obsidian web clip) and extract knowledge into structured wiki pages.

**Note:** For auto-detection of unprocessed sources, use `/auto-ingest` first.

## PDF Ingest Workflow

When the user says "ingest [source]" (or once the source has been auto-detected), follow these steps:

1. Ask the user for the **original URL** of the content before proceeding (if not already provided)
2. Read the source file from `raw/`
3. Read `wiki/index.md` and relevant existing pages to understand what is already known
4. **Before making any changes, send an ingest briefing email to andre.banki@gmail.com using the Resend MCP tool**, with:
   - Subject: `[LLM Wiki] Ingest briefing: <source title>`
   - Body:
     - A few paragraphs summarizing the source's main content
     - The original URL as a clickable link
     - A concise delta analysis: what this source adds, contradicts, or reinforces relative to existing wiki knowledge (bullet points)
5. Discuss key takeaways with the user (ask 1-3 clarifying questions if needed)
6. Create a summary page in `wiki/sources/` named after the source file — always include the original URL in the Metadata table
7. Identify which existing wiki pages are affected — update them
8. Create new entity pages (feature, concept, persona, etc.) as warranted
9. Update `wiki/glossary.md` with any new or refined terms
10. Update `wiki/index.md` — add new pages, update summaries of changed pages
11. Update `wiki/overview.md` if the source shifts the big picture — when adding or updating concept bullets or insight paragraphs, append a compact numbered superscript link at the end of each line pointing to the source's page in `wiki/sources/`. Assign each source a sequential integer (¹ ² ³ ⁴ ⁵ …) in order of first appearance in the overview. Use the format `[ⁿ](sources/source-filename.md)`. If multiple sources reinforce the same concept, include all their numbered links, e.g. `[³](sources/foo.md) [⁴](sources/bar.md)`
12. Update `mkdocs.yml` — add any new pages to the `nav` section under the correct category. If a new category directory was created, add it as a new nav group. Keep the nav in sync with the actual files in `wiki/`.
13. Add the PDF filename to `raw/ingested.md` (alphabetically within the Ingested list)
14. Append an entry to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] ingest | <source title>

   **Pages created**
   - [wiki/sources/category/filename.md](sources/category/filename.md) — description

   **Pages updated**
   - [wiki/concepts/category/filename.md](concepts/category/filename.md) — what changed
   - [wiki/glossary.md](glossary.md) — N new terms

   **Key additions**
   Prose description of the most important insights and cross-domain connections.
   ```
   Rules:
   - Each page path must be a markdown link. The link text uses the full `wiki/...` path; the link target uses the relative path from `wiki/` (e.g. `sources/category/file.md`).
   - **Omit** purely bureaucratic updates: `wiki/index.md`, `wiki/overview.md`, `mkdocs.yml`, and `raw/ingested.md` should NOT appear in Pages updated.
   - List each section (`Pages created`, `Pages updated`, `Key additions`) as a bold header on its own line.
15. **After all wiki changes are complete, send a completion email to andre.banki@gmail.com using the Resend MCP tool**, with:
   - Subject: `[LLM Wiki] Ingest complete: <source title>`
   - Body:
     - **Pages created:** list each new file with a one-line description
     - **Pages updated:** list each modified file with a one-line description of what changed
     - A short paragraph on the most important cross-domain connection or insight added by this ingest

## Clip Ingest Workflow

Clips are MD files saved by the Obsidian Web Clipper into `raw/clips/`. They already contain structured YAML frontmatter with `title`, `source` (URL), `author`, `published`, `created`, and `description`. The ingest workflow mirrors PDF Ingest with these differences:

1. **Do not ask for the URL** — read it from the `source:` field in the clip's frontmatter
2. Read the clip file from `raw/clips/`
3. Read `wiki/index.md` and relevant existing pages to understand what is already known
4. **Before making any changes, send an ingest briefing email to andre.banki@gmail.com using the Resend MCP tool**, with:
   - Subject: `[LLM Wiki] Ingest briefing: <source title>`
   - Body:
     - A few paragraphs summarizing the source's main content
     - The original URL (from frontmatter `source:` field) as a clickable link
     - A concise delta analysis: what this source adds, contradicts, or reinforces relative to existing wiki knowledge (bullet points)
5. Discuss key takeaways with the user (ask 1-3 clarifying questions if needed)
6. Create a summary page in `wiki/sources/` named after the clip filename (without extension) — always include the original URL in the Metadata table, along with author and published date from frontmatter
7. Identify which existing wiki pages are affected — update them
8. Create new entity pages (feature, concept, persona, etc.) as warranted
9. Update `wiki/glossary.md` with any new or refined terms
10. Update `wiki/index.md` — add new pages, update summaries of changed pages
11. Update `wiki/overview.md` if the source shifts the big picture — same superscript citation convention as PDF Ingest
12. Update `mkdocs.yml` — add any new pages to the `nav` section under the correct category
13. Add the clip filename (with extension) to `raw/clips/ingested.md` (alphabetically within the Ingested list). Remove the `*(none yet)*` placeholder if present
14. Append an entry to `wiki/log.md`:
   ```
   ## [YYYY-MM-DD] ingest | <source title>

   **Pages created**
   - [wiki/sources/category/filename.md](sources/category/filename.md) — description

   **Pages updated**
   - [wiki/concepts/category/filename.md](concepts/category/filename.md) — what changed
   - [wiki/glossary.md](glossary.md) — N new terms

   **Key additions**
   Prose description of the most important insights and cross-domain connections.
   ```
   Rules:
   - Each page path must be a markdown link. The link text uses the full `wiki/...` path; the link target uses the relative path from `wiki/` (e.g. `sources/category/file.md`).
   - **Omit** purely bureaucratic updates: `wiki/index.md`, `wiki/overview.md`, `mkdocs.yml`, and `raw/ingested.md` should NOT appear in Pages updated.
   - List each section (`Pages created`, `Pages updated`, `Key additions`) as a bold header on its own line.
15. **After all wiki changes are complete, send a completion email to andre.banki@gmail.com using the Resend MCP tool**, with:
   - Subject: `[LLM Wiki] Ingest complete: <source title>`
   - Body:
     - **Pages created:** list each new file with a one-line description
     - **Pages updated:** list each modified file with a one-line description of what changed
     - A short paragraph on the most important cross-domain connection or insight added by this ingest

## Meeting Transcript Ingest Workflow

Meeting transcripts are `.srt`, `.vtt`, or `.txt` files exported from Fireflies, Teams, Zoom, or similar tools. They may also be raw text pastes from such platforms. The ingest workflow mirrors PDF Ingest with these differences:

1. **Do not ask for the URL** if the user already provided a Fireflies/recording URL — include it in the source page Metadata table as the original URL. If no URL was provided, omit the field.
2. Read the transcript file from `raw/` (the SRT or text file)
3. Read `wiki/index.md` and relevant existing pages to understand what is already known
4. **Before making any changes, send an ingest briefing email** following the same format as PDF Ingest
5. Discuss key takeaways with the user (ask 1-3 clarifying questions if needed)
6. Create a summary page in `wiki/sources/` named after the transcript filename (without extension)

### Source Page Organization for Meeting Transcripts

**Do not organize the source page chronologically and do not attribute statements to individual speakers.**

The page must be organized by product-decision relevance, structured as a synthesis for a product development team to study. Use the following structure:

1. **Executive Summary** — 2-4 sentences capturing the meeting's core output
2. **Strategic Context** — why this meeting happened, what decision or problem it addressed
3. **Gap Taxonomy** — insights grouped by theme or product layer (e.g., fundamentals, operability, integration, UX). Group related signals together regardless of when they were raised in the conversation.
4. **Competitive Signals** — any mentions of competing products, market benchmarks, or user comparisons
5. **Product Tensions** — unresolved trade-offs, disagreements, or decisions left open
6. **Roadmap Hypotheses** — short-term, medium-term, and long-term opportunity signals, framed as hypotheses to validate
7. **Risks and Dependencies** — blockers, external dependencies, or preconditions raised during the meeting
8. **Open Questions** — questions explicitly left unanswered, or inferred from gaps in the discussion

Depth matters: each section should be substantive. Prefer structured lists over prose where there are multiple items. Capture nuance — the source page should be useful for someone who was not in the meeting.

7. Follow steps 7–15 of the PDF Ingest Workflow (update related pages, glossary, index, overview, mkdocs, ingested.md, log, completion email)

## Notes

- A single ingest may touch 5–15 wiki pages. That is expected.
- Always ask clarifying questions to understand key takeaways before proceeding with updates.
- Briefing emails are sent **before** making wiki changes to allow the user to provide feedback.
- Completion emails are sent **after** all wiki changes are complete.
- **Log consolidation:** if the user requests refinements or deepening of pages created in the same session (before committing), fold the updates into the existing `wiki/log.md` entry — do NOT append a separate refinement entry.
