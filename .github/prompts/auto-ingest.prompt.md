---
name: auto-ingest
description: "Use when: user says 'ingest the new file' or similar without specifying a source. Auto-detects unprocessed sources and routes to /ingest-wiki."
---

# Auto Ingest

When the user says "ingest the new file" (or similar phrasing without specifying a source), use this workflow to detect which file to ingest.

## Workflow

1. Read `raw/ingested.md` to get the list of already-ingested PDFs
2. Read `raw/clips/ingested.md` to get the list of already-ingested clips
3. List all PDFs in `raw/` (non-recursive) that are not in `raw/ingested.md` — **do not treat `.md` files in `raw/` root as ingestable sources**
4. List all `.md` files in `raw/clips/` (excluding `ingested.md` itself) that are not in `raw/clips/ingested.md`
5. Combine both lists

## Decision

- **If exactly one file has not been ingested:** Route to `/ingest-wiki` with that filename as the source
- **If more than one file has not been ingested:** List them and ask the user which one to ingest, then route to `/ingest-wiki` with the chosen source
- **If all files have been ingested:** Inform the user that everything is up to date

## Next Step

Once the source is identified, invoke `/ingest-wiki` to proceed with the full ingestion workflow.
