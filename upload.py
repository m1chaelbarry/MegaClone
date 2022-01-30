from RegisterMegaAcc import CheckApiKey, register, ExtractURL
import clone 
import os, sys
from rich import print
from rich.spinner import Spinner
from rich.live import Live


# upload.py <path>
# output: to file Original, Ousername, Mirror, Musername
# megatools put <path> -u <username> -p <pass>
# megatools copy -l <path> -r /Root -u <username> -p <pass>


# readable = f'{gen_email}:{gen_password}\n'
# print(readable)
# file_object = open('creds.txt', 'a')
# file_object.write(readable)
# file_object.close()

def mega_put(path):
    # print('Uploading file...')
    os.popen(f'mega-put -c --ignore-quota-warn "{path}"')


def log(_filename, Omail, Opass, Olink, Mmail, Mpass, Mlink):
    filename = _filename.strip("\'\n")
    # print('Creating log file')
    file_object = open(f'{filename}.log', 'w')
    file_object.write(f'#### EXPORT LOG ####\nFile: {filename}\nOriginal:\n    {Omail}\n    {Opass}\n    {Olink}\nMirror:\n    {Mmail}\n    {Mpass}\n    {Mlink}')
    file_object.close()

def upload(_path, _O_email, _O_password, _M_email, _M_password):
    clone.logout()
    clone.login(_O_email, _O_password)
    mega_put(_path)
    filename = clone.mega_ls()
    # print(filename)
    exported_link = ExtractURL(clone.export_file(filename))
    clone.logout()
    # time.sleep(10) i think it isnt needed
    mirror_link = ExtractURL(clone.clone(exported_link, _M_email, _M_password))

    log(filename, _O_email, _O_password, exported_link, _M_email, _M_password, mirror_link)
    return(exported_link, mirror_link)

if __name__ == "__main__":
    CheckApiKey()
    print('Your api key is: [bold green]valid[/bold green]')
    path = sys.argv[1]
    path_stripped = path.strip("'\"")
    with Live(Spinner('dots', text='Registering original account...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            Oemail,Opassword = register()
            break
    with Live(Spinner('dots', text='Registering mirror account...', style='blue'), refresh_per_second=20, transient=True):
        while True:
            Memail, Mpassword = register()
            break
    exported, mirrored = upload(path_stripped, Oemail, Opassword, Memail, Mpassword)
    print()
    print(f'[cyan]Original link: {exported}[/cyan]')
    print(f'[cyan]Mirror link: {mirrored}[/cyan]')
