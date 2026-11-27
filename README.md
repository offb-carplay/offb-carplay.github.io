# OFFB-Carplay — ba phiên bản

| Phiên bản | Trạng thái | Tải |
|---|---|---|
| 1.0.4.2+offb1 | Bản mới, chưa kiểm chứng trên iPhone | [DEB](debs/OFFB-CarPlay_1.0.4.2+offb1_Trial15_RootHide_TEST.deb) |
| 1.0.4.1+offb1 | Chủ máy đã xác nhận cài thành công | [DEB](debs/OFFB-CarPlay_1.0.4.1+offb1_Trial15_RootHide_TEST.deb) |
| 1.0.3.10+offb4 | Bản trước để lựa chọn | [DEB](debs/OFFB-CarPlay_1.0.3.10+offb4_Trial15_RootHide_TEST.deb) |

Cùng package ID, cài thay thế nhau, không cài song song. Nguồn APT thường ưu tiên bản mới nhất; chọn phiên bản nếu trình quản lý hỗ trợ hoặc tải DEB bản cũ trực tiếp. Giữ đúng ba DEB trong release-policy.json và cập nhật toàn bộ chỉ mục cùng nhau.

1.0.4.2 bổ sung chế độ Mát 30 Hz, thu nhỏ HUD và khôi phục module; có thay đổi xử lý video/scene. Nhận định từ phân tích tĩnh; chưa xác minh hết lỗi hoặc tương thích mọi iOS/xe.

Tên/icon OFFB, hỗ trợ 0945070632. Cấu hình license như offb4: máy mới tự xin 15 ngày khi xác thực trực tuyến; license đã có giữ nguyên, đổi phiên bản với cùng khóa máy không cộng thêm ngày. Mã vĩnh viễn từ bot hiện tại tiếp tục dùng.

Workflow Publish OFFB APT repository chạy thủ công. latest.json là 1.0.4.2/build 262. Chỉ xuất bản sau khi đã thử bản mới. Không đưa token, private key hoặc mã server vào repo công khai.
