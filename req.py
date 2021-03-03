"""
bs4
instaloader
scapy
twint
pandas
wikipedia
requests
cybercrimetracker
pytube
folium
chatterbot
"""
import os, time
from etc.set import clear
from etc.set import *
def install():
    try:
        print(f'{PULS} Instaling requirements...')
        os.system('pip3 install bs4 instaloader scapy twint pandas wikipedia requests cybercrimetracker pytube folium')
        clear()
        print(f'{SUCES_SYM} Successfully... \n{SUCES_SYM} Running main.py... \n{SUCES_SYM} Please wait...')
        time.sleep(3)
        clear()
        os.system('python3 main.py')
    except KeyboardInterrupt:
        sys.exit(f'{Aborted}')
if __name__ == '__main__':
    install()
