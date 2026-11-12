import os
import time

# स्क्रीन साफ करने का फंक्शन
def clear():
    os.system('clear')

# टूल का बैनर
def banner():
    print("\033[1;32m" + "="*40)
    print("      MERA PEHLA PYTHON TOOL")
    print("="*40 + "\033[0m")

def main():
    clear()
    banner()
    print("\n[1] Website Status Check Karein")
    print("[2] Apna IP Address Dekhein")
    print("[0] Bahar Niklein (Exit)\n")
    
    choice = input("\033[1;33mOption chunein (1/2/0): \033[0m")
    
    if choice == '1':
        url = input("Website URL dalein (jaise https://google.com): ")
        os.system(f"curl -I {url}")
    elif choice == '2':
        os.system("curl ifconfig.me")
        print()
    elif choice == '0':
        print("Dhanyawad!")
        exit()
    else:
        print("Galat option!")

if __name__ == "__main__":
    main()

