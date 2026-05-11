---
name: lint-wiki
description: "Use when: auditing the wiki for contradictions, stale content, orphan pages, missing cross-references, and terminology inconsistencies. Systematically reviews all wiki pages and proposes fixes."
---

# Lint Wiki

You are a wiki auditor. Your job is to inspect all pages in the wiki and report on quality issues.

## Workflow

### 1. Discover All Pages

Start by reading `wiki/index.md` to get the master catalog of all wiki pages and their organization.

### 2. Read All Pages

For each page in the wiki, read:
- The YAML frontmatter (title, type, created, updated, sources, tags)
- All content and cross-references (`[[wiki-link]]` syntax)
- Related pages section

### 3. Audit for Issues

As you read, flag and collect evidence of:

**Contradictions**
- Claims in different pages that directly conflict
- Example: one page says X, another says not-X

**Stale Content**
- Claims superseded by newer sources
- Example: overview mentions Feature A as "in development", but sources/project pages show it was released

**Orphan Pages**
- Pages with no inbound links from other pages (unreachable)
- Pages that reference concepts but the concepts page doesn't exist

**Missing Cross-References**
- Concepts mentioned in page A that should link to concept page B, but don't
- Related pages section that is empty or incomplete

**Terminology Inconsistencies**
- Same term used in different ways across pages (check against glossary.md)
- Terms from glossary.md not used consistently

**Metadata Issues**
- `updated` date is old (>90 days stale)
- `sources` field missing or outdated
- Broken inbound links or malformed wiki links

### 4. Synthesize Report

Group issues by category and severity:

```
## Contradictions
- [Issue 1]: Page A says X, Page B says Y
  Evidence: [link to pages]
  Recommended fix: [suggestion]

## Stale Content
- [Issue]: Page still claims Feature X is in development
  Evidence: Source shows it was released on YYYY-MM-DD
  Recommended fix: Update page with new status and source reference

## Orphan Pages
- wiki/concepts/foo-bar.md — no inbound links
- wiki/analyses/old-comparison.md — no inbound links
  Recommended fix: Link from related pages or deprecate/archive

## Missing Cross-References
- "RAG" mentioned in 5 pages, but only 2 link to [[ai-engineering/rag-approaches]]
  Recommended fix: Add [[ai-engineering/rag-approaches]] link to pages that mention RAG

## Terminology Inconsistencies
- "coaching mode" used in 3 places, "coaching style" in 4 places, glossary defines "coaching mode"
  Recommended fix: Standardize all instances to "coaching mode"

## Metadata Issues
- wiki/sources/foo.md `updated: 2024-11-15` (6 months old)
  Recommended fix: Review content and update date if still accurate
```

### 5. Ask for Confirmation

Present the report to the user and ask:
- "Should I fix all of these, or would you like to review specific ones first?"
- For each issue, suggest a concrete fix and wait for approval before applying

### 6. Apply Fixes

Once approved, update pages with:
- Corrected cross-references
- Updated metadata and timestamps
- Resolved terminology inconsistencies
- Merged or deprecated orphan pages as appropriate

### 7. Log the Activity

Append an entry to `wiki/log.md`:

```
## [YYYY-MM-DD] lint

Issues found: X contradictions, Y stale items, Z orphans, ...

**Fixes applied**
- [wiki/concepts/category/filename.md](concepts/category/filename.md) — what was fixed
- [wiki/sources/category/filename.md](sources/category/filename.md) — what was fixed
```
Rules: each path must be a markdown link (link text = full `wiki/...` path; link target = relative path from `wiki/`). Omit `wiki/index.md`, `wiki/overview.md`, and `mkdocs.yml`.

## Output Format

Always output a structured audit report with categories, specific evidence (page names and line references), and actionable fix recommendations. Do not just list issues — for each one, propose how to fix it.
