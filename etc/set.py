#Module
import sys,os,socket,time,datetime
#Setting
def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')
promt_choice = '\u001b[1m[\u001b[32;1m+\u001b[0m\u001b[1m] Choice\u001b[0m: '
promt_target = '\u001b[1m[\u001b[32;1m+\u001b[0m\u001b[1m] Target\u001b[0m: '
private_ip = socket.gethostbyname(socket.gethostname())
