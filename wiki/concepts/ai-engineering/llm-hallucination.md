---
title: LLM Hallucination
type: concept
created: 2026-05-01
updated: 2026-05-01
sources: [Five LLM concepts I keep explaining to engineers shipping their first agents.md]
tags: [hallucination, grounding, rag, output-verification, ai-engineering, llm]
---

Hallucination is when an LLM generates a confident, fluent, incorrect assertion. The key insight for production systems: it is better understood as a feature of the architecture than a bug to be patched — and it is controlled at the system layer, not the model layer.

## The Core Mental Model

**Wrong:** LLMs are knowledge bases that occasionally malfunction and return wrong facts.

**Right:** LLMs are **pattern continuation engines**. They are trained on vast text corpora and learn which token sequences follow which other token sequences — including what a plausible answer looks like.

When a model lacks a strong training pattern for the *actual* answer to a question, it generates a strong pattern for what *an answer to that kind of question looks like*. The two outputs — correct answer and confident wrong answer — look identical to the user. The model provides no reliable internal signal to distinguish them.

---

## Why "Feature, Not Bug" Is the Useful Frame

Calling hallucination a bug implies it can be patched. It cannot, at the model level, because:

1. Pattern completion is the fundamental mechanism that makes LLMs useful
2. The same mechanism that generates fluent correct answers generates fluent incorrect ones
3. Training reduces hallucination frequency but cannot eliminate it for open-ended questions

**The productive reframe:** hallucination frequency is a model property; hallucination *consequences* are a system design choice. Engineers who treat hallucination as a model problem waste cycles hoping for better models. Engineers who treat it as a system problem design mitigations into the architecture.

> "Anybody who claims that a particular model 'doesn't hallucinate' is trying to sell you something." — Harika Yenuga

---

## Three System-Layer Controls

### 1. Ground in Retrieved Source Material

Instead of asking the model to *recall*, provide the relevant content and ask the model to *reason over it*.

This shifts the model from open-ended pattern completion ("what would an answer to this question look like?") to constrained synthesis ("what does this source material say about this question?"). The model can still hallucinate details not in the source, so verification remains necessary, but the failure mode changes from fabricated facts to incorrect synthesis — which is more detectable and correctable.

See [[ai-engineering/rag-approaches]] for retrieval architecture options.

### 2. Constrain the Output Space

Use **schemas, function signatures, or controlled generation** to limit what the model can produce:

- Structured output (JSON with a defined schema) constrains the model to valid field names and value types
- Function signatures define valid tool calls and argument types
- Grammars or constrained decoding (e.g., Outlines, llguidance) restrict token selection to grammatically valid outputs

The smaller the output space, the fewer opportunities for hallucination. The cost is reduced flexibility.

### 3. Verify Before Acting

For any action with real-world consequences — especially irreversible ones — validate the model's output before execution:

- Parse and validate structured outputs against their schema
- Check that referenced entities (files, APIs, IDs) exist before using them
- For tool calls with side effects, confirm the arguments are valid before execution
- For multi-step agent loops, checkpoint between steps

This is especially critical for **coding agents** (see below).

---

## Coding Agent Hazard: Phantom APIs

The most common coding agent hallucination is confident calls to **APIs that do not exist**:

```python
# Model generates this confidently — but get_embedding_by_semantic_query() does not exist
result = vectordb.get_embedding_by_semantic_query(
    query=user_query,
    top_k=5,
    filter={"source": "production"}
)
```

The function name sounds plausible, the arguments look correct, the naming convention matches the library — but the function does not exist. This is not a prompting problem. The fix is feedback in the agent loop: the tool call fails, the error is returned to the model, and the model corrects. Systems without this feedback loop fail silently or require manual debugging.

---

## Relationship to Grounding and RAG

Hallucination and RAG are directly related: RAG's primary value proposition is grounding — reducing hallucination by giving the model source material to reason over rather than open-ended recall space.

However, RAG does not eliminate hallucination. The model can still:
- Misinterpret the retrieved content
- Mix retrieved content with training priors
- Hallucinate details not in the retrieved chunks

The deeper RAG analysis (gradient wall, recall@k=10) applies here too: if retrieval fails to surface the right content, grounding is illusory — the model hallucinates from the absence of evidence. See [[ai-engineering/rag-approaches]].

---

## Related Pages

- [[ai-engineering/rag-approaches]]
- [[ai-engineering/llm-context-window]]
- [[ai-engineering/temperature]]
- [[ai-engineering/genai-security-workflow]]
- [[ai-engineering/ai-agent-governance]]
- [[ai-engineering/harika-yenuga-five-llm-concepts-first-agents]] (source article)
