#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_windows
#===================
from lib.tools.Win.Windows_Meterpreter import windows_meterpreter
from lib.tools.Win.Windows_Reverse import windows_reverse
from lib.tools.Win.Windows_Encoded import windows_encoded
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
def back_windows():
    clear()
    try:
        banner_drgn()
        list_windows()
        choice = input(promt_choice)
        if choice == '1':
            mtr()
        elif choice == '2':
            rvs()
        elif choice == '3':
            ecd()
        else:
            sys.exit(NFound)
    except KeyboardInterrupt:
        sys.exit(Aborted)
class mtr:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            windows_meterpreter(target, port)
class rvs:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == ' ':
            sys.exit(NFound)
        else:
            windows_reverse(target, port)
class ecd:
    def __init__(self):
        windows_encoded()
