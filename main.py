
# Dont be a kid!
# this tools only for education
# Made by DR4G0N5

#Module
from etc.banner import banner_drgn
from etc.set import clear
from etc.set import *
from etc.version import __version__
from lib.about import about_me
from lib.list import list_tools
from lib.console import console
from lib.install import install
from lib.tools.Windows import back_windows
from lib.tools.Mac import back_mac
from lib.tools.Linux import back_linux
from lib.tools.Web import back_web
from lib.tools.Script import back_script
from lib.tools.Shell import back_shell
from lib.tools.Android import back_android
from lib.list import *
from tools.net.ddos import tools_list
from tools.net.scrap import mainscrap
from tools.net.scanner import mainscan
from tools.net.scrap import main_scraper
from tools.net.scrap import stat
from tools.net.scrap import youtube_scr
from tools.net.mapper import main_map
import sys,os
import socket
import time
try:
    import bs4
    import instaloader
    import scapy
    import twint
    import pandas
    import requests
    import cybercrimetracker
    import pytube
    import folium
    import wikipedia as wiki
except ImportError:
    clear()
    os.system('python3 req.py')
#==================
NFound   ='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted  ='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
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
        elif (choice == '00') or (choice == '0'):
            os.system('python3 main.py')
        else:
            sys.exit(NFound)
    except KeyboardInterrupt:
        sys.exit(Aborted)

def main_tools():

    try:

        clear()
        banner_drgn()
        pen_tools()
        while True:
            x = input(promt_choice)
            if len(x) == 3:
                sys.exit(NFound)
            elif (x == '1') or (x == '01'):
                tools_list()
            elif (x == '2') or (x == '02'):
                os.system('python3 tools/track/cybercrime.py')
            elif (x == '3') or (x == '03'):
                mainscan()
            elif (x == '4') or (x == '04'):
                clear()
                banner_drgn()
                try:
                    print(f'''
    \u001b[1m[\u001b[32;1m1\u001b[0m\u001b[1m]\u001b[0m Web Scrape ........ {SUCES_SYM}
    \u001b[1m[\u001b[32;1m2\u001b[0m\u001b[1m]\u001b[0m Instagram Scrape .. {SUCES_SYM}
    \u001b[1m[\u001b[32;1m3\u001b[0m\u001b[1m]\u001b[0m Twitter Scrape .... {SUCES_SYM}
    \u001b[1m[\u001b[32;1m4\u001b[0m\u001b[1m]\u001b[0m Wikipedia Scrape .. {SUCES_SYM}
    \u001b[1m[\u001b[32;1m5\u001b[0m\u001b[1m]\u001b[0m Youtube Scrape .... {SUCES_SYM}''')
                    x = input(promt_choice)
                    if x == '1':
                        rl = input(f'{PULS} Url: ')
                        if ('https' not in rl) or ('http' not in rl):
                            sys.exit(f'{ERRORS} INVALID URL.')
                        else:
                            mainscrap(rl)
                    elif x == '2':
                        main_scraper()
                    elif x == '3':
                        try:
                            names = input(f'{PULS} Username: ')
                            if names == '':
                                sys.exit(f'{ERRORS}')
                            stat(names)
                        except:
                            pass
                    elif x == '4':
                        clear()
                        try:
                            print('[+] WIKIPEDIA [+]')
                            xi = input(f'{PULS} Search[Ex: python]: ')
                            try:
                                clear()
                                print(wiki.search(f"{xi}"))
                                xs = input(f'{PULS} Summary: ')
                                try:
                                    clear()
                                    print(wiki.summary(f"{xs}"))
                                    RES = wiki.summary(f"{xs}")
                                    NAME_PATH = 'result/wiki_logs.txt'
                                    with open(f'{NAME_PATH}', 'w') as wrt:
                                        wrt.write(RES)
                                        print(f'{SUCES_SYM} Wikipedia Logs saved at [{NAME_PATH}]')
                                except:
                                    sys.exit(f"{ERRORS}")
                            except ValueError:
                                sys.exit(f'{ERRORS}')
                        except KeyboardInterrupt:
                            sys.exit(Aborted)
                    elif x == '5':
                        youtube_t()
                        try:
                            def youtube_t():
                                urls = input(f'{PULS} Youtube Link: ')
                                if 'https://www.youtube.com/' not in urls:
                                    sys.exit(f'{ERROR_SYM} Try again.')
                                    time.sleep(1)
                                    clear()
                                    banner_drgn()
                                    youtube_t()
                                else:
                                    youtube_scr(urls)
                        except ValueError:
                            sys.exit(f"{ERROS}")
                    else:
                        raise ValueError(NFound)
                except ValueError:
                    sys.exit(NFound)
                except KeyboardInterrupt:
                    sys.exit(Aborted)
            elif (x == '5') or (x == '05'):
                main_map()
            elif (x == '6') or (x == '06'):
                main_tools()
            elif (x == '00') or (x == '0'):
                os.system('python3 main.py')
            else:
                sys.exit(NFound)

    except KeyboardInterrupt:
        sys.exit(Aborted)

def some_tools():

    try:

        clear()
        banner_drgn()
        small_tools()
        x = input(promt_choice)
        if x == '1' or x == '01':
            z = input(f'{PULS} Url : ')
            os.system('python3 tools/small/url_short.py {}'.format(z))
        elif x == '2' or x == '02':
            os.system('python3 tools/small/miner.py')
        elif x == '3' or x == '03':
            pass
        elif len(x) == '3':
            sys.exit(NFound)
        elif (x == '00') or (x == '0'):
            os.system('python3 main.py')
        else:
            sys.exit(NFound)

    except KeyboardInterrupt:
        sys.exit(Aborted)

if __name__ == '__main__':
    try:
        clear()
        banner_drgn()
        print(f'''
\u001b[1m[\u001b[32;1m01\u001b[0m\u001b[1m]\u001b[0m Payload METASPLOIT .... [\u001b[32m✔\u001b[0m]
\u001b[1m[\u001b[32;1m02\u001b[0m\u001b[1m]\u001b[0m Network Tools ......... [\u001b[32m✔\u001b[0m]
\u001b[1m[\u001b[32;1m03\u001b[0m\u001b[1m]\u001b[0m Multi Tools ........... [\u001b[32m✔\u001b[0m]
\u001b[1m[\u001b[36m00\u001b[0m\u001b[1m]\u001b[0m About US \n\n''')
        try:
            x = input(promt_choice)
            if x == '1' or x == '01':
                main()
            elif x == '2' or x == '02':
                main_tools()
            elif x == '3' or x == '03':
                some_tools()
            elif len(x) == '3':
                raise ValueError(NFound)
            elif x == '00':
                clear()
                about_me()
            else:
                sys.exit(NFound)
        except ValueError:
            sys.exit(NFound)
    except KeyboardInterrupt:
        sys.exit(Aborted)
