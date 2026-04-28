---
title: "RAG Is Fundamentally Broken. Here’s Why."
source: "https://generativeai.pub/rag-is-a-hack-heres-why-it-s-fundamentally-broken-6d7aa87f9ddd"
author:
  - "[[Gaurav Shrivastav]]"
published: 2026-04-16
created: 2026-04-27
description: "RAG retrieval blocks gradient flow to the LLM, making end-to-end training impossible. Learn why every patch fails and what CLaRa by Apple changes."
tags:
  - "clippings"
---
## You aren’t fixing bugs when you tune chunk sizes. You are patching over a missing feedback loop that was never there in the first place.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*ELUnkbxielnp7rGuLOdAwA.png)

Credits: Gemini

Three months after shipping my first production RAG system, I got paged at 11 PM.

An enterprise client’s chatbot had pulled the wrong HR policy for a completely different employee tier. The language was similar enough that the retriever thought it matched. It didn’t. I spent two days tuning, smaller chunks, bigger overlap, a different embedding model. The problem kept happening.

That’s when I realized I wasn’t fixing a bug. The flaw was inside the architecture itself, somewhere no chunk size could ever reach.

> **Non members can read** [**here for free**](https://medium.com/@gaurav21s/6d7aa87f9ddd?sk=52f0b5c93e6b04a9ceb566f850f22090)

It wasn’t until I came across Apple’s CLaRa and a technique called Golden Retriever RAG that it finally clicked. Once you see it, you can’t unsee it. Keep reading to understand exactly what that flaw is, why every popular fix only papers over it, and what CLaRa actually does differently.

## Why Do LLMs Need RAG at All? (The Compression Problem)

To understand why RAG is broken, you need to understand what LLMs actually are. Most explanations skip this part and jump straight to the pipeline. That’s a mistake.

**Large Language Models** are not databases. They do not store facts. They do not have lookup tables with “the capital of France is Paris” written somewhere in a file.

What they actually do is compress.

Take LLaMA 3 8B as a concrete example. It was trained on roughly 15 trillion tokens, which represents around 44 terabytes of internet text pulled from CommonCrawl, GitHub, Wikipedia, books, and similar sources. The resulting model file in FP16 precision? About 16 gigabytes.

Think about that ratio for a second. You are taking 44 terabytes of human knowledge and squeezing it into 16 gigabytes. That is not a lossless operation. You cannot do that with a zip file. What’s happening is **lossy compression**, similar to a JPEG cranked up to maximum compression. The model does not memorize facts. It learns statistical patterns. It learns that after “the capital of France is,” the token “Paris” has a very high probability of following. Statistics all the way down.

This works beautifully for generating fluent, contextually appropriate text. It falls apart the moment you need specific, factual recall. A precise date. A contract clause. Your company’s current pricing table. Information that was either too rare to survive the compression intact, or that didn’t exist when training data was collected.

That is the problem RAG was invented to solve.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0gtG9MWMJE_XYYuS26e1eg.png)

Credits: OpenAI

## Hallucinations Are Not Bugs. They Are the Expected Output.

Hallucinations are not failures to fix. They are the predictable result of a lossy compressor being asked to reconstruct data it no longer has.

Compress a photo to 5% of its size and zoom back in. The image doesn’t crash. It invents. It fills missing pixels with plausible-looking patterns that were never there. Blocky, smeared, artifact-riddled. An LLM hallucinating is the exact same thing. Not broken. Just doing what compressed systems do when forced to fill gaps.

For creative writing, that’s fine. For enterprise documents, patient records, or legal contracts, it’s a serious problem. That is why **Retrieval-Augmented Generation** exists: hand the model exact text at query time instead of making it reconstruct from memory.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*02UxLxFeyForIFX1lOfshw.png)

Credits: OpenAI

## What Is Standard RAG and Why Does It Mostly Work?

**Retrieval-Augmented Generation** treats the LLM like a student in an open-book exam. Instead of recalling from memory, it gets the relevant pages handed to it at query time.

The pipeline:

1\. User submits a query

2\. Query gets embedded into a vector

3\. Vector database finds similar document chunks

4\. Matching chunks get pasted into the LLM’s context window

5\. The LLM answers based only on that context

It works. New documents are immediately usable without retraining. That is genuinely useful.

