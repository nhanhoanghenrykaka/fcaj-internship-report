---
title: "Worklog Tuần 5"
date: 2026-07-13
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:

* Triển khai frontend React/Vite theo hướng S3 + CloudFront.
* Dùng ALB làm entry point cho backend Fargate.
* Ghép frontend và backend thành một request flow rõ ràng.
* Tìm hiểu cache behavior, SPA routing, health check và CORS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Build frontend**<br>- React/Vite build output và biến môi trường<br>- Kết quả: Có artifact frontend | 13/07/2026 | 13/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **S3 hosting layer**<br>- Upload static files và quyền truy cập<br>- Kết quả: Có S3 origin cho frontend | 14/07/2026 | 14/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **CloudFront**<br>- Distribution, cache behavior, SPA routing<br>- Kết quả: Có entry point cho website | 15/07/2026 | 15/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **ALB**<br>- Listener, target group `ip`, health check<br>- Kết quả: Có API entry point tới Fargate | 16/07/2026 | 16/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Ghép frontend/API**<br>- `/api/*` behavior, CORS, health check<br>- Kết quả: Hoàn thiện request flow | 17/07/2026 | 17/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 5:

* Hiểu cách frontend static được lưu trên S3 và phân phối qua CloudFront.
* Hiểu ALB forward request tới private Fargate task bằng target type ip.
* Chốt request flow Browser → CloudFront → S3 hoặc /api/* → ALB → ECS → RDS.
* Có thứ tự troubleshoot từ CloudFront đến ALB, target health và ECS logs.
