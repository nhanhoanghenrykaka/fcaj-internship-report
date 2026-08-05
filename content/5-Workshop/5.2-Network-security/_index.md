---
title: "VPC, IAM, and Security Group setup"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

# 5.2. VPC, IAM, and Security Group setup

## 1. Preparation

I used one Region consistently for the VPC, ECR, ECS, ALB, and RDS resources. The local machine requires AWS CLI, Docker, Git, Java/Maven, and Node.js/npm.

Quick AWS CLI checks:

```bash
aws sts get-caller-identity
aws configure get region
```

Access keys must not be stored in source code or Docker images.

![The `us-east-1` Region selected for the workshop](images/5-Workshop/region.png?featherlight=false)
*Figure 1. US East (N. Virginia) – `us-east-1` is selected before resources are created. Using one Region allows the VPC, ECR, ECS, ALB, and RDS resources to connect correctly.*

## 2. Create the VPC

The VPC is the network boundary of the workshop. A dedicated VPC keeps the deployment routes, subnets, and Security Groups separate from default resources.



![The VPC used by Shopsflow](images/5-Workshop/vpc.jpg?featherlight=false)
*Figure 2. The VPC page confirms that the isolated Shopsflow network exists. It contains the public and private subnets used by the ALB, ECS, and RDS layers.*

| Component | Design |
|---|---|
| VPC | A CIDR large enough for multiple subnets, for example `10.0.0.0/16` |
| Availability Zones | Two AZs so the ALB and DB subnet group do not depend on one AZ |
| Public subnets | ALB and NAT Gateway placement |
| Private subnets | ECS tasks and RDS placement |

## 3. Create public subnets

A public subnet has a default route to an Internet Gateway. An internet-facing ALB requires subnets in at least two Availability Zones.



![Public subnet 1 in `us-east-1a`](images/5-Workshop/public_subnet_1.jpg?featherlight=false)
*Figure 3. The first public subnet is placed in `us-east-1a`. It belongs to the public tier and can host the Application Load Balancer or NAT Gateway.*



![Public subnet 2 in `us-east-1b`](images/5-Workshop/public_subnet_2.jpg?featherlight=false)
*Figure 4. The second public subnet is placed in `us-east-1b`. Two public subnets in different Availability Zones satisfy the ALB multi-AZ requirement.*

After creating the subnets:

1. Create and attach an Internet Gateway.
2. Create a public route table.
3. Add `0.0.0.0/0 → Internet Gateway`.
4. Associate both public subnets with that route table.

## 4. Create private subnets

Private subnets do not route directly to the Internet Gateway. ECS and RDS are placed here so they do not accept direct Internet traffic.



![Private subnet 1 in `us-east-1a`](images/5-Workshop/private_subnet_1.jpg?featherlight=false)
*Figure 5. The first private subnet is used for ECS tasks or data components and does not accept direct inbound traffic from the Internet Gateway.*



![Private subnet 2 in `us-east-1b`](images/5-Workshop/private_subnet_2.jpg?featherlight=false)
*Figure 6. The second private subnet completes the private tier in another Availability Zone and is used by ECS or the DB subnet group.*

When ECS requires outbound access, create a NAT Gateway in a public subnet, assign an Elastic IP, and add `0.0.0.0/0 → NAT Gateway` to the private route table. NAT does not make ECS a public service; inbound traffic still enters through the ALB.

## 5. Design Security Groups

I created three Security Groups instead of using one group for the entire system.



![Shopsflow Security Group list](images/5-Workshop/security_groups.jpg?featherlight=false)
*Figure 7. The Security Group list shows separate access controls for the ALB, ECS, and RDS layers instead of one shared group for the entire system.*

### 5.1. ALB Security Group



![Inbound rules for the ALB Security Group](images/5-Workshop/alb_sg_inbound_rules.jpg?featherlight=false)
*Figure 8. The ALB Security Group accepts web traffic from users. The ALB is the public entry point, while the backend remains private.*

Recommended rules:

- inbound TCP `80` from the Internet or the source required by the architecture;
- inbound TCP `443` after a certificate is configured;
- outbound to `ecs-sg` on application port `8080`.

### 5.2. ECS Security Group



![Inbound rules for the ECS Security Group](images/5-Workshop/ecs_sg_inbound_rules.jpg?featherlight=false)
*Figure 9. The ECS Security Group accepts the application port only from the ALB Security Group, preventing direct Internet access to Fargate tasks.*

Main rules:

- inbound TCP `8080` with `alb-sg` as the source;
- outbound TCP `5432` to RDS;
- outbound HTTPS or Internet access through NAT when the application calls ECR, CloudWatch, VNPAY, or external services.

## 6. ECS IAM roles

Create two separate roles:

- **Task execution role:** used by the ECS agent to pull images from ECR and send logs to CloudWatch.
- **Task role:** used by application code when it must call an AWS API.

Do not place every permission in the task role. The deploying identity also needs tightly scoped `iam:PassRole` access when creating or updating ECS resources.

## 7. Pre-deployment checks

- Both public subnets route to the Internet Gateway.
- Private subnets do not route directly to the Internet Gateway.
- NAT routes are added only when private workloads require outbound access.
- The ALB SG does not expose the database port.
- The ECS SG accepts port `8080` only from the ALB SG.
- The RDS SG will accept `5432` only from the ECS SG in the next section.
