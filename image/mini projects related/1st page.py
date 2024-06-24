'''*****IMPORT MODULES****'''
from tkinter import *
from functools import partial
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import re


conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
cursor=conn.cursor()
'''////////////////////////////////////////'''

class firstPage:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x1000")
        self.root.overrideredirect(True) #hide the title bar

        #___________________________________________________________
        topFrame = LabelFrame(self.root,relief=RIDGE,bd=3 ,text="select your choice")
        topFrame.place(x=5,y=30,width=630,height=100)

        '''midFrame = Frame(self.root,bd=10,relief=RIDGE)
        midFrame.place(x=10, y=100, width=1300,height=750)'''
        #-----------------------------------------------------------
        img  =Image.open(r"image\register.png")
        img = img.resize((160,60),Image.ANTIALIAS)
        self.registerlogo = ImageTk.PhotoImage(img)
        Button(topFrame,image=self.registerlogo,text="register",command=self.registerWindow).place(x=10,y=5,width=160,height=60);

        img1  =Image.open(r"image\login.png")
        img1 = img1.resize((160,60),Image.ANTIALIAS)
        self.loginlogo = ImageTk.PhotoImage(img1)
        Button(topFrame,image=self.loginlogo, text="Login window" ,command=self.loginWindow).place(x=220,y=5,width=160,height=60);

        img2  =Image.open(r"image\exit.png")
        img2 = img2.resize((160,60),Image.ANTIALIAS)
        self.exitlogo = ImageTk.PhotoImage(img2)
        Button(topFrame,image=self.exitlogo ,text="Quit" ,command=self.quit).place(x=430,y=5,width=160,height=60);

        #__________________________________________________________
        '''============== register window variables=============='''
        self.register_window_open=False
        self.login_window_open=False
    
     #____________________________________________________________________________________
    '''============================ main window methods ==============================='''
    def registerWindow(self):
        if self.login_window_open == True:
            self.loginFrame.destroy()
            self.login_window_open=False
            
        if self.register_window_open == False:
            self.registerFrame = Frame(self.root,bd=10,bg="#53eee5",relief=RIDGE)
            self.registerFrame.place(x=20, y=200, width=900,height=500)

            '''bg  =Image.open(r"image\background.png")
            bg = bg.resize((900,500),Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(bg)
            Label(self.registerFrame,image=self.photo).place(x=0,y=0)'''

            '''canvas = Canvas(self.registerFrame, width= 900, height=500)
            canvas.pack()
            bg  =Image.open(r"image\background.png")
            bg = bg.resize((900,500),Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(bg)
            Label(canvas,image=self.photo).place(x=0,y=0)'''

            #canvas.create_text(250,10,text="REGISTER YOUR SHOP",font=('time',18,'bold'))
            reg = Label(self.registerFrame,bg="#53eee5",text="REGISTER YOUR SHOP" , font=("Modern No. 20",22,"bold"))
            reg.place(x=250,y=10)

            Label(self.registerFrame,bg="#53eee5" ,text="YOUR SHOP SH ID : ").place(x=600,y=23)
            ids = Entry(self.registerFrame, bd=5,state='readonly')
            ids.place(x=720,y=23)
            
            Label(self.registerFrame,bg="#53eee5", text="ENTER YOUR SHOP NAME : ").place(x=100,y=80)
            self.e1 = Entry(self.registerFrame, font=('time',14,'bold'),bd=5)
            self.e1.place(x=100,y=110)

            Label(self.registerFrame,bg="#53eee5", text="ENTER Mo.No : ").place(x=500,y=80)
            self.e2 = Entry(self.registerFrame, font=('time',14,'bold'),bd=5)
            self.e2.place(x=500,y=110)
            
            Label(self.registerFrame,bg="#53eee5", text="ENTER PASSWORD : ").place(x=100, y=200)
            self.e3 = Entry(self.registerFrame, font=('time',14,'bold'),bd=5)
            self.e3.place(x=100,y=230)
            
            Label(self.registerFrame,bg="#53eee5", text="CONFIRM PASSWORD : ").place(x=500, y=200)
            self.e4 = Entry(self.registerFrame, font=('time',14,'bold'),bd=5)
            self.e4.place(x=500,y=230)

            self.e1.focus()

            img  =Image.open(r"image\register1.png")
            img = img.resize((290,70),Image.ANTIALIAS)
            self.reglogo = ImageTk.PhotoImage(img)
            Button(self.registerFrame,image=self.reglogo,text="REGISTER NOW",command=self.registerbtn, bd=5).place(x=100,y=300,width=290,height=70)

            img1  =Image.open(r"image\clear1.png")
            img1 = img1.resize((290,70),Image.ANTIALIAS)
            self.clrlogo = ImageTk.PhotoImage(img1)
            Button(self.registerFrame,image=self.clrlogo ,text="CLEAR", bd=5, command=self.clear).place(x=442,y=300,width=290,height=70)

            self.register_window_open=True

        else:
            self.registerFrame.destroy()
            self.register_window_open=False
        

    def loginWindow(self):
        if self.register_window_open == True:
            self.registerFrame.destroy()
            self.register_window_open=False
            
            
        if self.login_window_open == False:
            self.loginFrame = Frame(self.root,bd=10,bg="#53eee5",relief=RIDGE)
            self.loginFrame.place(x=20, y=200, width=900,height=500)

            reg = Label(self.loginFrame,bg="#53eee5", text="LOGIN YOUR SHOP" , font=("Modern No. 20",22,"bold"))
            reg.place(x=280,y=10)

            Label(self.loginFrame,bg="#53eee5", text="ENTER YOUR SHOP NAME : ").place(x=100,y=80)
            self.e1 = Entry(self.loginFrame, font=('time',14,'bold'),bd=5)
            self.e1.place(x=100,y=110)

            Label(self.loginFrame,bg="#53eee5", text="ENTER Mo.No : ").place(x=500,y=80)
            self.e2 = Entry(self.loginFrame, font=('time',14,'bold'),bd=5)
            self.e2.place(x=500,y=110)
            
            Label(self.loginFrame,bg="#53eee5", text="ENTER PASSWORD : ").place(x=100, y=200)
            self.e3 = Entry(self.loginFrame, font=('time',14,'bold'),bd=5)
            self.e3.place(x=100,y=230)

            self.e1.focus()

            img=Image.open(r"image\login.png")
            img = img.resize((160,40),Image.ANTIALIAS)
            self.loglogo = ImageTk.PhotoImage(img)
            Button(self.loginFrame,image=self.loglogo,text="LOGIN",command=self.loginbtn, bd=5).place(x=400,y=230,width=160,height=40)

            img1=Image.open(r"image\clear2.png")
            img1 = img1.resize((160,40),Image.ANTIALIAS)
            self.cllogo = ImageTk.PhotoImage(img1)
            Button(self.loginFrame,image=self.cllogo , text="CLEAR", bd=5, command=self.clearlogin).place(x=600,y=230,width=160,height=40)
            Button(self.loginFrame, text="forgot password",bg="#53eee5",width=25,fg='red',font=('time',12,'bold'),command=self.forgotbtn,relief='flat').place(x=600,y=300)


            self.login_window_open=True

        else:
            self.loginFrame.destroy()
            self.login_window_open=False

    def quit(self):
        ch = messagebox.askquestion("warning","ARE YOU SURE TO CLOSE THIS APPLICATION")

        if ch=='yes':
            self.root.destroy()

     #____________________________________________________________________________________
    '''============================ register window functions ========================='''
    def registerbtn(self):
        if self.e1.get()=="" or self.e2.get()=="" or self.e3.get()=="" or self.e4.get()=="":
            messagebox.showinfo('info','All fields required..')

        else:
            shop_name = self.e1.get()
            mo_no= self.e2.get()
            
            pas = self.e3.get()
            c_pass = self.e4.get()


            if(pas == c_pass):
                cursor = conn.cursor()
                cursor.execute('''select *from shop WHERE sh_name='{}' and mono='{}' '''.format(shop_name,mo_no))
                ch = cursor.fetchall()
            
            
                if ch:    
                    messagebox.showinfo('info',"this shop is already register")

                else:   #if shop is does not register
                    try:
                        cursor = conn.cursor()
                        cursor.execute(''' update shop set sh_status='no' ''')
                        cursor.execute("INSERT INTO SHOP(sh_name,sh_status,mono,pass) VALUES('{}','{}','{}','{}')".format(shop_name,'yes',mo_no,pas))
                        conn.commit()
                                            
                        messagebox.showinfo("info","Register successfully")
                        print("go to stock window..")
                    except Exception:
                        messagebox.showinfo('info','mo.no length must be 10')
            else:
                messagebox.showinfo("info","password and confirm password must be same")
                


    def clear(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e4.delete(0,END)
        self.e1.focus()

     #____________________________________________________________________________________
    '''============================ login window functions ========================='''
    def loginbtn(self):
        if self.e1.get()=="" or self.e2.get()=="" or self.e3.get()=="":
            messagebox.showinfo('info','all fields are required');

        else:
            shop_name = self.e1.get()
            mo_no = self.e2.get()
            pas = self.e3.get()

            print(shop_name,mo_no,pas)
            cursor = conn.cursor()
            cursor.execute('''select *from shop WHERE sh_name='{}' and mono='{}' and pass='{}' '''.format(shop_name,mo_no,pas))
            ch = cursor.fetchall()

            if ch:
                cursor = conn.cursor()
                cursor.execute('''update shop set sh_status='yes' WHERE sh_name='{}' and mono='{}' and pass='{}' '''.format(shop_name,mo_no,pas))
                conn.commit()
            
                print("go to stock page")
                
            else:
                messagebox.showinfo("info","this shop is unavailable");
            
            
    def forgotbtn(self):
        pass
    
    def clearlogin(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.e1.focus()
                
'''////////////////////////////////////////////'''
if __name__ == '__main__':
    root=Tk()
    obj = firstPage(root)
    root.mainloop
