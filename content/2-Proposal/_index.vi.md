---
title: "Bản đề xuất"
date: 2026-06-15
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Đề xuất triển khai Shopsflow trên AWS

## 1. Bối cảnh và lý do lựa chọn đề tài

Trong kỳ thực tập FCAJ, em muốn sử dụng những kiến thức AWS đã học để triển khai một hệ thống có đầy đủ frontend, backend, database và luồng nghiệp vụ thay vì chỉ thực hiện từng dịch vụ riêng lẻ. Vì vậy, em chọn **Shopsflow**, một ứng dụng thương mại điện tử full-stack do nhóm em phát triển.

Ứng dụng sử dụng **React/Vite** cho frontend, **Spring Boot** cho backend và **PostgreSQL** cho cơ sở dữ liệu. Ngoài các chức năng cơ bản như đăng nhập, danh mục, sản phẩm, giỏ hàng và đơn hàng, Shopsflow còn có các luồng như phân quyền Admin/Customer, thanh toán, đổi trả, đánh giá, hỗ trợ khách hàng và thông báo. Điều này giúp em kiểm tra kiến trúc cloud bằng một ứng dụng có nhiều mối liên hệ thực tế hơn một trang web tĩnh đơn giản.

Mục tiêu của đề xuất không chỉ là làm cho website truy cập được trên Internet. Em muốn tách từng tầng của hệ thống, giới hạn quyền truy cập giữa các tầng, quản lý backend bằng container, theo dõi lỗi bằng log và xây dựng một quy trình triển khai có thể lặp lại.

