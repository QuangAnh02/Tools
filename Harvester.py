import os

def harvester():
    # Lấy domain từ người dùng
    domain = input("Nhập domain: ")

    # Command để chạy theHarvester với domain được nhập từ người dùng
    command = f"theHarvester -d {domain} -l 200 -b all"

    # Thực thi lệnh
    os.system(command)

if __name__ == "__main__":
    harvester()
