# OFFB CarPlay — kho APT thử nghiệm

Bản mới nhất là `1.0.3.7+offb1`, Package ID `vn.cloud247.carplay-rebuild.m1`, kiến trúc `iphoneos-arm64e`, ứng dụng đặt iOS tối thiểu 15.0. Bên cung cấp thông báo hỗ trợ iOS 15/16/17/18; chưa kiểm thử thực tế tại đây. Bản mới không chứa module iOS 18 test1. Bản `1.0.3.4+ios18test1.offb1` được giữ để khôi phục khi phù hợp.

Chưa kiểm thử trên iPhone/xe. Bản quyền gốc còn nguyên; cơ chế dùng thử OFFB 168 giờ và Telegram mới **chưa tích hợp vào gói này**.

## Xuất bản

1. Đưa toàn bộ nội dung thư mục này vào root của repository Public.
2. **Settings → Pages → Source → GitHub Actions**.
3. **Actions → Publish OFFB APT repository → Run workflow**.
4. Lấy địa chỉ chính thức trong Settings → Pages.

Địa chỉ `offb-carplay.github.io` yêu cầu Owner là `offb-carplay` và repository tên `offb-carplay.github.io`. Nếu Owner khác, dùng URL Pages tương ứng của tài khoản đó.

## Cập nhật

Thêm DEB phiên bản mới vào `debs/`. Chạy workflow lại hoặc tạo metadata cục bộ:

```sh
python scripts/build_repo.py
```

Kho chưa ký GPG. Không chứa source máy chủ, bot token hoặc dữ liệu khách hàng.
