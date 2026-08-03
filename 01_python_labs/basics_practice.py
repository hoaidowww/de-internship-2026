# Bài tập 1.1: Đảo ngược thứ tự log

event_logs = ["User Login", "View Product", "Add to Cart", "Checkout"]

event_logs.reverse()

print("Bài 1.1 - Danh sách log sau khi đảo ngược:")
print(event_logs)


# Bài tập 1.2: Lọc giao dịch giá trị cao

transactions = [120.5, 50.0, 300.2, 75.5, 500.0, 20.0]

high_value_transactions = [transaction for transaction in transactions if transaction > 100]

print("Bài 1.2 - Các giao dịch có giá trị lớn hơn 100:")
print(high_value_transactions)

# Bài tập 1.3: Trích xuất tọa độ bản đồ

locations = [
    ("Hanoi", 21.0285, 105.8542),
    ("Saigon", 10.8231, 106.6297)
]

for city, lat, lon in locations:
    print(f"Thành phố: {city} - Kinh độ: {lon} - Vĩ độ: {lat}")
# Bài tập 1.4: Phân tích chỉ số cảm biến

temps = [23.5, 25.0, 19.8, 32.4, 28.1, 15.2, 30.0]

max_temp = temps[0]
min_temp = temps[0]
tong = 0

for temp in temps:
    if temp > max_temp:
        max_temp = temp

    if temp < min_temp:
        min_temp = temp

    tong += temp

avg_temp = tong / len(temps)

print("\nBài 1.4 - Phân tích chỉ số cảm biến")
print(f"Nhiệt độ cao nhất: {max_temp}")
print(f"Nhiệt độ thấp nhất: {min_temp}")
print(f"Nhiệt độ trung bình: {avg_temp:.2f}")
## Bài 1.5: Thuật toán gom nhóm dữ liệu (Batching / Chunking)

### Đề bài

Cho danh sách ID:

```python
ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
```

Yêu cầu:

- Chia danh sách `ids` thành các danh sách con.
- Mỗi danh sách con chứa tối đa **5 phần tử**.

Kết quả mong muốn:

```python
[[1, 2, 3, 4, 5],
 [6, 7, 8, 9, 10],
 [11, 12, 13]]
```

### Code

```python
ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

kich_thuoc_batch = 5
cac_batch = []

for i in range(0, len(ids), kich_thuoc_batch):
    batch = ids[i:i + kich_thuoc_batch]
    cac_batch.append(batch)

print("\nBài 1.5 - Chia dữ liệu thành các batch:")
print(cac_batch)
```

### Giải thích

- Khởi tạo `kich_thuoc_batch = 5` để quy định mỗi batch chứa tối đa 5 phần tử.
- Sử dụng `range(0, len(ids), kich_thuoc_batch)` để duyệt danh sách theo bước nhảy 5.
- Dùng phép cắt danh sách `ids[i:i + kich_thuoc_batch]` để lấy từng nhóm dữ liệu.
- Thêm từng nhóm vào danh sách `cac_batch` bằng `append()`.

### Kết quả

```text
Bài 1.5 - Chia dữ liệu thành các batch:
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]]
```

### Ảnh minh chứng

![Bài 1.5](images/bai-1.5.jpg)
