---
title: "[Logix] Bài 11: Mô phỏng chương trình RSLogix 5000 với RSEmulate 5000"
date: 2012-10-23
categories: [Logix, Rockwell]
tags: [rslogix 5000, rsemulate, mô phỏng, plc]
summary: "Hướng dẫn mô phỏng chương trình RSLogix 5000 với RSEmulate 5000, kinh nghiệm thực chiến từ kỹ sư tự động hóa."
---

# [Logix] Bài 11: Mô phỏng chương trình RSLogix 5000 với RSEmulate 5000

> **Chia sẻ từ kinh nghiệm thực tế của một kỹ sư tự động hóa hơn 15 năm trong nghề.**

Mô phỏng là công cụ không thể thiếu với bất kỳ ai làm lập trình PLC. Nhờ mô phỏng, chúng ta kiểm tra logic, phát hiện lỗi và tối ưu chương trình trước khi triển khai lên hệ thống thực tế – tiết kiệm rất nhiều thời gian, chi phí và tránh rủi ro khi vận hành.

## 1. Lựa chọn phần mềm mô phỏng

Để mô phỏng cho RSLogix 5000, bạn có hai lựa chọn: **RSEmulate 5000** hoặc **SoftLogix**. Thông thường, nếu chỉ cần mô phỏng, RSEmulate 5000 là lựa chọn tối ưu vì thao tác đơn giản, không cần cấu hình lại IO khi thay đổi CPU.

> **Lưu ý:**
> - Phải dùng đúng phiên bản RSEmulate 5000 tương ứng với RSLogix 5000 (ví dụ: version 20).
> - RSEmulate 5000 hoạt động như một CPU thật trên chassis ảo.

## 2. Tạo CPU giả lập trên RSEmulate 5000

Khởi động phần mềm, bạn sẽ thấy giao diện với các slot trống trên chassis:

![Chassis ban đầu](../../assets/images/logix/102312_1622_bi11mphn1.png)

**Các bước tạo CPU:**
- Click phải vào slot trống (nên chọn từ slot 2 trở đi, slot 1 dành cho RSLinx Enterprise).

![Chọn slot](../../assets/images/logix/102312_1622_bi11mphn2.png)

- Chọn loại CPU phù hợp, nhấn OK.

![Chọn CPU](../../assets/images/logix/102312_1622_bi11mphn3.png)

- Next liên tục để xác nhận các thông số mặc định.

![Next 1](../../assets/images/logix/102312_1622_bi11mphn4.png)
![Next 2](../../assets/images/logix/102312_1622_bi11mphn5.png)

- Finish để hoàn tất.

![Finish](../../assets/images/logix/102312_1622_bi11mphn6.png)

- CPU sẽ xuất hiện trên chassis ảo:

![CPU đã tạo](../../assets/images/logix/102312_1622_bi11mphn7.png)

Bạn có thể tạo nhiều CPU trên chassis ảo, tương tự như phần cứng thật.

## 3. Cấu hình RSLinx Classic để nhận CPU mô phỏng

Để RSLogix 5000 giao tiếp với CPU mô phỏng, cần cấu hình driver trong RSLinx Classic:

- Mở RSLinx Classic, chọn **Configure Drivers**.

![Configure Drivers](../../assets/images/logix/102312_1622_bi11mphn8.png)

- Thêm driver mới, chọn **Virtual Backplane** và nhấn **Add New**.

![Chọn Virtual Backplane](../../assets/images/logix/102312_1622_bi11mphn9.png)
![Add New](../../assets/images/logix/102312_1622_bi11mphn10.png)

- Nhấn OK để xác nhận.

![OK](../../assets/images/logix/102312_1622_bi11mphn11.png)

- Sau khi cấu hình xong, CPU mô phỏng sẽ xuất hiện trong RSLinx:

![CPU xuất hiện](../../assets/images/logix/102312_1622_bi11mphn12.png)

## 4. Download/Upload và chỉnh sửa Online với CPU mô phỏng

- Trong RSLogix 5000, thay CPU thật bằng CPU mô phỏng:
  - Click phải vào CPU, chọn **Properties**.

![Properties](../../assets/images/logix/102312_1622_bi11mphn13.png)

  - Chọn **Change Controller**.

![Change Controller](../../assets/images/logix/102312_1622_bi11mphn14.png)

  - Chọn **Emulator**, đúng revision, nhấn OK.

![Chọn Emulator](../../assets/images/logix/102312_1622_bi11mphn15.png)

  - Xác nhận, chọn đúng slot đã cấu hình (ví dụ: slot 2).

![Xác nhận](../../assets/images/logix/102312_1622_bi11mphn16.png)
![Chọn slot](../../assets/images/logix/102312_1622_bi11mphn17.png)

- Bây giờ bạn có thể **Download** chương trình:

![Download](../../assets/images/logix/102312_1622_bi11mphn18.png)

- Và **Online** để kiểm tra, chỉnh sửa trực tiếp:

![Online](../../assets/images/logix/102312_1622_bi11mphn19.png)

Các thao tác upload, chỉnh sửa online hoàn toàn tương tự như trên CPU thật.

## 5. Ghi chú thực tế

- RSEmulate 5000 là phần mềm thương mại, cần mua license.
- Khi lập trình, nên chủ động viết các đoạn code kiểm thử mô phỏng để kiểm tra logic, giảm thiểu lỗi khi triển khai thực tế.

---

*Bài viết được biên soạn lại từ kinh nghiệm thực chiến, hy vọng giúp ích cho anh em kỹ sư tự động hóa.*
