---
title: "Worklog Tuần 6"
date: 2026-07-20
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:

* Bổ sung CloudWatch để quan sát backend và hỗ trợ troubleshoot.
* Hiểu payment flow từ private backend ra payment provider.
* Thực hành phân tích một số failure scenario cơ bản.
* Nhận biết cost driver và đưa cleanup vào quy trình thực hành.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **CloudWatch Logs**<br>- `awslogs`, log group, startup/error logs<br>- Kết quả: Có log tập trung cho backend | 20/07/2026 | 20/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Metrics & health**<br>- ECS task, ALB target, RDS metrics<br>- Kết quả: Có checklist quan sát hệ thống | 21/07/2026 | 21/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Payment flow**<br>- Create Payment URL, outbound NAT, callback/status<br>- Kết quả: Mô tả được payment path | 22/07/2026 | 22/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Failure testing**<br>- Health check sai, DB config sai, stopped reason<br>- Kết quả: Thực hành troubleshoot theo layer | 23/07/2026 | 23/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Cost review**<br>- NAT, ALB, Fargate, RDS, CloudWatch, Cross-AZ<br>- Kết quả: Có checklist cost và cleanup | 24/07/2026 | 24/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 6:

* Có checklist troubleshoot theo request path thay vì chỉ xem application log.
* Hiểu Fargate private subnet cần NAT Gateway khi gọi payment provider bên ngoài AWS.
* Hiểu backend cần xác minh trạng thái/signature thanh toán trước khi cập nhật order.
* Nhận biết các cost driver chính và xem cleanup là một bước bắt buộc.
