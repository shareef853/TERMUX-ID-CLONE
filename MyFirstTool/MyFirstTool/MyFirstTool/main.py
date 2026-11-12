import os
import requests

def clear():
    os.system('clear')

def banner():
    print("\033[1;36m" + "="*42)
    print("      SHAREEF853 - PROFILE & NET TOOL")
    print("="*42 + "\033[0m")

def github_info():
    username = input("\nGitHub Username dalein: ")
    url = f"https://github.com{username}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        print(f"\n\033[1;32mNaam:\033[0m {data.get('name')}")
        print(f"\033[1;32mPublic Repos:\033[0m {data.get('public_repos')}")
        print(f"\033[1;32mFollowers:\033[0m {data.get('followers')}")
        print(f"\033[1;32mBio:\033[0m {data.get('bio')}\n")
    else:
        print("\n\033[1;31mUser nahi mila!\033[0m\n")

def main():
    clear()
    banner()
    print("\n1. GitHub Public Profile Check Karein")
    print("2. Apna Public IP Dekhein")
    print("0. Exit\n")
    
    choice = input("Option chunein (1/2/0): ")
    if choice == '1':
        github_info()
    elif choice == '2':
        ip = requests.get("https://ipify.org").text
        print(f"\n\033[1;32mAapka IP:\033[0m {ip}\n")
    elif choice == '0':
        exit()
    else:
        print("Galat option!")

if __name__ == "__main__":
    main()

