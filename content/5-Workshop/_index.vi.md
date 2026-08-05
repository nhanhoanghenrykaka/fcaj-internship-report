---
title: "Thực hành (Workshop)"
date: 2026-06-15
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Triển khai Shopsflow trên AWS

## Mục đích của workshop

Phần này ghi lại quy trình em đã dùng để đưa Shopsflow từ môi trường local lên AWS. Nội dung được sắp xếp theo dependency của tài nguyên: hiểu kiến trúc trước, tạo network và quyền truy cập, chuẩn bị database, triển khai backend và frontend, sau đó mới kiểm thử, giám sát và cleanup.

Em không trình bày workshop theo kiểu liệt kê ảnh AWS Console. Mỗi ảnh được đặt ngay tại bước liên quan và có chú thích giải thích tài nguyên đó làm gì trong hệ thống.

**Website đã triển khai:** [Mở Shopsflow](https://d2m34udjfc5fxq.cloudfront.net/)

**Video demo ứng dụng:** [Xem demo Shopsflow](https://www.youtube.com/watch?v=iwRwS-HEzGw)

## Kết quả cần đạt

Sau workshop, người thực hiện cần có thể:

- giải thích đường đi `User → CloudFront → S3 hoặc ALB → ECS Fargate → RDS`;
- phân biệt public subnet và private subnet;
- cấu hình Security Group theo nguồn thay vì mở rộng bằng `0.0.0.0/0`;
- build, push và triển khai một backend Docker image qua ECR và ECS;
- triển khai React/Vite lên S3 và phân phối bằng CloudFront;
- dùng CloudWatch, target health và ECS stopped reason để tìm lỗi;
- kiểm tra VNPAY sandbox cùng các nghiệp vụ quan trọng của Shopsflow;
- dọn tài nguyên đúng thứ tự để tránh lỗi dependency và chi phí ngoài ý muốn.

## Nội dung workshop

1. [Kiến trúc và luồng triển khai](5.1-workshop-overview/)
2. [Thiết lập VPC, IAM và Security Group](5.2-network-security/)
3. [Tạo RDS PostgreSQL private](5.3-rds/)
4. [Triển khai backend và frontend](5.4-application-deployment/)
5. [Giám sát, kiểm thử và xử lý lỗi](5.5-monitoring-validation/)
6. [Dọn dẹp tài nguyên](5.6-cleanup/)

> Tên và giá trị trong ảnh là tài nguyên của môi trường thực hành. Khi thực hiện lại, cần thay account ID, endpoint, repository URI, bucket name và secret bằng giá trị của tài khoản đang sử dụng.
