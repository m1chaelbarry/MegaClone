import os, re, time, sys, http.client, string, random, dotenv
from rich import print
from rich.prompt import Prompt

dotenv.load_dotenv()
Mailsac_Api_Key = os.getenv('API_KEY')
def SetApiKey():
    Api_Key = Prompt.ask("Enter your api key")
    file = open('.env', 'w+')
    file.close()
    dotenv.set_key('.env', 'API_KEY', Api_Key)
    os.environ['API_KEY'] = Api_Key
    global Mailsac_Api_Key
    Mailsac_Api_Key = Api_Key
    CheckApiKey(Api_Key)

def CheckApiKey(api_key=os.getenv('API_KEY')):
    conn = http.client.HTTPSConnection("mailsac.com")

    headersList = {
    "Mailsac-Key": api_key 
    }

    payload = ""

    conn.request("GET", "/api/me", payload, headersList)
    response = conn.getresponse()
    result = response.read().decode("utf-8")

    if result == "null":
        print('Your api key is: [red]invalid[/red]')
        SetApiKey()


def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generateCreds():
    gen_email = f'{id_generator(10)}@mailsac.com'
    gen_password = id_generator(12)
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
    print(f'[cyan]{gen_email}:{gen_password}[/cyan]')
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
    

    CheckApiKey(Mailsac_Api_Key)
    startcmdserver()
    logout()
    gen_email, gen_password = generateCreds()
    registerAcc(gen_email, gen_password)
    link = get_verify_link(gen_email)
    VerifyAcc(link, gen_email, gen_password)
    Credentials = [gen_email, gen_password]
    return(Credentials)

if __name__ == "__main__":
    if os.getenv('API_KEY') == None:
        print('[bold red]You dont have api key set.[/bold red]')
        SetApiKey()
    else:
        print('Your api key is: [bold green]valid[/bold green]')

    if len(sys.argv) == 2:
        amount = int(sys.argv[1])
        for _ in range(amount):
            AppendToFile()
    else:
        AppendToFile()