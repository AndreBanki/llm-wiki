---
title: "Implement AI Security in the Generative AI Workflow"
type: source
created: 2026-04-22
updated: 2026-04-22
sources: [gartner-genai-security-workflow]
tags: [ai-security, genai, workflow, gartner, 3H, constitutional-ai, data-security-debt, TRiSM]
---

# Implement AI Security in the Generative AI Workflow

Gartner research note mapping security controls to each stage of the GenAI workflow — the canonical 6-stage model for securing AI development and deployment.

---

## Metadata

| Field | Value |
|---|---|
| **Authors** | Joerg Fritsch, Marissa Schmidt, et al. |
| **Publisher** | Gartner |
| **Date** | 17 October 2025 |
| **ID** | G00832004 |
| **URL** | [https://www.gartner.com/doc/reprints?id=1-2MS6Q352&ct=260129&st=sb](https://www.gartner.com/doc/reprints?id=1-2MS6Q352&ct=260129&st=sb) |
| **Domain** | AI Engineering / AI Security |

---

## Key Findings

1. GenAI workflows follow a unique 6-stage process — each stage requires distinct security controls; no single centralized console covers all of them.
2. Many organizations face **data security debt** — unaddressed data governance work that GenAI adoption forces to the surface.
3. **Continuous feedback loops** are not optional: they are needed to detect model drift, remediate vulnerabilities, and maintain 3H (helpful, honest, harmless) outputs.
4. **Human in the loop** is a required architectural element at every stage, not a nice-to-have.

---

## The Six-Stage GenAI Workflow

### Stage 1: Data (Acquisition)

Data ingested by GenAI must be safe, protected, and free from security risks. Includes converting raw data to tokens and vector embeddings.

**Key threats and countermeasures:**

| Threat | Description | Countermeasures |
|---|---|---|
| **Data polymorphism** | Conflicting copies/versions of unstructured data with inconsistent metadata/security | DSPM tools, eliminate duplicates, address versioning |
| **Data proliferation** | More sensitive data used than necessary | Data minimization techniques |
| **Data leakage/sensitive data exposure** | Unauthorized access to training data via model outputs | Anonymization, masking, pseudonymization, differential privacy |
| **Data poisoning** | Attacker introduces corrupted/misleading data into dataset | Secure ingest, monitor supply chain, control prompt injection |
| **Biased or toxic data** | Data leading to biased or harmful outputs | Security guardrails, content filtering |
| **Data security debt** | Accumulated unaddressed data governance work | Data catalogs, data maps, classification and sensitivity labeling |

### Stage 2: Model

Protect the underlying AI model from attacks and vulnerability exploits.

**Key threats and countermeasures:**

| Threat | Description | Countermeasures |
|---|---|---|
| **Software/supply chain risks** | Vulnerabilities in model dependencies and third-party software | SCA tools (e.g., scan Python packages for CVEs), third-party risk management |
| **Model leakage/inversion** | Proprietary/regulated training data extracted from the model | Canary testing, pretrain with less-sensitive data + fine-tune, adversarial robustness testing |
| **Model evasion** | Slightly modified inputs cause model to misclassify or misbehave | Input validation, model monitoring, adversarial training, incident response |
| **Model tampering** | Attacker modifies trained model weights | Code/model signing, TensorFlow Privacy to conceal weights |

### Stage 3: Generation

Control what the model outputs. Focus on ensuring outputs are 3H-compliant and preventing misuse.

**Two categories:**
1. **Preventing non-3H output** — Constitutional AI framework; real-time content moderation
2. **Preventing output misuse** — Watermarking, access logging, takedown playbooks

**Constitutional AI** — a formalized set of high-level directives/principles governing AI output and behavior. Ensures 3H alignment. Organizations may maintain multiple constitutions tailored to different use cases.

**Tools mentioned:** OpenAI Moderation API, NVIDIA NeMo Guardrails, DSPM, Hugging Face transformers, AWS Toxic Content Detector, Intel FakeCatcher, Google SynthID, Adobe ContentID.

### Stage 4: Deployment

Protect the GenAI system in production: secure APIs, runtime environments, and ongoing integrity.

| Threat | Description | Countermeasures |
|---|---|---|
| **API hijacking** | Mass-querying API to reconstruct model weights | Auth/MFA, scope-based access (Open Policy Agent) |
| **DoS/cost exhaustion** | Flooding model with requests to cause outages or cost spikes | API gateways, rate limiters, quotas, load balancers, traffic filtering, Falco |
| **Model theft/extraction** | Reverse-engineering model internals via query analysis | Rate limits, authentication, adversarial training, anomaly detection |

### Stage 5: Compliance and Monitoring

Implement regulatory compliance, audit logging, bias detection, and model drift monitoring.

**Key regulatory contexts:** GDPR, EU AI Act. No US federal AI law as of Oct 2025; several states have laws (Texas HB4, TRAIGA).

**Key principle:** Don't create a universal AI ethics checklist. Develop a use-case-by-use-case ethics procedure — blanket policies silence awareness when most needed.

**Tools:** LangChain, LlamaIndex (data flow monitoring), bias detection tools (fairness across demographics).

### Stage 6: Feedback Loops

Feedback from users, sensors, and AI agents is used to enhance output, optimize data, or retrain models.

| Threat | Description | Countermeasures |
|---|---|---|
| **Feedback poisoning** | Fake feedback injected to manipulate model training | Canary-mode sandbox testing, anomaly detection |
| **Sensor/agent spoofing** | Attackers spoof sensors/agents to manipulate input data | Feedback provenance verification, signing/attestation |

---

## Cross-Cutting Controls

**Guardrails** — span generation, deployment, and feedback stages. Implement multiple controls simultaneously.

**Human in the loop** — required at every stage. Validates outputs, interprets compliance requirements, provides nuanced oversight that automated systems cannot.

**TRiSM (Trust, Risk, and Security Management)** — Gartner meta-framework for AI governance; combined with 3H principles via constitutional AI workflow.

---

## Key Recommendations

1. Incorporate stage-specific safeguards (data classification, model red teaming, guardrails for multistep architectures, data leakage prevention)
2. Consolidate governance with an AI security platform spanning multiple environments (full consolidation currently unachievable)
3. Mature data provenance — budget for DSPM, entitlement management, and bias detection tools
4. Automate model security: integrate vulnerability scanning, model drift detection, red teaming, and adversarial testing into CI/CD
5. Institute constitutional AI and human-in-the-loop processes focused on TRiSM and 3H

---

## Related Pages

- [[ai-engineering/genai-security-workflow]]
- [[ai-engineering/constitutional-ai]]
- [[ai-engineering/rag-approaches]]
- [[ai-engineering/pageindex]]
- [[glossary]]
