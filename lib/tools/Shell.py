#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Shell
#===================
from lib.tools.Shells.Windows_Meterpreter import shell_windows_meterpreter
from lib.tools.Shells.Linux_Meterpreter import shell_linux_meterpreter
from lib.tools.Shells.Mac_Reverse import shell_mac_reverse
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
def back_shell():
    clear()
    try:
        banner_drgn()
        list_Shell()
        choice = input(promt_choice)
        if choice == '1':
            spr()
        elif choice == '2':
            sbu()
        elif choice == '3':
            spu()
        else:
            sys.exit(NFound)
    except KeyboardInterrupt:
        sys.exit(Aborted)
class spr:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        lang = input('[+] Language: ')
        if port == '':
            port += '4444'
        if lang == '':
            sys.exit(NFound)
        if target == '':
            sys.exit(NFound)
        else:
            shell_windows_meterpreter(target, port, lang)
class sbu:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        lang = input('[+] Language: ')
        if port == '':
            port += '4444'
        if lang == '':
            sys.exit(NFound)
        if target == '':
            sys.exit(NFound)
        else:
            shell_linux_meterpreter(target, port, lang)
class spu:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        lang = input('[+] Language: ')
        if port == '':
            port += '4444'
        if lang == '':
            sys.exit(NFound)
        if target == '':
            sys.exit(NFound)
        else:
            shell_mac_reverse(target, port, lang)
