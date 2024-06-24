from tkinter import *
from functools import partial
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc
import re
import random
import mysql.connector as connector
import datetime

'''
class one:
    def __init__(self,root):
        self.root = root
        self.root.geometry('400x400')
        self.e1=Button(self.root,text="save").pack()
        self.e2=Button(self.root,text="save").pack()

        self.entriList = [self.e1,self.e2]
        
        self.bindall()
        

    def bindall(self):
        for button in self.entriList:
           button.bind('<Buttob-1>',self.save)
        #entries.bind('<Control_L><s>',self.save)

    def save(self,*args):
        print("save")
'''
if __name__ == '__main__':
    root = Tk()
    #obj = one(root)

    e1=Button(root,text="save")
    e1.pack()
    e2=Button(root,text="save")
    e2.pack()

    entriList = [e1,e2]

    def save(*args):
        print("save")

    
    for e in entriList:
       e.bind('<Button-1>',save)

    
    root.mainloop()
