---
title: LLM Temperature
type: concept
created: 2026-05-01
updated: 2026-05-01
sources: [Five LLM concepts I keep explaining to engineers shipping their first agents.md]
tags: [temperature, sampling, reproducibility, tail-risk, ai-engineering, llm]
---

Temperature controls how aggressively the sampler selects lower-probability tokens. In production, the useful framing is not "creativity dial" but **tail risk and reproducibility regulator**.

## What Temperature Actually Does

Temperature is a scalar applied to the probability distribution over next tokens before sampling. Higher temperature flattens the distribution — making low-probability tokens more likely to be selected. Lower temperature sharpens it — concentrating selection on the highest-probability tokens.

The "creativity dial" framing is correct in a narrow sense but misleading in production: it suggests that raising temperature always produces better, more diverse outputs. In practice, raising temperature primarily **increases variance in correctness**, not creativity.

---

## The Production Framing: Tail Risk and Reproducibility

**Tail risk:** temperature controls the probability of the model selecting a token that is technically possible but unexpected — including both correct surprises (creative outputs) and incorrect ones (hallucinations, format violations, wrong tool calls). Higher temperature raises both.

**Reproducibility:** lower temperature narrows the distribution, making the same input more likely to produce the same output across calls. This matters for:
- Debugging (can you reproduce the failure?)
- Evaluation (are you measuring the same system across runs?)
- Auditability (can you trace why the model made a decision?)

---

## When to Use Low Temperature (Near Zero)

For any task where **correctness matters more than variety**, temperature should be at or near zero:

| Task type | Reasoning |
|---|---|
| Tool-calling agents | Same call, same input → same tool selection required for debugging |
| Structured extraction | Schema adherence matters; variance means format violations |
| Classification | Deterministic labeling across runs |
| Code generation against a spec | Spec-correct output > varied output |
| Routing decisions | Wrong route wastes compute and cascades errors |

The rule: **if you need to verify the output, you need reproducibility, which requires low temperature.**

---

## When Higher Temperature Is Justified

The case for higher temperature is narrower than most engineers expect. It is appropriate when:

1. **You want diverse samples** — generating N variants and selecting the best (brainstorming, name generation, creative copy variants)
2. **The answer space is genuinely large** — no single correct answer exists; exploring the distribution is useful
3. **Variety itself is the product** — e.g., generating distinct creative outputs for A/B testing

Outside these cases, raising temperature is typically a mistake: engineers raise it, can't reproduce a bug, and learn the lesson the hard way.

---

## Critical Production Nuance: Temperature Zero ≠ Deterministic

In most hosted APIs, **temperature=0 is not actually deterministic**. Sources of nondeterminism that persist even at temperature=0:

- **Request routing:** requests may go to different backend servers or model replicas
- **Mixed-precision arithmetic:** floating-point operations on GPU hardware are not strictly reproducible across runs without bit-identical conditions
- **Inference batching:** requests batched together can affect results

**True reproducibility** requires seeded inference on infrastructure under your control — and even then, guarantees are weaker than most engineers assume. For production systems requiring exact reproducibility (e.g., regulatory audit trails), this is a meaningful architectural constraint.

---

## Common Failure Pattern

```
Engineer raises temperature → model produces more varied outputs
→ engineer encounters a bug
→ engineer cannot reproduce the bug
→ engineer files issue blaming "model inconsistency"
→ engineer learns about temperature
```

The systematic mistake: raising temperature is the first lever people reach when outputs feel "too safe." The correct first response to outputs being too safe is improving the prompt, not raising temperature.

---

## Related Pages

- [[ai-engineering/llm-context-window]]
- [[ai-engineering/llm-hallucination]]
- [[ai-engineering/rag-approaches]]
- [[ai-engineering/llm-model-economics]]
- [[ai-engineering/harika-yenuga-five-llm-concepts-first-agents]] (source article)
