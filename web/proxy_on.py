import tkinter as tk
import os
import winreg

from IPython.core.magics.config import reg

root = tk.Tk()
root.title('test')
root.geometry(f"400x155")
root['bg'] = 'grey'

# reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v AutoConfigURL /t REG_SZ /d "http://proxy.pac" /f
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Internet Settings", 0,
                     winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key, "AutoConfigURL", 0, winreg.REG_SZ, "http://proxy.pac")
key.Close()


def click(text):
    btn.config(text="{}".format(text))


btn = tk.Button(root, text="привет", width=400, command=click)
btn.grid(row=0, column=0, stick='news')

root.mainloop()
