![megaclone](https://user-images.githubusercontent.com/69900794/150953918-be777d95-a346-4f32-9321-e2c7051ba57b.png)


# MegaClone
you need to 
`pip install -r requirements.txt`

also install `megatools (on Windows I've downloaded it from chocolatey)` AND `megacmd from https://mega.nz/cmd` and add them to PATH

scripts will ask you for your [mailsac API key](https://mailsac.com/docs/api)

megaclone.py is CLI menu where you can use other scripts interactively.

RegisterMegaAcc.py makes mega.nz account for you, and adds it to creds.txt file

clone.py takes mega link as an argument and exports it on new account

upload.py uploads file or directory to new "Original" account, then imports it to "Mirror" account and gives you link to share with the world. At the end makes log file with both accounts detail, Original and Mirror link. 

Also there is exe file in [releases](https://github.com/m1chaelbarry/MegaClone/releases/), its megaclone.py compiled with PyyInstaller

## Usage:

`python.exe .\megaclone.py`

`python.exe .\RegisterMegaAcc.py <opt. number of accounts>`

`python.exe .\clone.py <mega link>`

`python.exe .\upload.py <path to file or directory>`

![upload.py](https://user-images.githubusercontent.com/69900794/150818982-8d257269-621e-4ac7-a2d8-db4495a3d05b.png)

## TODO

stop using megatools

### Contact
Discord: michaelbarry#6568
