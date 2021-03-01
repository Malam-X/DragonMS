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
PULS         = '\u001b[1m[\u001b[32;1m+\u001b[0m\u001b[1m]\u001b[0m'
MINS         = '\u001b[1m[\u001b[31m-\u001b[0m\u001b[1m]\u001b[0m'
ERRORS       = '\u001b[1m[\u001b[31mERROR!\u001b[0m\u001b[1m]\u001b[0m'
private_ip   = socket.gethostbyname(socket.gethostname())
ERROR_SYM    = '[\u001b[31m✘\u001b[0m]'
SUCES_SYM    = '[\u001b[32;1m✔\u001b[0m]'
NFound       = '\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted      = '\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
