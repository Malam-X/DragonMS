import os
G = '\u001b[32m'
End = '\u001b[0m'
def install():
    os.system(G+'''
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
chmod 755 msfinstall && \
./msfinstall\033[0m
'''+End)
