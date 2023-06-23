import time
from pathlib import Path
from datetime import datetime

import pyfiglet
from colorama import init, Fore

init()

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Fore.RESET

def log_scanner():
    bf = 0
    flag = 0
    bf_Attck = 1
    filesize = 0
    # p = Path("/var/log")
    while bf_Attck:
        with open("/var/log/auth.log","r") as f:
            lines = f.readlines()
            if len(lines) != filesize:
                for l in range(filesize, len(lines)):
                    # print(l)
                    #print(lines[l])
                    p =lines[l].split()
                    if ("Failed" in p and "password" in p and "for" in p) and flag:
                        bf += 1
        if (bf >=5) and flag:
            print(f"bf =  {bf}")
            print(f"{RED}You are under Brute Force Attack!{RESET}")
            exit(0)
        else:
            flag = 1
        time.sleep(5)
        print(f"bf attempts = {bf}")
        filesize = len(lines)


if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("Mitigation Tool")
    print(ascii_banner)
    print("-" * 50)
    print(f"{GREEN}The Mitigation Tool has been start{RESET}")
    log_scanner()
