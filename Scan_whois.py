import whois

def query_whois(domain_name):
    try:
        # Truy vấn thông tin WHOIS của tên miền
        domain_info = whois.whois(domain_name)
        return domain_info
    except Exception as e:
        print("Error:", e)
        return None

def main():
    # Lấy input từ người dùng
    domain = input("Nhập tên miền bạn muốn truy vấn thông tin WHOIS: ")
    # Gọi hàm query_whois để truy vấn thông tin WHOIS và in kết quả
    result = query_whois(domain)
    if result:
        print("Thông tin WHOIS cho", domain)
        print(result)

if __name__ == "__main__":
    main()
