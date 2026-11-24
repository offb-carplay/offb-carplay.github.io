# OFFB CarPlay — kho APT thử nghiệm

Bản mới nhất là `1.0.3.8+offb2`, Package ID `vn.cloud247.carplay-rebuild.m1`, kiến trúc `iphoneos-arm64e`, ứng dụng đặt iOS tối thiểu 15.0. Bên cung cấp thông báo hỗ trợ iOS 15/16/17/18; chưa kiểm thử thực tế tại đây.

Bản offb2 bỏ OFFBBranding.dylib và plist nạp module vì đường khởi động arm64e vẫn trùng module gây lỗi ở log iOS 17.0 của bản 1.0.3.7. Icon và tên OFFB vẫn giữ. Chưa xác nhận xử lý hết lỗi phải mở 2–3 lần; cần kiểm thử trên thiết bị và log của lần mở đầu nếu tái diễn.

Chưa kiểm thử trên iPhone/xe. Bản quyền gốc còn nguyên; cơ chế dùng thử OFFB 168 giờ và Telegram mới **chưa tích hợp vào gói này**.

## Xuất bản

1. Đưa toàn bộ nội dung thư mục này vào root của repository Public.
2. **Settings → Pages → Source → GitHub Actions**.
3. **Actions → Publish OFFB APT repository → Run workflow**.
4. Lấy địa chỉ chính thức trong Settings → Pages.

Địa chỉ `offb-carplay.github.io` yêu cầu Owner là `offb-carplay` và repository tên `offb-carplay.github.io`. Nếu Owner khác, dùng URL Pages tương ứng của tài khoản đó.

## Cập nhật

Thư mục `debs/` của bộ này chỉ chứa 1.0.3.8+offb2. Khi cập nhật một kho đã có sẵn, xóa các DEB cũ trong kho công khai để không đưa lại module lỗi vào chỉ mục. Bản sao cục bộ trước đó vẫn được giữ riêng.

`release-policy.json` quy định phiên bản được xuất bản và cấm module OFFBBranding cũ. Script sẽ báo lỗi nếu có sai phiên bản hoặc module này quay lại. Khi chuẩn bị phiên bản kế tiếp, cập nhật chính sách sau khi kiểm tra gói.

Chạy workflow lại hoặc tạo metadata cục bộ:

```sh
python scripts/build_repo.py
```

Kho chưa ký GPG. Không chứa source máy chủ, bot token hoặc dữ liệu khách hàng.
