def square_area():
    try:
        # Nhập dữ liệu từ bàn phím
        side = float(input("Nhập độ dài cạnh hình vuông: "))

        if side <= 0:
            print("Độ dài cạnh phải là một số dương!")
        else:
            # Tính toán diện tích
            area = side ** 2
            print(f"Diện tích hình vuông có cạnh {side} là: {area}")

    except ValueError:
        print("Lỗi: Vui lòng nhập một con số hợp lệ.")

# Thực thi hàm
if __name__ == "__main__":
    square_area()
