from clint.textui import prompt, puts, colored
from clint import resources

resources.init('michaelbarry', 'MegaClone')

def checkApiKey():
    Mailsac_Api_Key = resources.user.read('api-key.txt')
    if Mailsac_Api_Key == None or 'api-key':
        Mailsac_Api_Key = prompt.query("Your api key >>")
        print('%s created.' % resources.user.path)
        resources.user.write('api-key.txt', Mailsac_Api_Key)




def Logo():
    print()
    print('$$\      $$\                                $$$$$$\  $$\                               ')
    print('$$$\    $$$ |                              $$  __$$\ $$ |                              ')
    print('$$$$\  $$$$ | $$$$$$\   $$$$$$\   $$$$$$\  $$ /  \__|$$ | $$$$$$\  $$$$$$$\   $$$$$$\  ')
    print('$$\$$\$$ $$ |$$  __$$\ $$  __$$\  \____$$\ $$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ ')
    print('$$ \$$$  $$ |$$$$$$$$ |$$ /  $$ | $$$$$$$ |$$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |')
    print('$$ |\$  /$$ |$$   ____|$$ |  $$ |$$  __$$ |$$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|')
    print('$$ | \_/ $$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ ')
    print('\__|     \__| \_______| \____$$ | \_______| \______/ \__| \______/ \__|  \__| \_______|')
    print('                       $$\   $$ |                                                      ')
    print('                       \$$$$$$  |                                                      ')
    print('                        \______/                                                       ')
    print()


if __name__ == "__main__":
    checkApiKey()