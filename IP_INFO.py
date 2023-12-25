import requests


def get_ip_info():
    print("\n")
    target_ip = input("請輸入目標 IP 地址: ")
    api_url = f"https://ipinfo.io/{target_ip}/json"
    response = requests.get(api_url)
    # data = response.json()
    # return data
    ip_info = response.json()
    print(f"[+] IP 地址: {ip_info.get('ip', 'N/A')}")
    print(
        f"[+] 位置: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}"
    )
    print(f"[+] 座標: ({ip_info.get('loc', 'N/A')})")
    print(f"[+] ISP: {ip_info.get('org', 'N/A')}")
    print(f"[+] 郵遞區號: {ip_info.get('postal', 'N/A')}")
    print("\n")


def get_my_ip():
    print("\n")
    api_url = f"https://ipinfo.io/json"
    response = requests.get(api_url)
    ip_info = response.json()
    print(f"[+] IP 地址: {ip_info.get('ip', 'N/A')}")
    print(
        f"[+] 位置: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}"
    )
    print(f"[+] 座標: ({ip_info.get('loc', 'N/A')})")
    print(f"[+] ISP: {ip_info.get('org', 'N/A')}")
    print("\n")


if __name__ == "__main__":
    hello = r"""
_____________________  _________________ 
____  _/__  __ \__   |/  /__    |__  __ \
 __  / __  /_/ /_  /|_/ /__  /| |_  /_/ /
__/ /  _  ____/_  /  / / _  ___ |  ____/ 
/___/  /_/     /_/  /_/  /_/  |_/_/      
    """
    print(hello)
    while True:
        options = int(input("請輸入選項:\n1. 查詢自身IP\n2. 查詢他人IP\n3. 退出\n選項: "))
        if options == 1:
            get_my_ip()
        elif options == 2:
            get_ip_info()
        elif options == 3:
            quit = r"""
____________  ________________
__  __ \_  / / / /_  _/__  __/
_  / / /  / / /__  / __  /   
/ /_/ // /_/ /__  /_ _  /    
\___\_\\____/ /____/ /_/     
            """
            print(quit)
            break
        else:
            print("請重新輸入")
