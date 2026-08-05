---
title: "Week 2 Worklog"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:

* Understand VPC design for an AWS application.
* Distinguish public and private subnets based on routing.
* Understand inbound traffic through ALB and outbound traffic through NAT Gateway.
* Design the ALB → ECS → RDS Security Group chain.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **CIDR and subnet design**<br>- Two public + two private subnets across two AZs<br>- Result: Initial network map | 22/06/2026 | 22/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Public routing**<br>- IGW, route tables, public connectivity<br>- Result: Clear inbound/public route | 23/06/2026 | 23/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Private outbound**<br>- NAT Gateway, Elastic IP, private routes<br>- Result: Clear outbound path | 24/06/2026 | 24/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Security Groups**<br>- ALB SG → ECS SG → RDS SG<br>- Result: Security chain by hop | 25/06/2026 | 25/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Failure/cost review**<br>- NAT cost, Cross-AZ, routing and SG issues<br>- Result: Networking checklist | 26/06/2026 | 26/06/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 2 Achievements:

* Created a Multi-AZ network plan with public/private subnets.
* Explained Internet → ALB → ECS inbound traffic and ECS → NAT → Internet outbound traffic.
* Kept RDS private and allowed PostgreSQL 5432 only from the ECS Security Group.
* Started troubleshooting networking layer by layer.
