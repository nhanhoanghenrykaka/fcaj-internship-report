---
title: "Event 1 - Meet 13/6"
date: 2026-06-13
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Báo cáo sự kiện: Meet 13/6

## Tổng quan

Meet 13/6 là sự kiện em tham gia ngay trước khi bắt đầu giai đoạn Worklog chính của kỳ thực tập. Nội dung buổi gặp khá đa dạng: từ system design trên AWS, câu chuyện phát triển nghề nghiệp trong cộng đồng AWS, công việc DevOps thực tế đến Data Analytics và văn hóa làm việc ở tập đoàn đa quốc gia.

Điều em thích ở buổi này là các phần chia sẻ không chỉ liệt kê công nghệ. Mỗi speaker đều nói nhiều về cách suy nghĩ, cách học và những kỹ năng cần có khi bước từ môi trường sinh viên sang công việc thực tế. Vì vậy, sau sự kiện em không xem mục tiêu của kỳ thực tập chỉ là “biết dùng thêm nhiều AWS service”, mà muốn học cách giải thích một hệ thống và hiểu trách nhiệm của mình khi vận hành nó.

## 1. A Scalable URL Shortening Service on AWS

Phần đầu trình bày một hệ thống rút gọn URL có khả năng mở rộng. Bài toán nhìn qua khá đơn giản: nhận URL dài, sinh short code và redirect. Tuy nhiên khi đặt vào môi trường có nhiều người dùng, bài toán bắt đầu liên quan tới latency, cache, database, khả năng scale và cách tránh tạo bottleneck.

### Điều em chú ý

Em thấy phần này hữu ích vì nó cho em một ví dụ system design dễ hiểu hơn so với việc học từng service riêng lẻ. Thay vì bắt đầu bằng câu “dùng DynamoDB hay ECS”, cách trình bày bắt đầu từ request của user rồi mới lựa chọn các lớp xử lý phù hợp.

Điều đó ảnh hưởng trực tiếp tới Shopsflow: em bắt đầu vẽ luồng `User → entry point → application → database` trước, sau đó mới gắn tên AWS service vào từng vị trí.

### Điều em học được

- Kiến trúc có khả năng mở rộng cần tách các responsibility thay vì dồn hết vào một server.
- Cache, load balancing và data layer phải được cân nhắc theo traffic pattern.
- Một service chỉ có ý nghĩa khi em giải thích được nó đang giải quyết bottleneck nào.

## 2. From First Cloud AI Journey to AWS Partner

Phần chia sẻ về hành trình từ FCAJ tới AWS Student Builder Group, AWS Community Builder và môi trường AWS Partner cho em một góc nhìn khá thực tế về việc phát triển nghề nghiệp.

Trước đó em thường nghĩ chứng chỉ hoặc số lượng service biết sử dụng là thước đo chính. Sau phần này, em thấy community, khả năng chia sẻ kiến thức, xây project và duy trì quá trình học dài hạn cũng quan trọng không kém.

### Điều em rút ra

Em muốn xem báo cáo thực tập và các Blog không chỉ là yêu cầu phải nộp, mà là cách ghi lại quá trình học để sau này có thể nhìn lại mình đã đi từ đâu. Việc viết lại kiến thức bằng ngôn ngữ của mình cũng giúp em nhận ra phần nào em thật sự hiểu, phần nào mới chỉ nhớ thao tác.

## 3. What Does a DevOps Engineer Really Do?

Đây là một trong những phần em thấy gần với project Shopsflow nhất. Nội dung nhấn mạnh rằng DevOps không chỉ là “người viết CI/CD” hay “người biết Docker/Kubernetes”. Công việc thực tế đòi hỏi hiểu cách application chạy, network hoạt động, log nằm ở đâu và cách giúp team deploy ổn định hơn.

### Những nền tảng được nhắc tới

- Linux.
- Networking basics.
- Python/Golang hoặc một ngôn ngữ lập trình.
- Git và CI/CD.
- Container.
- Cách build, test, deploy và đọc log của application.

### Điều em học được

Câu em nhớ nhất về tinh thần của phần này là **copy command không đồng nghĩa với hiểu**. Khi làm Workshop, em cố gắng không chỉ ghi “bấm vào đâu” mà còn giải thích vì sao ALB cần target group, vì sao Fargate ở private subnet cần NAT cho outbound hay vì sao RDS chỉ mở 5432 từ ECS SG.

## 4. Công việc thực tế và văn hóa tại tập đoàn đa quốc gia

Phần chia sẻ của Data Analytics Engineer và Process Engineer giúp em nhìn kỹ thuật từ góc độ business hơn.

### Data Analytics Engineer thực tế làm gì

Các ví dụ về dashboard, phân tích performance, tìm nguyên nhân biến động và phối hợp nhiều phòng ban cho em thấy công việc dữ liệu không dừng ở việc “làm báo cáo”. Giá trị nằm ở việc biến dữ liệu thành thông tin có thể hỗ trợ quyết định.

### Tư duy phát triển nghề nghiệp

Mô hình từ Follower → Learner → Problem Solver → System Thinker → Leader làm em khá ấn tượng. Em thấy mình đang ở giai đoạn Learner: vẫn cần hướng dẫn, nhưng cần tập đặt câu hỏi sâu hơn và chủ động giải thích tại sao mình làm một việc.

### Văn hóa và tuyển dụng tại MNC

Phần này giúp em hiểu thêm về quy trình phỏng vấn, communication và sự phù hợp văn hóa. Em cũng chú ý tới tinh thần no-blame khi xử lý sự cố: mục tiêu là tìm root cause và cải thiện hệ thống thay vì chỉ tìm người gây lỗi.

## Bài học em mang về từ Meet 13/6

Sau sự kiện, em ghi lại bốn điều muốn áp dụng trong kỳ thực tập:

1. Học AWS nhưng không bỏ qua nền tảng Linux, network, Git và programming.
2. Luôn bắt đầu từ problem/request flow trước khi chọn service.
3. Khi gặp lỗi, cố tìm root cause và hiểu vì sao, không chỉ copy một command để “fix tạm”.
4. Kỹ năng trình bày và viết tài liệu là một phần của công việc kỹ thuật, không phải phần phụ.

## Liên hệ với Shopsflow

Những bài học này ảnh hưởng khá rõ tới cách em xây architecture sau đó. Em chọn tách frontend, backend và database; xây security theo từng hop; ghi deployment flow từ Docker/ECR tới ECS; và cố gắng viết Workshop theo hướng người đọc hiểu được logic thay vì chỉ làm theo ảnh chụp màn hình.

## Tài liệu sự kiện

[Tài liệu Meet 13/06/2026 trên Google Drive](https://drive.google.com/drive/folders/1XYe3c3jX0F432hyQiCZBOGF2dDlIEwB4)

---

## Minh chứng tham gia

{{< report-image src="images/4-EventParticipated/event1-participation-proof.png" alt="Minh chứng tham gia Event 1 - Meet 13/6" width="520px" caption="Hình 1. Minh chứng em tham gia sự kiện Meet 13/6." >}}
