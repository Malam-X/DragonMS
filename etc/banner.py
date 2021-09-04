import time
from etc.version import __version__
from colorama import Fore

fr       =   Fore.RED
fc       =   Fore.CYAN
fw       =   Fore.WHITE
fg       =   Fore.GREEN
fm       =   Fore.MAGENTA
fy       =   Fore.YELLOW
fb       =   Fore.BLUE

def banner_drgn():
    BANNER = """ 
    %s  _____                              __  __  _____ 
    %s |  __ \                            |  \/  |/ ____|
    %s | |  | |_ __ __ _  __ _  ___  _ __ | \  / | (___  
    %s | |  | | '__/ _` |/ _` |/ _ \| '_ \| |\/| |\___ \ 
    %s | |__| | | | (_| | (_| | (_) | | | | |  | |____) |
    %s |_____/|_|  \__,_|\__, |\___/|_| |_|_|  |_|_____/ 
    %s                    __/ |                          
    %s                   |___/     %sV0.5
    %s
        Programmed By DR4G0N5 / TEMO
        GitHub : https://github.com/malam-x
        YouTube: DR4G Clew
        [NEWS] Added Pentest Tools.
    """%(fm,fb,fm,fb,fm,fb,fm,fb,fc,fm)
    for line in BANNER.split("\n"):
        print(line)
        time.sleep(0.1)
