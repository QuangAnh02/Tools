import subprocess

def run_nmap(domain):
    command = "sudo nmap -vv -O "+ domain
    try:
        # Sử dụng shell=True để chạy lệnh qua shell của hệ thống
        # Lưu ý: Sử dụng sudo trong subprocess có thể yêu cầu nhập mật khẩu của người dùng
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        # Kiểm tra nếu có lỗi
        if error:
            print("Error:", error.decode("utf-8"))
        else:
            print("Output:", output.decode("utf-8"))
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    domain = input()
    # Gọi hàm để chạy lệnh Nmap
    run_nmap(domain)
