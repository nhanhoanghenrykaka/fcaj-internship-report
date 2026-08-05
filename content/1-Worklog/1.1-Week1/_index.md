---
title: "Week 1 Worklog"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

### Week 1 Objectives:

* Understand FCAJ requirements and define the internship-report scope.
* Review AWS fundamentals and major service categories.
* Analyze Shopsflow frontend, backend, database, and payment requirements.
* Create the first architecture draft as a roadmap.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Internship setup**<br>- FCAJ requirements, Hugo report structure, Shopsflow features<br>- Result: Initial requirement list | 15/06/2026 | 15/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **AWS foundations**<br>- Region/AZ, compute, storage, networking, database, IAM<br>- Result: Service responsibilities became clearer | 16/06/2026 | 16/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Application analysis**<br>- React/Vite, Spring Boot, PostgreSQL<br>- Result: Split the system into Delivery / Compute / Data | 17/06/2026 | 17/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Compute comparison**<br>- EC2, container on EC2, ECS Fargate<br>- Result: Chose Fargate as the final backend direction | 18/06/2026 | 18/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Architecture draft**<br>- User, deployment, database and payment flows<br>- Result: First Proposal draft and AWS roadmap | 19/06/2026 | 19/06/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 1 Achievements:

* Improved my understanding of AWS services by responsibility.
* Selected S3 + CloudFront for frontend delivery, ECS Fargate for backend runtime, and RDS PostgreSQL for data.
* Understood source code → Docker image → ECR → Task Definition → ECS/Fargate Task.
* Created the first architecture draft and AWS learning roadmap for Shopsflow.
