![megaclone.py](https://user-images.githubusercontent.com/69900794/151705198-3599d2f8-319d-45e6-9649-54789b91a606.png)

# ON HOLD! using MegaCMD and steering it through python doesnt work well, and I cant get mega sdk to work so project is on hold.

# MegaClone
you need to 
`pip install -r requirements.txt`

also install `megacmd from https://mega.nz/cmd` and add it to PATH

scripts will ask you for your [mailsac API key](https://mailsac.com/docs/api)

megaclone.py is CLI menu where you can use other scripts interactively.

RegisterMegaAcc.py makes mega.nz account for you, and adds it to creds.txt file

clone.py takes mega link as an argument and exports it on new account

upload.py uploads file or directory to new "Original" account, then imports it to "Mirror" account and gives you link to share with the world. At the end makes log file with both accounts detail, Original and Mirror link. 

#### Also there are exe files in [releases](https://github.com/m1chaelbarry/MegaClone/releases/), there are scripts compiled with PyInstaller

## Usage:

`python.exe .\megaclone.py`

`python.exe .\RegisterMegaAcc.py <opt. number of accounts>`

`python.exe .\clone.py <mega link>`

`python.exe .\upload.py <path to file or directory>`

---

### Contact

Use it if you HAVE to, for issues with script use githubs issues please.

Discord: michaelbarry#6568

Email: mbaryczka@protonmail.com
