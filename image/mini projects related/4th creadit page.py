'''*****IMPORT MODULES****'''
from tkinter import *
from functools import partial
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import re

class Creadit:
        def __init__(self,root,total_price,remaining_price):
                self.root = root
                self.root.state("zoomed")
                self.root.resizable(False,False)

                '''----------------------- shop name and shop no ----------------------------'''
                conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
                cursor = conn.cursor()
                
                cursor.execute("SELECT sh_id FROM shop WHERE sh_status='yes' ")
                self.shop_no = cursor.fetchone()
                #cursor.execute("SELECT sh_name FROM shop WHERE sh_id={} ".format(self.shop_no[0]))
                #self.shop_name = cursor.fetchone()
                
                conn.close()
                
                print("shop no = "+str(self.shop_no[0]))

                '''-------------------------------FRAMES---------------------------------------'''
                cTopFrame = Frame(self.root,bd=10,relief=RIDGE)
                cTopFrame.place(x=0,y=0,width=1530,height=250)

                cMainFrame = Frame(self.root,bd=10, relief=RIDGE)
                cMainFrame.place(x=0,y=250,width=1530,height=755)
                cMainFrame.focus()
                

                treeFrame = Frame(cMainFrame)
                treeFrame.pack(fill=BOTH,expand=True)

                '''================================ top frame label and entries ======================'''
                Label(cTopFrame, text="customer name :",font=('ALGERIAN',14)).place(x=160,y=7)
                self.c_name = Entry(cTopFrame,font=('ALGERIAN',12),bd=5,relief=RIDGE)
                self.c_name.place(x=100,y=40,width=270,height=30)
                
                Label(cTopFrame, text="mobile no :",font=('ALGERIAN',14)).place(x=515,y=7)
                self.c_mono = Entry(cTopFrame,font=('ALGERIAN',14),bd=5,relief=RIDGE)
                self.c_mono.place(x=430,y=40,width=270)
                
                
                Label(cTopFrame, text="total price :",font=('ALGERIAN',14)).place(x=830,y=7)
                self.total_price = Entry(cTopFrame,font=('ALGERIAN',14),bd=5,relief=RIDGE)
                self.total_price.place(x=750,y=40,width=270)
                
                Label(cTopFrame, text="remaining rs :",font=('ALGERIAN',14)).place(x=1140,y=7)
                self.remaining_price = Entry(cTopFrame,font=('ALGERIAN',14),bd=5,relief=RIDGE)
                self.remaining_price.place(x=1080,y=40,width=260)

                Label(cTopFrame, text="selling id :",font=('ALGERIAN',14)).place(x=100,y=100)
                self.selling_id = Entry(cTopFrame,font=('ALGERIAN',14),bd=5,relief=RIDGE)
                self.selling_id.place(x=230,y=95,width=130)

                Button(cTopFrame,text="insert",font=('ALGERIAN',14,'bold')).place(x=850,y=100,width=150,height=50)
                Button(cTopFrame,text="update",font=('ALGERIAN',14,'bold')).place(x=1050,y=100,width=150,height=50)                
                Button(cTopFrame,text="delete",font=('ALGERIAN',14,'bold')).place(x=1250,y=100,width=150,height=50)
                Button(cTopFrame,text="reseat",font=('ALGERIAN',14,'bold')).place(x=1050,y=170,width=150,height=50)                
                Button(cTopFrame,text="clr",font=('ALGERIAN',14,'bold')).place(x=1250,y=170,width=150,height=50)
            
                













if __name__ == '__main__':
        root  = Tk()
        obj = Creadit(root,None,None)
        root.mainloop()
