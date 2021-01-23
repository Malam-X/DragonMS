#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Script
#===================
from lib.tools.Scripts.Python_Reverse import script_python_reverse
from lib.tools.Scripts.Bash_Unix import script_bash_unix
from lib.tools.Scripts.Perl_Unix import script_perl_unix
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
def back_script():
    clear()
    try:
        banner_drgn()
        list_Script()
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
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            script_python_reverse(target, port)
class sbu:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            script_bash_unix(target, port)
class spu:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            script_perl_unix(target, port)
