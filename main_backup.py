#import tkinter as tk

from tkinter import *
from tkinter.ttk import Radiobutton
import tkinter


def clicked():
    lblclick.configure(text=selected.get())

import requests
#r = requests.get('https://ip.beget.ru').text
#print(r)

root =Tk()

root.title('Auchan MG')
root.geometry('800x600')

#ip device
lbl_ip = Label(root, text="ip device", font=("calibri light", 20))
lbl_ip.grid(column=0, row=0)
#show_ip = Label(root, r.text)

#proxy
selected = StringVar()

proxy_lbl = Label(root, text="proxy", font=("calibri light", 20))
radbtn1 = Radiobutton(root, text='proxy.pac', value="Установлен proxy.pac", variable=selected)
radbtn2 = Radiobutton(root, text='proxy_001.pac', value="Установлен proxy_001.pac", variable=selected)
radbtn3 = Radiobutton(root, text='delete_proxy', value="Настройки proxy удалены", variable=selected)
btnclick = Button(root, text="Клик", command=clicked)
lblclick = Label(root, font=("calibri light", 20))

proxy_lbl.grid(column=0, row=2)
radbtn1.grid(column=0, row=3, sticky=tkinter.W, padx=20)
radbtn2.grid(column=0, row=4, sticky=tkinter.W, padx=20)
radbtn3.grid(column=0, row=5, sticky=tkinter.W, padx=20)
btnclick.grid(column=0, row=6, sticky=tkinter.W, padx=20)
lblclick.grid(column=0, row=7)



root.mainloop()
