---
title: "Proposal"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Proposal for deploying Shopsflow on AWS

## 1. Background and project motivation

During the FCAJ internship, I wanted to apply the AWS concepts I had learned to a complete system instead of treating each service as an isolated lab. I therefore selected **Shopsflow**, a full-stack e-commerce application developed by my team.

The application uses **React/Vite** for the frontend, **Spring Boot** for the backend, and **PostgreSQL** for persistent data. In addition to authentication, catalog, cart, and order management, Shopsflow contains role-based Admin/Customer flows, online payment, returns, reviews, customer support, and notifications. These workflows provide a practical environment for validating a cloud architecture.

The goal is not only to make the website publicly accessible. The proposal separates the application layers, limits communication between them, manages the backend as a versioned container workload, collects operational logs, and defines a repeatable deployment process.

**Deployed website:** [Shopsflow on Amazon CloudFront](https://d2m34udjfc5fxq.cloudfront.net/)

## 2. Proposal objectives

The proposal has the following objectives:

1. Deliver the React/Vite frontend using services designed for static content.
2. Run the Spring Boot backend in containers without managing EC2 hosts directly.
3. Keep PostgreSQL in a private network and allow access only from the backend.
4. Provide a stable API entry point with health checks before traffic is forwarded.
5. Version Docker images so releases and rollbacks can be traced.
6. Collect logs and metrics to isolate network, container, load-balancer, and database failures.
7. Provide controlled outbound access when the backend calls the VNPAY sandbox, mail services, or external APIs.
8. Define validation and cleanup checklists so workshop resources do not continue generating unnecessary cost.

The expected deliverables include the architecture design, deployed AWS resources, a hands-on workshop, configuration evidence, validation scenarios, and troubleshooting guidance.

## 3. Application context and deployment requirements

When Shopsflow runs locally through Docker Compose, the frontend, backend, and database can communicate on one machine. That setup is convenient for development but does not provide the separation, security boundaries, and lifecycle management expected from a cloud deployment.

| Requirement area | Deployment requirement |
|---|---|
| Frontend | Fast HTTPS delivery without maintaining a server only for HTML, CSS, and JavaScript |
| Backend | Consistent Docker runtime, versioned releases, health checks, and no direct public task access |
| Database | Durable PostgreSQL storage, private connectivity, backup, and snapshot support |
| Network | Public/private subnet separation with explicit routing and Security Group rules |
| Security | No long-lived access keys or application secrets committed to source code |
| Payment | Outbound access to the VNPAY sandbox and server-side verification before updating an order |
| Operations | Central logs, useful metrics, validation steps, and troubleshooting procedures |
| Cost | Awareness of time-based charges from NAT Gateway, ALB, Fargate, and RDS |

## 4. Proposed architecture

![Shopsflow deployment architecture on AWS](images/5-Workshop/architecture.png?featherlight=false)
*Figure 1. Overall Shopsflow architecture on AWS. CloudFront and S3 deliver the frontend; the Application Load Balancer routes API requests to ECS Fargate; the backend connects to RDS PostgreSQL in the private network; ECR stores Docker images and CloudWatch supports system monitoring.*




### 4.1. Frontend request flow

1. A user opens the Amazon CloudFront domain.
2. CloudFront accepts the HTTPS request and retrieves static artifacts from the S3 origin.
3. React/Vite assets are cached at edge locations when appropriate.
4. The S3 bucket remains private and CloudFront reads objects through Origin Access Control.

### 4.2. API request flow

1. The frontend sends a request to `/api/*`.
2. CloudFront forwards that behavior to the Application Load Balancer.
3. The ALB performs health checks and sends traffic only to healthy ECS targets.
4. An ECS Fargate task runs the Spring Boot application in private subnets.
5. The backend connects to RDS PostgreSQL through port `5432` inside the VPC.

### 4.3. Payment and external-service flow

During checkout, the backend creates payment parameters and a signature for the VNPAY sandbox. Because the task is placed in a private subnet, outbound communication uses a NAT Gateway. After payment, the backend verifies the signature, transaction reference, and provider status before changing the order state. A browser redirect alone is not treated as proof of successful payment.

### 4.4. Release flow

```text
Source code
→ Build the application
→ Build a Docker image
→ Push the image to Amazon ECR
→ Register a new ECS Task Definition revision
→ Update the ECS Service
→ ALB checks the new target
→ Traffic is sent after the target becomes healthy
```

The frontend follows a separate release path: build the `dist` directory, synchronize it to S3, and create a CloudFront invalidation when cached files must be refreshed.

## 5. AWS service selection

### Amazon S3 and Amazon CloudFront

A React/Vite production build consists mainly of static files. S3 stores those artifacts, while CloudFront provides HTTPS delivery, caching, and a public domain. This avoids maintaining a web server only to return frontend assets.

### Application Load Balancer

The ALB is the backend entry point. It hides task addresses from clients, checks application health, and allows the service to scale to multiple tasks later.

### Amazon ECS on AWS Fargate

Fargate lets me focus on the container image, CPU and memory, environment variables, IAM roles, networking, and service deployment without managing EC2 instances or host patching.

### Amazon ECR

ECR separates source code from deployable artifacts. Each backend release can be associated with an image tag or digest and a specific ECS task-definition revision.

### Amazon RDS for PostgreSQL

Shopsflow already uses PostgreSQL, so RDS preserves the database engine while separating the database lifecycle from the container lifecycle. The instance is placed in a private DB subnet group and public access is disabled.

### VPC, Internet Gateway, NAT Gateway, and Security Groups

The ALB uses public subnets, while ECS and RDS use private subnets. The Internet Gateway supports public routing, the NAT Gateway provides outbound-only access for private workloads, and Security Groups enforce the `ALB → ECS → RDS` path.

### IAM and Amazon CloudWatch

IAM separates deployment permissions, the ECS task execution role, and the application task role. CloudWatch centralizes logs and metrics for task failures, target health, HTTP errors, and database connectivity.

## 6. Security and operational principles

- CloudFront and the ALB are the only public entry points.
- ECS tasks and RDS do not receive public IP addresses.
- `alb-sg` exposes only the required HTTP/HTTPS ports.
- `ecs-sg` accepts the application port only from `alb-sg`.
- `rds-sg` accepts PostgreSQL `5432` only from `ecs-sg`.
- Security Group references are used instead of broad CIDR rules for backend and database access.
- The task execution role is used for image pulling and logging; the task role grants only application permissions.
- Database passwords, JWT secrets, mail credentials, and VNPAY secrets are not committed to GitHub.
- Every backend release creates a new image and task-definition revision rather than modifying a running container.
- RDS automated backups and snapshots protect important data changes.

## 7. Deployment and validation plan

1. Prepare the AWS account, Region, AWS CLI, Docker, Java/Maven, and Node.js.
2. Create the VPC, two public subnets, two private subnets, route tables, Internet Gateway, and NAT Gateway.
3. Create Security Groups and IAM roles before deploying workloads.
4. Create a private DB subnet group and RDS PostgreSQL instance.
5. Build the backend image, push it to ECR, and register an ECS Task Definition.
6. Create the ALB, listeners, target group, and health check.
7. Create the ECS Fargate Service in private subnets and connect it to RDS.
8. Build the frontend, upload it to S3, and configure CloudFront.
9. Validate the frontend, API, database, authentication, orders, inventory, returns, reviews, support, and VNPAY sandbox flow.
10. Review CloudWatch logs, target health, task replacement, and redeployment.
11. Clean up resources in dependency order when the lab is finished.

Acceptance criteria include a working CloudFront frontend, API traffic through the ALB to ECS, a private RDS database, successful application data operations, server-side payment verification, and sufficient logs to diagnose failures.

## 8. Risks, constraints, and mitigation

| Risk or constraint | Mitigation within this proposal |
|---|---|
| ECS task does not start | Check image URI, execution role, CPU/memory, environment variables, and stopped reason |
| ALB target remains unhealthy | Check the health path, container port, target group, and `ecs-sg` inbound rule |
| Backend cannot connect to RDS | Check endpoint, database name, credentials, datasource URL, and `rds-sg` |
| SPA refresh returns 403/404 | Configure SPA fallback or CloudFront custom error responses to `index.html` |
| Payment state is updated incorrectly | Verify provider signature and transaction status on the backend |
| Secret appears in the repository | Remove it, rotate it, and move it to a managed secret store when available |
| Unexpected AWS cost | Review NAT Gateway, ALB, Fargate, RDS, log retention, and data transfer |
| Data loss | Enable automated backup, create snapshots, and test restore procedures |
| Scope becomes too broad | Report only deployed or validated features; keep IaC, WAF, full CI/CD, and advanced scaling in the roadmap |

## 9. Expected outcome and future work

The completed proposal should make the full request path, the purpose of every AWS service, and the failure boundaries understandable. The target outcome is:

- React/Vite frontend delivered through S3 and CloudFront.
- Spring Boot backend stored as Docker images in ECR and executed by ECS Fargate.
- ALB routes traffic only to healthy tasks.
- RDS PostgreSQL remains private and accepts connections only from ECS.
- CloudWatch provides logs and metrics for troubleshooting.
- Frontend and backend have separate, repeatable release procedures.
- The proposal, architecture diagram, workshop, and AWS Console evidence describe the same deployment.

Future improvements may include AWS Secrets Manager, AWS WAF, ACM and Route 53 with a custom domain, ECS Service Auto Scaling, CI/CD through GitHub Actions or CodePipeline, and Infrastructure as Code. These are roadmap items rather than claims of completed workshop work.
