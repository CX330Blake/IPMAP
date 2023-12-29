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


required_modules = ["requests", "webbrowser", "rgbprint"]
if all(check_module(module) for module in required_modules):
    pass
else:
    install_requirement()

from rgbprint import gradient_print, Color, rgbprint
import requests
import webbrowser


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
    ip_info = response.json()
    print(
        rgbprint("[+]", color="green"),
        f"IP address: {ip_info.get('ip', 'N/A')}",
    )
    print(
        rgbprint("[+]", color="green"),
        f"Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}",
    )
    print(
        rgbprint("[+]", color="green"),
        f"Coordinate: ({ip_info.get('loc', 'N/A')})",
    )
    print(
        rgbprint("[+]", color="green"),
        f"ISP: {ip_info.get('org', 'N/A')}",
    )
    print(
        rgbprint("[+]", color="green"),
        f"Postal: {ip_info.get('postal', 'N/A')}",
    )
    print("\n")
    openmap = input("Open Map on browser? (Y/n)")
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
    print(
        rgbprint("[+]", color="green"),
        f"IP address: {ip_info.get('ip', 'N/A')}",
    )
    print(
        rgbprint("[+]", color="green"),
        f"Location: {ip_info.get('city', 'N/A')}, {ip_info.get('region', 'N/A')}, {ip_info.get('country', 'N/A')}",
    )
    print(
        rgbprint("[+]", color="green"),
        f"Coordinate: ({ip_info.get('loc', 'N/A')})",
    )
    print(
        rgbprint("[+]", color="green"),
        f"ISP: {ip_info.get('org', 'N/A')}",
    )
    print("\n")
    openmap = input("Open Map on browser? (Y/n)")
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
    gradient_print(hello, start_color=0x4BBEE3, end_color=Color.medium_violet_red)
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
            gradient_print(
                quit, start_color=0x4BBEE3, end_color=Color.medium_violet_red
            )
            break
        else:
            rgbprint("Plz input again", color="red")
