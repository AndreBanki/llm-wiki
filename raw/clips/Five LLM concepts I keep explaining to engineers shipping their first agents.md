---
title: "Five LLM concepts I keep explaining to engineers shipping their first agents"
source: "https://generativeai.pub/five-llm-concepts-i-keep-explaining-to-engineers-shipping-their-first-agents-87c502f3c378"
author:
  - "[[Harika Yenuga]]"
published: 2026-04-17
created: 2026-05-01
description: "Five LLM concepts I keep explaining to engineers shipping their first agents The model is simple. It is in these five operating characteristics that teams truly burn out. I’ve spent the last few …"
tags:
  - "clippings"
---
*The model is simple. It is in these five operating characteristics that teams truly burn out.*

I’ve spent the last few years building ML systems for a living, and the last stretch of that has been on LLM-based products, including a coding agent I now use daily. The pattern I see with engineers moving into this space, even strong ones, is that the model alone doesn’t cause the trouble. The trouble comes from a small set of operating characteristics that don’t behave like anything else in software, and most teams learn them by getting burned.

These are the five I end up explaining most regularly. None of them are research-grade. All of them will save you a week of confused debugging.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*C8bDUqQx7bTUb7lDgaAHvw.png)

Image generated with AI tool

## 1) Context window

Instead of treating it as document length, treat it as RAM. The same bounded buffer contains everything the model can view at the moment, including your system prompt, the conversation history, every tool output, and every prior response. You don’t receive a helpful error when you go over it. The model will no longer be able to access anything that slid off the back as a result of truncation.

Engineers frequently make the error of confusing “the model has a 200K context” with “I can use 200K.” System instructions, tool schemas, previous turns, and everything your retrieval layer throws in are all part of that budget. Before the model has completed any significant work, a simple read of three medium files and a few tool answers can use 30 to 50K on a coding agent.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*OrXhURyS7-dY9DXeCjMQcA.png)

Image generated for Context window by author using AI tool

At every stage of the design process, it is your responsibility to determine what the model truly needs to see as opposed to what it can obtain on demand. The majority of agent architecture is based on that choice. When this is done well, teams create systems that grow smoothly beyond simple demos. Teams that don’t end up with agents that perform well on toy tasks but deteriorate when faced with a real workload.

## 2) Tokens

The unit price and restrictions really run on. The model’s tokenizer creates tokens, which are sub-word fragments. The count deviates from your character or word intuition in ways that are significant for cost.

A few things worth internalizing.

Tokenization in code is worse than in prose. Tokens are consumed by brackets, underscores, indentation, and identifiers. A 200-line Python file is typically closer to 3K tokens than 2K.

Non-English text tokenizes much worse than English in most production tokenizers. If your product touches Japanese, Arabic, or Hindi, expect 2 to 4x the token count for the same semantic content. This breaks naive cost models built on English benchmarks.

Structured output (JSON, XML) costs more than the equivalent prose. Schema enforcement is not free.

The approach I would advocate is to run a representative sample of your actual workload through the tokenizer for the model you are using before shipping anything that scales. Avoid estimating based on word counts. The estimate will be inaccurate, usually by a significant amount and always in the direction of higher costs.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XVmjkHA0MhXbs9UgmNzX7w.png)

Image generated for Tokens by author using AI tool

## 3) Temperature

A scalar that regulates the sampler’s aggressiveness in selecting tokens with lower probability. Although correct, the framing as a “creativity dial” is vague. My preferred framing for production work is that temperature regulates tail risk and reproducibility.

For anything where correctness matters more than variety, temperature should be at or near zero. Tool-calling agents, structured extraction, classification, code generation against a spec. For both dependability and your own debugging capabilities, you want the model to make the same call given the same input.

The case for higher temperature is narrower than people assume. It’s appropriate when you genuinely want diverse samples (generate ten variants and pick), or for tasks where the space of acceptable answers is large and you’re not trying to hit a specific one. Brainstorming, creative copy, name generation. Outside those cases, raising temperature is usually a mistake people make once, can’t reproduce a bug, and learn from.

For the majority of hosted APIs, temperature zero is not deterministic in reality. This is important to note because it is often misinterpreted. Routing, mixed-precision math, and batching all still have nondeterminism. True reproducibility requires seeded inference on infrastructure under your control, and even then, the assurances are not as strong as many might think.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sC05K8SeSNC3yxaEp1DDPQ.png)

Image generated for Temperature by author using AI tool

## 4) Hallucination

A confident, fluid, misleading assertion is generated by the model. My preferred framing for junior engineers is that the model should be viewed as a pattern continuation engine that has been educated on a wealth of knowledge, not as a knowledge base. It generates a strong pattern for what an answer might look like when it lacks a strong pattern for the actual response. Those two outputs look identical to you, and the model gives you no reliable internal signal to tell them apart.

It took me the longest to explain to colleagues that hallucinations behave more like a feature of these systems than a fault that needs to be fixed. It is within your control at the system layer.

The needle is really moved by three controls. Instead of asking the model to recall, ground it in retrieved source material. Use controlled generation, function signatures, or schemas to limit the output space. Before taking any action, be sure the output is correct, especially if there are any adverse effects. Anybody who claims that a particular model “doesn’t hallucinate” is trying to sell you something.

Specifically for coding agents, created APIs are the cause of failure to be on the aware of. With seemingly correct arguments, the model will confidently call a function that does not exist on a library. Feedback in the loop is not the answer to better prompting.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*HDcBDGeTwTTFiz25yW-ZkA.png)

Image generated for Hallucination by author using AI tool

## 5) Retrieval-Augmented Generation

The architecture that gets the most credit for working and the most blame for failing. RAG is best understood as a system rather than a model technique. You index your data, retrieve relevant chunks at query time, and pass them to the model as context.

The model is the simple part where the part that no one tells you about. Retrieval is the hard job that determines whether your RAG system is embarrassing or helpful. Chunking strategy, embedding model choice, hybrid search, reranking, query rewriting, evaluation. The LLM you’re utilizing behind it is more important than any of that, and none of it is attractive.

What does your retrieval recall look like at k=10 on a held-out assessment set? is the diagnostic question I pose to teams whose RAG system is performing poorly. The majority of teams have never measured it. They have been accusing the model of obtaining incorrect documents.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KvVkLqZwpTA2fFqwK2XcRA.png)

Image generated for RAG by author using AI tool

## What I’d actually leave you with

If you’re newer to building on LLMs and you only internalize one of these, make it the context window. Every architectural choice you make is shaped by this limitation, which also happens to be the one that breaks so gradually. Eventually, everything else makes an announcement. Context budgets just cause your system to become less effective until you question why it ceased functioning.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*jJHO5VQHzMJoh2vL.png)

This story is published on [Generative AI](https://generativeai.pub/). Connect with us on [LinkedIn](https://www.linkedin.com/company/generative-ai-publication) and follow [Zeniteq](https://www.zeniteq.com/) to stay in the loop with the latest AI stories.

Subscribe to our [newsletter](https://www.generativeaipub.com/) and [YouTube](https://www.youtube.com/@generativeaipub) channel to stay updated with the latest news and updates on generative AI. Let’s shape the future of AI together!

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*3ev1HRF6RTAKQzJR.png)