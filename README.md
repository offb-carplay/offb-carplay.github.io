# OFFB-Carplay — chọn phiên bản

Cùng một nguồn APT, giữ hai phiên bản để lựa chọn:

| Phiên bản | Tải trực tiếp |
|---|---|
| 1.0.4.1+offb1 — bản mới, chủ máy đã xác nhận cài thành công | [Tải DEB](debs/OFFB-CarPlay_1.0.4.1+offb1_Trial15_RootHide_TEST.deb) |
| 1.0.3.10+offb4 — bản trước | [Tải DEB](debs/OFFB-CarPlay_1.0.3.10+offb4_Trial15_RootHide_TEST.deb) |

Hai bản có cùng package ID, thay thế nhau khi cài; không cài song song. Trình quản lý gói thường chọn bản mới nhất. Muốn bản cũ, chọn phiên bản nếu trình quản lý hỗ trợ hoặc tải DEB cũ bằng liên kết trên rồi cài theo quy trình jailbreak đang dùng. Tên tệp có TEST được giữ nguyên để bảo toàn DEB đã thử.

Cả hai dùng license OFFB: thiết bị mới tự đăng ký 15 ngày khi xác thực trực tuyến thành công; máy đã có license giữ nguyên. Cài lại/đổi phiên bản với cùng khóa thiết bị không đặt lại ngày dùng thử. Mã vĩnh viễn 10 số tiếp tục dùng qua bot hiện tại. Liên hệ: 0945070632.

Bản 1.0.4.1 được chủ máy xác nhận cài thành công; chưa có kiểm chứng đầy đủ mọi tính năng/mọi iOS 15–18. Báo cáo kỹ thuật riêng không thay thế thử trên xe.

Kho này chỉ chứa DEB và tài nguyên công khai. Giữ mã máy chủ, token và khóa riêng trong hệ thống riêng tư. release-policy.json yêu cầu đủ cả hai phiên bản; scripts/build_repo.py sinh Packages và các bản nén chứa cả hai. latest.json tiếp tục chỉ bản mới nhất. Workflow Publish OFFB APT repository chạy thủ công.
