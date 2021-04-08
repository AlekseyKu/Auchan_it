# 08.04.2021 20:17
import tkinter as tk
import tkinter.ttk as ttk
import requests
import os

root = tk.Tk()
root.title('Auchan MG')
root.geometry(f"400x600+100+200")
root['bg'] = 'grey'

# grid configure
root.grid_columnconfigure(0, minsize=200)
root.grid_columnconfigure(1, minsize=200)
root.grid_rowconfigure(0, minsize=50)

# ip device

my_ip = requests.get('https://ramziv.com/ip').text

lbl_ip = tk.Label(root, text="ip device", bg="grey")
lbl_show_ip = tk.Label(root, text=my_ip, bg="grey")

lbl_ip.grid(row=0, column=0, stick="nsew")
lbl_show_ip.grid(row=0, column=1, stick="nsew")


# proxy
# proxy_on = os.system("bat\proxy_on.bat")
# proxy_001_on = os.system("bat\proxy_001_on.bat")
# proxy_delete = os.system("bat\proxy_delete.bat")


def click_btn_proxy(text):
    lbl_proxy_show.config(text="{}".format(text))


btn1_proxy = tk.Button(root, text='proxy.pac', command=lambda: click_btn_proxy("Прописан proxy.pac"))
btn2_proxy = tk.Button(root, text='proxy_001.pac', command=lambda: click_btn_proxy("Прописан proxy_001.pac"))
btn3_proxy = tk.Button(root, text='delete_proxy', command=lambda: click_btn_proxy("AutoConfigURL удален"))

lbl_proxy_show = tk.Label(root)

btn1_proxy.grid(row=2, column=0, stick="we")
btn2_proxy.grid(row=3, column=0, stick="we")
btn3_proxy.grid(row=4, column=0, stick="we")
lbl_proxy_show.grid(row=3, column=1, stick="we")

# acu_proxy ="http://proxy/proxy.pac"

# def acu():
#    os.system('reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings" | findstr "AutoConfigURL"')

# AutoConfigURL    REG_SZ    http://proxy/proxy.pac


root.mainloop()

"""

root =tk.Tk()

def clicked():
    lblclick.configure(text=selected.get())

selected = tk.StringVar()

proxy_lbl = tk.Label(root, text="proxy", font=("calibri light", 20))
btn1 = tk.Button(root, text='proxy.pac', value="Установлен proxy.pac", variable=selected)
btn2 = tk.Button(root, text='proxy_001.pac', value="Установлен proxy_001.pac", variable=selected)
btn3 = tk.Button(root, text='delete_proxy', value="Настройки proxy удалены", variable=selected)
btnclick = tk.Button(root, text="Клик", command=clicked)
lblclick = tk.Label(root, font=("calibri light", 20))

proxy_lbl.grid(column=0, row=2)
btn1.grid(column=0, row=3, sticky=tkinter.W, padx=20)
btn2.grid(column=0, row=4, sticky=tkinter.W, padx=20)
btn3.grid(column=0, row=5, sticky=tkinter.W, padx=20)
btnclick.grid(column=0, row=6, sticky=tkinter.W, padx=20)
lblclick.grid(column=0, row=7)



root.mainloop()
"""
