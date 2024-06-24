from tkinter import *
from functools import partial
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import re
import mysql.connector as connector


conn = connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
cursor=conn.cursor()

cursor.execute("SELECT *FROM shop WHERE sh_status='yes' ")
status_ch = cursor.fetchall()


class splash:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x1000")
        self.root.overrideredirect(True) #hide the title bar


        self.root.configure(bg='silver')

        Label(self.root, text="STOCK MANAGEMENT SYSTEM", font=("Algerian",30),fg="red").pack(pady=150)

        Label(self.root, text="Developed By : ", font=("Algerian",18)).place(x=150,y=500)
        Label(self.root, text="TUSHAR MAHAJAN ", font=("Algerian",18)).place(x=350,y=550)

          

        def main_window(*args):
         
             self.root.destroy() #destroy a splash window
             #--------------------------

           
             #--------------------------    
             root2 = Tk()   # create a stock window
             
             if status_ch:   # if no any shop are logged in move on register window
                 print("any shop is register");
                 #go to stock page
                
             else:                      # if any shop are logged in move on stock page
                 print("no any shop are register")
                 #go to 1st main page
                 obj = firstPage()
             #---------------------------
        self.root.after(3000,main_window)

class firstPage:
    def __init__(self):
        print("first page")

if __name__ == '__main__':
    root = Tk()
    obj = splash(root)
    root.mainloop()
