from RegisterMegaAcc import ExtractURL, register
import os, sys


link = sys.argv[1]
email, password = register()
print(f'Credentials:\n{email}, {password}')
def login(email, password):
    stream = os.popen(f'mega-login {email} {password}')
    output = stream.read()
    return(output) 

def logout():
    stream = os.popen(f'mega-logout')
    output = stream.read()
    return(output) 

def import_file(link):
    stream = os.popen(f'mega-import {link}')
    output = stream.read()
    return(output)

def export_file(filename):
    stream = os.popen(f'mega-export -a -f {filename}')
    output = stream.read()
    print(output)
    return(output)

def mega_ls():
    stream = os.popen('mega-ls')
    output = stream.read()
    return(output) 

def clone(_link, _email, _password):
    # os.popen('$env:PATH += ";$env:LOCALAPPDATA\MEGAcmd"')
    print('Logging in...')
    login(_email, _password)
    print('Importing file...')
    import_file(_link)
    filename = f"'{mega_ls()}'"
    print(filename)
    mirror_link = ExtractURL(export_file(filename))
    print('Logging out...')
    logout()
    return(mirror_link)
    

if __name__ == "__main__":
    clone(link, email, password)