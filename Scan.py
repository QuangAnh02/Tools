import Scan_nslookup
import Scan_Dig
import Scan_whois
import Scan_whatweb
import Scan_sub
import Recon_ng
import scan_shodan
import webbrowser
import Scan_nmap
import Harvester

def main():
    print("Footprinting and Reconnaissance:")
    print("1. Collect information ")
    print("2. Scan Network")
    print("3. Scan Recon")
    
    choice = input("Nhập số tương ứng với chức năng bạn muốn sử dụng: ")
    
    if choice == "1":
        xu_ly_chucnang1()
    elif choice == "2":
        xu_ly_chucnang2()
    elif choice == "3":
        xu_ly_chucnang3()
    else:
        print("Lựa chọn không hợp lệ.")

def xu_ly_chucnang1():
    print("Thu thập thôn tin:")
    print("1. Specified Domain")
    print("2. Information Public(Search engine)")
    chon= input("Nhập số tương ứng với chức năng: ")
    if chon == "1":
        print("Nhập domain: ", end="")
        domain = input()
        record_types = ["A", "NS", "MX", "SOA"] 
        print("Đang xử lý chức năng 1...")

        print("--------------------------------------------")
        print("Kết quả của NSlookup", domain)
        for record_type in record_types:
            print(f"Truy vấn bản ghi {record_type} cho tên miền {domain}:")
            Scan_nslookup.query_dns_records(domain, record_type)

        print("--------------------------------------------")
        print("Kết quả của Dig")
        s_dig = Scan_Dig.dig(domain)
        print(s_dig)

        print("--------------------------------------------")
        print("Kết quả của whois", domain)
        s_whois = Scan_whois.query_whois(domain)
        print(s_whois)

        print("--------------------------------------------")
        print("Kết quả của whatweb", domain)
        s_whatweb = Scan_whatweb.run_whatweb(domain)
        print(s_whatweb)

        print("--------------------------------------------")
        print("Kết quả của sublister", domain)
        s_sub = Scan_sub.run_sublist3r(domain)
        print(s_sub)
        print("--------------------------------------------")
        print("Kết quả của nmap", domain)
        Scan_nmap.run_nmap(domain)
        print("--------------------------------------------")
    elif chon == "2":
        Harvester.harvester()
    else:
        print("Lựa chọn không hợp lệ.")

    # Xử lý chức năng 1 ở đây

def xu_ly_chucnang2():
    print("Quét mạng và các cổng dịch vụ")
    print("1. Shodan ")
    print("2. Netcraft")
    chon= input("Nhập số tương ứng với chức năng: ")
    if chon == "1":
        scan_shodan.shodan()
    elif chon == "2":
        domain = input("Nhập domain: ")
        webbrowser.open(f"https://sitereport.netcraft.com/?url=http://{domain}")
        webbrowser.open(f"https://searchdns.netcraft.com/?restriction=site+contains&host={domain}&position=limited")
    else:
        print("Lựa chọn không hợp lệ.")
    # Xử lý chức năng 2 ở đây

def xu_ly_chucnang3():
    print("Quét thông tin bằng recon-ng")
    domain = input("Nhập domain: ")
    company = input("Nhập company: ")
    Recon_ng.recon_ng(domain, company)
    # Xử lý chức năng 3 ở đây

if __name__ == "__main__":
    main()
