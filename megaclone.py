from RegisterMegaAcc import register, CheckApiKey, SetApiKey
from clone import clone
from upload import upload
import dotenv
from rich import print
from rich.prompt import Prompt, IntPrompt
from rich.spinner import Spinner
from rich.live import Live

dotenv.load_dotenv()

def Logo():
    print()
    print('[bold blue]$$\      $$\                                $$$$$$\  $$\                               [/bold blue]')
    print('[bold blue]$$$\    $$$ |                              $$  __$$\ $$ |                              [/bold blue]')
    print('[bold blue]$$$$\  $$$$ | $$$$$$\   $$$$$$\   $$$$$$\  $$ /  \__|$$ | $$$$$$\  $$$$$$$\   $$$$$$\  [/bold blue]')
    print('[bold blue]$$\$$\$$ $$ |$$  __$$\ $$  __$$\  \____$$\ $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ [/bold blue]')
    print('[bold blue]$$ \$$$  $$ |$$$$$$$$ |$$ /  $$ | $$$$$$$ |$$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |[/bold blue]')
    print('[bold blue]$$ |\$  /$$ |$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|[/bold blue]')
    print('[bold blue]$$ | \_/ $$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ [/bold blue]')
    print('[bold blue]\__|     \__| \_______| \____$$ | \_______| \______/ \__| \______/ \__|  \__| \_______|[/bold blue]')
    print('[bold blue]                       $$\   $$ |                                                      [/bold blue]')
    print('[bold blue]                       \$$$$$$  |                                                      [/bold blue]')
    print('[bold blue]                        \______/                                                       [/bold blue]')
    print()
    print('[blue]Version: 0.3.0[/blue]')
    print()

def reg_handler():
    with Live(Spinner('dots', text='Generating Mega account...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            email, password = register()
            break
    print()
    print(f'[cyan]Email: {email}[/cyan]')
    print(f'[cyan]Password: {password}[/cyan]')
    menu()


def clone_handler():
    link  = Prompt.ask("Mega link")
    with Live(Spinner('dots', text='Generating Mega account...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            email, password = register()
            break
    with Live(Spinner('dots', text='Cloning link...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            mirror_link = clone(link, email, password)
            break
    print()
    print(f'[cyan]Mega link: {mirror_link}[/cyan]')
    menu()

def upload_handler():
    link  = (Prompt.ask("Path to file/dir to upload")).strip("'\"")
    with Live(Spinner('dots', text='Registering original account...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            Oemail,Opassword = register()
            break
    with Live(Spinner('dots', text='Registering mirror account...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            Memail, Mpassword = register()
            break
    with Live(Spinner('dots', text='Uploading...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            exported, mirrored = upload(link, Oemail, Opassword, Memail, Mpassword)
            break
    print()
    print(f'[cyan]Original link: {exported}[/cyan]')
    print(f'[cyan]Mirror link: {mirrored}[/cyan]')
    menu()

def menu():
    print()
    print('[blue][1][/blue] Register Mega account')
    print('[blue][2][/blue] Clone link to new account')
    print('[blue][3][/blue] Upload file/dir to new account, then import it to another')
    print('[blue][4][/blue] Change your API key')
    print('[blue][5][/blue] Exit')
    print()

    option = IntPrompt.ask('Choose option')
    
    if option == 1:
        reg_handler()
    elif option == 2:
        clone_handler()
    elif option == 3:
        upload_handler()
    elif option == 4:
        SetApiKey()
        menu()
    elif option == 5:
        exit()

if __name__ == "__main__":
    Logo()
    CheckApiKey()
    print('Your api key is: [bold green]valid[/bold green]')
    menu()


