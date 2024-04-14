import webbrowser

def shodan():
    # Nhập domain và company từ người dùng
    domain = input("Nhập domain: ")
    ip = input("Nhập IP: ")
    
    # Mở trang Shodan với domain và IP được cung cấp
    webbrowser.open(f"https://www.shodan.io/domain/{domain}")
    webbrowser.open(f"https://www.shodan.io/host/{ip}")

if __name__ == "__main__":
    shodan()