But RAG is a hack. You are gluing together two systems built on completely different principles: a **Retriever** doing vector space math and a **Generator** doing probabilistic token prediction. They were not designed for each other. And that mismatch has a consequence most tutorials never bother to explain.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*nl1xokmM3U_216gDLxzT2Q.png)

Credits: OpenAI

## What Is the Real Problem With RAG? (The Gradient Wall)

Here is the actual flaw. The one that chunk tuning cannot touch.

Modern deep learning works because of **backpropagation**. Every time a neural network makes a mistake, a loss function calculates how wrong the output was. That error signal travels backward through every layer of the network, using the **chain rule** to figure out how much each weight contributed to the mistake. Then each weight gets adjusted accordingly.

This process only works if every step in the chain is differentiable: smooth, continuous, and mathematically well-behaved enough for gradients to flow through.

Now look at what happens in a RAG pipeline during retrieval.

The retriever scores every document in your database against the incoming query. You might have 100,000 documents. Each gets a similarity score. Then the system picks **top K** results. K equals 5, or 10, or whatever you configured. That’s it. Documents above the cutoff go in. Everything else is discarded.

That “pick top K” step is a hard, discrete choice. A document is either in or out. There is no smooth transition. There is no fractional document. There is no continuous function a gradient can flow through.

So when the retriever pulls irrelevant documents and the LLM produces a wrong answer, what happens to that error? The LLM has no mechanism to send the error signal back to the retriever. The math literally does not allow it. The gradient dies at the boundary between the two systems.

The retriever never finds out it made a mistake. Next time an identical query comes in, it makes the same mistake. The LLM cannot say “that document was wrong, adjust your weights.” There is no adjustment. There is no learning. The two components are permanently decoupled, trained in isolation, and that isolation is baked into the architecture.

That is the core problem. Not your chunk size. Not your embedding model. Not your similarity threshold.

The gradient cannot flow. The system cannot learn end-to-end. Everything else is downstream of that.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ZzVSyuFBmMwDtiLJ2vWXBw.png)

Credits: OpenAI

### The Patches People Are Using (And Their Real Costs)

Once you understand the gradient wall, you start to see the entire ecosystem of RAG “improvements” differently. Almost all of them are workarounds. Some are very good workarounds. But they are workarounds.

## Does GraphRAG Actually Solve the Retrieval Problem?

**GraphRAG** replaces flat vector search with a knowledge graph. Instead of finding semantically similar chunks, it builds a graph of entities and their relationships, then traverses that graph to find connected concepts.

For questions about relationships between things, this is genuinely better. “What companies are connected to the executive who left in 2023?” is a question vector search handles poorly. A knowledge graph handles it cleanly.

But GraphRAG is complex to build, expensive to maintain, and it does not touch the gradient problem at all. The retriever is smarter, yes. It still cannot receive feedback from the generator. The decoupling is fully intact.

## Does Putting Everything in the Context Window Work?

This approach skips retrieval entirely. Models like Gemini 2.0 Flash support 1 million token context windows; Gemini 2.0 Pro goes to 2 million. The argument: dump the entire document corpus into the context for every query and let the model figure it out. No retrieval means no retrieval errors.

For bounded document sets and reasoning-heavy tasks, this actually works. The model sees everything.

The problem is physics. Transformer attention is quadratic:

Compute Cost = O(N²)

Where N is the number of tokens in context. Double your context length and you quadruple the compute required. At 1 million tokens, this is expensive. At 2 million tokens, running this inference for every single user query in production is financially brutal. You cannot scale it to real query volumes at real costs.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*c_K55aOnEy2W0DQCnK0jBg.png)

Credits: OpenAI

## Fix the Process: What Is Golden Retriever RAG?

**Golden Retriever RAG** is a process-level fix, and it’s actually clever. The idea is to make the query smarter before it ever reaches the retriever.

The standard flow sends the raw user query directly to vector search. Golden Retriever RAG inserts an LLM-powered reflection step first:

1. The LLM reads the raw user query
2. It identifies jargon, expands abbreviations, adds contextual detail
3. It rewrites the query into an explicit, search-friendly version
4. That expanded query goes to the retriever instead of the original

If someone asks “what was our Q3 ARR delta vs. plan,” the model first expands that to something like “what was the difference between actual annual recurring revenue and the planned revenue target for the third quarter of the fiscal year.” A retriever has a dramatically better chance of finding the right document chunk with that expanded query.

