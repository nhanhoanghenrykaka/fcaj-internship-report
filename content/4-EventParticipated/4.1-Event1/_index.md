---
title: "Event 1 - Meet 13/6"
date: 2026-06-13
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Event Report: Meet 13/6

## Overview

Meet 13/6 took place just before the main worklog period of my internship. The sessions covered several different areas: AWS system design, career development in the AWS community, real DevOps work, Data Analytics, and working culture in multinational companies.

What I liked about this event was that the speakers did not only list tools. They talked about how they think, how they learned, and what changed when they moved from university into real work. After the event, I stopped treating the internship as a challenge to memorize more AWS services and started thinking more about how to explain and operate a system.

## 1. A Scalable URL Shortening Service on AWS

The URL shortener session was a useful system-design example because the business idea is simple, but scaling it introduces questions about latency, caching, data storage, and bottlenecks.

The biggest lesson for me was the order of thinking: start from the user request and system responsibility, then choose services. I applied the same approach to Shopsflow by drawing `User → entry point → application → database` before deciding which AWS service should sit at each layer.

## 2. From First Cloud AI Journey to AWS Partner

This session showed a career path from FCAJ through AWS student/community programs and into the AWS Partner ecosystem.

It made me think differently about the report and Blogs. Instead of treating them as things I only needed to submit, I began to see them as a record of my learning and a way to test whether I could explain a topic in my own words.

## 3. What Does a DevOps Engineer Really Do?

This was one of the sessions that connected most strongly to Shopsflow. The message was that DevOps is not just CI/CD or Docker/Kubernetes. A DevOps engineer needs to understand how applications run, how networks behave, how deployments fail, and how teams work together.

The fundamentals mentioned—Linux, networking, programming, Git, CI/CD, and containers—reminded me not to hide behind AWS Console steps.

One lesson I carried into the Workshop was: **copying a command is not the same as understanding it**. I tried to explain why ALB needs a target group, why private Fargate tasks need NAT for outbound traffic, and why RDS only allows PostgreSQL traffic from the ECS Security Group.

## 4. Real work and culture in multinational companies

The Data Analytics and Process Engineering sharing gave me a broader business perspective. The examples were not just about making dashboards; they were about finding the cause behind a metric, communicating it clearly, and helping teams make decisions.

I also liked the career progression idea from Follower to Learner, Problem Solver, and System Thinker. At this point I see myself mainly as a Learner: I still need guidance, but I should ask better questions and become more responsible for understanding why I am doing something.

## What I took away from Meet 13/6

I wrote down four lessons for myself:

1. Learn AWS without skipping Linux, networking, Git, and programming fundamentals.
2. Start from the problem and request flow before choosing services.
3. When something breaks, look for the root cause instead of copying a quick fix.
4. Writing and communication are part of technical work, not an optional extra.

## Connection to Shopsflow

These lessons influenced the way I later separated frontend, backend, and database layers, designed Security Groups by hop, documented the Docker/ECR/ECS release flow, and wrote the Workshop to explain the reasoning behind each step.

## Event materials

[Meet 13/06/2026 materials on Google Drive](https://drive.google.com/drive/folders/1XYe3c3jX0F432hyQiCZBOGF2dDlIEwB4)

---

## Participation Evidence

{{< report-image src="images/4-EventParticipated/event1-participation-proof.png" alt="Participation evidence for Event 1 - Meet 13/6" width="520px" caption="Figure 1. Photo evidence of my participation in Meet 13/6." >}}
