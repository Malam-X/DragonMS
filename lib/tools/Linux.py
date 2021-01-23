#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Linux
#===================
from lib.tools.Linuxs.Linux_Meterpreter import linux_meterpreter
from lib.tools.Linuxs.Linux_Bind_Shell import linux_bind_shell
from lib.tools.Linuxs.Linux_Bind_Meterpreter import linux_bind_meterpreter
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
def back_linux():
    clear()
    try:
        banner_drgn()
        list_Linux()
        choice = input(promt_choice)
        if choice == '1':
            lmt()
        elif choice == '2':
            lbmt()
        elif choice == '3':
            lbs()
        else:
            sys.exit(NFound)
    except KeyboardInterrupt:
        sys.exit(Aborted)
class lmt:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            linux_meterpreter(target, port)
class lbmt:
    def __init__(self):
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        linux_bind_meterpreter(port)
class lbs:
    def __init__(self):
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        linux_bind_shell(port)
