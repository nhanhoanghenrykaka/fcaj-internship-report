---
title: "ECR và ECS Task Definition"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 5.4.1. </b> "
---

# 5.4.1. Build image, push ECR và tạo Task Definition

## 1. Build backend artifact và Docker image

Tại thư mục backend, chạy quy trình build phù hợp với project. Ví dụ:

```bash
./mvnw clean package -DskipTests
docker build -t shopsflow-backend:1.0.0 .
```

Trước khi push, chạy image local để kiểm tra container start, port và environment variable. Không đưa file `.env` chứa secret vào image.

## 2. Tạo ECR repository và push image

```bash
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com

docker tag shopsflow-backend:1.0.0 \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com/shopsflow-repo:1.0.0

docker push \
  <account-id>.dkr.ecr.us-east-1.amazonaws.com/shopsflow-repo:1.0.0
```



![Docker image của backend trong Amazon ECR](images/5-Workshop/ecr_image.jpg?featherlight=false)
*Hình 1. ECR repository lưu Docker image của Spring Boot backend. Image URI và tag được đưa vào ECS Task Definition để triển khai đúng phiên bản ứng dụng.*

Em ưu tiên tag theo version hoặc commit thay vì chỉ dùng `latest`, vì `latest` không cho biết chính xác revision nào đang chạy.

## 3. Tạo ECS cluster và Task Definition

Tạo cluster cho Fargate, sau đó đăng ký Task Definition với các cấu hình chính:

| Cấu hình | Giá trị hoặc nguyên tắc |
|---|---|
| Launch compatibility | Fargate |
| Network mode | `awsvpc` |
| Container image | URI image trong ECR |
| Container port | `8080` |
| CPU/Memory | Chọn theo nhu cầu của Spring Boot và giới hạn lab |
| Execution role | Quyền ECR pull và CloudWatch Logs |
| Task role | Chỉ quyền application cần |
| Log driver | `awslogs` |
| Log group | Ví dụ `/shopsflow/ecs/backend` |

Thêm datasource, JWT, mail và VNPAY config dưới dạng environment variable hoặc secret. Không ghi password thật vào nội dung báo cáo.

## 4. Kiểm tra trước khi tạo Service

- Image pull được từ ECR.
- Task Definition dùng đúng port `8080`.
- Execution role có quyền ECR và Logs.
- Datasource URL trỏ đến RDS endpoint đúng.
- Health-check endpoint của backend có thể trả trạng thái thành công mà không yêu cầu đăng nhập.
