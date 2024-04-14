import dns.resolver

def query_dns_records(domain, record_type):
    try:
        # Tạo một resolver DNS
        resolver = dns.resolver.Resolver()
        # Thực hiện truy vấn DNS cho các bản ghi cụ thể
        result = resolver.resolve(domain, record_type)
        # In ra tất cả các giá trị bản ghi trả về
        for data in result:
            print(data)
    except dns.resolver.NoAnswer:
        print(f"Không tìm thấy bản ghi {record_type} cho tên miền {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Tên miền {domain} không tồn tại")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

# Ví dụ sử dụng
if __name__ == "__main__":
    domain = "ptit.edu.vn"  # Thay đổi tên miền cần truy vấn
    record_types = ["A", "NS", "MX", "SOA"]  # Các loại bản ghi cần truy vấn

    for record_type in record_types:
        print(f"Truy vấn bản ghi {record_type} cho tên miền {domain}:")
        query_dns_records(domain, record_type)
