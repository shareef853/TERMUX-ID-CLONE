import os
import sys
from datetime import datetime

R = '\033[31m'   # Red
G = '\033[32m'   # Green
Y = '\033[33m'   # Yellow
B = '\033[34m'   # Blue
C = '\033[36m'   # Cyan
W = '\033[0m'    # White

def clear_screen():
    os.system('clear')

def show_banner():
    now = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    print(G + "====================================" + W)
    print(B + "       ★ MY ADVANCED TERMUX TOOL ★  " + W)
    print(G + "====================================" + W)
    print(C + " Created by: OWNER SHAREEF LADKA" + W)
    print(C + f" Date & Time: {now}" + W)
    print(G + "====================================\n" + W)

def main_menu():
    clear_screen()
    show_banner()
    print("[1] Phone ki System Info dekhein")
    print("[2] Termux Packages Update karein")
    print("[3] Internet Speed Check karein")
    print("[4] Device ki Storage Status dekhein")
    print("[5] Tool se Bahar Niklein (Exit)")
    print(G + "====================================" + W)
    
    choice = input("\nApna option chunein (1-5): ")
    if choice == '1':
        clear_screen(); show_banner()
        print(C + "--- System Info ---" + W)
        os.system('uname -a')
        input(G + "\nWapas jaane ke liye Enter dabayein..." + W); main_menu()
    elif choice == '2':
        clear_screen(); show_banner()
        print(Y + "Updating system packages...\n" + W)
        os.system('pkg update && pkg upgrade -y')
        input(G + "\nUpdate poora hua! Enter dabayein..." + W); main_menu()
    elif choice == '3':
        clear_screen(); show_banner()
        print(Y + "Internet Speed Check ho rahi hai...\n" + W)
        os.system('speedtest-cli --simple')
        input(G + "\nWapas jaane ke liye Enter dabayein..." + W); main_menu()
    elif choice == '4':
        clear_screen(); show_banner()
        print(C + "--- Phone Storage Status ---" + W)
        os.system('df -h')
        input(G + "\nWapas jaane ke liye Enter dabayein..." + W); main_menu()
    elif choice == '5':
        print(R + "\nTool band ho raha hai. Goodbye! 👋" + W); sys.exit()
    else:
        print(R + "\n[!] Galat option!" + W); input("Enter dabayein..."); main_menu()

if __name__ == "__main__":
    main_menu()
