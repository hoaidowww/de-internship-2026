## Bài 3.1 [Rất dễ] — Kiểm tra kết nối mạng bằng `ping`

### Đề bài

Kiểm tra kết nối mạng (Network Connectivity) tới máy chủ Database thông qua địa chỉ IP của nó bằng lệnh `ping`.

### Lệnh thực hiện

Sử dụng lệnh sau để kiểm tra kết nối tới địa chỉ IP `127.0.0.1`:

```bash
ping -c 4 127.0.0.1
```

### Kết quả

```text
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.692 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.028 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.023 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.027 ms

--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss
```

### Nhận xét

Kết quả cho thấy đã gửi 4 gói tin và nhận lại đủ 4 gói tin, tỷ lệ mất gói là `0%`. Điều này chứng minh kết nối mạng tới địa chỉ `127.0.0.1` hoạt động bình thường.

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.1](images/bai-3.1.jpg)

### Kết luận

Đã kiểm tra thành công kết nối mạng tới địa chỉ IP `127.0.0.1` bằng lệnh `ping`. Kết nối ổn định và không có gói tin bị mất.

---
## Bài 3.2 [Rất dễ] — Kết nối tới máy chủ Database bằng SSH

### Đề bài

Sử dụng lệnh `ssh` để kết nối tới máy chủ Database thông qua địa chỉ IP của máy chủ.

### Lệnh thực hiện

Sử dụng lệnh sau để kết nối SSH tới máy chủ:

```bash
ssh hoaido@127.0.0.1
```

Sau đó nhập mật khẩu của tài khoản `hoaido`.

### Kết quả

Kết nối SSH thành công và hiển thị thông tin hệ thống Ubuntu:

```text
Welcome to Ubuntu 24.04.4 LTS
```

Sau khi đăng nhập thành công, prompt chuyển thành:

```text
hoaido@DESKTOP-4PVJOAL:~$
```

Điều này cho thấy đã đăng nhập thành công vào máy chủ thông qua SSH.

### Kiểm tra người dùng

```bash
whoami
```

Kết quả:

```text
hoaido
```

### Thoát phiên SSH

```bash
exit
```

### Kết luận

Đã kết nối thành công tới máy chủ Database thông qua SSH bằng địa chỉ IP `127.0.0.1` với tài khoản `hoaido`.

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.2](images/bai-3.2.jpg)

---
## Bài 3.3 [Dễ] — Kết nối SSH bằng Private Key

### Đề bài

Sử dụng SSH kết hợp với tệp khóa riêng tư `private.key` để kết nối tới máy chủ Ubuntu từ xa.

### Lệnh thực hiện

Sử dụng cú pháp SSH với khóa riêng tư:

```bash
ssh -i private.key username@IP
```

Trong đó:

- `-i private.key`: chỉ định tệp khóa riêng tư dùng để xác thực.
- `username`: tên tài khoản trên máy chủ.
- `IP`: địa chỉ IP của máy chủ.

### Kết quả

Kết nối SSH bằng khóa riêng tư thành công khi đăng nhập được vào máy chủ Ubuntu và xuất hiện giao diện dòng lệnh của máy chủ.

### Kết luận

Đã thực hiện kết nối tới máy chủ Ubuntu từ xa bằng SSH sử dụng tệp khóa riêng tư `private.key`.

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.3](images/bai-3.3.jpg)

---

## Bài 3.4 — Đóng gói và nén thư mục logs

### Đề bài

Đóng gói và nén toàn bộ thư mục chứa các file log `logs/` thành một tệp tin lưu trữ nén duy nhất dạng `.tar.gz` bằng lệnh `tar -czf`.

### Bước 1: Tạo thư mục logs

```bash
mkdir -p logs
```

### Bước 2: Tạo file log

```bash
echo "Log line 1" > logs/app.log
echo "Log line 2" >> logs/app.log
echo "Log line 3" >> logs/app.log
```

### Bước 3: Đóng gói và nén thư mục logs

```bash
tar -czf logs.tar.gz logs/
```

### Bước 4: Kiểm tra file nén

```bash
ls -lh logs.tar.gz
```

Kết quả:

```text
-rw-rw-r-- 1 hoaido hoaido 169 Jul 28 05:06 logs.tar.gz
```

### Bước 5: Kiểm tra nội dung file nén

```bash
tar -tzf logs.tar.gz
```

Kết quả:

```text
logs/
logs/app.log
```

### Kết luận

Đã đóng gói và nén thành công toàn bộ thư mục `logs/` thành file `logs.tar.gz` bằng lệnh:

```bash
tar -czf logs.tar.gz logs/
```

File nén chứa thư mục `logs/` và file `logs/app.log`.

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.4](images/bai-3.4.jpg)

---
## Bài 3.5 [Trung bình - Dễ] — Giải nén tệp tin ZIP vào thư mục `/tmp/data/`

### Đề bài

Giải nén tệp tin ZIP dữ liệu `dataset.zip` tải từ Internet vào thư mục `/tmp/data/` bằng lệnh `unzip -d`.

### Bước 1: Tạo thư mục đích

```bash
mkdir -p /tmp/data
```

### Bước 2: Tải tệp dữ liệu ZIP từ Internet

```bash
wget https://github.com/mwaskom/seaborn-data/archive/refs/heads/master.zip -O dataset.zip
```

### Bước 3: Kiểm tra tệp ZIP

```bash
ls -lh dataset.zip
```

Kết quả:

```text
-rw-rw-r-- 1 hoaido hoaido 4.9M Jul 28 05:43 dataset.zip
```

