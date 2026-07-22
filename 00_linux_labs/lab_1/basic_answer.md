# LAB 1 - LINUX BASICS

---

# CHỦ ĐỀ 1: THAO TÁC HỆ THỐNG FILE & ĐIỀU HƯỚNG CLI

## Bài 1.1

### Đề bài

Hiển thị đường dẫn đầy đủ của thư mục hiện tại bạn đang đứng.

### Lệnh thực thi

```bash
hoaido@DESKTOP-4PVJOAL:~/de-internship-2026/00_linux_labs/lab_1$ pwd
/home/hoaido/de-internship-2026/00_linux_labs/lab_1
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.1](images/bai-1.1.jpg)

---

## Bài 1.2

### Đề bài

Liệt kê toàn bộ các file trong thư mục hiện tại bao gồm cả các file ẩn (bắt đầu bằng dấu `.`) kèm theo kích thước định dạng dễ đọc như KB/MB.

### Lệnh thực thi

```bash
hoaido@DESKTOP-4PVJOAL:~/de-internship-2026/00_linux_labs/lab_1$ ls -laH
total 60
drwxr-xr-x 2 hoaido hoaido  4096 Jul 22 07:32 .
drwxr-xr-x 3 hoaido hoaido  4096 Jul 21 16:23 ..
-rwxr-xr-x 1 hoaido hoaido 48792 Jul 21 17:00 bai-1.1.jpg
-rw-r--r-- 1 hoaido hoaido   605 Jul 22 07:32 basic_answer.md
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.2](images/bai-1.2.jpg)

---

## Bài 1.3

### Đề bài

Tạo cấu trúc thư mục `data/raw/2026/07` bằng một lệnh duy nhất.

### Lệnh thực thi

```bash
mkdir -p data/raw/2026/07
```

### Kiểm tra kết quả

```bash
ls -R 00_linux_labs
```

### Kết quả

```text
00_linux_labs:
lab_1

00_linux_labs/lab_1:
```

Sau khi thực hiện tạo thư mục:

```text
.
├── data
│   └── raw
│       └── 2026
│           └── 07
└── images
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.3](images/bai-1.3.jpg)

---

## Bài 1.4

### Đề bài

Tạo file `README.txt` chứa nội dung `Data Engineering Curriculum 2026`.

### Lệnh thực thi

```bash
echo "Data Engineering Curriculum 2026" > README.txt
```

### Kiểm tra kết quả

```bash
cat README.txt
```

### Kết quả

```text
Data Engineering Curriculum 2026
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.4](images/bai-1.4.jpg)

---

## Bài 1.5

### Đề bài

Sao chép file `README.txt` vào thư mục `data/raw/2026/07/`.

### Lệnh thực thi

```bash
cp README.txt data/raw/2026/07/
```

### Kiểm tra kết quả

```bash
ls -l data/raw/2026/07/
```

### Kết quả

```text
total 4
-rw-r--r-- 1 hoaido hoaido 33 Jul 22 08:24 README.txt
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.5](images/bai-1.5.jpg)

---

## Bài 1.6

### Đề bài

Di chuyển tệp `README.txt` trong thư mục `data/raw/2026/07/` ra thư mục cha `data/raw/2026/` và đổi tên thành `info.metadata`.

### Lệnh thực thi

```bash
mv data/raw/2026/07/README.txt data/raw/2026/info.metadata
```

### Kiểm tra kết quả

```bash
ls -l data/raw/2026/
```

### Kết quả

```text
total 8
drwxr-xr-x 2 hoaido hoaido 4096 Jul 22 08:50 07
-rw-r--r-- 1 hoaido hoaido   33 Jul 22 08:49 info.metadata
```

### Kiểm tra nội dung file

```bash
cat data/raw/2026/info.metadata
```

### Kết quả

```text
Data Engineering Curriculum 2026
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.6](images/bai-1.6.jpg)

---

## Bài 1.7

### Đề bài

Kiểm tra dung lượng ổ đĩa còn trống của toàn bộ các phân vùng trên hệ thống.

### Lệnh thực thi

```bash
df -h
```

### Kết quả

```text
Filesystem      Size  Used Avail Use% Mounted on
none            3.9G     0  3.9G   0% /usr/lib/modules/6.18.33.2-microsoft-standard-WSL2
none            3.9G  4.0K  3.9G   1% /mnt/wsl
drivers         477G  334G  143G  71% /usr/lib/wsl/drivers
/dev/sdd       1007G  2.1G  954G   1% /
none            3.9G   64K  3.9G   1% /mnt/wslg
none            3.9G     0  3.9G   0% /usr/lib/wsl/lib
rootfs          3.9G  2.8M  3.9G   1% /init
none            3.9G  508K  3.9G   1% /run
none            3.9G     0  3.9G   0% /run/lock
none            3.9G     0  3.9G   0% /run/shm
none            3.9G   80K  3.9G   1% /mnt/wslg/versions.txt
none            3.9G   80K  3.9G   1% /mnt/wslg/doc
C:\             477G  334G  143G  71% /mnt/c
D:\             487G  111G  377G  23% /mnt/d
G:\             200G   64G  137G  32% /mnt/g
tmpfs           787M   20K  787M   1% /run/user/1000
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.7](images/bai-1.7.jpg)

---

## Bài 1.8

### Đề bài

Tính toán tổng dung lượng thực tế đang bị chiếm dụng bởi thư mục `data/` và hiển thị kết quả ở định dạng dễ đọc.

### Lệnh thực thi

```bash
du -sh data/
```

### Kết quả

```text
20K     data/
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.8](images/bai-1.8.jpg)

