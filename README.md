# LLM Wiki (Karpathy Pattern)

A self-maintaining personal knowledge base powered by LLMs, based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285).

Instead of re-searching raw documents on every question (like RAG), the LLM **reads your sources once and builds a persistent, interlinked wiki** that compounds over time. The more sources you feed it, the richer and more connected it gets.

---

## Prerequisites

- Python 3.10+
- [Cursor](https://cursor.sh/) (or any LLM-powered editor that reads a schema file)
- [Obsidian](https://obsidian.md/) (free) for browsing the wiki in real time

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/balukosuri/llm-wiki-karpathy.git
cd llm-wiki-karpathy
```

### 2. Open the project in Cursor

Cursor reads `CLAUDE.md` automatically and understands the wiki's structure, page formats, and workflows.

If you use a different AI agent (Claude Code, Codex, etc.), paste the contents of `CLAUDE.md` into your agent's context.

### 3. Open the same folder in Obsidian

Open the project directory as an Obsidian vault. You'll have two windows side by side — Cursor on the left where you talk to the AI, Obsidian on the right where you browse the wiki as pages appear.

### 4. Drop a source into `raw/`

Any document works:

- Product specs, design docs, or PRDs
- Meeting transcripts
- Web articles (use [Obsidian Web Clipper](https://obsidian.md/clipper) to save pages as markdown)
- Style guides
- PDFs, reports, email threads saved as text
- Competitor documentation

### 5. Say "ingest"

Type this in Cursor:

> ingest raw/my-document.pdf

The AI will:

1. Read the document
2. Discuss key takeaways with you
3. Create a source summary page in `wiki/sources/`
4. Create new pages for any products, features, personas, or concepts it finds
5. Update the glossary with new terms
6. Update the index with all new pages
7. Update the overview if the big picture shifted
8. Log everything in `wiki/log.md`

A single source can touch 5-15 wiki pages. Watch them appear in Obsidian in real time.

### 6. Ask questions

> What are the main risks identified across all my sources?

The AI reads the wiki, synthesizes an answer with citations, and asks: *"Should I save this as a wiki page?"* If you say yes, the answer becomes a permanent analysis page. Your questions make the knowledge base richer over time.

### 7. Lint the wiki

Every 10 ingests or so, run a health check:

> lint the wiki

The AI checks for contradictions between pages, stale claims, orphan pages with no links, missing cross-references, and inconsistent terminology. It reports what it found and asks which fixes to apply.

---

## Local Development

```bash
pip install -r requirements.txt
mkdocs serve
```

The site is available at `http://localhost:8000`.

---

## Deploy on Render.com

The project includes a Python server (`server.py`) that serves the static site with basic authentication (username and password). No extra dependencies beyond the standard library.

### 1. Create the GitHub repository

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<your-org>/llm-wiki.git
git push -u origin main
```

### 2. Create the Web Service on Render

1. Go to [render.com](https://render.com) and log in with GitHub
2. **New** → **Web Service** → connect the repository
3. Configure:

   | Field | Value |
   |---|---|
   | **Name** | `llm-wiki` |
   | **Runtime** | `Python 3` |
   | **Build Command** | `pip install -r requirements.txt && mkdocs build` |
   | **Start Command** | `python server.py` |
   | **Instance Type** | Free |

### 3. Set environment variables

Under **Environment**, add:

| Variable | Description |
|---|---|
| `AUTH_USER` | Site login username |
| `AUTH_PASS` | Site login password |

> **Never commit `.env` to the repository.** The file is already in `.gitignore`.

### 4. Deploy

Click **Create Web Service**. Render will build MkDocs and start the server. The site will be available in ~3 minutes.

Every `git push` to `main` triggers an automatic redeploy.

### Notes

- On the Free plan, the service sleeps after 15 min of inactivity (~30s to wake on the next request)
- To change the password, update `AUTH_PASS` in the Render environment variables (no redeploy needed)
- Share credentials with your team through a secure channel

---

## Repo Structure

```
llm-wiki-karpathy/
├── CLAUDE.md          # Schema — the AI's operating manual
├── llm-wiki.md        # Karpathy's original idea document
├── article.md         # Walkthrough article explaining this project
├── requirements.txt   # Python dependencies (MkDocs Material)
├── server.py          # Static site server with basic auth (for Render deploy)
│
├── raw/               # Your source documents (AI reads, never writes)
│   └── .gitkeep
│
├── wiki/              # AI-generated knowledge base (AI owns this layer)
│   ├── index.md       # Master catalog — the AI reads this first on every query
│   ├── overview.md    # Big-picture synthesis (evolves with each ingest)
│   ├── glossary.md    # Terms, definitions, and style conventions
│   └── log.md         # Chronological record of all activity
│
└── .obsidian/         # Pre-configured Obsidian vault settings
```

### How the layers work

| Layer | Folder | Who owns it | Purpose |
|-------|--------|-------------|---------|
| Raw sources | `raw/` | You | Immutable source documents. The AI reads from here but never modifies anything. |
| The wiki | `wiki/` | The AI | Structured, interlinked markdown pages. The AI creates, updates, and maintains everything here. |
| The schema | `CLAUDE.md` | You + AI | Defines page types, workflows, and conventions. Edit this to customize the AI's behavior for your domain. |

### Wiki page types

The AI creates different page types depending on what it finds in your sources:

| Type | Location | What it captures |
|------|----------|-----------------|
| Source | `wiki/sources/` | Summary of a raw document — key facts, quotes, metadata |
| Feature | `wiki/features/` | A product feature — what it does, how it works |
| Product | `wiki/products/` | A product or tool — overview, versions, related features |
| Persona | `wiki/personas/` | A user type — goals, pain points, expertise level |
| Concept | `wiki/concepts/` | A domain idea — definition, related terms, common misconceptions |
| Style Rule | `wiki/style/` | A writing convention — when to apply, examples, exceptions |
| Analysis | `wiki/analyses/` | A synthesized output — comparison table, gap analysis, outline |

---

## Customizing for Your Domain

The schema file `CLAUDE.md` is not set in stone. Edit it to fit your needs:

- **Add new page types.** If your domain needs "API endpoints" or "customer segments" or "recipe variations", add them to the entity types table and tell the AI.
- **Change the ingest workflow.** If you want the AI to skip the discussion step and just process silently, update the workflow section.
- **Adjust output formats.** The AI can produce markdown pages, comparison tables, doc outlines, release notes drafts, or persona briefs. Add formats that make sense for your work.

---

## Tips

**Ingest one source at a time.** You can batch-ingest, but you lose the chance to guide the AI. Stay involved — read the summaries, tell it what to emphasize, ask follow-ups during ingestion.

**Save your best questions.** When you ask something and get a useful answer, tell the AI to save it as an analysis page. Your explorations compound in the wiki instead of disappearing into chat history.

**Use graph view often.** Press `Cmd+G` in Obsidian. The visual map shows which pages are hubs, which are orphans, and how everything connects.

**Check the glossary before writing.** Open `wiki/glossary.md` before you write anything. It has the right terms, the wrong terms, and the reasons behind each choice.

**Don't write wiki pages yourself.** Your job is to find good sources and ask good questions. The AI handles the summarizing, cross-referencing, filing, and bookkeeping.

---

## Use Cases

- **Technical writers** — Ingest specs, transcripts, and competitor docs. Get a living glossary, persona pages, and structured outlines without writing them yourself.
- **Researchers** — Feed it papers, articles, and reports over weeks. End up with a wiki that has an evolving thesis and all the connections already made.
- **Product managers** — Ingest PRDs, customer interviews, competitive analyses, and retros. The wiki maintains the big picture.
- **Students** — Ingest textbook chapters one at a time. The AI builds concept pages, links them together, and flags connections between chapters.
- **Anyone accumulating knowledge** — Trip planning, hobby research, health tracking, course notes, book clubs. Anything where information comes from multiple sources and you want it organized.

---

## Credits

- Pattern by [Andrej Karpathy](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285)
- Implementation and article by [Balu Kosuri](https://github.com/balukosuri)