### Bước 4: Giải nén tệp ZIP

```bash
unzip dataset.zip -d /tmp/data/
```

Kết quả cho thấy các tệp dữ liệu đã được giải nén vào:

```text
/tmp/data/seaborn-data-master/
```

### Bước 5: Kiểm tra dữ liệu sau khi giải nén

```bash
find /tmp/data -type f | head
```

Kết quả:

```text
/tmp/data/seaborn-data-master/png/img4.png
/tmp/data/seaborn-data-master/png/img3.png
/tmp/data/seaborn-data-master/png/img1.png
/tmp/data/seaborn-data-master/png/img2.png
/tmp/data/seaborn-data-master/png/img6.png
/tmp/data/seaborn-data-master/png/img5.png
/tmp/data/seaborn-data-master/titanic.csv
/tmp/data/seaborn-data-master/anscombe.csv
/tmp/data/seaborn-data-master/diamonds.csv
/tmp/data/seaborn-data-master/dots.csv
```

### Kết luận

Đã tải thành công tệp `dataset.zip` từ Internet và giải nén toàn bộ dữ liệu vào thư mục `/tmp/data/` bằng lệnh:

```bash
unzip dataset.zip -d /tmp/data/
```

Dữ liệu sau khi giải nén được lưu trong thư mục:

```text
/tmp/data/seaborn-data-master/
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.5](images/bai-3.5.jpg)

---
## Bài 3.6 [Trung bình] — Sao chép file bằng `scp`

### Đề bài

Sao chép một file dữ liệu từ máy local lên thư mục `/home/ubuntu/data/` của máy chủ từ xa bằng lệnh `scp`.

### Bước 1: Tạo thư mục đích

Trong môi trường Ubuntu hiện tại, tài khoản SSH sử dụng là `hoaido`, vì vậy tạo thư mục dữ liệu tại `/home/hoaido/data/`:

```bash
mkdir -p ~/data
```

### Bước 2: Sao chép file bằng `scp`

Sử dụng file `dataset.zip` đã tải ở Bài 3.5 để truyền lên máy chủ:

```bash
scp dataset.zip hoaido@127.0.0.1:/home/hoaido/data/
```

Nhập mật khẩu tài khoản `hoaido` để xác thực.

### Kết quả

File được truyền thành công:

```text
dataset.zip                                                                           100% 4954KB  24.5MB/s   00:00
```

### Bước 3: Kiểm tra file đã được sao chép

```bash
ls -lh ~/data/
```

Kết quả:

```text
total 4.9M
-rw-rw-r-- 1 hoaido hoaido 4.9M Jul 28 07:37 dataset.zip
```

### Kết luận

Đã sao chép thành công file `dataset.zip` từ máy local lên máy chủ thông qua SSH bằng lệnh `scp`.

File được lưu tại:

```text
/home/hoaido/data/dataset.zip
```

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.6](images/bai-3.6.jpg)

---
## Bài 3.7 — Đồng bộ dữ liệu bằng `rsync`

### Đề bài

Sử dụng công cụ `rsync` để đồng bộ hóa dữ liệu thông minh giữa hai thư mục, đảm bảo chỉ sao chép các tệp tin mới được thay đổi để tối ưu hóa băng thông truyền tải mạng bằng lệnh `rsync -avz`.

### Bước 1: Tạo thư mục nguồn và thư mục đích

```bash
mkdir -p sync_source
mkdir -p sync_destination
```

### Bước 2: Tạo file dữ liệu trong thư mục nguồn

```bash
echo "Data line 1" > sync_source/data.txt
```

Kiểm tra nội dung:

```bash
cat sync_source/data.txt
```

Kết quả:

```text
Data line 1
```

### Bước 3: Đồng bộ dữ liệu lần đầu

Sử dụng lệnh:

```bash
rsync -avz sync_source/ sync_destination/
```

Kết quả:

```text
sending incremental file list
./
data.txt

sent 146 bytes  received 38 bytes  368.00 bytes/sec
total size is 12  speedup is 0.07
```

Kiểm tra thư mục đích:

```bash
ls -l sync_destination/
```

Kết quả:

```text
total 4
-rw-rw-r-- 1 hoaido hoaido 12 Jul 28 07:54 data.txt
```

### Bước 4: Thay đổi file dữ liệu nguồn

Thêm một dòng mới vào file:

```bash
echo "Data line 2" >> sync_source/data.txt
```

### Bước 5: Đồng bộ lại dữ liệu

Chạy lại lệnh:

```bash
rsync -avz sync_source/ sync_destination/
```

Kết quả:

```text
sending incremental file list
data.txt

sent 154 bytes  received 35 bytes  378.00 bytes/sec
total size is 24  speedup is 0.13
```

Kết quả cho thấy `rsync` phát hiện file `data.txt` đã thay đổi và thực hiện đồng bộ file này.

### Bước 6: Kiểm tra dữ liệu sau khi đồng bộ

```bash
cat sync_destination/data.txt
```

Kết quả:

```text
Data line 1
Data line 2
```

### Kết luận

Đã sử dụng thành công lệnh:

```bash
rsync -avz sync_source/ sync_destination/
```

để đồng bộ dữ liệu giữa hai thư mục. Sau khi file `data.txt` được thay đổi, chạy lại `rsync` đã cập nhật dữ liệu mới sang thư mục đích.

### Ảnh minh chứng

![Ảnh minh chứng Bài 3.7](images/bai-3.7.jpg)

---
