# OFFB CarPlay 1.0.3.10+offb4 — bản thử 15 ngày

Thiết bị chưa có license tự yêu cầu dùng thử sau respring khi khóa thiết bị và mạng sẵn sàng. Máy chủ bắt đầu đúng 15 ngày sau lần xác thực thành công. Không cần nhập mã. Máy đã có license giữ nguyên quyền hiện tại; cùng khóa thiết bị không được đặt lại thời hạn khi cài lại.

Hết dùng thử, quản trị viên tạo mã 10 số bằng `/vinhvien` trong @OFFBLicense_bot. Hạn offline 72 giờ là lịch làm mới biên nhận, không phải hạn của gói 15 ngày.

Gói giữ cấu trúc iphoneos-arm64e/RootHide của bản cung cấp, thêm OFFBAutoTrial.dylib gọi luồng ký và xác minh gốc. Không dùng module chuyển URL cũ. **Chưa xác nhận offb4 chạy trên iPhone thực tế**; thử trước khi phát hành rộng. Giữ bản offb3 để quay lại.

Đây là kho APT công khai. Chỉ để DEB offb4 trong debs/. Các chỉ mục phải cập nhật đồng bộ. Workflow “Publish OFFB APT repository” chạy thủ công. Không đưa token, khóa riêng hoặc mã máy chủ riêng tư vào kho này.
