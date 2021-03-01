import os
def install():
    os.system('clear')
    os.system('curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall &&')
    os.system('./msfinstall')
    os.system('chmod 755 msfinstall &&')
