---
title: "Architecture and deployment flow"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

# 5.1. Architecture and deployment flow

## 1. Overall architecture

![Overall Shopsflow architecture used in the Hands-on Workshop](images/5-Workshop/architecture.png)
*Figure 1. Architecture used throughout the Hands-on Workshop. CloudFront and S3 deliver the frontend; the Application Load Balancer receives API requests and routes them to ECS Fargate; the backend connects to RDS PostgreSQL in private subnets; ECR stores Docker images and CloudWatch provides logging and monitoring.*

Before creating resources, I defined the responsibility of each layer. This prevents incorrect decisions such as placing the database in a public subnet or allowing the frontend to depend on the address of an individual ECS task.


| Layer | Service | Role in the workshop |
|---|---|---|
| Edge and frontend | CloudFront, S3 | Deliver the React/Vite build over HTTPS without exposing the bucket publicly |
| API entry | Application Load Balancer | Accept requests, perform health checks, and route to ECS targets |
| Application | ECS on Fargate | Run the Spring Boot container in private subnets |
| Data | RDS PostgreSQL | Store Shopsflow business data |
| Artifact | Amazon ECR | Store versioned backend Docker images |
| Operations | CloudWatch | Collect container logs and metrics |
| Network | VPC, subnets, IGW, NAT, SG | Separate public/private resources and control traffic |

## 2. Request flow

### Frontend

1. The browser sends an HTTPS request to CloudFront.
2. CloudFront retrieves `index.html`, JavaScript, CSS, and assets from S3.
3. React client-side routes require an SPA fallback that returns `index.html` when appropriate.

### Backend API

1. The frontend sends `/api/*` requests through the CloudFront domain.
2. CloudFront forwards the API behavior to the ALB origin.
3. The ALB selects a healthy target from the ECS target group.
4. Spring Boot processes JWT/RBAC and business logic.
5. The backend connects to RDS through port `5432` when data is required.

### Outbound communication

The ECS task has no public IP. Calls to the VNPAY sandbox, mail server, or external APIs follow the private-subnet route to a NAT Gateway in a public subnet and then to the Internet Gateway.

## 3. Deployment flow

The backend and frontend are released independently:

- **Backend:** build JAR → build Docker image → push to ECR → register a task revision → update the ECS service.
- **Frontend:** build React/Vite → upload `dist` to S3 → invalidate CloudFront when required.

This separation allows a frontend change to be released without rebuilding the backend and vice versa.

## 4. Final workshop acceptance checks

- CloudFront loads the frontend over HTTPS.
- The S3 bucket remains private.
- API requests reach a healthy ECS target through the ALB.
- ECS tasks have no public IP.
- RDS is private and accepts connections only from `ecs-sg`.
- The backend can read and write Shopsflow data.
- CloudWatch contains logs for task startup, database failures, and HTTP errors.
- A new release can be created through a new image and task-definition revision.
