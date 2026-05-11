---
title: "How Anthropic PMs Ship Features in 45 Minutes (Without Writing PRDs)"
source: "https://medium.com/agileinsider/how-anthropic-pms-ship-features-in-45-minutes-without-writing-prds-50102a25bdfc"
author:
  - "[[Shailesh Sharma]]"
published: 2026-04-25
created: 2026-05-11
description: "If you are still writing 15-page strategy documents, your career is already over."
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*YtA5_Ves0XQfCZ3_yyRsQg.png)

## If you are still writing 15-page strategy documents, your career is already over.

## [The Last Product Manager](https://medium.com/agileinsider/the-last-product-manager-401c91b60574?source=post_page-----50102a25bdfc---------------------------------------)

### Most PMs are on the wrong side

medium.com

In this artcile we will see the exact workflow that is being used by the Top Companies like Anthropic, Shopify, etc

The average Product Manager spends 40% of their week writing Jira tickets, updating roadmaps, and arguing over edge cases in 15-page Product Requirements Documents (PRDs).

At elite AI labs like Anthropic, Senior PMs spend exactly 0% of their week doing this.

Instead, a PM has an idea. They write a concise, 3-paragraph Product Note.

They drop it into an automated agentic workflow. 45 minutes later, there is a functional, tested Pull Request (PR) waiting in GitHub for engineering review.

No refinement meetings. No 15-page PRDs. No six-week development cycles.

This is not a sci-fi prediction for 2030. This is happening *right now*.

It is called the **Execution Collapse** — the cost and time of turning a product thought into production code has effectively dropped to zero.

To survive the next wave of tech, you have to become an “Orchestrator.”

> Orchestrators don’t write PRDs. They write `***context.md***` files.

## The PM Workflow of 2026

### Step 1: The Product Note (The Seed)

You no longer write a PRD. You write a “Product Note.”

==This is a raw, 3-to-4 paragraph summary of the user intent, the desired outcome, and the specific metrics you want to move.==

It is pure strategy, stripped of any implementation details.

### Step 2: The Injection (context.md)

This is the secret weapon. The PM takes the Product Note and feeds it into an orchestrating LLM, but they inject two critical system files alongside it to constrain the AI’s hallucinations:

**product\_area\_context.md:** Maintained strictly by the PM. This file defines the rigid business rules.

- *Example Content:* Free users can only generate 5 reports per day. Do not allow PDF exports for Free Tier. If a user hits a paywall, route them to /upgrade. Our tone is professional, never conversational.”

**code\_context.md:** Maintained by the engineering lead. This file maps the current technical reality.

- *Example Content:* “We use React for the frontend and Python/FastAPI for the backend. All user data must pass through the auth\_v2 middleware. Our database schema for users is located in /db/schema/users.sql.”

### Step 3: The Functional Spec & The PM Review (The New Hero Skill)

The Orchestrator LLM synthesises the Product Note with the strict constraints of the Context files.

It instantly generates a highly technical **Functional Spec**.

*This is the new job of the Product Manager.* You don’t write the spec from scratch; you *evaluate* it.

You act as the Editor-in-Chief.

You review the AI’s logic, check for edge cases it missed, verify it adhered to the `product_area_context.md` rules, and adjust its assumptions. You are the taste-maker and the final human in the loop.

Once you approve it, you hit “Proceed.”

### Step 4: Tech Spec to Autonomous PR

Once the PM approves the Functional Spec, the workflow becomes fully autonomous.

1. The agent converts the Functional Spec into a **Tech Spec** (defining architecture and data models).
2. The agent hands the Tech Spec to a coding model (like Claude 4.6).
3. The coding model writes the actual code, runs the unit tests, and automatically raises a Pull Request in GitHub.

**Total time elapsed: 45 minutes.** — -

## [\*FREE\* 90-Day Plan: Become an AI PM (starting from Zero)](https://medium.com/agileinsider/90-day-plan-become-an-ai-pm-starting-from-zero-9ce902f4904c?source=post_page-----50102a25bdfc---------------------------------------)

### If I Had to Start Over in 2026

medium.com

## The Terrifying Future of Product Management

Read that workflow again. At no point did the PM schedule a backlog refinement meeting.

At no point did they write a user story in Jira.

The Execution Collapse means that engineering execution is rapidly becoming a commodity.

In this new reality, companies don’t need 50 Product Managers to coordinate sprints.

They need 5 elite PMs who understand how to structure `context.md` files, evaluate AI logic, and orchestrate autonomous agents.

If you don’t understand how to build these pipelines, you are fighting a losing battle against a PM who does.

> [FREE Book Giveaway — AI & Tech Simplified](https://topmate.io/technomanagers/1084615)

## Stop Coordinating. Start Orchestrating.

Understanding that this is the future is just a theory.

Actually building these agentic workflows for your own product is how you survive the transition.

You cannot learn this by just reading Medium articles. You have to build it.

If this article changed how you think about Product Management in the AI Era, you will find much [more depth in our AI PM course](https://topmate.io/technomanagers/new/fK374qFpvL).

Check our **highest-rated AI PM course (Including AI PM Interview Preparation) · 4.9/5 · 600+ enrollments →** [**See testimonials and course details**](https://topmate.io/technomanagers/new/fK374qFpvL)

## About Author

[*Shailesh Sharma*](https://www.linkedin.com/in/shailesh-sharma/)*! I help PMs and business leaders excel in Product, Strategy, and AI using First Principles Thinking.* [***Weekly Live Webinars/MasterClass ( Here )***](https://topmate.io/technomanagers)

## [AI Product Management 2026 — Winner’s Playbook](https://medium.com/agileinsider/ai-product-management-2026-winners-playbook-7ee3aa6dc057?source=post_page-----50102a25bdfc---------------------------------------)

### Do this to win in 2026

medium.com