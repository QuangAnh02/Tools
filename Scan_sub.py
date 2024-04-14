import subprocess

def run_sublist3r(domain):
    try:
        # Gọi lệnh Sublist3r từ terminal
        result = subprocess.check_output(['sublist3r', '-d', domain], stderr=subprocess.STDOUT)
        # Trả về kết quả
        return result.decode('utf-8')
    except subprocess.CalledProcessError as e:
        # Xử lý lỗi nếu có
        return "Error: " + e.output.decode('utf-8')

def main():
    # Lấy input từ người dùng
    domain = input("Nhập tên miền bạn muốn tìm kiếm các subdomains: ")
    # Gọi hàm run_sublist3r để tìm kiếm subdomains và in kết quả
    output = run_sublist3r(domain)
    print(output)

if __name__ == "__main__":
    main()
