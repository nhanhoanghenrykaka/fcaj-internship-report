---
title: "Deploy the backend and frontend"
date: 2026-06-15
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

# 5.4. Deploy the backend and frontend

The deployment is divided into three steps so that each failure boundary can be tested separately:

1. [Build the image, push to ECR, and create a Task Definition](5.4.1-ecr-task-definition/)
2. [Create the ALB and deploy the ECS Fargate Service](5.4.2-alb-ecs/)
3. [Deploy the frontend with S3 and CloudFront](5.4.3-s3-cloudfront/)

The backend is completed first so CloudFront can use a working ALB origin for the `/api/*` behavior. The frontend and backend still have independent release lifecycles.
