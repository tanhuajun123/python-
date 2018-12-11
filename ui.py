#!/usr/bin/python
from Tkinter import *
from Tkinter import Message
import Tkinter as tk
root = Tk()
root.geometry('500x300+500+300')
root.title("premaning")
label1 = tk.Label(root, text='heigui:')
label1.grid(row = 0 , column = 0)
label2 = tk.Label(root, text='ououou:')
label2.grid(row = 1, column = 0)

entry1 = tk.Entry(root)
entry1.grid(row = 0, column = 1)
entry2 = tk.Entry(root)
entry2.grid(row = 1, column = 1)

checkbutton = tk.Checkbutton(root, text='phelise on')
checkbutton.grid(row = 2, column = 0, rowspan = 1, columnspan = 2, sticky = tk.W)

#img = tk.PhotoImage(file = "~\image\\1_test.git")
#imageview = tk.Label(root, image = img)
#imageview.grid(row = 4, column = 1, rowspan= 2, columnspan = 2)

button1 = tk.Button(root, text = "chenggong")
button1.grid(row = 5, column = 0)
button2 = tk.Button(root, text = 'shibai')
button2.grid(row = 5, column = 1)

root.mainloop()