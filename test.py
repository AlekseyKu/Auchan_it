from tkinter import *
from tkinter import ttk

root = Tk()
note = ttk.Notebook(root)

ms = ttk.Frame(note)
note.add(ms, text = "Main-Screen")

mn = ttk.Frame(note)
note.add(mn, text = "Manual")

note.grid()

btn = Button(ms, text="1")
btn.grid(row=1, column=1)

root.mainloop()

# Вкладки
"""from tkinter import *
from tkinter import ttk
import os
import glob
from PIL import Image, ImageTk, ImageGrab
from pathlib import Path

class App():
    def __init__(self,master):
        notebook = ttk.Notebook(master)
        notebook.pack()

        #Frames
        left_frame = ttk.Frame(notebook)
        right_frame = ttk.Frame(notebook)
        notebook.add(left_frame, text='Main-Screen')
        notebook.add(right_frame, text='Manual')

        var1 = IntVar()
        var1a = IntVar()

        #Displaying checkboxes and assigning to variables
        self.Checkbox = Checkbutton(right_frame, text="Ingredients present in full (any allergens in bold with allergen warning if necessary)", variable=var1)
        self.Checkbox.grid(column = 1, row = 1, sticky = W)
        self.Checkbox2 = Checkbutton(right_frame, variable = var1a)
        self.Checkbox2.grid(column = 0, row = 1, sticky = W)

       ###FRAME 2###
        #widgets
        self.msg1 = Label(left_frame, text = "Choose here")
        self.msg1.grid(column = 0, row = 0)

root = Tk()
root.minsize(890, 400)
root.title("test only")
app = App(root)
root.mainloop()"""

# вкладки
"""from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('test')

nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')

f1 = Text(root)
f2 = Text(root)
f3 = Text(root)

nb.add(f1, text='page1')
nb.add(f2, text='page2')
nb.add(f3, text='page3')

root.mainloop()"""

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