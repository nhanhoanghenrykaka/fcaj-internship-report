---
title: "ECR and ECS Task Definition"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 5.4.1. </b> "
---

# 5.4.1. Build the image, push to ECR, and create a Task Definition

## 1. Build the backend artifact and Docker image

Run the build process from the backend directory. For example:

```bash
./mvnw clean package -DskipTests
docker build -t shopsflow-backend:1.0.0 .
```

Run the image locally before pushing it to verify startup, the container port, and required environment variables. Do not copy a secret-containing `.env` file into the image.

## 2. Create an ECR repository and push the image

```bash
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com

docker tag shopsflow-backend:1.0.0 \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com/shopsflow-repo:1.0.0

docker push \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com/shopsflow-repo:1.0.0
```



![Backend Docker image in Amazon ECR](images/5-Workshop/ecr_image.jpg?featherlight=false)
*Figure 1. The ECR repository stores the Spring Boot backend image. Its image URI and tag are referenced by the ECS Task Definition.*

Use a version or commit-based tag rather than relying only on `latest`, which does not clearly identify the running revision.

## 3. Create the ECS cluster and Task Definition

Create a Fargate cluster and register a Task Definition with the following settings:

| Setting | Value or principle |
|---|---|
| Launch compatibility | Fargate |
| Network mode | `awsvpc` |
| Container image | ECR image URI |
| Container port | `8080` |
| CPU/Memory | Based on Spring Boot requirements and lab limits |
| Execution role | ECR pull and CloudWatch Logs permissions |
| Task role | Only permissions required by the application |
| Log driver | `awslogs` |
| Log group | For example `/shopsflow/ecs/backend` |

Provide datasource, JWT, mail, and VNPAY settings through environment variables or secrets. Real passwords are not included in the report.

## 4. Checks before service creation

- The image can be pulled from ECR.
- The Task Definition exposes the correct container port `8080`.
- The execution role can access ECR and CloudWatch Logs.
- The datasource URL points to the correct RDS endpoint.
- The backend health endpoint returns success without requiring authentication.
