---
title: "S3 và CloudFront cho frontend"
date: 2026-06-15
weight: 3
chapter: false
pre: " <b> 5.4.3. </b> "
---

# 5.4.3. Deploy frontend bằng S3 và CloudFront

## 1. Build frontend

Tại thư mục frontend:

```bash
npm ci
npm run build
```

Kiểm tra biến môi trường build. Khi dùng CloudFront làm một domain chung, frontend nên gọi API bằng path phù hợp như `/api` thay vì hard-code `localhost`.

## 2. Tạo S3 bucket private và upload artifact

1. Tạo bucket có tên duy nhất.
2. Giữ **Block Public Access** được bật.
3. Upload nội dung bên trong thư mục `dist`.
4. Không public object bằng ACL.

Có thể đồng bộ bằng AWS CLI:

```bash
aws s3 sync dist/ s3://<frontend-bucket> --delete
```



![S3 bucket chứa frontend build](images/5-Workshop/s3_bucket.jpg?featherlight=false)
*Hình 1. S3 bucket lưu các artifact được tạo bởi `npm run build`, gồm `index.html`, JavaScript, CSS và các static asset của React/Vite.*

## 3. Tạo CloudFront distribution

Cấu hình distribution:

- S3 bucket là default origin;
- dùng Origin Access Control để CloudFront đọc bucket private;
- default root object là `index.html`;
- cấu hình SPA fallback cho client-side route;
- thêm ALB làm origin thứ hai;
- tạo behavior `/api/*` trỏ đến ALB và forward method, header, query string cần thiết;
- không cache API động theo chính sách dành cho static file.



![CloudFront distribution phân phối frontend](images/5-Workshop/fe_cloudfront.jpg?featherlight=false)
*Hình 2. CloudFront distribution cung cấp domain HTTPS cho người dùng, lấy frontend từ S3 và có thể chuyển behavior `/api/*` đến ALB.*

## 4. Kiểm tra frontend và API

1. Mở domain CloudFront.
2. Refresh ở một route con để kiểm tra SPA fallback.
3. Đăng nhập và gọi API qua cùng domain.
4. Kiểm tra browser Network để bảo đảm request không còn trỏ đến `localhost`.
5. Kiểm tra CORS nếu frontend và API dùng domain khác nhau.

## 5. Phát hành frontend mới

Sau khi upload bản build mới, tạo invalidation nếu file cũ vẫn bị cache:

```bash
aws cloudfront create-invalidation \
  --distribution-id <distribution-id> \
  --paths "/*"
```

Trong môi trường production, có thể dùng tên file có content hash để giảm phạm vi invalidation; `index.html` thường cần thời gian cache ngắn hơn asset đã hash.
