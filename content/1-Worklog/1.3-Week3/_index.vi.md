---
title: "Worklog Tuần 3"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:

* Đóng gói backend Spring Boot bằng Docker và kiểm tra ở local.
* Hiểu ECR, ECS Cluster, Task Definition, Task, Service và Fargate.
* Nắm deployment lifecycle từ source code đến ECS workload.
* Phân biệt Task Execution Role và Task Role.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Rà backend và Dockerfile**<br>- Maven build, port, environment variables, datasource, health endpoint<br>- Kết quả: Có kế hoạch containerize backend | 29/06/2026 | 29/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Build/test local**<br>- Build image và chạy Spring Boot trong Docker<br>- Kết quả: Image chạy được ở local | 30/06/2026 | 30/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Amazon ECR**<br>- Tạo repository, login, tag và push image<br>- Kết quả: Có image backend trên ECR | 01/07/2026 | 01/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **ECS Task Definition**<br>- CPU/memory, `awsvpc`, port, env, role, log driver<br>- Kết quả: Hiểu cấu trúc một task definition | 02/07/2026 | 02/07/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **ECS Service**<br>- Desired count, revision, target health, rolling replacement<br>- Kết quả: Hiểu deployment lifecycle | 03/07/2026 | 03/07/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 3:

* Build và chạy được backend Spring Boot dưới dạng Docker container ở local.
* Hiểu quy trình Docker → ECR → ECS Service → Fargate Task.
* Phân biệt Cluster, Task Definition, Task, Service và Fargate.
* Phân biệt Task Execution Role, Task Role và hiểu thêm về iam:PassRole.
