from RegisterMegaAcc import ExtractURL, register
import os, sys
from rich import print
from rich.spinner import Spinner
from rich.live import Live



# print(f'Credentials:\n{email}, {password}')
def login(email, password):
    stream = os.popen(f'mega-login "{email}" "{password}"')
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
    stream = os.popen(f'mega-export -a -f "{filename}"')
    output = stream.read()
    # print(output)
    return(output)

def mega_ls():
    stream = os.popen('mega-ls')
    output = stream.read()
    return(output) 

def clone(_link, _email, _password):
    # os.popen('$env:PATH += ";$env:LOCALAPPDATA\MEGAcmd"')
    # print('Logging in...')
    login(_email, _password)
    # print('Importing file...')
    import_file(_link)
    filename = str(mega_ls()).strip("'")
    # print(filename)
    mirror_link = ExtractURL(export_file(filename))
    # print('Logging out...')
    logout()
    return(mirror_link)
    

if __name__ == "__main__":
    link = sys.argv[1]
    link_stripped = link.strip("'\"")
    with Live(Spinner('dots', text='Registering account...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            email, password = register()
            break
    with Live(Spinner('dots', text='Cloning...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            exported = clone(link, email, password)
            break
    print()
    print(f'[cyan]Cloned link: {exported}[/cyan]')