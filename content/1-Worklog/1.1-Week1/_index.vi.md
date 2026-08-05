---
title: "Worklog Tuần 1"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

### Mục tiêu tuần 1:

* Làm quen với yêu cầu của chương trình FCAJ và phạm vi báo cáo thực tập.
* Ôn AWS Foundations và các nhóm dịch vụ cơ bản.
* Phân tích source Shopsflow để xác định frontend, backend, database và payment flow.
* Tạo draft kiến trúc đầu tiên làm roadmap cho các tuần tiếp theo.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Bắt đầu kỳ thực tập**<br>- Đọc yêu cầu FCAJ, cấu trúc báo cáo Hugo và rà lại các chức năng của Shopsflow<br>- Kết quả: Có danh sách requirement ban đầu | 15/06/2026 | 15/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Ôn AWS Foundations**<br>- Region, AZ, compute, storage, networking, database, IAM và shared responsibility<br>- Kết quả: Hiểu cách nhóm service theo trách nhiệm | 16/06/2026 | 16/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Phân tích ứng dụng**<br>- Xem React/Vite, Spring Boot và PostgreSQL cần loại hạ tầng nào<br>- Kết quả: Tách hệ thống thành Delivery / Compute / Data | 17/06/2026 | 17/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **So sánh compute**<br>- So sánh EC2 tự quản, container trên EC2 và ECS Fargate<br>- Kết quả: Chọn Fargate làm hướng chính cho backend | 18/06/2026 | 18/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Vẽ draft architecture**<br>- Nối user flow, backend flow, database và payment<br>- Kết quả: Có bản draft Proposal đầu tiên | 19/06/2026 | 19/06/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 1:

* Hiểu rõ hơn cách phân nhóm dịch vụ AWS theo trách nhiệm.
* Xác định hướng S3 + CloudFront cho frontend, ECS Fargate cho backend và RDS PostgreSQL cho database.
* Hiểu chuỗi source code → Docker image → ECR → Task Definition → ECS/Fargate Task.
* Có draft kiến trúc và roadmap học AWS gắn với Shopsflow.
