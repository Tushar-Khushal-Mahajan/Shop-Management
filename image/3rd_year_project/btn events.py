from tkinter import *;
from functools import partial
from tkinter import ttk

root = Tk()
root.geometry('400x400+500+100')

def rclick(*args):
    print("right btn clicked")

def lclick(*args):
    print("left btn clicked")

def reclick(*args):
    print("btn release")

def hour(*args):
    print("hour")
    a.set("this is label")
    l1=Label(root,text=a,font=('Time',8))
    l1.pack(after=b1,padx=100)

def hour_out(*args):
    l1=Label(root,text="",font=('Time',8))
    l1.pack(after=b1,padx=100)
    print("hour out ")

def down(*args):
    print('down arrow click')

def enter(*args):
    print('enter click')

def ctrl_shift_s(*args):
    print('ctrl+shift+s')
    
def ctrl_s(*args):
    print('ctrl+s')

def focus(*args):
    e1.configure(background='red')
    e1.configure(foreground='white')


b1 = Button(root, text="click me")
b1.pack()
b1.bind('<Button-1>',lclick) #left btn click
b1.bind('<Button-3>',rclick) #right btn click
b1.bind('<ButtonRelease-1>',reclick)  #btn release
b1.bind('<Enter>',hour)  #btn release
b1.bind('<Leave>',hour_out)  #btn release


e1 = Entry(root)
e1.place(x=140,y=30)

e1.bind('<Down>',down)  #down arrow click
e1.bind('<Return>',enter)   #enter btn click
e1.bind('<Control-Shift-S>',ctrl_shift_s)
e1.bind('<Control_L><s>',ctrl_s)   #ctrl + shift + s 
e1.bind('<FocusIn>',focus) 

x = e1.winfo_rootx()

a = StringVar()

root.mainloop()
