import os
os.system("J:\Python_project\Auchan_it\.bat\proxy.bat")


"""from pypac import PACSession, get_pac

pac = get_pac(url='http://your/pac/url/file.pac')
session = PACSession(pac)"""


"""import winreg

def get_proxy_state(self):
    REG_PATH = r'Software\Microsoft\Windows\CurrentVersion\Internet Settings'
    INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_ALL_ACCESS)

    AutoConfigURL, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, 'AutoConfigURL')
        if AutoConfigURL:
            return "auto"
"""


"""
import winreg
import os

def getProxy():
    proxy = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings")
    server, type = winreg.QueryValueEx(proxy, "ProxyServer")
    enabled, type = winreg.QueryValueEx(proxy, "ProxyEnable")
    if enabled:
        return server
    return None

acu_proxy ="http://proxy/proxy.pac"

def acu():
    os.system('reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" | findstr "AutoConfigURL"')

#AutoConfigURL    REG_SZ    http://proxy/proxy.pac"""

"""
from tkinter import *
root = Tk()

def tk_print(new_string):
    text.insert(END, new_string+'\n')

def printName():
    tk_print('My name is Sam')

text = Text(root)
text.grid()
button = Button(root, text='Print my name', command=printName)
button.grid()

root.mainloop()
"""