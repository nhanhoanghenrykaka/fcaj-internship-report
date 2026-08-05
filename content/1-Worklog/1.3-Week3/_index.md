---
title: "Week 3 Worklog"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Week 3 Objectives:

* Dockerize the Spring Boot backend and validate it locally.
* Understand ECR, ECS Cluster, Task Definition, Task, Service, and Fargate.
* Understand the deployment lifecycle from source code to ECS workload.
* Distinguish Task Execution Role and Task Role.

### Tasks to be carried out this week:

| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - **Backend/Dockerfile review**<br>- Maven build, port, env vars, datasource, health<br>- Result: Containerization plan | 29/06/2026 | 29/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Local container test**<br>- Build and run Spring Boot image<br>- Result: Working local image | 30/06/2026 | 30/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Amazon ECR**<br>- Repository, login, tag and push<br>- Result: Backend image stored in ECR | 01/07/2026 | 01/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Task Definition**<br>- CPU/memory, `awsvpc`, roles, logs<br>- Result: Task Definition became clear | 02/07/2026 | 02/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **ECS Service**<br>- Desired count, revisions, health, replacement<br>- Result: Deployment lifecycle understood | 03/07/2026 | 03/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 3 Achievements:

* Built and ran the Spring Boot backend as a Docker container locally.
* Understood Docker → ECR → ECS Service → Fargate Task.
* Distinguished Cluster, Task Definition, Task, Service, and Fargate.
* Distinguished Task Execution Role and Task Role and learned why iam:PassRole matters.
