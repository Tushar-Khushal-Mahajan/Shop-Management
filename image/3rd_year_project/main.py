from tkinter import *

root = Tk()
root.geometry('600x600')

def press(*args):
    print('key press')

i=2
if i == 1:

    f1 = Frame(root,bd=10,relief=RIDGE,width=300,height=250)
    f1.pack()
    f1.focus()
    f1.bind('<Key>',press)

root.mainloop()
