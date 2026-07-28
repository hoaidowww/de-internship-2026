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

