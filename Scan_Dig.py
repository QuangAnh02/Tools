import subprocess

def dig(domain):
    try:
        # Gọi lệnh dig từ Python và lấy kết quả bằng subprocess
        result = subprocess.run(['dig', domain], capture_output=True, text=True)
        # Trả về kết quả định dạng text
        return result.stdout
    except Exception as e:
        return str(e)
    
def main():
    # Lấy input từ người dùng
    domain = input("Nhập tên miền bạn muốn truy vấn: ")
    # Sử dụng hàm dig để truy vấn tên miền và in kết quả
    print(dig(domain))

if __name__ == "__main__":
    main()
