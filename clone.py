from RegisterMegaAcc import register
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

def main():
    # os.popen('$env:PATH += ";$env:LOCALAPPDATA\MEGAcmd"')
    logout()
    print('Logging in...')
    login(email, password)
    print('Importing file...')
    import_file(link)
    filename = mega_ls()
    print(filename)
    export_file(filename)
    print('Logging out...')
    logout()
    

if __name__ == "__main__":
    main()
