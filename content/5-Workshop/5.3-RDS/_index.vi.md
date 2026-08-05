---
title: "Tạo RDS PostgreSQL private"
date: 2026-06-15
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# 5.3. Tạo RDS PostgreSQL private

## 1. Lý do tạo database trước ECS Service

Backend cần endpoint, port, database name và credential để khởi động. Vì vậy em tạo RDS trước khi hoàn thiện ECS Service. Nếu task được triển khai khi datasource chưa đúng, Spring Boot có thể dừng ngay ở giai đoạn startup và ALB sẽ báo target unhealthy.

## 2. Tạo DB subnet group

1. Mở Amazon RDS Console.
2. Tạo DB subnet group cho VPC của Shopsflow.
3. Chọn hai private subnets ở hai Availability Zone.
4. Không chọn public subnets cho database tier.

DB subnet group không tự mở kết nối. Nó chỉ xác định các subnet mà RDS có thể sử dụng.

## 3. Tạo RDS PostgreSQL

Cấu hình chính:

| Thuộc tính | Giá trị hoặc nguyên tắc |
|---|---|
| Engine | PostgreSQL |
| DB identifier | `database-shopsflow` hoặc tên tương đương của môi trường |
| Connectivity | VPC Shopsflow và private DB subnet group |
| Public access | `No` |
| Port | `5432` |
| Security Group | `rds-sg` |
| Backup | Bật automated backup phù hợp với thời gian lab |
| Credential | Không ghi trực tiếp vào source code |


![RDS PostgreSQL của Shopsflow](images/5-Workshop/rds.jpg?featherlight=false)
*Hình 1. Trang RDS xác nhận PostgreSQL instance đã được tạo và ở trạng thái sẵn sàng. Endpoint này được backend sử dụng thông qua kết nối private trong VPC.*

## 4. Giới hạn kết nối bằng RDS Security Group



![Inbound rule của Security Group dành cho RDS](images/5-Workshop/rds_sg_inbound_rules.jpg?featherlight=false)
*Hình 2. Security Group của RDS chỉ cho phép PostgreSQL TCP `5432` từ Security Group của ECS, không mở database trực tiếp ra Internet.*

Không thêm rule `PostgreSQL 5432` từ `0.0.0.0/0`. Khi cần kiểm tra bằng máy local, nên sử dụng một phương thức truy cập quản trị có kiểm soát thay vì public database lâu dài.

## 5. Chuẩn bị cấu hình cho backend

Lưu endpoint và truyền cấu hình cho ECS task qua environment variable hoặc secret:

```properties
SPRING_DATASOURCE_URL=jdbc:postgresql://<rds-endpoint>:5432/<database-name>
SPRING_DATASOURCE_USERNAME=<database-user>
SPRING_DATASOURCE_PASSWORD=<database-password>
```

Các biến khác như JWT secret, mail password và VNPAY secret cũng không được hard-code vào image.

## 6. Kiểm tra database

Sau khi RDS ở trạng thái `Available`:

1. Xác nhận Publicly accessible là `No`.
2. Xác nhận DB subnet group gồm private subnets.
3. Xác nhận `rds-sg` chỉ nhận source `ecs-sg`.
4. Ghi lại endpoint, port và database name.
5. Khi ECS đã chạy, thực hiện một API đọc và một API ghi để kiểm tra end-to-end.

Nếu backend báo timeout, ưu tiên kiểm tra route, subnet và Security Group. Nếu báo authentication failed, kiểm tra username, password, database name và datasource URL.
