#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Android
#===================
from lib.tools.Androids.Android_Meterpreter import android_meterpreter
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
def back_android():
    clear()
    try:
        banner_drgn()
        list_Android()
        choice = input(promt_choice)
        if choice == '1':
            lmt()
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
            android_meterpreter(target, port)
