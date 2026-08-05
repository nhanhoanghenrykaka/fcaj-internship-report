---
title: "Triển khai backend và frontend"
date: 2026-06-15
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

# 5.4. Triển khai backend và frontend

Phần triển khai được tách thành ba bước để dễ kiểm tra:

1. [Build image, push ECR và tạo Task Definition](5.4.1-ecr-task-definition/)
2. [Tạo ALB và triển khai ECS Fargate Service](5.4.2-alb-ecs/)
3. [Deploy frontend bằng S3 và CloudFront](5.4.3-s3-cloudfront/)

Backend được hoàn thiện trước để CloudFront có một ALB origin hoạt động khi cấu hình behavior `/api/*`. Frontend và backend vẫn có release lifecycle riêng.
