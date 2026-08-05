---
title: "Hands-on Workshop"
date: 2026-06-15
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Deploying Shopsflow on AWS

## Workshop purpose

This section records the process I used to move Shopsflow from a local environment to AWS. The pages follow resource dependencies: understand the architecture, create networking and access controls, prepare the database, deploy the backend and frontend, and then validate, monitor, and clean up the environment.

The workshop is not presented as a gallery of AWS Console screenshots. Every image appears at the step it supports, with a caption explaining the resource's role in the system.

**Deployed website:** [Open Shopsflow](https://d2m34udjfc5fxq.cloudfront.net/)

**Application demo:** [Watch the Shopsflow demo](https://www.youtube.com/watch?v=iwRwS-HEzGw)

## Target outcomes

After the workshop, the reader should be able to:

- explain the `User → CloudFront → S3 or ALB → ECS Fargate → RDS` request path;
- distinguish public and private subnets;
- configure Security Groups by source instead of exposing broad CIDR ranges;
- build, push, and deploy a backend Docker image through ECR and ECS;
- deploy a React/Vite build to S3 and deliver it through CloudFront;
- use CloudWatch, target health, and ECS stopped reasons for troubleshooting;
- validate the VNPAY sandbox and important Shopsflow workflows;
- remove resources in dependency order to prevent errors and unintended cost.

## Workshop contents

1. [Architecture and deployment flow](5.1-workshop-overview/)
2. [VPC, IAM, and Security Group setup](5.2-network-security/)
3. [Private RDS PostgreSQL deployment](5.3-rds/)
4. [Backend and frontend deployment](5.4-application-deployment/)
5. [Monitoring, validation, and troubleshooting](5.5-monitoring-validation/)
6. [Resource cleanup](5.6-cleanup/)

> Names and values shown in the screenshots belong to the workshop environment. Replace account IDs, endpoints, repository URIs, bucket names, and secrets with values from the account used for a new deployment.
