import os
import time

# स्क्रीन साफ करने के लिए
os.system('clear')

# रंगों के कोड
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# टूल का बैनर
print(CYAN + "========================================" + RESET)
print(GREEN + "   --- SHAREEF CUSTOM CLI TOOL v1.0 ---" + RESET)
print(CYAN + "========================================" + RESET)

# की (Key) चेक करने का सिस्टम
key = "SHAREEF-2026"
print(f"{YELLOW}[*] YOUR KEY -> {key}{RESET}")
time.sleep(1)
print(f"{GREEN}[✓] ACCESS GRANTED! Welcome Owner SHAREEF.{RESET}\n")

# यूज़र से इनपुट लेना
repo_name = input("[+] GitHub Repo Name Dalein (e.g. shareef853/TERMUX-ID-CLONE): ")
print(f"\n{CYAN}[*] Connecting to: https://github.com{repo_name}.git{RESET}")
time.sleep(2)
print(f"{GREEN}[✓] Process Complete!{RESET}")

0

