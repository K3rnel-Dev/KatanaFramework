import os
import sys
from main_modules.banner import katana_banner, banner_andro, anonymous_banner, anon_style, gun
from time import sleep
from sys import exit
import random

Black = '\033[1;30m'        # Black
Red = '\033[1;31m'          # Red
Green = '\033[1;32m'        # Green
Yellow = '\033[1;33m'       # Yellow
Blue = '\033[1;34m'         # Blue
Purple = '\033[1;35m'       # Purple
Cyan = '\033[1;36m'         # Cyan
White = '\033[1;37m'        # White
NC = '\033[0m'


def clear_console():
    os.system('clear')


def enter_menu():
    print(f'''{Green}
[---]        The Katana Framework Kit (KFT)         [---]
[---]            Created by: K3RNEL-DEV             [---]
                     Version: 0.2 
                  Codename: 'Katana'
[---]      Github: https://github.com/k3rnel-dev    [---]
                Welcome to KATANA-FRAMEWORK
                    Have a good day! :D''')


def select_menu():
    print(f'''{Cyan}
        [*]Select tool:\n
        +---------------------------------------------------+
        |                    [0] EXIT                       |
        +---------------------------------------------------+
        | [1]Katana-Password-Generator    [2]KATANA-PHISHER |
        | [3]MASK-URL                     [4]RevShell Gen   |
        | [5]KATANA-PHP-BACKDOOR          [6]NTLM-WORD STEAL|
        |---------------------------------------------------+
        | [7]WIFI-PENTESTING       [8]METASPLOIT-AUTOPAYLOAD|
        +---------------------------------------------------+
        | [9]Seeker                    [10]NETDISCOVER(ROOT)|
        +---------------------------------------------------+
        |            [11]Scan-Local-Network                 |
        +---------------------------------------------------+
''')


def about():
    print(f'''{Green}
[---]        The KATANA PENETRATION TOOLKIT (KPT)         [---]
[---]        Created by: 404-NOTFOUND (K3rnel-Dev)        [---]
                      Version: 1.0
                    Codename: 'KATAPRETER'
[---]       My Forum: https://www.infosecure.space       [---]
        Welcome to The KATANA PENETRATION TOOLKIT (KPT).
         
     [!] The Penetration toolkit for your ethical hacking [!]

             Visit: https://infosecure.space

''')

def check_root():
    if 'root' in os.popen('whoami').read():
        main()
    else:
        katana_banner()
        print(f'{Red}\t\t\t[-]Script run only root!')


def randomizer_banners(rand_num):
    if rand_num == '1':
        katana_banner()
    elif rand_num == '2':
        banner_andro()
    elif rand_num == '3':
        anonymous_banner()
    elif rand_num == '4':
        gun()

def selector_banner():
    rand_banners = ['1', '2', '3', '4']
    random.shuffle(rand_banners)
    banner = random.choice(rand_banners)
    randomizer_banners(banner)

def check_tool():
    netdiscover_location = os.popen('which netdiscover').read().strip()

    if netdiscover_location == '/usr/sbin/netdiscover' or netdiscover_location == '/usr/bin/netdiscover':
        os.system('netdiscover')
        enter = input('[+]Enter to continue . . .')
        main()

    else:
        print('[!] NetDiscover not installed!')
        install_or_no = input('[+] Install NetDiscover (y/n)?: ')
        if install_or_no.lower() == 'y':
            os.system('sudo apt install netdiscover')
            clear_console()
            banner_andro()
            print('[!] NetDiscover installed successfully!')
            sleep(1)
            main()


def run_seeker(port):
    command = f'cd seeker; python seeker.py -p {port}'
    os.system(command)


def scan_local_network():
    random_patterns = random.randint(1, 5000)
    scan_file = f'scan_0x{random_patterns}.xml'
    choice_interface = input('[+]Enter range-ip your network(default 192.168.0.0/24): ')
    os.system(f'nmap --open -T5 --min-rate=10000 {choice_interface} -oX loot/{scan_file}')
    clear_console()
    selector_banner()
    print(f'[+]Your scan output in loot/{scan_file}')
    input('[*]Enter to continue. . .')
    main()


def main():
    clear_console()
    selector_banner()
    about()
    select_menu()

    while True:

        try:

            variable_tool = input('kat4na> ')
            if variable_tool.isalpha() or variable_tool.isnumeric():

                if variable_tool == '1':
                    clear_console()
                    os.system('cd pwdgen_modules;python3 katana_gen.py')
                    sleep(1.5)
                    main()

                elif variable_tool == '0':
                    print(f'[+]G00d Bye!')
                    sys.exit(0)

                elif variable_tool == '2':
                    clear_console()
                    os.system('cd phish_modules;bash katana_phisher.sh')
                    sleep(1.5)
                    main()

                elif variable_tool == '3':
                    clear_console()
                    os.system('cd maskurl_modules;bash katana_mask.sh')
                    main()

                elif variable_tool == '4':
                    clear_console()
                    os.system('cd revshell_modules;python revshellgen.py')
                    main()

                elif variable_tool == '5':
                    clear_console()
                    os.system('cd kata_phpbackdoor;python builder.py')
                    clear_console()
                    main()

                elif variable_tool == '6':
                    ip = input('[*]Enter ip: ')
                    listener = input('[*]Start listener? y/n: ')

                    if listener.lower() == 'y':
                        os.system(f'cd katana_ntlmsteal;python katana_ntlmword.py {ip} rick.png 1')
                        clear_console()
                        main()

                    elif listener.lower() =='n':
                        os.system(f'cd katana_ntlmsteal; python katana_ntlmword.py {ip} rick.png 0')
                        clear_console()
                        main()

                    else:
                        print('[-]Not correct enter!')

                elif variable_tool == '7':
                    os.system('cd katana_wifi;python katana_vardrive.py')
                    clear_console()
                    main()

                elif variable_tool == '8':
                    os.system('cd katana_msf;python katana_msf.py')
                    clear_console()
                    main()

                elif variable_tool == '9':
                    port = input('[+] Do you want to run on a special port? (default 8080): ')

                    while True:

                        if not port:
                            clear_console()
                            port = '8080'  # Используйте порт 8080 по умолчанию, если строка пуста
                            run_seeker(port)
                            clear_console()
                            main()

                        if port.isnumeric():
                            clear_console()
                            run_seeker(port)
                            clear_console()
                            main()

                        else:
                            port = input('Enter a valid numeric port: ')

                elif variable_tool == '10':
                    check_tool()

                elif variable_tool == '11':
                    scan_local_network()

                elif variable_tool == 'clear':
                    clear_console()
                    main()

            else:
                print('[!]Empty line detected!\n[*]Please enter a valid option!')
        except KeyboardInterrupt:
            print(' DETECTED, Aborting . . .')
            exit(0)
