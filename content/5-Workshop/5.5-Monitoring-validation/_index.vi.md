---
title: "Giám sát, kiểm thử và xử lý lỗi"
date: 2026-06-15
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# 5.5. Giám sát, kiểm thử và xử lý lỗi

Triển khai thành công không đồng nghĩa toàn bộ nghiệp vụ đã đúng. Sau khi các tài nguyên hoạt động, em kiểm tra theo ba lớp: hạ tầng, application và business flow.

## 1. CloudWatch Logs

Task Definition sử dụng `awslogs` để gửi stdout/stderr của Spring Boot vào log group, ví dụ:

```text
/shopsflow/ecs/backend
```

Các nội dung cần tìm trong log:

- container start và Spring Boot startup;
- lỗi thiếu environment variable;
- lỗi datasource, migration hoặc authentication database;
- JWT/RBAC exception;
- lỗi gửi mail hoặc Google OAuth nếu được bật;
- lỗi tạo payment URL và xác minh VNPAY;
- HTTP `4xx`/`5xx`;
- revision đang được triển khai.

Không ghi password, token hoặc secret đầy đủ vào log.

## 2. Metric cần theo dõi

| Dịch vụ | Metric hoặc trạng thái quan trọng |
|---|---|
| ECS | Running task count, CPU, memory, deployment status, stopped reason |
| ALB | HealthyHostCount, UnHealthyHostCount, TargetResponseTime, HTTP 4xx/5xx |
| RDS | CPU, DatabaseConnections, FreeStorageSpace, FreeableMemory |
| CloudFront | Request count, error rate, cache hit rate |

Với workshop ngắn, em ưu tiên dashboard và alarm cho tình huống dễ gây gián đoạn như không còn healthy target hoặc RDS gần hết storage.

## 3. Kiểm thử hạ tầng

### Scenario A — Frontend delivery

- Mở domain CloudFront.
- Kết quả mong đợi: React SPA load đầy đủ và S3 bucket vẫn private.

### Scenario B — API routing

- Gọi API từ frontend.
- Kết quả mong đợi: request đi qua CloudFront/ALB, target healthy và nhận response từ Spring Boot.

### Scenario C — Private workload

- Kiểm tra ECS task không có public IP.
- Kết quả mong đợi: API vẫn truy cập được qua ALB; outbound vẫn hoạt động qua NAT khi cần.

### Scenario D — Database isolation

- Kiểm tra RDS Publicly accessible là `No` và rule `5432` chỉ có source `ecs-sg`.

### Scenario E — Task replacement

- Dừng một task trong service.
- Kết quả mong đợi: ECS tạo task thay thế và ALB chỉ route đến target healthy.

## 4. Kiểm thử nghiệp vụ Shopsflow

| Nhóm chức năng | Kiểm tra chính |
|---|---|
| Authentication | Sign up, email/OTP nếu bật, sign in, Google login, sign out và token expiry |
| Authorization | Customer không truy cập API Admin; tài khoản bị khóa không đăng nhập được |
| Catalog | Category, product, stock adjustment và pagination hoạt động đúng |
| Cart/Order | Tạo giỏ hàng, checkout, trạng thái đơn và shipping method |
| Inventory | Nhiều request không làm stock âm; xử lý conflict bằng transaction/locking của ứng dụng |
| Payment | Tạo VNPAY URL, hoàn tất sandbox, xác minh signature/status trước khi cập nhật order |
| Return/Refund | Customer request, Admin approve, hoàn trả và xác nhận refund đúng thứ tự |
| Review/Support | Review theo đơn hàng, chat hỗ trợ và đóng hội thoại |
| Notification | Chỉ tạo notification đúng người nhận và đúng sự kiện |

## 5. Kiểm tra payment flow

1. Backend lấy amount và order information từ dữ liệu server, không tin giá trị do client tự gửi.
2. Backend tạo payment parameters và signature.
3. ECS gọi VNPAY sandbox qua outbound route.
4. Browser mở Payment URL.
5. Khi nhận return/callback, backend xác minh checksum, transaction reference, amount và status.
6. Chỉ cập nhật order sau khi xác minh thành công; request lặp lại phải được xử lý an toàn.

## 6. Bảng xử lý lỗi nhanh

| Hiện tượng | Nơi kiểm tra đầu tiên | Nguyên nhân thường gặp |
|---|---|---|
| ECS task dừng ngay | ECS stopped reason và CloudWatch log | Sai image, thiếu role, thiếu biến môi trường, JVM hết memory |
| Task chạy nhưng ALB unhealthy | Target health, health path, SG | Sai port, endpoint yêu cầu auth, `ecs-sg` không nhận từ `alb-sg` |
| API timeout khi truy cập RDS | Log backend, `rds-sg`, subnet | Sai endpoint, route hoặc SG |
| Database authentication failed | Datasource config | Sai username/password/database name |
| Frontend trắng hoặc asset 403 | S3 object, OAC, CloudFront origin | Upload sai thư mục hoặc bucket policy/OAC chưa đúng |
| Refresh route 403/404 | CloudFront error response | Chưa cấu hình SPA fallback |
| API vẫn gọi localhost | Frontend build config | Biến môi trường được build sai |
| Payment thành công nhưng order chưa đổi | Backend payment log | Signature/status không hợp lệ hoặc callback config sai |

## 7. Kiểm tra release

- Push image tag mới, tạo task revision mới và update service.
- Xác nhận task mới healthy trước khi kết luận release thành công.
- Kiểm tra frontend version sau S3 sync và CloudFront invalidation.
- Ghi lại image tag, task revision và thời điểm triển khai để có thể rollback.

## 8. Cost review

Kiểm tra Billing/Cost Explorer và các resource page, đặc biệt là NAT Gateway, ALB, Fargate, RDS, CloudWatch Logs và data transfer. Giới hạn log retention và không để môi trường lab chạy khi không còn sử dụng.