---

## Bài 1.9

### Đề bài

Tạo một liên kết mềm (Symbolic Link) tên là `latest_data` trỏ tới thư mục `data/raw/2026/07/` ngay tại thư mục hiện hành.

### Lệnh thực thi

```bash
ln -s data/raw/2026/07/ latest_data
```

### Kiểm tra kết quả

```bash
ls -l latest_data
```

### Kết quả

```text
lrwxrwxrwx 1 hoaido hoaido 17 Jul 22 16:17 latest_data -> data/raw/2026/07/
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.9](images/bai-1.9.jpg)

---

## Bài 1.10

### Đề bài

Thay đổi thời gian sửa đổi của file `data/raw/2026/info.metadata` thành ngày `15/06/2026` lúc `12:00`.

### Lệnh thực thi

```bash
touch -t 202606151200 data/raw/2026/info.metadata
```

### Kiểm tra kết quả

```bash
ls -l --full-time data/raw/2026/info.metadata
```

### Kết quả

```text
-rw-r--r-- 1 hoaido hoaido 33 2026-06-15 12:00:00.000000000 +0000 data/raw/2026/info.metadata
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 1.10](images/bai-1.10.jpg)

---

# CHỦ ĐỀ 2: PHÂN QUYỀN FILE & QUẢN LÝ SỞ HỮU

## Bài 2.1

### Đề bài

Xem quyền truy cập chi tiết của tệp `info.metadata`.

### Lệnh thực thi

```bash
ls -l data/raw/2026/info.metadata
```

### Kết quả

```text
-rw-r--r-- 1 hoaido hoaido 33 Jun 15 12:00 data/raw/2026/info.metadata
```

### Giải thích

- `-rw-r--r--`: quyền truy cập của file.
- `rw-`: Owner (`hoaido`) có quyền đọc và ghi.
- `r--`: Group (`hoaido`) chỉ có quyền đọc.
- `r--`: Others chỉ có quyền đọc.
- `33`: kích thước file là 33 bytes.
- `Jun 15 12:00`: thời gian sửa đổi của file.
- `data/raw/2026/info.metadata`: đường dẫn của file.

### Ảnh minh chứng

![Ảnh minh chứng Bài 2.1](images/bai-2.1.jpg)

---
## Bài 2.2

### Đề bài

Cấp quyền thực thi (Execute) cho tệp `script.sh` chỉ dành cho người sở hữu tệp (Owner).

### Lệnh thực thi

```bash
touch script.sh
chmod u+x script.sh
```

### Kiểm tra kết quả

```bash
ls -l script.sh
```

### Kết quả

```text
-rwxr--r-- 1 hoaido hoaido 0 Jul 22 16:57 script.sh
```

### Giải thích

- `-rwx`: Owner (`hoaido`) có quyền đọc (`r`), ghi (`w`) và thực thi (`x`).
- `r--`: Group (`hoaido`) chỉ có quyền đọc.
- `r--`: Others chỉ có quyền đọc.
- Quyền `x` đã được thêm cho Owner, đáp ứng yêu cầu của bài.

### Ảnh minh chứng

![Ảnh minh chứng Bài 2.2](images/bai-2.2.jpg)

---
## Bài 2.3

### Đề bài

Thu hồi quyền ghi (Write) của nhóm Khác (Others) đối với tệp `database.config`.

### Lệnh thực thi

```bash
touch database.config
ls -l database.config
chmod o-w database.config
ls -l database.config
```

### Kết quả trước khi thu hồi quyền ghi

```text
-rw-r--r-- 1 hoaido hoaido 0 Jul 22 16:59 database.config
```

### Kết quả sau khi thu hồi quyền ghi

```text
-rw-r--r-- 1 hoaido hoaido 0 Jul 22 16:59 database.config
```

### Giải thích

- `o`: đại diện cho Others.
- `-w`: thu hồi quyền Write.
- Quyền hiện tại của Others là `r--`, không có quyền ghi `w`.
- Lệnh `chmod o-w database.config` được thực hiện thành công.
- Do file ban đầu đã không có quyền ghi cho Others nên sau khi thực hiện lệnh, quyền của file không thay đổi.

### Ảnh minh chứng

![Ảnh minh chứng Bài 2.3](images/bai-2.3.jpg)

---
