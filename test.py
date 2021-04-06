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