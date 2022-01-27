import os, re, time, sys, http.client
from faker import Faker
from faker.providers import person, internet, misc
from clint import resources
from clint.textui import prompt


resources.init('michaelbarry', 'MegaClone')

if resources.user.read('api-key.txt') == None  or '':
    print('You dont have api key set.')
    print('%s created.' % resources.user.path)
    Mailsac_Api_Key = prompt.query("Your api key >>")
    resources.user.write('api-key.txt', Mailsac_Api_Key)

Mailsac_Api_Key = resources.user.read('api-key.txt').strip()

fake = Faker()

def generateCreds():
    gen_email = fake.lexify(text='????????????@mailsac.com')
    gen_password = fake.password(length=12)
    return(gen_email, gen_password)

def registerAcc(email, password):
    stream = os.popen(f'mega-signup "{email}" "{password}"')
    output = stream.read()
    return(output) 

def GetEmailID(email):
    conn = http.client.HTTPSConnection("mailsac.com")
    headersList = {
    "Mailsac-Key": Mailsac_Api_Key 
    }
    payload = ""
    # print(f'checking email: {email}')
    conn.request("GET", f"/api/addresses/{email}/messages", payload, headersList)
    response = conn.getresponse()
    result = response.read().decode("utf-8")
    extracted_id = str(re.findall('(?<="_id":").[^"]+', result))
    extracted_id = str(extracted_id[2:-2])
    # print(extracted_id)
    if len(extracted_id) == 0:
        time.sleep(5)
        GetEmailID(email)
    
    return(extracted_id)

def GetEmailContentFromID(email, id):
    _id = id

    conn = http.client.HTTPSConnection("mailsac.com")

    headersList = {
    "Mailsac-Key": Mailsac_Api_Key 
    }
    payload = ""
    conn.request("GET", f'/api/text/{email}/{_id}', payload, headersList)
    response = conn.getresponse()
    result = response.read()
    return(result.decode("utf-8"))

def ExtractURL(url):
    return(re.search("(?P<url>https?://[^\s]+)", url).group("url"))

def VerifyAcc(_link, _email, _password):
    stream = os.popen(f'mega-confirm "{_link}" "{_email}" "{_password}"')
    output = stream.read()
    return(output) 

def startcmdserver():
    os.popen('mega-whoami')

def logout():
    os.popen('mega-logout')

def AppendToFile():
    gen_email, gen_password = register()
    readable = f'{gen_email}:{gen_password}\n'
    print(f'{gen_email}:{gen_password}')
    file_object = open('creds.txt', 'a')
    file_object.write(readable)
    file_object.close()

def get_verify_link(_gen_email):
    GetEmailID(_gen_email)
    mail_content = GetEmailContentFromID(_gen_email, GetEmailID(_gen_email))
    try:
        link = (ExtractURL(mail_content))
    except AttributeError:
        get_verify_link(_gen_email)
    return(link)

    
def register():
    startcmdserver()
    logout()
    gen_email, gen_password = generateCreds()
    # print(f"email: {gen_email}, name: {gen_name}, password: {gen_password}.")  
    registerAcc(gen_email, gen_password)
    link = get_verify_link(gen_email)
    # print(verify)
    # print(link)
    VerifyAcc(link, gen_email, gen_password)
    Credentials = [gen_email, gen_password]
    return(Credentials)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        amount = int(sys.argv[1])
        for _ in range(amount):
            AppendToFile()
    else:
        AppendToFile()