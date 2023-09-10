import os
from main_modules.banner import katana_banner
from time import sleep


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
                     Version: 0.1 
                  Codename: 'Katana'
[---]      Github: https://github.com/k3rnel-dev    [---]
                Welcome to KATANA-FRAMEWORK
                    Have a good day! :D''')


def select_menu():
    print(f'''{Yellow}
        [*]Select tool:\n
        +---------------------------------------------------+
        | [1]Katana-Password-Generator    [2]KATANA-PHISHER |
        | [3] MASK-URL                    [4]RevShell Gen   |
        | [5]KATANA-PHP-BACKDOOR          [6]NTLM-WORD STEAL|
        +---------------------------------------------------+
''')


def main():
    clear_console()
    katana_banner()
    enter_menu()
    select_menu()
    while True:
        try:
            variable_tool = input('kat@na@framework$> ')
            if variable_tool.isalpha() or variable_tool.isnumeric():

                if variable_tool == '1':
                    clear_console()
                    os.system('cd pwdgen_modules;python3 katana_gen.py')
                    sleep(1.5)
                    main()
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
                elif variable_tool == 'clear':
                    clear_console()
                    main()

            else:
                print('Empty line detected!\n[*]Please enter a valid option!')
        except KeyboardInterrupt:
            print(' DETECTED, Aborting . . .')
            break