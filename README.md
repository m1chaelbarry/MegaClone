# MegaClone
you need to 
`pip install -r requirements.txt`

also install `megatools (on Windows I've downloaded it from chocolatey)` AND `megacmd from https://mega.nz/cmd` and add them to PATH

in RegisterMegaAcc.py add your [mailsac API key](https://mailsac.com/docs/api)

RegisterMegaAcc.py makes mega.nz account for you, and adds it to creds.txt file

clone.py takes mega link as an argument and exports it on new account

upload.py uploads file or directory to new "Original" account, then imports it to "Mirror" account and gives you link to share with the world. At the end makes log file with both accounts detail, Original and Mirror link. 

Usage:

`python.exe .\RegisterMegaAcc.py`

`python.exe .\clone.py <mega link>`

`python.exe .\upload.py <path to file or directory>`

![upload.py](https://user-images.githubusercontent.com/69900794/150818982-8d257269-621e-4ac7-a2d8-db4495a3d05b.png)
