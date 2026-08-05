---
title: "Worklog Tuần 4"
date: 2026-07-06
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:

* Tìm hiểu Amazon RDS PostgreSQL và thiết kế data layer cho Shopsflow.
* Giữ database private và chỉ cho backend được phép kết nối.
* Hiểu cách truyền datasource configuration vào ECS task.
* Rà lại concurrency và credential handling trong luồng order/inventory.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Tìm hiểu RDS**<br>- DB subnet group, endpoint, engine, storage, backup<br>- Kết quả: Có cấu hình RDS lab phù hợp | 06/07/2026 | 06/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Database networking**<br>- RDS private, SG `5432` chỉ từ ECS SG<br>- Kết quả: Chốt data path ECS → RDS | 07/07/2026 | 07/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Backend configuration**<br>- Datasource URL, username/password, migration<br>- Kết quả: Hiểu cách inject config vào task | 08/07/2026 | 08/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Test dữ liệu**<br>- Category, product, order, inventory<br>- Kết quả: Kiểm tra backend đọc/ghi RDS | 09/07/2026 | 09/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Concurrency & security review**<br>- Optimistic locking, credential handling, IAM<br>- Kết quả: Có checklist database/security | 10/07/2026 | 10/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 4:

* Thiết kế RDS PostgreSQL trong private network và xác định đường ECS → RDS.
* Biết phân biệt lỗi network, credentials/configuration và application/migration.
* Hiểu vì sao inventory concurrency cần xử lý ở application/database layer.
* Không đưa database credential vào source code và ghi nhận Secrets Manager/KMS là hướng học tiếp.