Retrieval accuracy improves. That part is real.

But here’s the honest assessment. You have added an extra LLM call to every single query, which adds latency to the entire pipeline. The fundamental architecture is unchanged. The retriever is still receiving better input, not learning from feedback. You are treating the symptom, not the cause.

More steps built on top of the same broken foundation.

## Fix the Process Better: What Does the Instructed Retriever Do?

Databricks’ **Instructed Retriever**, released in January 2026, is a more ambitious process-level fix. The premise: since you cannot train the retriever with gradients from the generator, guide it with instructions instead.

The retriever gets three upgraded capabilities:

- **Query Decomposition**: Complex multi-part questions get broken into simpler, independently searchable components before hitting the database
- **Contextual Relevance**: Instead of pure vector overlap, the retriever reasons about actual intent and meaning, not just keyword proximity
- **Metadata Reasoning**: When a user asks “sales from last year,” the system converts that into a concrete filter like `date >= 2025-01-01` rather than doing a semantic search over the phrase "last year"

The results from Databricks’ StaRK-Instruct benchmark, designed specifically to test instruction-following retrieval, showed 35 to 50% recall gains over standard RAG. On harder enterprise question-answering tasks requiring precise instruction following, they demonstrated up to 70% improvement.

Those numbers are real. That is not incremental. This is a genuinely useful system.

But it is still a patch. A smart, well-engineered patch built by a strong team. The retriever is not learning from the generator’s outcomes. It has been given better rules upfront. The gradient wall is still there. Databricks is just working more intelligently around it.

## Fix the Architecture: What Is Apple’s CLaRa and Why Is It Actually Different?

**CLaRa** (Continuous Latent Reasoning), published in December 2025 by researchers from Apple and the University of Edinburgh, is the first approach I’ve seen that attacks the gradient wall directly rather than working around it.

Standard RAG takes your document, breaks it into text chunks, embeds those chunks, and retrieves by vector similarity. CLaRa throws out that entire workflow.

Instead it introduces **memory tokens**: compressed representations of pure document content. Not text chunks. Not embeddings of text. Small sets of continuous, learned tokens that encode the semantic meaning of a document at 16x to 128x compression, stripped of syntax noise, filler words, and structural overhead.

Then it introduces a **Query Reasoner**. Rather than matching your query to document embeddings, the Query Reasoner generates a hypothetical ideal answer first, then searches for memory tokens that would support that hypothetical. It is searching for what should be there, not what looks statistically similar.

Here is the piece that changes everything: CLaRa uses a **differentiable top-k estimator** to perform retrieval. That phrase is doing enormous work. It means the selection of which memory tokens to retrieve is not a hard discrete step. It is made mathematically smooth enough that gradients can flow backward from the answer generation step, through the retrieval step, into the Query Reasoner itself.

The retriever can now learn from the generator’s mistakes. End-to-end training is possible. The wall between the two systems, the wall that made standard RAG a permanent hack, comes down.

Apple released three models on Hugging Face: CLaRa-7B-Base, CLaRa-7B-Instruct, and CLaRa-7B-E2E. The E2E variant is the one trained with the full differentiable retrieval loop.

![](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*P2vLNJDf1Civ9d5tK7VoLg.jpeg)

Credits: Apple Research Paper

## What Should You Actually Build With Today?

Here’s the honest answer based on where the field actually is.

**For production systems shipping now**, combine the Instructed Retriever approach with Golden Retriever query expansion. Add a reranker after initial retrieval. Monitor retrieval quality and generation quality as separate metrics, because the problems live in different places and a drop in answer quality might be a retrieval failure, not an LLM failure.

**For structured document domains** like finance, legal, medical, or regulatory, evaluate hierarchical indexing approaches. If your documents have intentional structure (sections, subsections, numbered clauses), vector chunking is actively destroying that structure. Stop rebuilding what was already there.

### Let’s Keep Learning Together

Did this actually help you think differently about RAG or How Fixing the Architecture improves performance? I’d love to hear about it.

- Show your support with a **👏 clap (or many!)**
- Follow me on LinkedIn for more practical AI insights that actually matter

> Follow me on LinkedIn: [Gaurav Shrivastav](https://www.linkedin.com/in/gaurav-shrivastav-gs/)
> 
> Support the work: [https://coff.ee/gaurav21s](https://coff.ee/gaurav21s)