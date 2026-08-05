---
title: "Thiết lập VPC, IAM và Security Group"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

# 5.2. Thiết lập VPC, IAM và Security Group

## 1. Chuẩn bị

Trước khi tạo tài nguyên, em sử dụng cùng một Region cho VPC, ECR, ECS, ALB và RDS. Các công cụ cần có ở máy local gồm AWS CLI, Docker, Git, Java/Maven và Node.js/npm.

Kiểm tra nhanh AWS CLI:

```bash
aws sts get-caller-identity
aws configure get region
```

Không lưu Access Key trong source code hoặc Docker image.

![Region `us-east-1` được chọn cho workshop](images/5-Workshop/region.png?featherlight=false)
*Hình 1. Region US East (N. Virginia) – `us-east-1` được chọn trước khi tạo tài nguyên. Việc dùng cùng một Region giúp VPC, ECR, ECS, ALB và RDS có thể liên kết đúng với nhau.*

## 2. Tạo VPC

VPC là ranh giới mạng của workshop. Em sử dụng một VPC riêng để các route, subnet và Security Group không bị trộn với tài nguyên mặc định.



![VPC của môi trường Shopsflow](images/5-Workshop/vpc.jpg?featherlight=false)
*Hình 2. Trang VPC xác nhận mạng riêng của Shopsflow đã được tạo. VPC này là phạm vi chứa public subnet, private subnet, ALB, ECS và RDS.*

Cấu hình logic được sử dụng:

| Thành phần | Thiết kế |
|---|---|
| VPC | CIDR đủ lớn để chia nhiều subnet, ví dụ `10.0.0.0/16` |
| Availability Zone | Hai AZ để ALB và DB subnet group không phụ thuộc một AZ |
| Public subnet | Dành cho ALB và NAT Gateway |
| Private subnet | Dành cho ECS task và RDS |

## 3. Tạo public subnets

Public subnet có route mặc định `0.0.0.0/0` đến Internet Gateway. ALB cần ít nhất hai subnet ở hai Availability Zone.



![Public subnet 1 tại `us-east-1a`](images/5-Workshop/public_subnet_1.jpg?featherlight=false)
*Hình 3. Public subnet thứ nhất được đặt tại `us-east-1a`. Subnet này thuộc tầng public và có thể được dùng cho Application Load Balancer hoặc NAT Gateway.*



![Public subnet 2 tại `us-east-1b`](images/5-Workshop/public_subnet_2.jpg?featherlight=false)
*Hình 4. Public subnet thứ hai được đặt tại `us-east-1b`. Hai public subnet ở hai Availability Zone giúp ALB đáp ứng yêu cầu triển khai đa AZ.*

Sau khi tạo subnet:

1. Tạo Internet Gateway và attach vào VPC.
2. Tạo public route table.
3. Thêm route `0.0.0.0/0 → Internet Gateway`.
4. Associate hai public subnets với route table này.

## 4. Tạo private subnets

Private subnet không có route trực tiếp đến Internet Gateway. ECS và RDS được đặt ở đây để không nhận inbound Internet trực tiếp.



![Private subnet 1 tại `us-east-1a`](images/5-Workshop/private_subnet_1.jpg?featherlight=false)
*Hình 5. Private subnet thứ nhất dành cho ECS task hoặc thành phần dữ liệu. Subnet không nhận inbound trực tiếp từ Internet Gateway.*



![Private subnet 2 tại `us-east-1b`](images/5-Workshop/private_subnet_2.jpg?featherlight=false)
*Hình 6. Private subnet thứ hai hoàn thiện tầng private ở Availability Zone còn lại và được dùng khi cấu hình ECS hoặc DB subnet group.*

Nếu ECS cần outbound, tạo NAT Gateway trong public subnet, cấp Elastic IP và thêm route `0.0.0.0/0 → NAT Gateway` cho private route table. NAT không biến ECS thành public service; inbound vẫn phải đi qua ALB.

## 5. Thiết kế Security Group

Em tạo ba Security Group riêng thay vì dùng một group cho toàn hệ thống.



![Danh sách Security Group của Shopsflow](images/5-Workshop/security_groups.jpg?featherlight=false)
*Hình 7. Danh sách Security Group thể hiện việc tách quyền truy cập theo từng tầng: ALB, ECS và RDS, thay vì dùng một nhóm bảo mật chung cho toàn hệ thống.*

### 5.1. Security Group cho ALB



![Inbound rule của Security Group dành cho ALB](images/5-Workshop/alb_sg_inbound_rules.jpg?featherlight=false)
*Hình 8. Security Group của ALB cho phép traffic web từ phía người dùng. ALB là điểm vào public; backend không được mở trực tiếp ra Internet.*

Cấu hình đề xuất:

- inbound TCP `80` từ Internet hoặc từ nguồn phù hợp với kiến trúc;
- inbound TCP `443` khi đã cấu hình certificate;
- outbound đến `ecs-sg` trên port ứng dụng `8080`.

### 5.2. Security Group cho ECS



![Inbound rule của Security Group dành cho ECS](images/5-Workshop/ecs_sg_inbound_rules.jpg?featherlight=false)
*Hình 9. Security Group của ECS chỉ nhận port ứng dụng từ Security Group của ALB. Rule này bảo đảm Fargate task không thể bị truy cập trực tiếp từ Internet.*

Cấu hình chính:

- inbound TCP `8080` với source là `alb-sg`;
- outbound TCP `5432` đến RDS;
- outbound HTTPS hoặc Internet thông qua NAT khi ứng dụng gọi ECR, CloudWatch, VNPAY hoặc dịch vụ ngoài.

## 6. IAM role cho ECS

Tạo hai role riêng:

- **Task execution role:** ECS agent dùng để pull image từ ECR và gửi log đến CloudWatch.
- **Task role:** application code bên trong container sử dụng khi cần gọi AWS API.

Không gộp mọi quyền vào task role. Khi người triển khai tạo hoặc cập nhật ECS service, quyền `iam:PassRole` cũng cần được giới hạn vào đúng role.

## 7. Kiểm tra trước khi chuyển bước

- Hai public subnets có route đến Internet Gateway.
- Hai private subnets không route trực tiếp đến Internet Gateway.
- NAT route chỉ được thêm khi private workload cần outbound.
- ALB SG không mở port database.
- ECS SG chỉ nhận port `8080` từ ALB SG.
- RDS SG sẽ chỉ nhận `5432` từ ECS SG ở bước tiếp theo.
