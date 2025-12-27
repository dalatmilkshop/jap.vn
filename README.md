# jap.vn
Just Automation Platform | Rockwell Automation Archive

## Cấu trúc thư mục

- `index.html`: Trang chủ với tìm kiếm và chế độ tối
- `story.html`: Trang nội dung phụ
- `assets/`: Chứa tài nguyên tĩnh (ảnh, CSS, JS)
- `docs/`: Lưu trữ tài liệu, hướng dẫn mở rộng
  - `docs/logix/`: Series hướng dẫn Logix với breadcrumb và lazy loading
- `sitemap.xml`: Sitemap cho SEO
- `robots.txt`: Hướng dẫn cho bot crawler

## Tính năng chính

### 🎨 Giao diện người dùng
- **Chế độ tối (Dark Mode)**: Toggle button với localStorage
- **Tìm kiếm**: Hộp tìm kiếm real-time trên trang chủ
- **Đa ngôn ngữ**: Hỗ trợ tiếng Việt và tiếng Anh
- **Responsive**: Tương thích mobile và desktop

### 🔍 SEO & Performance
- **Structured Data**: JSON-LD cho Google Rich Snippets
- **Lazy Loading**: Tải hình ảnh theo yêu cầu cho hiệu suất tốt hơn
- **Breadcrumb Navigation**: Điều hướng dễ dàng trong docs
- **Meta Tags**: Open Graph, Twitter Cards, canonical URLs
- **Sitemap & Robots.txt**: Tối ưu hóa cho công cụ tìm kiếm

### 📚 Nội dung
- **Logix Series**: 17 bài hướng dẫn PLC Logix chi tiết
- **Bilingual**: Nội dung song ngữ Việt-Anh
- **Technical Archive**: Tài liệu Rockwell Automation

## Quy ước phát triển

- Thêm trang mới: tạo file `.html` ở root, liên kết từ `index.html`
- Tài nguyên dùng chung (ảnh, style, script) đặt trong `assets/`
- Tài liệu, hướng dẫn đặt trong `docs/`
- Sử dụng CSS variables cho theme consistency
- Áp dụng lazy loading cho tất cả hình ảnh
- Thêm structured data cho SEO

## Công nghệ sử dụng

- **HTML5**: Semantic markup
- **CSS3**: Variables, Flexbox, Media queries
- **JavaScript**: ES6+ cho interactivity
- **Schema.org**: Structured data
- **Google Fonts**: Roboto typography

## Hướng dẫn đóng góp

- Giữ cấu trúc thư mục rõ ràng, dễ mở rộng
- Đặt tên file ngắn gọn, không dấu, dùng tiếng Anh nếu có thể
- Cập nhật README.md khi thêm tính năng mới
- Kiểm tra SEO và performance trước khi commit

---
_Cập nhật: 2025-12-27_
