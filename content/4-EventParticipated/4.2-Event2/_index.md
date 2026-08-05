---
title: "Event 2 - FCAJ x Agentic AI Build Week"
date: 2026-07-25
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Event Report: FCAJ x Agentic AI Build Week: Show Up. Build. Pitch. WIN!

## Overview

By 25 July, I had already studied most of the main building blocks of Shopsflow, so I could connect the team presentations directly to questions I was facing: how much scope is enough, how to explain architecture, how cost fits into a solution, and what makes a demo reliable.

The four presentations were different, but they shared one thing: each team had to turn an idea into a product with a clear flow, architecture, and demo. That was the most useful part for me.

## 1. OneTeam - AI-Powered Conversational Ordering

OneTeam presented a conversational ordering agent for KFC. The interesting part was that real ordering is much harder than a chatbot that only replies to questions: the system needs to handle menu data, quantity, variants, promotions, cart state, and order confirmation.

The **Goal → Plan → Tools → Act → Verify** workflow helped me understand why an AI system still needs trusted tools and real business data before it performs actions.

I also liked the “design once, deploy everywhere” idea. It made me think more carefully about boundaries in Shopsflow: frontend channels, backend API, deployment artifact, and database should not be unnecessarily coupled.

## 2. Signal Scout - Evidence-Driven Strategic Intelligence

Signal Scout focused on detecting strategic changes from multiple evidence sources and presenting them in a decision-support dashboard.

The cost discussion stood out to me because the team did not stop at naming services. They estimated different usage levels and explored a more cost-efficient architecture.

That connected directly to my NAT Gateway and Cross-AZ work in Shopsflow: an architecture can be technically correct and still be expensive if traffic paths are not reviewed.

## 3. Plan V - Solution Architect Professional AI Native App

Plan V proposed an AI Native App that helps Solution Architects extract requirements, draft architecture options, generate diagrams/IaC, and estimate AWS cost.

This was very close to what I was doing manually in my Proposal. The important lesson was that an architecture should surface assumptions and requirement gaps instead of pretending every requirement is already clear.

After this session, I reviewed Shopsflow and separated the current scope from future improvements. I did not want WAF, KMS, Secrets Manager, or autoscaling to appear as completed work without hands-on evidence.

## 4. Team 3KA - 24 Hours of Building, Failing, and Learning

Team 3KA shared their hackathon journey with S.H.E.P.H.E.R.D., combining computer vision, tracking, cloud inference, dashboards, and Agentic AI for crowd monitoring.

What I appreciated most was how honestly they discussed the difficult parts: limited time, first-time AWS experience, broken code, late-night debugging, missed commits, and the pressure of preparing a demo.

The lesson I took from this was simple: a small finished feature is better than a large list of unfinished features. Clear roles, a ready toolkit, and a demo plan matter as much as the idea itself.

## How I changed Shopsflow after the event

After the event, I reviewed every architecture component using three questions: **does it solve a current requirement, have I validated it, and can I explain the trade-off?**

I kept the final scope focused on CloudFront/S3, ALB, ECS Fargate, ECR, RDS, NAT, IAM, CloudWatch, and the payment flow. More advanced services moved to the roadmap.

This event also changed how I wrote the Proposal and Workshop: I tried to tell the story by flow and problem, not by listing AWS services.

## Conclusion

The event showed me that building a solution involves technical decisions, cost, scope, teamwork, and communication at the same time. It also made me more comfortable saying “not yet” to a service when I could not justify or validate it.

## Event materials

[FCAJ x Agentic AI Build Week materials on Google Drive](https://drive.google.com/drive/folders/1goIcF8jRIGZczB4DBHGTsS6mp41FWmLL)

---

## Participation Evidence

{{< report-image src="images/4-EventParticipated/event2-participation-proof.png" alt="Participation evidence for Event 2 - FCAJ x Agentic AI Build Week" width="520px" caption="Figure 2. Photo evidence of my participation in FCAJ x Agentic AI Build Week: Show Up. Build. Pitch. WIN!" >}}
