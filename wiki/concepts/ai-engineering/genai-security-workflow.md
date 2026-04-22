---
title: GenAI Security Workflow
type: concept
created: 2026-04-22
updated: 2026-04-22
sources: [gartner-genai-security-workflow]
tags: [ai-security, genai, workflow, gartner, data-security-debt, human-in-the-loop, guardrails]
---

# GenAI Security Workflow

The 6-stage model for securing GenAI systems end-to-end, mapped from Gartner research (Oct 2025). Each stage has distinct security risks requiring dedicated tool chains — no single centralized console covers all stages.

---

## Core Model: Six Stages

| Stage | Security Goal | Primary Threats |
|---|---|---|
| **1. Data (Acquisition)** | Ingest only safe, protected data | Data polymorphism, proliferation, poisoning, leakage, toxic data, data security debt |
| **2. Model** | Protect model from attacks and exploits | Supply chain risks, model leakage/inversion, model evasion, model tampering |
| **3. Generation** | Outputs must be 3H-compliant and not misused | Non-3H outputs, output misuse/disinformation |
| **4. Deployment** | Secure runtime, APIs, and infrastructure | API hijacking, DoS/cost exhaustion, model theft/extraction |
| **5. Compliance & Monitoring** | Meet regulatory and ethical requirements | Governance gaps, ethical violations, model drift |
| **6. Feedback Loops** | Protect iterative learning from manipulation | Feedback poisoning, sensor/agent spoofing |

The workflow is continuous and agile — analogous to DevOps/DevSecOps. It emphasizes ongoing learning, iterative improvement, and model retraining.

---

## Cross-Cutting Design Principles

### Human in the Loop

Required at every stage. Not a nice-to-have — a structural necessity for:
- Validating outputs that automated tools can miss
- Interpreting complex regulatory requirements
- Adapting to evolving compliance requirements
- Providing nuanced oversight for ethical edge cases

### Guardrails

Controls that span multiple stages (generation, deployment, feedback). Implement content moderation, DLP, and safety constraints as a unified layer.

**Tools:** OpenAI Moderation API, NVIDIA NeMo Guardrails, Hugging Face transformers, AWS Toxic Content Detector, Intel FakeCatcher.

### Constitutional AI

See [[ai-engineering/constitutional-ai]].

### TRiSM

Gartner's **Trust, Risk, and Security Management** meta-framework for AI. Combined with 3H principles via Constitutional AI workflow. Operates as the governance layer across all stages.

---

## Key Concept: Data Security Debt

Technical and governance debt related to data security that accumulates silently — often unaddressed because unstructured data receives lower priority. GenAI initiatives expose this debt sharply: without classification, sensitivity labeling, and access controls, secure AI deployment is blocked.

**Countermeasures:**
- Develop and maintain data catalogs, data maps, and data flow diagrams
- Implement sensitivity labeling for unstructured data
- Deploy DSPM (Data Security Posture Management) tools
- Address this early — it compounds throughout the AI lifecycle

---

## Threat Taxonomy

### Data Stage
- **Data polymorphism** — conflicting copies of unstructured data with inconsistent metadata/security; model trains on contradictory inputs
- **Data proliferation** — more data used than necessary, including sensitive/restricted data
- **Data leakage** — unauthorized access to training data exposed via model outputs
- **Data poisoning** — attacker corrupts training dataset to manipulate model behavior
- **Biased/toxic data** — data producing stereotypes or harmful outputs

### Model Stage
- **Model leakage/inversion** — proprietary training data extracted by querying the model
- **Model evasion** — adversarial inputs that look normal but cause misclassification
- **Model tampering** — unauthorized modification of trained model weights

### Deployment Stage
- **API hijacking** — mass-querying API to reconstruct model weights (model extraction via API)
- **Cost exhaustion attacks** — malicious queries designed to drive up compute costs
- **Model theft/extraction** — reverse-engineering model behavior through query analysis

### Feedback Stage
- **Feedback poisoning** — fake reports injected to corrupt model retraining
- **Sensor/agent spoofing** — attackers spoof input sensors to suppress alerts or trigger false alarms

---

## Regulatory Landscape (as of Oct 2025)

- **GDPR** — privacy regulation, applies to AI data handling
- **EU AI Act** — dedicated AI regulation framework
- **US** — no federal AI law; sector-specific (FTC); state-level: Texas HB4 (data privacy), TRAIGA (AI governance)

**Principle:** Work use-case-by-use-case on AI ethics. Universal ethics checklists often silence awareness when most needed.

---

## Related Pages

- [[ai-engineering/constitutional-ai]]
- [[ai-engineering/rag-approaches]]
- [[sources/ai-engineering/gartner-genai-security-workflow]]
- [[glossary]]
