---
title: Constitutional AI and 3H Principles
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [gartner-genai-security-workflow]
tags: [ai-security, 3H, constitutional-ai, anthropic, generation-security, TRiSM]
---

# Constitutional AI and 3H Principles

Framework for governing GenAI output quality and safety. The 3H principles — **Helpful, Honest, Harmless** — provide the evaluative standard; Constitutional AI provides the architectural mechanism for enforcing it.

---

## 3H Principles (Anthropic)

Popularized by Anthropic, the 3H framework defines the three required properties of trustworthy GenAI output:

| Principle | Meaning |
|---|---|
| **Helpful** | Output must serve the user's legitimate needs effectively |
| **Honest** | Output must not mislead, deceive, or fabricate |
| **Harmless** | Output must not cause harm to the user or third parties |

The 3H framework is the primary output quality standard at the **generation stage** of the GenAI workflow, but it also informs model training (helpful data) and feedback loops (honest self-correction).

---

## Constitutional AI

**Definition:** A formalized set of high-level directives or principles that govern the output and behavior of an AI system — either implemented by the CISO/developer or encoded so the AI governs itself.

**Purpose:** Ensures AI outputs consistently align with 3H principles. Acts as a governance layer over the generation stage.

**Multi-constitution principle:** In complex environments, organizations may maintain multiple constitutions tailored to different use cases or audiences, providing flexibility for specific operational needs.

**Cross-cutting scope:** Constitutional AI has the most measurable impact at the generation stage but also spans:
- **Model stage** — informs use of helpful training data
- **Feedback stage** — enables honest self-correction

---

## Enforcement Tools

Real-time enforcement of 3H through content moderation and rule injection:

- **Microsoft Guidance** — generation-time rule injection
- **Anthropic Claude API** — built-in constitutional checks
- **OpenAI Moderation API** — real-time content scanning
- **NVIDIA NeMo Guardrails** — policy enforcement layer for LLM applications
- **AWS Toxic Content Detector** — content safety screening
- **Intel FakeCatcher** — deepfake/synthetic content detection
- **Google SynthID / Adobe ContentID** — watermarking for AI-generated content

---

## TRiSM (Trust, Risk, and Security Management)

Gartner's meta-framework for AI governance. Operates as the overarching governance structure within which Constitutional AI and 3H principles are implemented. Combined with Constitutional AI, TRiSM addresses the full governance stack: trust (helpful, honest), risk (harmless), and security (hardened deployment).

---

## Relationship to GenAI Security Workflow

Constitutional AI is not a stage-specific control — it is a cross-stage framework:

```
Model stage → training data quality (helpful)
Generation stage → output filtering and real-time moderation (3H enforcement)
Feedback stage → self-correction and drift prevention (honest)
```

---

## Related Pages

- [[ai-engineering/genai-security-workflow]]
- [[sources/ai-engineering/gartner-genai-security-workflow]]
- [[glossary]]
