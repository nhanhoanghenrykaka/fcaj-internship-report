---
title: "Worklog Tuần 2"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:

* Hiểu cách thiết kế VPC cho một ứng dụng chạy trên AWS.
* Phân biệt Public Subnet và Private Subnet dựa trên routing.
* Hiểu inbound traffic qua ALB và outbound traffic qua NAT Gateway.
* Thiết kế Security Group theo chuỗi ALB → ECS → RDS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - **Thiết kế CIDR và subnet**<br>- Chia VPC thành 2 public + 2 private subnet trên hai AZ<br>- Kết quả: Có network map ban đầu | 22/06/2026 | 22/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - **Public routing**<br>- IGW, route table và điều kiện để ALB/NAT có kết nối public<br>- Kết quả: Hiểu public path | 23/06/2026 | 23/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - **Private outbound**<br>- NAT Gateway, Elastic IP và route của private subnet<br>- Kết quả: Hiểu outbound path | 24/06/2026 | 24/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - **Security Groups**<br>- Thiết kế ALB SG → ECS SG → RDS SG<br>- Kết quả: Có security chain theo từng hop | 25/06/2026 | 25/06/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - **Review lỗi và chi phí**<br>- NAT cost, Cross-AZ, route sai, SG sai<br>- Kết quả: Có checklist troubleshoot networking | 26/06/2026 | 26/06/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 2:

* Vẽ được network plan Multi-AZ với Public/Private Subnet.
* Giải thích được inbound path Internet → ALB → ECS và outbound path ECS → NAT → Internet.
* Giữ RDS private và chỉ cho phép PostgreSQL 5432 từ ECS Security Group.
* Bắt đầu troubleshoot networking theo từng lớp route, subnet và Security Group.
