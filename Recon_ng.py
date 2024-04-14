import subprocess
import webbrowser
# Đường dẫn đến file bash.sh


def recon_ng(domain, company):
    bash_file_path = "./recon.sh"
    # Thực thi file bash từ Python với các đối số domain và company
    subprocess.run([bash_file_path, domain, company])
    webbrowser.open(f"{domain}.html")

def main():
    print("recon_ng")
    domain = input("Nhập domain: ")
    company = input("Nhập company: ")
    recon_ng(domain, company)

if __name__ == "__main__":
    main()

