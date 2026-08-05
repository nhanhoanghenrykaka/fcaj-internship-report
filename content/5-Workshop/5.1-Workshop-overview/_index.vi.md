---
title: "Kiến trúc và luồng triển khai"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

# 5.1. Kiến trúc và luồng triển khai

## 1. Kiến trúc tổng thể

![Sơ đồ kiến trúc tổng thể của Shopsflow trong Hands-on Workshop](images/5-Workshop/architecture.png)
*Hình 1. Kiến trúc được sử dụng trong Hands-on Workshop. CloudFront và S3 phân phối frontend; Application Load Balancer tiếp nhận API request và chuyển đến ECS Fargate; backend kết nối RDS PostgreSQL trong private subnet; ECR lưu Docker image và CloudWatch hỗ trợ ghi log, giám sát hệ thống.*

Trước khi tạo tài nguyên, em xác định rõ trách nhiệm của từng tầng. Việc này giúp tránh cấu hình ngược, ví dụ đặt database ở public subnet hoặc để frontend gọi trực tiếp vào địa chỉ của một ECS task.


| Tầng | Dịch vụ | Vai trò trong workshop |
|---|---|---|
| Edge và frontend | CloudFront, S3 | Phân phối React/Vite build qua HTTPS và không public bucket trực tiếp |
| API entry | Application Load Balancer | Nhận request, kiểm tra health và route đến ECS target |
| Application | ECS on Fargate | Chạy Spring Boot container trong private subnets |
| Data | RDS PostgreSQL | Lưu dữ liệu nghiệp vụ của Shopsflow |
| Artifact | Amazon ECR | Lưu backend Docker image theo phiên bản |
| Operations | CloudWatch | Lưu container log và theo dõi metric |
| Network | VPC, subnet, IGW, NAT, SG | Tách public/private và kiểm soát traffic |

## 2. Luồng request

### Frontend

1. Browser gửi request HTTPS đến CloudFront.
2. CloudFront lấy `index.html`, JavaScript, CSS và asset từ S3.
3. Với client-side route của React, CloudFront cần trả về `index.html` theo cấu hình SPA fallback.

### Backend API

1. Frontend gửi request `/api/*` qua domain CloudFront.
2. CloudFront chuyển request đến ALB origin.
3. ALB chọn một target đang healthy trong ECS target group.
4. Spring Boot xử lý JWT/RBAC và nghiệp vụ.
5. Khi cần dữ liệu, backend kết nối RDS qua port `5432`.

### Outbound

ECS task không có public IP. Khi backend gọi VNPAY sandbox, mail server hoặc API bên ngoài, packet đi qua route của private subnet đến NAT Gateway ở public subnet rồi ra Internet Gateway.

## 3. Luồng triển khai

Backend và frontend được phát hành độc lập:

- **Backend:** build JAR → build Docker image → push ECR → register task revision → update ECS service.
- **Frontend:** build React/Vite → upload `dist` lên S3 → invalidate CloudFront khi cần.

Cách này giúp một thay đổi giao diện không buộc phải build lại backend và ngược lại.

## 4. Tiêu chí kiểm tra cuối workshop

- CloudFront tải được frontend bằng HTTPS.
- S3 bucket vẫn private.
- API request đi qua ALB và target ECS ở trạng thái healthy.
- ECS task không có public IP.
- RDS không public và chỉ cho phép `ecs-sg` kết nối.
- Backend đọc/ghi được dữ liệu Shopsflow.
- CloudWatch có log khi task start, lỗi kết nối database hoặc HTTP error.
- Có thể tạo release mới bằng image và task-definition revision mới.
