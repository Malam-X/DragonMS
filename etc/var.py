import sys
def MAIN_LIST(x=''):
    return '\u001b[1m[\u001b[32;1m%s\u001b[0m\u001b[1m]\u001b[0m'%x
def input_drg(txt):
    try :
        if(sys.version_info[0] < 3):
            return raw_input(txt).strip()
        else :
            sys.stdout.write(txt)
            return input()
    except:
        return False