**Website đã triển khai:** [Shopsflow trên Amazon CloudFront](https://d2m34udjfc5fxq.cloudfront.net/)

## 2. Mục tiêu của đề xuất

Đề xuất tập trung vào các mục tiêu sau:

1. Phân phối frontend React/Vite bằng dịch vụ phù hợp với static content.
2. Chạy backend Spring Boot trong container mà không phải quản trị máy chủ EC2 trực tiếp.
3. Đặt PostgreSQL trong private network và chỉ cho backend kết nối.
4. Sử dụng một điểm vào ổn định cho API, có health check trước khi nhận traffic.
5. Quản lý Docker image theo phiên bản để việc release và rollback rõ ràng hơn.
6. Thu thập log và metric để có thể xác định lỗi ở network, container, load balancer hoặc database.
7. Hỗ trợ outbound traffic cho backend khi cần gọi VNPAY sandbox, dịch vụ email hoặc API bên ngoài.
8. Xây dựng checklist kiểm thử và cleanup để tránh tài nguyên AWS tiếp tục phát sinh chi phí sau workshop.

Kết quả đầu ra của đề xuất gồm sơ đồ kiến trúc, tài nguyên AWS đã triển khai, quy trình hands-on workshop, bằng chứng cấu hình, các tình huống kiểm thử và hướng xử lý lỗi thường gặp.

## 3. Hiện trạng ứng dụng và các yêu cầu cần giải quyết

Khi chạy local bằng Docker Compose, frontend, backend và database có thể giao tiếp trong cùng một máy. Mô hình này thuận tiện cho phát triển nhưng chưa phù hợp để triển khai lâu dài trên cloud vì các thành phần phụ thuộc chặt vào nhau và có thể bị public quá mức.

Các yêu cầu chính của Shopsflow khi đưa lên AWS gồm:

| Nhóm yêu cầu | Nội dung cần giải quyết |
|---|---|
| Frontend | Phân phối nhanh, hỗ trợ HTTPS, không cần duy trì server chỉ để trả HTML/CSS/JavaScript |
| Backend | Chạy đúng môi trường Docker, dễ thay phiên bản, có health check và không public task trực tiếp |
| Database | Lưu dữ liệu bền vững, không mở PostgreSQL ra Internet, có backup và snapshot |
| Network | Tách public/private subnet, kiểm soát từng hop bằng route table và Security Group |
| Security | Không lưu access key hoặc secret trong source code; tách execution role và task role |
| Payment | Backend có outbound để gọi VNPAY sandbox và chỉ cập nhật đơn hàng sau khi xác minh kết quả |
| Operations | Có log, metric, validation checklist và quy trình troubleshooting |
| Cost | Nhận biết các tài nguyên tính phí theo thời gian như NAT Gateway, ALB, Fargate và RDS |

## 4. Kiến trúc đề xuất

![Sơ đồ kiến trúc triển khai Shopsflow trên AWS](images/5-Workshop/architecture.png?featherlight=false)
*Hình 1. Sơ đồ kiến trúc tổng thể của Shopsflow trên AWS. CloudFront và S3 phân phối frontend; Application Load Balancer chuyển API request đến ECS Fargate; backend kết nối RDS PostgreSQL trong private network; ECR lưu Docker image và CloudWatch hỗ trợ giám sát hệ thống.*




Kiến trúc được chia thành bốn luồng chính.

### 4.1. Luồng truy cập frontend

1. Người dùng truy cập domain của Amazon CloudFront.
2. CloudFront nhận request HTTPS và lấy static artifact từ S3 origin.
3. Các file React/Vite được cache tại edge location khi phù hợp.
4. S3 bucket không cần public trực tiếp; CloudFront đọc object thông qua Origin Access Control.

### 4.2. Luồng gọi API

1. Frontend gửi request đến đường dẫn `/api/*`.
2. CloudFront chuyển nhóm request này đến Application Load Balancer.
3. ALB thực hiện health check và chỉ chuyển traffic đến ECS task đang healthy.
4. ECS Fargate task chạy Spring Boot trong private subnet và xử lý nghiệp vụ.
5. Backend kết nối RDS PostgreSQL qua port `5432` trong VPC.

### 4.3. Luồng thanh toán và dịch vụ bên ngoài

Khi khách hàng checkout, backend tạo dữ liệu thanh toán và chữ ký theo cấu hình VNPAY sandbox. Do task nằm trong private subnet, kết nối outbound được đi qua NAT Gateway. Sau khi người dùng hoàn tất thanh toán, backend phải xác minh chữ ký, mã giao dịch và trạng thái trước khi cập nhật đơn hàng. Redirect ở trình duyệt chỉ là một phần của luồng, không phải bằng chứng duy nhất cho giao dịch thành công.

### 4.4. Luồng phát hành phiên bản

```text
Source code
→ Build ứng dụng
→ Build Docker image
→ Push image lên Amazon ECR
→ Tạo ECS Task Definition revision mới
→ Update ECS Service
→ ALB kiểm tra target mới
→ Chuyển traffic khi target healthy
```

Frontend được phát hành riêng bằng cách build thư mục `dist`, đồng bộ lên S3 và tạo CloudFront invalidation khi cần làm mới cache. Cách tách này giúp frontend và backend có thể cập nhật độc lập.

## 5. Lý do lựa chọn các dịch vụ AWS

### Amazon S3 và Amazon CloudFront

React/Vite sau khi build tạo ra static files. S3 phù hợp để lưu artifact, còn CloudFront cung cấp HTTPS, CDN và một domain công khai. Em chọn cách này thay vì chạy Nginx trên một máy chủ chỉ để phục vụ frontend.

### Application Load Balancer

ALB là entry point của backend. ALB giúp tách client khỏi địa chỉ của ECS task, kiểm tra health và hỗ trợ nhiều task trong tương lai. Task Fargate không cần public IP.

### Amazon ECS on AWS Fargate

Fargate cho phép em tập trung vào Docker image, CPU, memory, environment variable, IAM role và networking mà không phải quản lý EC2 host. Đây là lựa chọn phù hợp với mục tiêu học container deployment trong phạm vi kỳ thực tập.

### Amazon ECR

ECR lưu backend image trong cùng hệ sinh thái AWS. Mỗi lần release có thể gắn với image tag hoặc digest và một task definition revision cụ thể, giúp kiểm tra phiên bản đang chạy dễ hơn.

### Amazon RDS for PostgreSQL

Shopsflow đã dùng PostgreSQL nên RDS giúp giữ nguyên engine, đồng thời tách lifecycle của database khỏi container. Database được đặt trong DB subnet group private và không bật public access.

### VPC, Internet Gateway, NAT Gateway và Security Group

ALB cần nằm ở public subnets để nhận request, còn ECS và RDS nằm ở private subnets. Internet Gateway phục vụ public route; NAT Gateway chỉ cung cấp outbound cho private workload. Security Group giới hạn traffic theo chuỗi `ALB → ECS → RDS` thay vì mở bằng CIDR rộng.

### IAM và Amazon CloudWatch

IAM dùng để tách quyền của người triển khai, ECS task execution role và application task role. CloudWatch tập trung log cùng metric để em kiểm tra task start/stop, target health, HTTP error và kết nối database.

## 6. Nguyên tắc bảo mật và vận hành

Các nguyên tắc em áp dụng trong thiết kế gồm:

- Chỉ CloudFront và ALB là các điểm vào public của ứng dụng.
- ECS task và RDS không được gán public IP.
- `alb-sg` chỉ mở port cần thiết cho HTTP/HTTPS.
- `ecs-sg` chỉ nhận port ứng dụng từ `alb-sg`.
- `rds-sg` chỉ nhận PostgreSQL `5432` từ `ecs-sg`.
- Dùng Security Group reference thay cho mở `0.0.0.0/0` ở tầng backend và database.
- Task execution role chỉ phục vụ pull image và ghi log; task role chỉ cấp quyền mà application cần.
- Không commit database password, JWT secret, mail credential hoặc VNPAY secret lên GitHub.
- Mỗi backend release tạo image và task definition revision mới; không SSH vào container để sửa code.
- Bật backup RDS và tạo snapshot trước thay đổi dữ liệu quan trọng.

## 7. Kế hoạch triển khai và kiểm thử

Em chia quá trình triển khai theo dependency để lỗi dễ được cô lập:

1. Chuẩn bị AWS account, Region, AWS CLI, Docker, Java/Maven và Node.js.
2. Tạo VPC, hai public subnets, hai private subnets, route table, Internet Gateway và NAT Gateway.
3. Tạo Security Group và IAM role trước khi tạo workload.
4. Tạo DB subnet group và RDS PostgreSQL private.
5. Build backend image, push lên ECR và khai báo ECS Task Definition.
6. Tạo ALB, listener, target group và health check.
7. Tạo ECS Fargate Service trong private subnets và kết nối RDS.
8. Build frontend, upload lên S3 và cấu hình CloudFront.
9. Kiểm tra frontend, API, database, authentication, order, inventory, return, review, support và VNPAY sandbox.
10. Kiểm tra CloudWatch log, target health, task replacement và quy trình redeploy.
11. Dọn tài nguyên theo thứ tự phụ thuộc nếu kết thúc lab.

Các tiêu chí nghiệm thu quan trọng là frontend tải qua CloudFront, API đến được ECS qua ALB, RDS không public, backend ghi/đọc dữ liệu thành công, payment chỉ cập nhật sau xác minh và log đủ để xác định nguyên nhân khi deployment lỗi.

## 8. Rủi ro, giới hạn và cách giảm thiểu

| Rủi ro hoặc giới hạn | Cách xử lý trong phạm vi đề xuất |
|---|---|
| ECS task không khởi động | Kiểm tra image URI, execution role, CPU/memory, environment variable và stopped reason |
| ALB target unhealthy | Kiểm tra health-check path, container port, target group và inbound rule của `ecs-sg` |
| Backend không kết nối RDS | Kiểm tra endpoint, database name, credential, datasource URL và `rds-sg` |
| Frontend refresh bị 403/404 | Cấu hình SPA fallback hoặc CloudFront custom error response về `index.html` |
| Payment bị cập nhật sai | Xác minh signature và trạng thái ở backend, không tin riêng redirect phía client |
| Secret xuất hiện trong repository | Xóa khỏi Git history nếu cần, rotate secret và chuyển sang secret store khi hoàn thiện |
| Chi phí ngoài dự kiến | Theo dõi NAT Gateway, ALB, Fargate, RDS, log retention và data transfer |
| Mất dữ liệu | Bật automated backup, tạo snapshot và thử quy trình restore |
| Phạm vi quá lớn | Chỉ ghi các chức năng đã triển khai hoặc đã kiểm thử; CI/CD, WAF, IaC và autoscaling nâng cao để ở roadmap |

## 9. Kết quả kỳ vọng và hướng phát triển

Sau khi hoàn thành đề xuất, em kỳ vọng có thể giải thích rõ toàn bộ đường đi của một request, lý do mỗi dịch vụ tồn tại và cách xử lý khi một tầng gặp lỗi. Hệ thống cần thể hiện được các kết quả sau:

- Frontend React/Vite được phân phối qua S3 và CloudFront.
- Backend Spring Boot được quản lý bằng Docker image trên ECR và chạy trên ECS Fargate.
- ALB chỉ gửi traffic tới task healthy.
- RDS PostgreSQL nằm trong private network và chỉ cho ECS truy cập.
- CloudWatch cung cấp log và metric phục vụ troubleshooting.
- Release backend và frontend có quy trình riêng, có thể lặp lại.
- Workshop, sơ đồ kiến trúc và bằng chứng AWS Console mô tả cùng một hệ thống.

Trong giai đoạn tiếp theo, kiến trúc có thể được mở rộng bằng AWS Secrets Manager, AWS WAF, ACM/Route 53 với custom domain, ECS Service Auto Scaling, CI/CD qua GitHub Actions hoặc CodePipeline, và Infrastructure as Code. Các hạng mục này được xem là hướng phát triển, không được trình bày như phần đã hoàn tất trong workshop hiện tại.
