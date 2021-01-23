#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Web
#===================
from lib.tools.Webs.PHP_Meterpreter import web_PHP_Meterpreter
from lib.tools.Webs.ASP_Meterpreter import web_ASP_Meterpreter
from lib.tools.Webs.JSP_Meterpreter import web_JSP_Meterpreter
from lib.tools.Webs.War import web_war
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
def back_web():
    clear()
    try:
        banner_drgn()
        list_Web()
        choice = input(promt_choice)
        if choice == '1':
            wpm()
        elif choice == '2':
            wam()
        elif choice == '3':
            wjm()
        elif choice == '4':
            ww()
        else:
            sys.exit(NFound)
    except KeyboardInterrupt:
        sys.exit(Aborted)
class wpm:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            web_PHP_Meterpreter(target, port)
class wam:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            web_ASP_Meterpreter(target, port)
class wjm:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            web_JSP_Meterpreter(target, port)
class ww:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            web_war(target, port)
