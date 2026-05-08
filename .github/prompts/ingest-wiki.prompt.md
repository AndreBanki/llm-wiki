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
   Pages created: ...
   Pages updated: ...
   Key additions: ...
   ```
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
   Pages created: ...
   Pages updated: ...
   Key additions: ...
   ```
15. **After all wiki changes are complete, send a completion email to andre.banki@gmail.com using the Resend MCP tool**, with:
   - Subject: `[LLM Wiki] Ingest complete: <source title>`
   - Body:
     - **Pages created:** list each new file with a one-line description
     - **Pages updated:** list each modified file with a one-line description of what changed
     - A short paragraph on the most important cross-domain connection or insight added by this ingest

## Notes

- A single ingest may touch 5–15 wiki pages. That is expected.
- Always ask clarifying questions to understand key takeaways before proceeding with updates.
- Briefing emails are sent **before** making wiki changes to allow the user to provide feedback.
- Completion emails are sent **after** all wiki changes are complete.
