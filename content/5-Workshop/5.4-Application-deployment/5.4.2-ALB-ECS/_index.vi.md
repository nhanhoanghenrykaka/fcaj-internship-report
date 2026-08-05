---
title: "ALB và ECS Fargate Service"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---

# 5.4.2. Tạo ALB và triển khai ECS Fargate Service

## 1. Tạo target group

Vì Fargate sử dụng network mode `awsvpc`, target type phải là **IP**.

Cấu hình chính:

- protocol HTTP;
- target port `8080`;
- VPC của Shopsflow;
- health check sử dụng endpoint nhẹ, ví dụ `/actuator/health` nếu Spring Boot Actuator đã được bật, hoặc endpoint health riêng của project;
- success code phù hợp với endpoint.

## 2. Tạo internet-facing ALB

1. Chọn hai public subnets ở hai Availability Zone.
2. Gắn `alb-sg`.
3. Tạo listener HTTP `80`; bổ sung HTTPS `443` khi có certificate ACM.
4. Forward listener đến target group của backend.



![Application Load Balancer của Shopsflow](images/5-Workshop/alb.jpg?featherlight=false)
*Hình 1. Application Load Balancer cung cấp một entry point ổn định cho API, thực hiện health check và chỉ chuyển request đến ECS target đang healthy.*

## 3. Tạo ECS Fargate Service

Trong cluster, tạo service từ Task Definition đã đăng ký:

| Cấu hình | Giá trị hoặc nguyên tắc |
|---|---|
| Compute option | Launch type hoặc capacity provider Fargate |
| Desired count | `1` cho lab; có thể tăng khi cần kiểm tra nhiều task |
| Subnets | Hai private subnets |
| Public IP | Disabled |
| Security Group | `ecs-sg` |
| Load balancer | ALB target group kiểu IP |
| Deployment | Rolling update mặc định, giữ task cũ đến khi task mới healthy khi tài nguyên cho phép |



![ECS cluster và Fargate service](images/5-Workshop/ecs_cluster_service.jpg?featherlight=false)
*Hình 2. Trang ECS xác nhận cluster và service chạy backend. Desired task, running task và deployment status được dùng để theo dõi quá trình phát hành phiên bản.*

## 4. Xác nhận backend hoạt động

1. Chờ ECS task chuyển sang `RUNNING`.
2. Mở target group và chờ target thành `healthy`.
3. Kiểm tra CloudWatch log để xác nhận Spring Boot startup hoàn tất.
4. Gọi health endpoint qua ALB.
5. Gọi một API đọc dữ liệu và một API ghi dữ liệu.

Nếu task dừng, xem **Stopped reason** trước. Nếu task chạy nhưng target unhealthy, kiểm tra health path, port mapping và Security Group. Nếu API trả lỗi database, kiểm tra datasource và `rds-sg`.

## 5. Redeploy một phiên bản mới

1. Build image với tag mới.
2. Push lên ECR.
3. Register Task Definition revision mới.
4. Update ECS Service sang revision mới.
5. Theo dõi deployment và target health.
6. Rollback về revision trước nếu task mới không healthy.

Không sửa file trực tiếp trong Fargate task vì task có thể bị ECS thay thế bất kỳ lúc nào.
