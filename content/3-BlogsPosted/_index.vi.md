---
title: "Các bài blogs đã đăng"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---


Trong quá trình học AWS, nhóm em có viết và chia sẻ ba bài Blog về những tình huống khá dễ bỏ qua khi chỉ làm theo tutorial. Nhóm em chọn các chủ đề này vì chúng buộc nhóm em phải nhìn AWS ở góc độ vận hành thực tế hơn: có những cấu hình vẫn chạy nhưng có thể gây thêm chi phí, có những quyền IAM tưởng nhỏ nhưng lại ảnh hưởng lớn tới security, và có những lỗi network chỉ xuất hiện khi hệ thống bắt đầu phức tạp hơn.

Nội dung các bài đã đăng được giữ nguyên. Ở phần này, nhóm em ghi lại những điều nhóm em rút ra và cách các bài viết ảnh hưởng tới kiến trúc Shopsflow.

### [Blog 1 - 3 CHI TIẾT "NGÁCH" TRÊN AWS ÍT AI NÓI CHO BẠN BIẾT, NHƯNG ĐỤNG VÀO LÀ DÍNH SỰ CỐ](3.1-Blog1/)

Bài đầu tiên nói về Incomplete Multipart Uploads trên S3, IMDSv2 Hop Limit khi chạy Docker trên EC2 và đặc tính của `/tmp` trong Lambda.

Điều nhóm em áp dụng trực tiếp vào Shopsflow là cách nhìn về lifecycle của storage và container runtime. Frontend của Shopsflow dùng S3 nên nhóm em chú ý hơn tới cách object được tạo/lưu. Phần IMDSv2 không còn xuất hiện trực tiếp trong kiến trúc cuối vì backend chuyển sang Fargate, nhưng nó giúp nhóm em hiểu vì sao việc phụ thuộc vào EC2 host metadata có thể làm container deployment phức tạp hơn.

### [Blog 2 - NHỮNG "CÁI BẪY" ẨN KỸ TRONG AWS MÀ TÀI LIỆU CHÍNH THỨC ÍT KHI CẢNH BÁO BẠN](3.2-Blog2/)

Bài thứ hai tập trung vào NAT Gateway/S3 data processing, Glacier overhead với object nhỏ, `iam:PassRole` và EBS volume modification.

Hai nội dung ảnh hưởng nhiều nhất tới Shopsflow là **NAT Gateway cost** và **`iam:PassRole`**. Vì Fargate task nằm private subnet và cần outbound, NAT Gateway trở thành một cost driver cần theo dõi. Với ECS, việc developer/service pass role cũng khiến nhóm em chú ý hơn tới least privilege thay vì cấp một role quá rộng cho tiện.

### [Blog 3 - NHỮNG KỸ THUẬT "NGẦM" TRÊN AWS: TỪ TIỀN PHẠT ẨN ĐẾN NHỮNG SỰ CỐ MẠNG VÔ HÌNH](3.3-Blog3/)

Bài thứ ba đi sâu vào Cross-AZ Data Transfer, MTU/Path MTU Discovery, DynamoDB On-Demand và CloudWatch Logs Insights scan cost.

Với Shopsflow chạy Fargate trên nhiều AZ, phần Cross-AZ giúp nhóm em để ý hơn tới network path và route theo AZ. Phần CloudWatch Logs Insights cũng nhắc nhóm em rằng observability có chi phí, vì vậy query log nên có time range và mục tiêu rõ thay vì quét toàn bộ dữ liệu chỉ để “tìm thử”.

## Điều nhóm em rút ra sau ba bài Blog

Sau khi viết ba bài, checklist của nhóm em khi nhìn một kiến trúc AWS đã thay đổi khá nhiều. Nhóm em không chỉ hỏi “service này có chạy được không” mà thường hỏi thêm:

1. Traffic đang đi qua đâu và có tạo data transfer/NAT cost không?
2. Role nào đang được gán, ai có quyền `iam:PassRole` và quyền đó có rộng quá không?
3. Khi có lỗi, log/metric nào giúp khoanh vùng nguyên nhân?
4. Kiến thức nào áp dụng trực tiếp cho Shopsflow, kiến thức nào chỉ giúp nhóm em so sánh lựa chọn khác?
5. Một managed service giúp giảm phần việc nào, và phần trách nhiệm nào vẫn còn ở phía nhóm em?

Đối với nhóm em, việc viết Blog cũng là một cách kiểm tra lại kiến thức. Có những khái niệm khi đọc thì thấy đã hiểu, nhưng đến lúc phải viết sao cho người khác đọc được thì nhóm em mới nhận ra mình còn thiếu phần “vì sao”.
