---
title: "Event 2 - FCAJ x Agentic AI Build Week"
date: 2026-07-25
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Báo cáo sự kiện: FCAJ x Agentic AI Build Week: Show Up. Build. Pitch. WIN!

## Tổng quan

Sự kiện ngày 25/7 diễn ra ở thời điểm em đã học qua phần lớn các thành phần chính của kiến trúc Shopsflow. Vì vậy khi nghe các team trình bày, em có thể liên hệ trực tiếp với những câu hỏi mình đang gặp: nên giới hạn scope tới đâu, làm sao giải thích architecture dễ hiểu, cost có được tính trong solution hay không và demo cần chuẩn bị như thế nào.

Bốn phần trình bày em theo dõi có chủ đề khác nhau, nhưng điểm chung là các team đều phải biến một ý tưởng thành một sản phẩm có flow, architecture và demo cụ thể. Đây là điều em thấy có giá trị nhất đối với kỳ thực tập của mình.

## 1. OneTeam - AI-Powered Conversational Ordering

OneTeam trình bày một conversational ordering agent cho KFC, với mục tiêu cho phép người dùng đặt hàng ngay trong kênh chat thay vì phải đổi ứng dụng.

### Điều em chú ý ở bài toán

Chatbot trả lời câu hỏi thì tương đối dễ hình dung, nhưng một agent tạo order thật phải xử lý menu, số lượng, variant, promotion, cart state và bước xác nhận. Khi sai, lỗi không chỉ là câu trả lời “không hay” mà có thể ảnh hưởng tới đơn hàng và tiền thật.

Phần workflow **Goal → Plan → Tools → Act → Verify** giúp em hiểu cách tách việc model hiểu ngôn ngữ khỏi phần business data cần được kiểm chứng bằng tool/system thật.

### Tư duy kiến trúc em học được

Em ấn tượng với ý “design once, deploy everywhere”: thay vì build riêng từng bot cho từng channel, solution tách adapter, connector và tool để dễ mở rộng. Điều này khiến em quay lại Shopsflow và nghĩ nhiều hơn về boundary giữa frontend, API, deployment artifact và database.

## 2. Signal Scout - Evidence-Driven Strategic Intelligence

Signal Scout tập trung vào việc phát hiện sớm các thay đổi chiến lược của doanh nghiệp từ nhiều nguồn tín hiệu khác nhau và hỗ trợ người dùng bằng dashboard có evidence.

### Điều em học được

Phần cost của solution làm em chú ý vì team không chỉ trình bày “dùng service gì” mà còn ước lượng nhiều mức sử dụng và thử một kiến trúc tiết kiệm hơn.

Điều này khá giống vấn đề em đang gặp với NAT Gateway và Cross-AZ trong Shopsflow: kiến trúc chạy được chưa đủ, cần biết thành phần nào có thể trở thành cost driver khi traffic tăng.

## 3. Plan V - Solution Architect Professional AI Native App

Plan V đề xuất một AI Native App hỗ trợ Solution Architect đọc requirement, draft kiến trúc, tạo diagram, IaC và ước lượng chi phí AWS.

### Điều em thấy hữu ích

Bài toán này rất gần với quá trình em tự làm Proposal. Khi requirement chưa rõ, việc vẽ một kiến trúc đẹp không giúp nhiều. Solution phải chỉ ra assumption và requirement gap, rồi cho phép refine dần.

Sau phần này, em rà lại Proposal Shopsflow và cố phân biệt rõ đâu là requirement hiện tại, đâu là roadmap. Em không muốn WAF, KMS, Secrets Manager hay Auto Scaling xuất hiện như phần đã triển khai khi em mới chỉ xem chúng là hướng mở rộng.

## 4. Team 3KA - 24 Hours of Building, Failing, and Learning

Team 3KA chia sẻ hành trình hackathon với dự án S.H.E.P.H.E.R.D, kết hợp computer vision, object tracking, cloud inference, dashboard và Agentic AI để hỗ trợ theo dõi crowd/queue.

### Điều em ấn tượng

Ngoài phần kỹ thuật, team nói khá nhiều về những khó khăn rất “thật”: thiếu thời gian, lần đầu làm AWS, code không chạy, thiếu ngủ, quên commit và phải debug tới khuya.

Em thích phần này vì nó làm em thấy quá trình build sản phẩm không hề tuyến tính. Việc gặp lỗi không có nghĩa là project thất bại; quan trọng là biết cắt scope, chia role, chuẩn bị demo và ưu tiên phần cần chạy được trước.

### Bài học em rút ra

- Một mục tiêu rõ ràng giúp team tránh bị kéo vào quá nhiều feature.
- Một feature hoàn chỉnh tốt hơn nhiều feature dở dang.
- Chuẩn bị account, template, role và demo plan từ trước sẽ tiết kiệm rất nhiều thời gian.
- Architecture cần phục vụ sản phẩm, không phải để trình diễn số lượng công nghệ.

## Những thay đổi em áp dụng vào Shopsflow sau sự kiện

Sau ngày 25/7, em review lại toàn bộ architecture với ba tiêu chí: **có phục vụ requirement không, em có kiểm chứng được không, và em có giải thích được trade-off không**.

Kết quả là em chốt scope tập trung vào CloudFront/S3, ALB, ECS Fargate, ECR, RDS, NAT, IAM và CloudWatch. Một số service nâng cao được chuyển sang roadmap thay vì giữ trong sơ đồ final.

Em cũng sửa cách trình bày Proposal và Workshop theo flow thay vì danh sách service. Với em, đây là ảnh hưởng rõ nhất của sự kiện tới báo cáo thực tập.

## Kết luận

Sự kiện giúp em hiểu thêm rằng kỹ năng build solution bao gồm cả kỹ thuật, cost, teamwork, scope và communication. Sau khi tham dự, em tự tin hơn trong việc nói “chưa cần” với một service nếu chưa có requirement rõ, thay vì cố làm kiến trúc lớn hơn mức project cần.

## Tài liệu sự kiện

[Tài liệu FCAJ x Agentic AI Build Week trên Google Drive](https://drive.google.com/drive/folders/1goIcF8jRIGZczB4DBHGTsS6mp41FWmLL)

---

## Minh chứng tham gia

{{< report-image src="images/4-EventParticipated/event2-participation-proof.png" alt="Minh chứng tham gia Event 2 - FCAJ x Agentic AI Build Week" width="520px" caption="Hình 2. Minh chứng em tham gia sự kiện FCAJ x Agentic AI Build Week: Show Up. Build. Pitch. WIN!" >}}
