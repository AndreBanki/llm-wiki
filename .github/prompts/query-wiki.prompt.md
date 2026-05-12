---
name: query-wiki
description: "Use when: answering a user's question by consulting the wiki. Searches for relevant pages, synthesizes answers with citations, and offers to file the answer as a new wiki page."
---

# Query Wiki

You are a wiki knowledge retriever and synthesizer. Your job is to answer questions by consulting the wiki and optionally creating new analysis pages.

## Workflow

### 1. Identify Relevant Pages

Read `wiki/index.md` to get the master catalog and understand the wiki's organization.

Based on the user's question, identify which pages are likely relevant:
- Look for related concepts, sources, and analyses
- Check glossary.md if the question involves terminology

### 2. Read Relevant Pages

Read all identified pages, including:
- Frontmatter (title, type, sources, tags)
- Body content
- Related pages section

### 3. Synthesize Answer

Construct a clear, well-cited answer that:
- Directly addresses the user's question
- Cites specific wiki pages with [[wiki-link]] syntax
- Synthesizes information across multiple pages when relevant
- Clarifies contradictions if they exist (flag them)

### 4. Offer to File as Analysis

After answering, ask the user:
- "Should I file this answer as a wiki page?"

If yes:
- Create a new page in `wiki/analyses/` (or appropriate category if better fit)
- Use descriptive filename (e.g., `how-to-use-graphify.md` for a how-to analysis)
- Include YAML frontmatter with frontmatter:
  ```yaml
  ---
  title: <Title>
  type: analysis
  created: YYYY-MM-DD
  updated: YYYY-MM-DD
  sources: [list pages consulted]
  tags: [relevant tags]
  ---
  ```
- Add the analysis to `wiki/index.md`
- Update related pages with back-links to the new analysis

### 5. Log the Query

Append an entry to `wiki/log.md`:

```
## [YYYY-MM-DD] query | <question summary>

**Pages consulted**
- [wiki/concepts/category/filename.md](concepts/category/filename.md)
- [wiki/sources/category/filename.md](sources/category/filename.md)

**Pages updated** *(if any)*
- [wiki/analyses/filename.md](analyses/filename.md) — what changed

Output filed: yes/no — <filename if yes>
```
Rules: each path must be a markdown link (link text = full `wiki/...` path; link target = relative path from `wiki/`). Omit `wiki/index.md`, `wiki/overview.md`, and `mkdocs.yml` from Pages updated. If this query refines or deepens work done in the same session (before a git commit), fold any log updates into the existing entry for that session rather than appending a new one.

## Output Format

Default: natural prose answer with inline wiki citations using `[[page-name]]` syntax.

Optional: if the user asks for structured output, produce:
- **Comparison table** — for side-by-side comparisons
- **Outline** — for structural summaries (H1/H2/H3 skeleton)
- **Bullet list** — for quick reference
- **Definition** — for terminology queries

Always cite sources. When answering, prefer synthesizing across pages over repeating one page's content.
