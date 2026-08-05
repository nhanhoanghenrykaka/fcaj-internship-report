---
title: "Dọn dẹp tài nguyên"
date: 2026-06-15
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# 5.6. Dọn dẹp tài nguyên

Cleanup là một bước của workshop, không phải phần tùy chọn. NAT Gateway, ALB, Fargate và RDS có thể tiếp tục phát sinh chi phí dù không có người dùng truy cập.

Em xóa theo thứ tự dependency sau để tránh lỗi `resource in use`.

## 1. Lưu lại những artifact cần giữ

- Ghi lại image tag, task-definition revision và cấu hình quan trọng.
- Tạo final snapshot nếu cần giữ database.
- Tải hoặc giữ log cần thiết cho báo cáo.
- Giữ ECR repository hoặc S3 artifact nếu còn dùng cho demo.

## 2. CloudFront và S3 frontend

1. Disable CloudFront distribution.
2. Chờ distribution deploy xong trạng thái disable.
3. Delete distribution nếu không còn dùng.
4. Empty S3 bucket.
5. Delete bucket khi không cần giữ frontend artifact.

## 3. ECS Service và task

1. Đặt desired count về `0` hoặc delete service.
2. Chờ tất cả Fargate task dừng.
3. Kiểm tra target group không còn target được service quản lý.
4. Delete ECS cluster khi không còn service hoặc task.

## 4. ALB và target group

1. Delete listener và rule tùy chỉnh khi cần.
2. Delete Application Load Balancer.
3. Delete target group sau khi ECS Service không còn tham chiếu.

## 5. ECR

- Nếu giữ artifact, đặt lifecycle policy để tránh lưu quá nhiều image cũ.
- Nếu xóa hoàn toàn, xóa image trước rồi delete repository.

## 6. RDS

1. Delete RDS instance.
2. Chọn tạo final snapshot nếu cần lưu dữ liệu.
3. Kiểm tra manual snapshot và automated backup còn lại.
4. Delete DB subnet group sau khi không còn database sử dụng.

## 7. CloudWatch và IAM

- Delete log group, alarm và dashboard chỉ khi không cần giữ lịch sử.
- Delete custom task role và execution role sau khi ECS không còn sử dụng.
- Không xóa role dùng chung với project khác.

## 8. NAT Gateway và Elastic IP

1. Delete NAT Gateway.
2. Chờ trạng thái `Deleted`.
3. Release Elastic IP không còn sử dụng.

NAT Gateway và Elastic IP chưa release là hai tài nguyên dễ bị bỏ quên sau lab.

## 9. VPC

Sau khi không còn ENI của ALB, ECS, RDS hoặc NAT:

1. Delete custom route tables.
2. Detach và delete Internet Gateway.
3. Delete private và public subnets.
4. Delete custom Security Groups.
5. Delete VPC.

## 10. Kiểm tra cuối

- Kiểm tra tất cả Region đã sử dụng, không chỉ Region đang mở trên Console.
- Mở Billing/Cost Explorer để xem tài nguyên vẫn phát sinh phí.
- Kiểm tra Elastic IP, snapshots, log groups và ECR images còn sót.
- Nếu giữ website demo, ghi rõ những tài nguyên nào phải tiếp tục chạy và chi phí dự kiến cần theo dõi.

Sau bước này, em hiểu rằng triển khai cloud bao gồm cả vòng đời tài nguyên: tạo, kiểm thử, cập nhật, quan sát và xóa khi không còn nhu cầu.
