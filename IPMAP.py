import requests
import webbrowser
import importlib
import subprocess
import sys


def check_module(module_name):
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False


def install_requirement():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("\nRequirements are successfully installed!!!\n")
    except subprocess.CalledProcessError:
        print("\nError installing requirements. Please make sure 'pip' is installed.\n")


required_modules = ["requests", "webbrowser"]
if all(check_module(module) for module in required_modules):
    pass
else:
    install_requirement()


def open_map(coordinate):
    latitude = coordinate.split(",")[0]
    longitude = coordinate.split(",")[1]
    google_maps_url = f"https://www.google.com/maps/search/{latitude},{longitude}"
    webbrowser.open(google_maps_url)


def get_ip_info():
    print("\n")
    target_ip = input("Target IP address: ")
    api_url = f"https://ipinfo.io/{target_ip}/json"
    response = requests.get(api_url)
    # data = response.json()
    # return data
    ip_info = response.json()
    print(f"[+] IP address: {ip_info.get('ip', 'N/A')}")
    print(
        f"[+] Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}"
    )
    print(f"[+] Coordinate: ({ip_info.get('loc', 'N/A')})")
    print(f"[+] ISP: {ip_info.get('org', 'N/A')}")
    print(f"[+] Postal: {ip_info.get('postal', 'N/A')}")
    print("\n")
    openmap = input("Open Map on broswer? (Y/n)")
    if openmap == "":
        open_map(ip_info.get("loc"))
    elif openmap[0].lower() == "n" or openmap[0].lower() == "no":
        pass
    else:
        open_map(ip_info.get("loc"))


def get_my_ip():
    print("\n")
    api_url = f"https://ipinfo.io/json"
    response = requests.get(api_url)
    ip_info = response.json()
    print(f"[+] IP address: {ip_info.get('ip', 'N/A')}")
    print(
        f"[+] Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}"
    )
    print(f"[+] Coordinate: ({ip_info.get('loc', 'N/A')})")
    print(f"[+] ISP: {ip_info.get('org', 'N/A')}")
    print("\n")
    openmap = input("Open Map on broswer? (Y/n)")
    if openmap == "":
        open_map(ip_info.get("loc"))
    elif openmap[0].lower() == "n" or openmap[0].lower() == "no":
        pass
    else:
        open_map(ip_info.get("loc"))


if __name__ == "__main__":
    hello = r"""
_____________________  _________________ 
____  _/__  __ \__   |/  /__    |__  __ \
 __  / __  /_/ /_  /|_/ /__  /| |_  /_/ /
__/ /  _  ____/_  /  / / _  ___ |  ____/ 
/___/  /_/     /_/  /_/  /_/  |_/_/      

</> Create by CX330Blake
</> Version 1.0
-----------------------------------------
    """
    print(hello)
    while True:
        options = int(
            input(
                "Choose an option:\n[1] Find my IP\n[2] Find other's IP\n[3] QUIT\nChoose: "
            )
        )
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
            print("Plz input again")
