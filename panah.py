import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')


def banner():
    os.system('clear')
    print(a+'Shortcut for help you'.center(40))
    print(b+'COPYRIGHT © SW1337 2020, ROBH HACKER TEAM ALL RIGHT RESERVED'.center(40))
    print("".join([i for i in "\n"*3]))


if __name__=='__main__':
    banner()
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/":
            print('\rPlease wait '+i+' ',end="",flush=True)
            sleep(0.1)
    banner()
    print(c+'Silahkan hubungi '+a+'https://instagram.com/hades.dewa'+c+' jika ada yang mau di bicarakan terkait tool ini, bisnis atau sekedar bertanya kabar. :v\nArigatou Mina >_<')

# COPYRIGHT © ROBH HACKER TEAM 2020 ALL RIGHT RESERVED
# SW1337