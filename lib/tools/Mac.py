#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Mac
#===================
from lib.tools.Macs.Mac_Reverse import mac_reverse
from lib.tools.Macs.Mac_Bind import mac_bind
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
def back_mac():
    clear()
    try:
        banner_drgn()
        list_Mac()
        choice = input(promt_choice)
        if choice == '1':
            mrv()
        elif choice == '2':
            mbd()
        else:
            sys.exit(NFound)
    except KeyboardInterrupt:
        sys.exit(Aborted)
class mrv:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        port = input('[+] Port[ENTER = DEFAULT]: ')
        if port == '':
            port += '4444'
        if target == '':
            sys.exit(NFound)
        else:
            mac_reverse(target, port)
class mbd:
    def __init__(self):
        print('[+] Private IP: '+private_ip)
        target = input(promt_target)
        if target == '':
            sys.exit(NFound)
        else:
            mac_bind(target)
