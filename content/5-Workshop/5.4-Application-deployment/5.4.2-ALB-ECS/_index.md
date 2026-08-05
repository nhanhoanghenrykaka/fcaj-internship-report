---
title: "ALB and ECS Fargate Service"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---

# 5.4.2. Create the ALB and deploy the ECS Fargate Service

## 1. Create the target group

Fargate with `awsvpc` networking requires the target type to be **IP**.

Main settings:

- HTTP protocol;
- target port `8080`;
- Shopsflow VPC;
- a lightweight health path, such as `/actuator/health` when Spring Boot Actuator is enabled, or the project's own health endpoint;
- a success code that matches the endpoint.

## 2. Create the internet-facing ALB

1. Select the two public subnets in different Availability Zones.
2. Attach `alb-sg`.
3. Create an HTTP listener on port `80`; add HTTPS `443` when an ACM certificate is available.
4. Forward the listener to the backend target group.



![The Shopsflow Application Load Balancer](images/5-Workshop/alb.jpg?featherlight=false)
*Figure 1. The Application Load Balancer provides a stable API entry point, performs health checks, and forwards requests only to healthy ECS targets.*

## 3. Create the ECS Fargate Service

Create a service from the registered Task Definition:

| Setting | Value or principle |
|---|---|
| Compute option | Fargate launch type or capacity provider |
| Desired count | `1` for the lab; increase when testing multiple tasks |
| Subnets | Two private subnets |
| Public IP | Disabled |
| Security Group | `ecs-sg` |
| Load balancer | ALB target group with IP targets |
| Deployment | Rolling update; keep the previous task until the new task is healthy when capacity allows |



![ECS cluster and Fargate service](images/5-Workshop/ecs_cluster_service.jpg?featherlight=false)
*Figure 2. The ECS page confirms the cluster and service that run the backend. Desired tasks, running tasks, and deployment status are used to monitor releases.*

## 4. Validate the backend

1. Wait for the ECS task to become `RUNNING`.
2. Open the target group and wait for the target to become `healthy`.
3. Review CloudWatch logs and confirm that Spring Boot startup is complete.
4. Call the health endpoint through the ALB.
5. Execute one read API and one write API.

When a task stops, inspect the **Stopped reason** first. When the task is running but the target is unhealthy, check the health path, port mapping, and Security Group. Database errors usually require datasource and `rds-sg` checks.

## 5. Redeploy a new version

1. Build an image with a new tag.
2. Push it to ECR.
3. Register a new Task Definition revision.
4. Update the ECS Service to the new revision.
5. Monitor deployment and target health.
6. Roll back to the previous revision if the new task does not become healthy.

Do not modify files inside a running Fargate task because ECS may replace that task at any time.
