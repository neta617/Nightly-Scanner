import socket
import sys
import os
import time
from colorama import Fore, init

init()

def menu():
    print(Fore.LIGHTBLACK_EX + """
 /$$   /$$ /$$           /$$         /$$     /$$                  /$$$$$$                                                             
| $$$ | $$|__/          | $$        | $$    | $$                 /$$__  $$                                                            
| $$$$| $$ /$$  /$$$$$$ | $$$$$$$  /$$$$$$  | $$ /$$   /$$      | $$  \__/  /$$$$$$$  /$$$$$$  /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$ $$ $$| $$ /$$__  $$| $$__  $$|_  $$_/  | $$| $$  | $$      |  $$$$$$  /$$_____/ |____  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  $$$$| $$| $$  \ $$| $$  \ $$  | $$    | $$| $$  | $$       \____  $$| $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$\  $$$| $$| $$  | $$| $$  | $$  | $$ /$$| $$| $$  | $$       /$$  \ $$| $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/| $$      
| $$ \  $$| $$|  $$$$$$$| $$  | $$  |  $$$$/| $$|  $$$$$$$      |  $$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$  | $$|  $$$$$$$| $$      
|__/  \__/|__/ \____  $$|__/  |__/   \___/  |__/ \____  $$       \______/  \_______/ \_______/|__/  |__/|__/  |__/ \_______/|__/      
               /$$  \ $$                         /$$  | $$                                                                            
              |  $$$$$$/                        |  $$$$$$/                                                                            
               \______/                          \______/                                                                                                                                                                                              
""" )


def scan_port(target, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"{Fore.GREEN}    {port} Port Open. ")
    else:
        print(f"{Fore.RED}    {port} Port Closed. ")

    s.close()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
menu()

target = input(f"{Fore.WHITE}    Hostname: ")

while True:


    port_scan_range = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 1433, 3306, 3389, 8080]

    for port in port_scan_range:    
        scan_port(target, port)

    print(f"{Fore.LIGHTWHITE_EX} Scan Succesfuly completed {Fore.RESET}")

    time.sleep(5)
    clear()
    menu()

    target = input(f"{Fore.WHITE}    Hostname: ")