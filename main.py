#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from lib.list import list_tools
from lib.console import console
from lib.install import install
#==================
from lib.tools.Windows import back_windows
from lib.tools.Mac import back_mac
from lib.tools.Linux import back_linux
from lib.tools.Web import back_web
from lib.tools.Script import back_script
from lib.tools.Shell import back_shell
from lib.tools.Android import back_android
#==================
import sys,os,socket,time,datetime
#==================
NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#==================
#Main
def main():
    clear()
    try:
        banner_drgn()
        print('-'*60)
        list_tools()
        choice = input(promt_choice)
        if choice == '1':
            back_windows()
        elif choice == '2':
            back_mac()
        elif choice == '3':
            back_linux()
        elif choice == '4':
            back_web()
        elif choice == '5':
            back_script()
        elif choice == '6':
            back_shell()
        elif choice == '7':
            back_android()
        elif choice == 'install' or choice == 'INSTALL':
            install()
        elif choice == 'start' or choice == 'START':
            console()
    except KeyboardInterrupt:
        sys.exit(Aborted)
if __name__ == '__main__':
    main()
