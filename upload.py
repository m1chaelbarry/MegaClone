from RegisterMegaAcc import register, ExtractURL
import clone 
import os, sys, re, time


# upload.py <path>
# output: to file Original, Ousername, Mirror, Musername
# megatools put <path> -u <username> -p <pass>
# megatools copy -l <path> -r /Root -u <username> -p <pass>


# readable = f'{gen_email}:{gen_password}\n'
# print(readable)
# file_object = open('creds.txt', 'a')
# file_object.write(readable)
# file_object.close()

def mega_put(path, email, password):
    stream = os.popen(f'megatools put "{path}" -u "{email}" -p "{password}"')
    output = stream.read()
    print(output)
    return(output) 

def mega_copy(path, email, password):
    stream = os.popen(f'megatools copy -l "{path}" -r /Root -u "{email}" -p "{password}"')
    output = stream.read()
    print(output)
    return(output) 

def log(_filename, Omail, Opass, Olink, Mmail, Mpass, Mlink):
    filename = _filename.strip("\'\n")
    print('Creating log file')
    file_object = open(f'Export_log_{filename}.log', 'w')
    file_object.write(f'#### EXPORT LOG ####\nFile: {filename}\nOriginal:\n    {Omail}\n    {Opass}\n    {Olink}\nMirror:\n    {Mmail}\n    {Mpass}\n    {Mlink}')
    file_object.close()

def upload(_path, _O_email, _O_password, _M_email, _M_password):
    #checks if path is a file
    isFile = os.path.isfile(_path)
    #checks if path is a directory
    isDirectory = os.path.isdir(_path)

    print(f'Is File: {isFile}')
    print(f'Is Directory: {isDirectory}')
    if isFile == True:
        mega_put(_path, _O_email, _O_password)
    elif isDirectory == True:
        mega_copy(_path, _O_email, _O_password)
    clone.logout()
    clone.login(_O_email, _O_password)
    filename = str(clone.mega_ls())
    print(filename)
    exported_link = ExtractURL(clone.export_file(filename))
    clone.logout()
    time.sleep(10)
    mirror_link = ExtractURL(clone.clone(exported_link, _M_email, _M_password))

    log(filename, _O_email, _O_password, exported_link, _M_email, _M_password, mirror_link)
    return(exported_link, mirror_link)

if __name__ == "__main__":
    print('Registering original acc...')
    O_email, O_password = register()
    print(f'Mail: {O_email}, Password: {O_password}')

    print('Registering mirror acc...')
    M_email, M_password = register()
    print(f'Mail: {M_email}, Password: {M_password}')
    
    path = sys.argv[1]
    upload(path, O_email, O_password, M_email, M_password)
