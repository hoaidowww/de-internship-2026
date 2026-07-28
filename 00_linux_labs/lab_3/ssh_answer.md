## Bài 3.8 [Trung bình - Khó] — Kiểm tra cổng Database từ xa

### Đề bài

Kiểm tra xem máy chủ từ xa có đang mở và kết nối được vào cổng `5432` của Database hay không mà không cần đăng nhập vào máy chủ đó, sử dụng công cụ `telnet` hoặc `nc -zv`.

### Thực hiện

Sử dụng lệnh `nc -zv` để kiểm tra cổng `5432` trên địa chỉ `127.0.0.1`:

```bash
nc -zv 127.0.0.1 5432
```

### Kết quả

```text
Connection to 127.0.0.1 5432 port [tcp/postgresql] succeeded!
```

### Phân tích kết quả

Kết quả `succeeded!` cho thấy kết nối TCP tới cổng `5432` đã thành công.

Cổng `5432` là cổng mặc định thường được sử dụng bởi PostgreSQL Database. Kết quả kiểm tra cho thấy hiện tại có dịch vụ đang lắng nghe và chấp nhận kết nối trên cổng này.

### Kết luận

Đã kiểm tra thành công khả năng kết nối tới cổng Database `5432` bằng công cụ `nc` mà không cần đăng nhập vào máy chủ.

Lệnh đã sử dụng:

```bash
nc -zv 127.0.0.1 5432
```

Kết quả:

```text
Connection to 127.0.0.1 5432 port [tcp/postgresql] succeeded!
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.8](images/bai-3.8.jpg)

---
## Bài 3.9 [Trung bình] — Tra cứu địa chỉ IP bằng DNS

### Đề bài

Tra cứu địa chỉ IP của tên miền dịch vụ API bằng lệnh `nslookup`.

Tên miền cần tra cứu:

```text
api.open-meteo.com
```

### Thực hiện

Sử dụng lệnh:

```bash
nslookup api.open-meteo.com
```

### Kết quả

```text
Server:         10.255.255.254
Address:        10.255.255.254#53

Non-authoritative answer:
Name:   api.open-meteo.com
Address: 94.130.142.35
```

Tên miền:

```text
api.open-meteo.com
```

được phân giải thành địa chỉ IP:

```text
94.130.142.35
```

### Kết luận

Đã tra cứu thành công địa chỉ IP của tên miền `api.open-meteo.com` bằng lệnh `nslookup`.

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.9](images/bai-3.9.jpg)

---

