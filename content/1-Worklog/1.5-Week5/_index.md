---
title: "Week 5 Worklog"
date: 2026-07-13
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:

* Deploy the React/Vite frontend with S3 + CloudFront.
* Use ALB as the entry point for Fargate backend tasks.
* Connect frontend and backend into one clear request flow.
* Learn cache behavior, SPA routing, health checks, and CORS.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Frontend build**<br>- React/Vite artifact and env configuration<br>- Result: Frontend build ready | 13/07/2026 | 13/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **S3**<br>- Static artifact storage and access<br>- Result: S3 origin ready | 14/07/2026 | 14/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **CloudFront**<br>- Distribution, cache behavior, SPA routing<br>- Result: Main website entry point | 15/07/2026 | 15/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **ALB**<br>- Listener, `ip` target group, health check<br>- Result: Backend entry point | 16/07/2026 | 16/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Integration**<br>- `/api/*`, CORS, target health<br>- Result: End-to-end request path | 17/07/2026 | 17/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 5 Achievements:

* Understood how static frontend artifacts are stored in S3 and delivered through CloudFront.
* Understood ALB forwarding to private Fargate task IPs.
* Finalized Browser → CloudFront → S3 or /api/* → ALB → ECS → RDS.
* Built a troubleshooting order from CloudFront to ALB, target health, and ECS logs.
