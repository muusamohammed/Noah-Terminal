import os
import socket
import random
import subprocess

# ڕەنگێن تێرمینالێ
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

def luhn_check(card):
    digits = [int(d) for d in card]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for d in even_digits:
        total += sum(divmod(d * 2, 10))
    return total % 10 == 0

def banner():
    print(f"""
    {CYAN}███╗   ██╗ ██████╗  █████╗ ██╗  ██╗
    ████╗  ██║██╔═══██╗██╔══██╗██║  ██║
    ██╔██╗ ██║██║   ██║███████║███████║
    ██║╚██╗██║██║   ██║██╔══██║██╔══██║
    ██║ ╚████║╚██████╔╝██║  ██║██║  ██║
    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝{RESET}
    {GREEN}>> Professional Cyber Security Terminal <<{RESET}
    {WHITE}Welcome, Musa Mohammed | Version: 2.0{RESET}
    -------------------------------------------
    """)

def main():
    banner()
    while True:
        cmd = input(f"{GREEN}NOAH@{RESET}{WHITE}terminal:~$ {RESET}").split()
        
        if not cmd: continue
        
        # 1. فەرمانا ڤەکرنا Zphisher (بۆ کالی لینوکس)
        if cmd == "zphisher":
            print(f"{CYAN}[*] Launching Zphisher...{RESET}")
            try:
                os.chdir("zphisher")
                subprocess.run(["bash", "zphisher.sh"])
            except FileNotFoundError:
                print(f"{RED}[!] Error: zphisher directory not found.{RESET}")

        # 2. فەرمانا دروستکرنا کارتان (CC Generator)
        elif cmd == "gen":
            # نموونە: gen 515462
            bin_val = cmd if len(cmd) > 1 else "515462"
            print(f"{CYAN}[*] Generating valid cards for BIN: {bin_val}{RESET}")
            for _ in range(5):
                card = bin_val
                while len(card) < 15: card += str(random.randint(0, 9))
                for i in range(10):
                    if luhn_check(card + str(i)):
                        print(f"{GREEN}[+] {card+str(i)}|11|2031|RND{RESET}")
                        break

        # 3. فەرمانا گرتنا ئایپی (IP Lookup)
        elif cmd == "track":
            if len(cmd) > 1:
                ip = cmd
                print(f"{CYAN}[*] Tracking IP: {ip}{RESET}")
                print(f"{WHITE}Link: https://www.ip-tracker.org/lookup.php?ip={ip}{RESET}")
            else:
                print(f"{RED}Usage: track [IP_Address]{RESET}")

        # 4. فەرمانا پاقژکرن (Clear)
        elif cmd == "clear":
            os.system('clear' if os.name == 'posix' else 'cls')
            banner()

        elif cmd == "exit":
            print(f"{RED}Exiting NOAH Terminal...{RESET}")
            break

        else:
            print(f"{RED}Unknown command: {cmd}{RESET}")

if __name__ == "__main__":
    main()