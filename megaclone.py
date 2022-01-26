from clint.textui import prompt, puts, colored, indent
from clint import resources
from RegisterMegaAcc import register
from clone import clone
from upload import upload

resources.init('michaelbarry', 'MegaClone')

def checkApiKey():
    Mailsac_Api_Key = resources.user.read('api-key.txt').strip()
    if resources.user.read('api-key.txt') == None:
        Mailsac_Api_Key = prompt.query("Your api key >>")
        print('%s created.' % resources.user.path)
        resources.user.write('api-key.txt', Mailsac_Api_Key)


def Logo():
    print()
    puts(colored.red('$$\      $$\                                $$$$$$\  $$\                               '))
    puts(colored.red('$$$\    $$$ |                              $$  __$$\ $$ |                              '))
    puts(colored.red('$$$$\  $$$$ | $$$$$$\   $$$$$$\   $$$$$$\  $$ /  \__|$$ | $$$$$$\  $$$$$$$\   $$$$$$\  '))
    puts(colored.red('$$\$$\$$ $$ |$$  __$$\ $$  __$$\  \____$$\ $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ '))
    puts(colored.red('$$ \$$$  $$ |$$$$$$$$ |$$ /  $$ | $$$$$$$ |$$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |'))
    puts(colored.red('$$ |\$  /$$ |$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|'))
    puts(colored.red('$$ | \_/ $$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ '))
    puts(colored.red('\__|     \__| \_______| \____$$ | \_______| \______/ \__| \______/ \__|  \__| \_______|'))
    puts(colored.red('                       $$\   $$ |                                                      '))
    puts(colored.red('                       \$$$$$$  |                                                      '))
    puts(colored.red('                        \______/                                                       '))
    print()
    puts(colored.red('Version: 0.1.1'))
    print()

def reg_handler():
    with indent(5, quote=colored.cyan(' |')):
        puts(f'Registering Mega Account...')
    email, password = register()
    with indent(5, quote=colored.cyan(' |')):
        puts(colored.magenta(f'Email: {email}'))
        puts(colored.magenta(f'Password: {password}'))
    menu()

def api():
        Mailsac_Api_Key = prompt.query("Your api key >>")
        resources.user.write('api-key.txt', Mailsac_Api_Key)
        menu()

def clone_handler():
    link  = prompt.query("Mega link >>")
    email, password = register()
    mirror_link = clone(link, email, password)
    with indent(5, quote=colored.cyan(' |')):
        puts(colored.magenta(f'Mega link: {mirror_link}'))
    menu()

def upload_handler():
    link  = (prompt.query("Path to file/dir to upload >>")).strip("'\"")
    with indent(5):
        puts(colored.red('Generating original account...'))
    Oemail,Opassword = register()
    with indent(5):
        puts(colored.red('Generating mirror account...'))
    Memail, Mpassword = register()
    exported, mirrored = upload(link, Oemail, Opassword, Memail, Mpassword)
    with indent(5, quote=colored.cyan(' |')):
        puts(colored.magenta(f'Original link: {exported}'))
        puts(colored.magenta(f'Mirror link: {mirrored}'))
    menu()

def menu():
    inst_options = [{'selector':'1','prompt':'Register Mega account','return':'reg'},
            {'selector':'2','prompt':'Clone link to new account','return':'clone'},
            {'selector':'3','prompt':'Upload file/dir to new account, then import it to another','return':'upload'},
            {'selector':'4','prompt':'change your api key','return':'api'},
            {'selector':'q','prompt':'quit','return':'quit'}]
    inst = prompt.options("Choose option:", inst_options)
    
    if inst == 'reg':
        reg_handler()
    elif inst == 'clone':
        clone_handler()
    elif inst == 'upload':
        upload_handler()
    elif inst == 'api':
        api()
    elif inst == 'quit':
        exit()

if __name__ == "__main__":
    Logo()
    checkApiKey()
    menu()


