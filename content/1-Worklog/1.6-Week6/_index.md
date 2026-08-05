---
title: "Week 6 Worklog"
date: 2026-07-20
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:

* Add CloudWatch observability for backend troubleshooting.
* Understand the payment path from private backend to an external provider.
* Practice basic failure-scenario analysis.
* Identify cost drivers and include cleanup in the workflow.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **CloudWatch Logs**<br>- `awslogs`, startup/error logs<br>- Result: Central backend logs | 20/07/2026 | 20/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Metrics/health**<br>- ECS, ALB, RDS<br>- Result: Monitoring checklist | 21/07/2026 | 21/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Payment**<br>- Payment URL, NAT outbound, callback/status<br>- Result: Payment path documented | 22/07/2026 | 22/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Failure tests**<br>- Bad health path, DB config, stopped reason<br>- Result: Layered troubleshooting practice | 23/07/2026 | 23/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Cost review**<br>- NAT, ALB, Fargate, RDS, CloudWatch<br>- Result: Cost/cleanup checklist | 24/07/2026 | 24/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 6 Achievements:

* Created a request-path troubleshooting checklist instead of relying only on application logs.
* Understood why private Fargate tasks need NAT Gateway for external payment calls.
* Understood backend payment verification before updating order status.
* Identified major cost drivers and treated cleanup as required.
