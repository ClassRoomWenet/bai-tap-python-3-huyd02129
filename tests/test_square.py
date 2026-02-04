# Chương trình tính diện tích hình vuông
import math

def tinh_dien_tich_hinh_vuong():
    try:
        # Nhập độ dài cạnh từ người dùng
        canh = float(input("Nhập độ dài cạnh của hình vuông: "))

        if canh <= 0:
            print("Độ dài cạnh phải là một số dương!")
        else:
            # Công thức: Diện tích = cạnh * cạnh (hoặc cạnh^2)
            dien_tich = canh ** 2
            
            print(f"--- Kết quả ---")
            print(f"Với cạnh là {canh}, diện tích hình vuông là: {dien_tich}")
            
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số thực.")

# Gọi hàm để thực thi
if __name__ == "__main__":
    tinh_dien_tich_hinh_vuong()
