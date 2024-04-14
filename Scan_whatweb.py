import subprocess

def run_whatweb(url):
    try:
        # Gọi lệnh WhatWeb thông qua subprocess
        #result = subprocess.run(['whatweb', '-v', '-a', '3', '--color=never', url], capture_output=True, text=True, timeout=30)
        result = subprocess.run(['whatweb', url], capture_output=True, text=True, timeout=30)

        # Kiểm tra kết quả trả về
        if result.returncode == 0:
            # Nếu thành công, trả về output dưới dạng văn bản
            return result.stdout
        else:
            # Nếu không thành công, in ra lỗi
            print("Error:", result.stderr)
            return None
    except subprocess.TimeoutExpired:
        print("Error: Timeout expired.")
        return None
    except Exception as e:
        print("Error:", e)
        return None

def main():
    # Lấy input từ người dùng
    url = input("Nhập URL bạn muốn chạy WhatWeb: ")
    # Gọi hàm run_whatweb để chạy WhatWeb và in kết quả
    result = run_whatweb(url)
    if result:
        print("Kết quả WhatWeb cho", url)
        print(result)

if __name__ == "__main__":
    main()
