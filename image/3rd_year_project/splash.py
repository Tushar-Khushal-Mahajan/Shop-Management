'''*****IMPORT MODULES****'''
from tkinter import *
from functools import partial
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import pyodbc
import re


'''***CREATE A CONNECTION****'''
conn = pyodbc.connect(
                        "Driver={SQL server};"
                        "Server=DESKTOP-SCH7GJR\SQLEXPRESS;"
                        "Database=project;"
                        "Trusted_Connection=yes;"

                      )
cursor = conn.cursor()
cursor.execute("SELECT shop_status FROM shop WHERE shop_status='yes' ")
shop_name = cursor.fetchone()
#conn.close()

'''========================================================================'''

'''CHECK WHETHER ANY SHOP LOGGED IN OR NOT'''
if shop_name == None:
    ch = 'no'

else:
    ch = 'yes'
'''========================================================================'''

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
             
             if ch == 'no':   # if no any shop are logged in move on register window
                 #obj = login(root2)
                 obj = Register(root2)
             else:                      # if any shop are logged in move on stock page
                 obj = stock(root2)  #<-- this is main window
                 #obj = order(root2)
                 #obj = (root2)
                 #obj = SoldClass(root2)
             #---------------------------
        self.root.after(1,main_window)

#______________________________________________________________________________________________________________
'''============================================= REGISTER CLASS ==========================================='''

class Register:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Register window")

        main_frame = Frame(self.root,bd=10, relief=RIDGE, width=850, height=500)
        main_frame.place(x=300, y=130)

        reg = Label(main_frame, text="REGISTER YOUR SHOP" , font=("Modern No. 20",22,"bold"))
        reg.place(x=250,y=10)
        
        Label(main_frame, text="ENTER YOUR SHOP NAME : ").place(x=100,y=80)
        e1 = Entry(main_frame, font=('time',14,'bold'),bd=5)
        e1.place(x=100,y=110)

        Label(main_frame, text="ENTER ANY UNIQUE ID : ").place(x=500,y=80)
        e2 = Entry(main_frame, font=('time',14,'bold'),bd=5)
        e2.place(x=500,y=110)
        
        Label(main_frame, text="ENTER PASSWORD : ").place(x=100, y=200)
        e3 = Entry(main_frame, font=('time',14,'bold'),bd=5)
        e3.place(x=100,y=230)
        
        Label(main_frame, text="CONFIRM PASSWORD : ").place(x=500, y=200)
        e4 = Entry(main_frame, font=('time',14,'bold'),bd=5)
        e4.place(x=500,y=230)

        self.register = partial(self.register,e1,e2,e3,e4)
        Button(main_frame, text="REGISTER NOW",width=25,command=self.register, bd=5).place(x=100,y=300)

        self.cancel = partial(self.cancel,e1,e2,e3,e4)
        Button(main_frame, text="CLEARE",width=25, bd=5, command=self.cancel).place(x=350,y=300)
        Button(main_frame, text="CLOSE",width=25, bd=5,command=self.close).place(x=600,y=300)

        Button(main_frame, text="Already Have An Shop Account",font=('time',12,'bold'),fg='red',relief="flat", command=self.go_login).place(x=550,y=400)

    def register(self,e1,e2,e3,e4):
        if e1.get() == '' or e2.get()=='' or e3.get=='' or e4.get()=='':
            messagebox.showerror("ERROR","ALL FIELDS ARE REQUIRED")

        else:
            shop_name = e1.get()
            id= e2.get()
            
            pas= e3.get()
            c_pass= e4.get()

            if(pas == c_pass):
                cursor = conn.cursor()
                cursor.execute('''SELECT *FROM shop WHERE sh_id=? and shop_name=?''',(id,shop_name))
                ch = cursor.fetchone()
                #conn.close()

                
                if ch != None:    
                    messagebox.showinfo('info',"this shop is already register")

                else:   #if shop is does not register
                    
                    cursor = conn.cursor()
                    cursor.execute("UPDATE shop SET shop_status='no' WHERE shop_status='yes'")
                    cursor.execute("INSERT INTO SHOP(sh_id,shop_name,shop_pass,shop_status) VALUES(?,?,?,?)",(id,shop_name,c_pass,'yes'))
                    conn.commit()
                                        
                    messagebox.showinfo("info","Register successfully")

                    
                    self.root.withdraw()
                    self.stock_w = Toplevel()
                    obj = stock(self.stock_w)
                    
            else:
                messagebox.showerror("password error","password and confirm password must be same")
    
    
    def cancel(self,e1,e2,e3,e4):
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)

            
    def close(self):
        self.root.destroy()
        
    def go_login(self):
        self.root.withdraw()
        self.login_w = Toplevel()
        obj = login(self.login_w)

        
        '''root = Tk()
        obj = login(root)'''

#______________________________________________________________________________________________________________
'''============================================= LOGIN CLASS ==========================================='''

class login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("500x500+500+180")
      
        self.root.resizable('false', 'false')
        Label(self.root, text="LOGIN WINDOW", font=('time',18,'bold')).pack()
        Label(self.root, text="________________________________", font=('time',18,'bold')).pack()
        
        Label(self.root, text="SHOP NAME : ",font=('time',10,'bold')).place(x=10,y=80)
        self.shname = Entry(self.root, font=('time',14,'bold'),bd=5,width=40)
        self.shname.place(x=20,y=110)

        Label(self.root, text="PASSWORD : ",font=('time',10,'bold')).place(x=10,y=150)
        self.shpass = Entry(self.root, font=('time',14,'bold'),bd=5,show='*',width=30)
        self.shpass.place(x=20,y=180)

        #self.loginbtn = partial(self.loginbtn,shname,shpass)
        fgpass=Button(self.root, text="LOGIN",width=30,bd=5,command=self.loginbtn)
        fgpass.place(x=20,y=240)

        #self.clear = partial(self.clear,shname,shpass)
        fgpass=Button(self.root, text="CLEAR",width=30,bd=5,command=self.clear).place(x=260,y=240)
        fgpass=Button(self.root, text="FORGOT PASSWORD",fg="red",relief="flat").place(x=360,y=300)
        Button(self.root, text="CLOSE WINDOW",fg="green",relief="flat",command=self.root.destroy).place(x=360,y=340)

    def loginbtn(self):
        if self.shpass.get() == "" or self.shname.get()=="":
            messagebox.showerror("error", "all fields are required")

        else:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM shop WHERE SHOP_NAME=? AND shop_pass=?''',(self.shname.get(),self.shpass.get()))
            check = cursor.fetchone()
         
            if check:
                #messagebox.showinfo("info", "THIS SHOP IS AVAILABLE")
                '''conn = pyodbc.connect(
                                        "Driver={SQL server};"
                                        "Server=DESKTOP-SCH7GJR\SQLEXPRESS;"
                                        "Database=project;"
                                        "Trusted_Connection=yes;"

                                )'''
                cursor = conn.cursor()
                cursor.execute('''UPDATE shop set shop_status=? WHERE sh_id=?''',('yes',check[0]))
                conn.commit()

                self.root.withdraw()
                self.stock_w = Toplevel()
                obj = stock(self.stock_w)

                '''self.root.destroy()
                root = Tk()
                obj = stock(root)'''

            else:
                messagebox.showerror("error", "THIS SHOP IS UNAVAILABLE")


        '''self.root.destroy()
        root = Tk()
        obj = stock(root)'''

    def clear(self):
        self.shname.delete(0,END)
        self.shpass.delete(0,END)


#______________________________________________________________________________________________________________
'''============================================ STOCK CLASS =============================================='''

class stock:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')
        self.root.resizable(False,False)

        '''
            =======================================( VARIABLES )===========================================
        '''
        cursor = conn.cursor()
        cursor.execute("SELECT sh_id FROM shop WHERE shop_status='yes' ")
        self.shop_no = cursor.fetchone()
        #------------------- STOCK FRAME VARIABLES -----------
        self.p_id = IntVar()
        self.p_name = StringVar()
        self.sqty = IntVar()
        self.sp_price = IntVar()
        self.ss_price = IntVar()
            
        #------------------- ADD VARIABLES -------------------
        self.ap_name = StringVar()

        
        '''
            ===============================================================================================
        '''
        
        cursor = conn.cursor()
        cursor.execute("SELECT shop_name FROM shop WHERE shop_status='yes' ")
        shop_name = cursor.fetchone()
    
        sh_name = shop_name[0]
        '''
            ===============================================================================================
        '''

        img1  =Image.open("bg.png")
        img1 = img1.resize((1600,850),Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(img1)
        
        self.mainmid_frame = Label(self.root,image=self.photo).place(x=0,y=0)
        
        topframe=Frame(self.root,bg="lightyellow",bd=10,relief=RIDGE)
        topframe.place(x=0,y=0,width=1533,height=100)
        
        

        btnframe = Frame(self.root,bg="red", bd=10,relief=RIDGE)
        btnframe.place(x=0,y=100,width=150,height=445)

        img  =Image.open(r"image\TE_logo.png")
        img = img.resize((80,80),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img)
        Button(topframe,text="click",command=self.logo ,image=self.photoimg1,borderwidth=0).place(x=0,y=0)
        
        Label(topframe, text=sh_name,bg="lightyellow",fg="red",font=("Algerian",30)).pack(side=TOP , fill=X,padx=100,pady=25)

        Button(btnframe, text="HOME",command=self.home,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=3,height=50,width=125)
        Button(btnframe, text="STOCK",command=self.stock,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=55,height=50,width=125)
        Button(btnframe, text="SOLD", command=self.sold,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=108,height=50,width=125)
        Button(btnframe, text="CREDIT", command=self.creadit,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=160,height=50,width=125)
        Button(btnframe, text="ORDER GOODS",command=self.order,font=('Sitka Small Semibold',11,'bold'),bd=5,relief=GROOVE).place(x=2,y=213,height=50,width=125)
        Button(btnframe,text="ACCOUNTING", command=self.accounting,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=266, height=50,width=125)
        Button(btnframe, text="NOTES",command=self.notes,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=319,height=50,width=125)
        Button(btnframe,text="LOG OUT", command=self.log_out,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=372, height=50,width=125)

        #---------------------------------methods--------------------------------------

        self.add_pro=0
        self.stock=0
        self.searchCount=0
        
    '''*********COMMON FUNCTIONS*********'''

    def refresh(self):
        self.clr_treeview()

    def home(self):
        if (self.add_pro) == 1:
            self.addf.destroy()
            self.add_pro=0

        elif (self.stock) == 1:
            self.stock_frame.destroy()
            self.stock=0

    def clr_treeview(self):
        self.order_tree.delete(*self.order_tree.get_children())  #clere treeview

       
        sh_id = self.shop_no
        cursor.execute("SELECT p_id,p_name,p_qty,p_price,s_price FROM products where sh_id=? order by p_qty asc",(sh_id[0]))
        data = cursor.fetchall()

        self.order_tree.tag_configure('lowstock',background="DarkOrange", font=('Times New Roman',12,'bold'))
        self.order_tree.tag_configure('midstock',background="yellow", font=('Times New Roman',12,'bold'))
        self.order_tree.tag_configure('highstock',background="lime", font=('Times New Roman',12,'bold'))
        
        count = 0
        for i in data:
            if i[2]<=10:
                self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]),tags=('lowstock',))
                count += 1
            if i[2]<=17 and i[2]>=11:
                self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]),tags='midstock',)
                count += 1
            if i[2]>=18:
                self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]),tags='highstock',)
                count += 1
                
    '''********STOCK FRAME FUNCTIONS********'''       
        
    def stock(self):
        if (self.add_pro) == 1:
            self.addf.destroy()
            self.add_pro=0

        if(self.stock == 0):
            self.stock_frame = Frame(self.root,bg='white',bd=10,relief=RIDGE)
            self.stock_frame.place(x=250,y=100,width=920,height=500) 
            

            Label(self.stock_frame, text="STOCK AVAILABLE ON SHOP",font=("Sitka Small Semibold",15,"bold")).pack(side=TOP,fill=X)

            self.o_frame = Frame(self.stock_frame,bd=10,relief=RIDGE)
            self.o_frame.place(x=0,y=30,width=900,height=250)

            self.stock_btm_frame = Frame(self.stock_frame,bg='red',bd=10,relief=RIDGE)
            self.stock_btm_frame.place(x=0,y=280,width=900,height=200)

            stock_left_frame = Frame(self.stock_btm_frame, bd=10,relief=RIDGE)
            stock_left_frame.place(x=1,y=0,width=660,height=180)
            #stock_left_frame.focus()
        
            stock_right_frame = Frame(self.stock_btm_frame, bd=10,relief=RIDGE)
            stock_right_frame.place(x=665,y=0,width=220,height=180)
            #-------------------------------------------------------------------------------------------
            sc_x = ttk.Scrollbar(self.o_frame, orient=HORIZONTAL)
            sc_x.pack(side=BOTTOM, fill=X)

            sc_y = ttk.Scrollbar(self.o_frame, orient=VERTICAL)
            sc_y.pack(side=RIGHT, fill=Y)
            
            self.order_tree = ttk.Treeview(self.o_frame,xscrollcommand=sc_x,yscrollcommand=sc_y)

            self.order_tree['columns'] = ("p_id","p_name","p_qty","p_price","sold_price")

            sc_x.config(command=self.order_tree.xview)
            sc_y.config(command=self.order_tree.yview)

            self.order_tree.column("#0", stretch=NO,width=0)
            self.order_tree.column("p_id",anchor=CENTER, minwidth=100,width=100)
            self.order_tree.column("p_name",minwidth=250,anchor=CENTER)
            self.order_tree.column("p_qty",minwidth=130,anchor=CENTER)
            self.order_tree.column("p_price",minwidth=130,anchor=CENTER)
            self.order_tree.column("sold_price",minwidth=130,anchor=CENTER)
            self.order_tree.column("#0", stretch=NO,width=0)
            self.order_tree.bind("<ButtonRelease-1>",self.stock_cursor)

            self.order_tree.heading("#0", text="")
            self.order_tree.heading("p_id", text="PRODUCT ID", anchor=CENTER)
            self.order_tree.heading("p_name", text="PRODUCT NAME", anchor=CENTER)
            self.order_tree.heading("p_qty", text="PRODUCT QTY", anchor=CENTER)
            self.order_tree.heading("p_price", text="PRODUCT PRICE", anchor=CENTER)
            self.order_tree.heading("sold_price", text="SELLING PRICE", anchor=CENTER)
            self.order_tree.heading("#0", text="")
           
            self.clr_treeview()

            self.order_tree.pack(fill=BOTH)
            #--------------------------------------------------------------------------------------------
            Label(stock_left_frame, text="P NAME", font=('time',12,'bold')).place(x=65,y=3)
            self.product = Entry(stock_left_frame,textvariable=self.p_name, font=('time',12,'bold'),bd=5)
            self.product.place(x=10,y=40,width=180)
            
            Label(stock_left_frame, text="QTY", font=('time',12,'bold')).place(x=210,y=3)
            self.qty = Entry(stock_left_frame,textvariable=self.sqty, font=('time',12,'bold'),bd=5)
            self.qty.place(x=210,y=40,width=120)
            
            Label(stock_left_frame, text="P PRICE", font=('time',12,'bold')).place(x=350,y=3)
            self.p_price = Entry(stock_left_frame,textvariable=self.sp_price, font=('time',12,'bold'),bd=5)
            self.p_price.place(x=350,y=40,width=140)

            Label(stock_left_frame, text="S PRICE", font=('time',12,'bold')).place(x=520,y=3)
            self.s_price = Entry(stock_left_frame,textvariable=self.ss_price, font=('time',12,'bold'),bd=5)
            self.s_price.place(x=500,y=40,width=140)
            self.stock_clere()

            img  =Image.open(r"image\insert.png")
            img = img.resize((140,30),Image.ANTIALIAS)
            self.insertlogo = ImageTk.PhotoImage(img)
            insert_btn = Button(stock_left_frame, text="INSERT",image = self.insertlogo,borderwidth=0,command=self.stock_insert)
            insert_btn.place(x=10, y=90,width=130)
            #stock_left_frame.bind('<Key>',self.stock_insert)
            
            img  =Image.open(r"image\update.png")
            img = img.resize((140,30),Image.ANTIALIAS)
            self.updatelogo = ImageTk.PhotoImage(img)
            Button(stock_left_frame, text="UPDATE",image=self.updatelogo,borderwidth=0, command=self.stock_update).place(x=170, y=90,width=130)

            img  =Image.open(r"image\delete.png")
            img = img.resize((140,30),Image.ANTIALIAS)
            self.deletelogo = ImageTk.PhotoImage(img)
            Button(stock_left_frame, text="DELETE",borderwidth=0,image=self.deletelogo ,command=self.stock_delete).place(x=330, y=90,width=130)

            img  =Image.open(r"image\clear.png")
            img = img.resize((140,30),Image.ANTIALIAS)
            self.clrlogo = ImageTk.PhotoImage(img)
            Button(stock_left_frame, text="CLERE",image=self.clrlogo, borderwidth=0 ,command=self.stock_clere).place(x=480, y=90,width=150)

            img  =Image.open(r"image\reseat.png")
            img = img.resize((140,30),Image.ANTIALIAS)
            self.reseatlogo = ImageTk.PhotoImage(img)
            Button(stock_left_frame, text="REFRESH",image= self.reseatlogo,borderwidth=0,command=self.refresh).place(x=490, y=130,width=130)


            img  =Image.open(r"image\search.png")
            img = img.resize((140,30),Image.ANTIALIAS)
            self.searchlogo = ImageTk.PhotoImage(img)
            Button(stock_left_frame, text="SEARCH",image= self.searchlogo,borderwidth=0,command=self.search).place(x=330, y=130,width=130)
   

            img  =Image.open(r"image\high stock.png")
            img = img.resize((175,70),Image.ANTIALIAS)
            self.hstocklogo = ImageTk.PhotoImage(img)
            Button(stock_right_frame, text="HIGH STOCK",image=self.hstocklogo,borderwidth=0,command=self.highStockFun).place(x=15, y=8, width=175,height=70)

            img  =Image.open(r"image\btn.png")
            img = img.resize((175,70),Image.ANTIALIAS)
            self.lstocklogo = ImageTk.PhotoImage(img)
            Button(stock_right_frame, text="LOW STOCK",image=self.lstocklogo,borderwidth=0,command=self.lowStockFun).place(x=15, y=85, width=175,height=70)
            
            self.stock=1
                

    def stock_insert(self):
        if self.product.get()=='' or self.qty.get()=='' or self.p_price.get()=='' or self.s_price.get()=='':
            messagebox.showerror("error", "all fields are required")

        else:
            cursor = conn.cursor()
            #cursor.execute("SELECT sh_id FROM shop WHERE shop_status ='yes'")
            #sh_id = cursor.fetchone()  # select shop id where status =  yes
            #sh_id = sh_id[0]
            sh_id=self.shop_no[0]
            
            cursor.execute("select *from products where p_name =?",(self.p_name.get()))
            avl = cursor.fetchone()

            if avl:
                messagebox.showerror('error', "product already available")

            else:
                cursor.execute("""INSERT INTO products(sh_id, p_name, p_qty, p_price, s_price) VALUES(?,?,?,?,?)""",
                            (sh_id,self.p_name.get(),self.qty.get(),self.p_price.get(), self.s_price.get() ))
                conn.commit()
                messagebox.showinfo('INFO','insert successfully')
                self.clr_treeview()
                
   

    def stock_update(self):
        if self.product.get()=='' or self.qty.get()=='' or self.p_price.get()=='' or self.s_price.get()=='':
            messagebox.showerror("error", "all fields are required")

        else:
            cursor = conn.cursor()
            cursor.execute("UPDATE products set p_name=?, p_qty=?, p_price=?, s_price=? where p_id =? ",(
                        self.p_name.get(),self.qty.get(),self.p_price.get(), self.s_price.get(),self.p_id
                ))            
            conn.commit();
            messagebox.showinfo('INFO','update successfully')
            self.clr_treeview()
            
        
    def stock_delete(self):
            if self.product.get()=='' or self.qty.get()=='' or self.p_price.get()=='' or self.s_price.get()=='':
                messagebox.showerror("error", "all fields are required")

            else:
                self.ch = messagebox.askquestion("warning","ARE YOU SURE TO DELETE THIS RECORD...")
                if self.ch == "yes":
                    cursor = conn.cursor()
                    cursor.execute("DELETE products WHERE p_id=?",(self.p_id))
                    conn.commit()
                    self.clr_treeview()
                    
                else:
                    #nothing
                    pass

    def itemSearch(self,):
        if self.option.get() == "Search By" or self.searchEntry.get() == "":
            messagebox.showerror("Error","all fields are required");
            

        else:
            check_selection = self.str_out.get()
            entry_value = '%'+self.searchEntry.get()+'%'
            
            
            if check_selection == 'By ID':   #if the user intrested to search a product by its id 
                cursor = conn.cursor()
                cursor.execute("""SELECT *FROM products WHERE p_id like ?  AND sh_id =? """,(entry_value,self.shop_no[0]))
                data = cursor.fetchall()

                
                
            else:     #if the user intrested to search a product by its id
                
                cursor = conn.cursor()
                cursor.execute("""SELECT *FROM products WHERE p_name like ? AND sh_id=? ORDER BY p_qty asc """,(entry_value,self.shop_no[0]))
                data = cursor.fetchall()
                
                
            if data:      #check the product is available or not                
                
                self.order_tree.delete(*self.order_tree.get_children())  #clere treeview

                self.order_tree.tag_configure('lowstock',background="DarkOrange", font=('Times New Roman',12,'bold'))
                self.order_tree.tag_configure('midstock',background="yellow", font=('Times New Roman',12,'bold'))
                self.order_tree.tag_configure('highstock',background="lime", font=('Times New Roman',12,'bold'))
                
                count = 0
                for i in data:
                    if i[3]<=10:
                        self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[1],i[2],i[3],i[4],i[5]),tags=('lowstock',))
                        count += 1
                    if i[3]<=17 and i[3]>=11:
                        self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[1],i[2],i[3],i[4],i[5]),tags='midstock',)
                        count += 1
                    if i[3]>=18:
                        self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[1],i[2],i[3],i[4],i[5]),tags='highstock',)
                        count += 1

        

            else:           #if the product is not available in our database
                messagebox.showinfo('INFO','This Product Is Unavailable')
                self.order_tree.delete(*self.order_tree.get_children())  #clere treeview
                
                



    def search_OptionMenu_Click(self,*args):  #this func. returns the value on option menu
        self.str_out = StringVar()
        self.str_out.set(self.option.get())
        
        self.e1_str = StringVar()
        self.searchEntry = Entry(self.stock_search_frame,bd=2,textvariable=self.e1_str,font=('time',10,'bold'),relief=RIDGE)
        self.searchEntry.place(x=3,y=40,height=30,width=190)

        img  =Image.open(r"image\round search.png")
        img = img.resize((40,30),Image.ANTIALIAS)
        self.rsearchlogo = ImageTk.PhotoImage(img)
        Button(self.stock_search_frame, text="SEARCH",image= self.rsearchlogo,borderwidth=0,command=self.itemSearch).place(x=200, y=40,width=40)

        '''==================================AUTO FILL LISTBOX CODE================================='''
        
        cursor = conn.cursor()
        cursor.execute("""SELECT p_name FROM products WHERE sh_id=?""",(self.shop_no[0]))
        d = cursor.fetchall()
        self.my_searchList=[r for r , in d]

        l1= Listbox(self.stock_search_frame,height=6,relief='flat',bg='SystemButtonFace',highlightcolor='SystemButtonFace')
        l1.place(x=3,y=70,height=80,width=190)

        def my_update(my_widget):
            my_w = my_widget.widget
            index=int(my_w.curselection()[0])
            value=my_w.get(index)
            self.e1_str.set(value)
            l1.delete(0,END)

        def my_down(my_widget):
            l1.focus()
            l1.selection_set(0)

        def get_data(*args):
            search_str = self.searchEntry.get() #user enter string

            if search_str != "":
                l1.delete(0,END)
                for element in self.my_searchList:
                    if(re.search(search_str, element, re.IGNORECASE)):
                        l1.insert(END, element)
            else:
                l1.delete(0,END)

        self.searchEntry.bind('<Down>',my_down)
        l1.bind('<Right>',my_update)
        l1.bind('<Return>',my_update)  #enter btn
        self.e1_str.trace('w',get_data)
    
        

    def search(self):
        if self.searchCount == 0:
            self.stock_search_frame = Frame(self.root, bd=10,relief=RIDGE)
            self.stock_search_frame.place(x=600,y=600,width=300,height=180)
            self.searchCount=1

            options = [
                "By ID",
                "By Name"
            ];
            self.option = StringVar()
            self.option.set("Search By")

            dropMenu = OptionMenu(self.stock_search_frame, self.option, *options)
            dropMenu.place(x=3,y=3)

            '''self.e1_str = StringVar()
            self.searchEntry = Entry(self.stock_search_frame,bd=2,textvariable=self.e1_str,font=('time',10,'bold'),relief=RIDGE)
            self.searchEntry.place(x=3,y=40,height=30,width=190)'''

            '''img  =Image.open(r"image\round search.png")
            img = img.resize((40,30),Image.ANTIALIAS)
            self.rsearchlogo = ImageTk.PhotoImage(img)'''

            self.option.trace('w',self.search_OptionMenu_Click)
            
            #Button(self.stock_search_frame, text="SEARCH",image= self.rsearchlogo,borderwidth=0,command=self.itemSearch).place(x=200, y=40,width=40)

        else:
            self.stock_search_frame.destroy()
            self.searchCount=0
    



    def stock_clere(self):
        self.product.delete(0,END)
        self.qty.delete(0,END)
        self.p_price.delete(0 ,END)
        self.s_price.delete(0,END)
        


    def creadit(self):   # move to creadit class
        print('creadit page')
        

        
    def order(self):  #move to order class
        print("order page")
        
        

    def logo(self):   # move to logo class
        self.root.destroy()
        root = Tk()
        obj = LogoClass(root)

           
    def aget_cursor(self,event=""):
        cursor_row = self.my_tree.focus()
        content=self.my_tree.item(cursor_row)
        row = content['values']
        self.ap_name.set(row[0])

    def stock_cursor(self, event=""):   
        cursor_row = self.order_tree.focus()
        content = self.order_tree.item(cursor_row)
        row = content['values']
        self.p_id = row[0]
        self.p_name.set(row[1])
        self.ss_price.set(row[4])
        self.sp_price.set(row[3])
        self.sqty.set(row[2])


    def highStockFun(self):
        cursor = conn.cursor()
        #cursor.execute("SELECT sh_id FROM shop where shop_status='yes'")
        #sh_id = cursor.fetchone()
        #sh_id = sh_id[0]
        sh_id = self.shop_no[0]
        
        cursor.execute("SELECT p_id,p_name,p_qty,p_price,s_price FROM products where sh_id=? and p_qty>=? order by p_qty desc",(sh_id,18))
        data = cursor.fetchall()
        self.order_tree.delete(*self.order_tree.get_children())  #clere treeview

        self.order_tree.tag_configure('highstock',background="lime", font=('Times New Roman',12,'bold'))

        count = 0
        for i in data:
            self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]),tags=('highstock',))
            count += 1
            
         
    def lowStockFun(self):
        cursor = conn.cursor()
        #cursor.execute("SELECT sh_id FROM shop where shop_status='yes'")
        #sh_id = cursor.fetchone()
        #sh_id = sh_id[0]
        sh_id = self.shop_no[0]
        cursor.execute("SELECT p_id,p_name,p_qty,p_price,s_price FROM products where sh_id=? and p_qty<=? order by p_qty asc",(sh_id,10))
        data = cursor.fetchall()
        self.order_tree.delete(*self.order_tree.get_children())  #clere treeview

        self.order_tree.tag_configure('lowstock',background="DarkOrange", font=('Times New Roman',12,'bold'))

        count = 0
        for i in data:
            self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]),tags=('lowstock',))
            count += 1
      



    '''*********SIDE FRAME FUNCTIONS*********'''

    def log_out(self):
        self.c=messagebox.askquestion("warning","ARE YOU SURE TO LOG OUT YOUR SHOP AC.")
        if self.c == "yes":
            messagebox.showinfo("info","LOG OUT SUCCESSFULLY")

            conn = pyodbc.connect(
                                        "Driver={SQL server};"
                                        "Server=DESKTOP-SCH7GJR\SQLEXPRESS;"
                                        "Database=project;"
                                        "Trusted_Connection=yes;"

                                  )
            cursor = conn.cursor()
            cursor.execute("UPDATE shop set shop_status='no' WHERE shop_status='yes'")
            conn.commit()
            #conn.close()

            self.root.withdraw()
            self.Register_w = Toplevel()
            obj = Register(self.Register_w)
            '''
            self.root.destroy()
            root2 =  Tk()
            obj = Register(root2)'''
            

        else:
            #nothing
            pass

    def sold(self):
        print("sold window")
        self.root.withdraw()
        self.SoldClass_w = Toplevel()
        obj = SoldClass(self.SoldClass_w)
    

    def accounting(self):
        print("accounting")

    def notes(self):
        print("notes")
#______________________________________________________________________________________________________________
'''================================================ LOGO PAGE =============================================='''        
class LogoClass:
    def __init__(self,root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("logo page")
#______________________________________________________________________________________________________________
'''================================================ ORDER PAGE =============================================='''

#______________________________________________________________________________________________________________
'''================================================ CREADIT PAGE =============================================='''

#______________________________________________________________________________________________________________
'''================================================ SOLD CLASS =============================================='''
class SoldClass:
    def __init__(self,root):
        self.root = root
        self.root.state("zoomed")
        '''----------------------- shop name and shop no ----------------------------'''
        cursor = conn.cursor()
        cursor.execute("SELECT sh_id FROM shop WHERE shop_status='yes' ")
        self.shop_no = cursor.fetchone()
        cursor.execute("SELECT shop_name FROM shop WHERE sh_id=? ",(self.shop_no[0]))
        self.shop_name = cursor.fetchone()
        cursor.execute("INSERT INTO sell_id VALUES(?)",('abc'))
        cursor.commit()
        cursor.execute("SELECT s_id FROM sell_id order by s_id desc")
        self.sellId = cursor.fetchone()
        
        print("shop no = "+str(self.shop_no[0]))

        '''-------------------------------FRAMES---------------------------------------'''
        sTopFrame = Frame(self.root,bd=10,relief=RIDGE)
        sTopFrame.place(x=0,y=0,width=1530,height=80)

        sMainFrame = Frame(self.root,bd=10, relief=RIDGE,bg="#53eee5")
        sMainFrame.place(x=0,y=80,width=1530,height=755)
        sMainFrame.focus()
        

        treeFrame = Frame(sMainFrame, bd=8,relief=RIDGE)
        treeFrame.place(x=18,y=220,width=1000,height=400)
        '''-------------------------------FRAMES---------------------------------------'''

        sTopFramefont=('Times New Roman',22,'bold')
        img  =Image.open(r"image\back.png")
        img  = img.resize((125,50),Image.ANTIALIAS)
        self.backlogo = ImageTk.PhotoImage(img)
        home_btn = Button(sTopFrame,image=self.backlogo,borderwidth=0,command=self.back).place(x=2,y=6)

        
        #----------------- Variables -----------------
        self.getDate = StringVar()
        self.getDay= StringVar()

        
        self.productName = StringVar()
        self.sellingId = StringVar()
        self.qty = IntVar()
        self.price = IntVar()
        shopname = StringVar()
        self.total_price = IntVar()
        self.cashPaid = IntVar()
        self.changeRs = IntVar()
        
        shopname = "tushant electronicks"
        self.total_price.set(0)

        shname_len = len(shopname)
        self.qty.set(1)
        #----------------------------set date and day------------
        cursor.execute('select convert(varchar,getdate(),3)')
        date = cursor.fetchall()
        self.getDate = date[0][0]

        cursor.execute('select datename(dw,getdate())')
        day = cursor.fetchall()
        self.getDay = day[0][0]
        

        
        #-------------------------------------------------------------------------------
        Label(sTopFrame,text=self.getDate,font=('Algerian',20,'bold'),fg="#FF26AE").place(x=1100,y=3)
        Label(sTopFrame, text = self.getDay,font=('Algerian',20,'bold'),fg="#09C446").place(x=1300,y=25)
        


        Label(sMainFrame, text="Product Name",bg="#53eee5", font=('Algerian0',15,'bold')).place(x=20,y=10)
        self.p_name = Entry(sMainFrame,textvariable=self.productName, font=('Algerian0',15,'bold'),bd=8,relief=RIDGE)
        self.p_name.place(x=20,y=45,width=250)
        self.p_name.focus()
        
        Label(sMainFrame, text="QTY", font=('Algerian0',15,'bold'),bg="#53eee5").place(x=330,y=10)
        self.p_qty = Entry(sMainFrame,textvariable=self.qty, font=('Algerian0',15,'bold'),bd=8,relief=RIDGE)
        self.p_qty.place(x=330,y=45,width=180)

        Label(sMainFrame, text="PRICE", font=('Algerian0',15,'bold'),bg="#53eee5").place(x=200,y=105)
        self.p_price = Entry(sMainFrame,textvariable=self.price, font=('Algerian0',15,'bold'),bd=8,relief=RIDGE)
        self.p_price.place(x=280,y=100,width=180)


        Label(sMainFrame, text="Total Price",font=('Times New Roman',18),bg="#53eee5").place(x=1300,y=365)
        self.total_e = Entry(sMainFrame, bd=5,textvariable=self.total_price,relief=RIDGE,font=('Times New Roman',18,'bold'))
        self.total_e.place(x=1300,y=400,height=35,width=180)

        Label(sMainFrame, text="Cash Paid RS -",font=('Times New Roman',18),bg="#53eee5").place(x=1300,y=450)
        self.cashpaid_e = Entry(sMainFrame,textvariable=self.cashPaid ,bd=5,relief=RIDGE,font=('Times New Roman',18,'bold'))
        self.cashpaid_e.place(x=1300,y=480,height=35,width=180)

        Label(sMainFrame, text="Change RS -",font=('Times New Roman',18),bg="#53eee5").place(x=1300,y=540)
        self.change_e = Entry(sMainFrame, bd=5,textvariable=self.changeRs,state='disable',relief=RIDGE,font=('Times New Roman',18,'bold'))
        self.change_e.place(x=1300,y=570,height=35,width=180)

        self.sellid = Entry(sMainFrame,state='disable',textvariable=self.sellingId)
        self.sellid.place(x=20,y=100,width=100)
        self.sellingId.set(self.sellId[0])

        

        self.productName.trace('w',self.select)


        img1  =Image.open(r"image\add.jpg")
        img1 = img1.resize((120,35),Image.ANTIALIAS)
        self.addbtn = ImageTk.PhotoImage(img1)
        Button(sMainFrame,image=self.addbtn,borderwidth=0,command=self.addtoMainTreeview).place(x=550,y=45)

        img2  =Image.open(r"image\update.png")
        img2 = img2.resize((120,35),Image.ANTIALIAS)
        self.updatebtn = ImageTk.PhotoImage(img2)
        Button(sMainFrame, image=self.updatebtn,borderwidth=0,command=self.update).place(x=700,y=45)
        
        img3  =Image.open(r"image\delete.png")
        img3 = img3.resize((120,40),Image.ANTIALIAS)
        self.deletebtn = ImageTk.PhotoImage(img3)
        Button(sMainFrame, image=self.deletebtn,command=self.delete).place(x=480,y=90,width=120,height=35)

        img4  =Image.open(r"image\clear.png")
        img4 = img4.resize((120,40),Image.ANTIALIAS)
        self.clrbtn = ImageTk.PhotoImage(img4)
        Button(sMainFrame,image=self.clrbtn,borderwidth=0,command=self.clr).place(x=650,y=90)



        

        if shname_len <= 22:
            Label(sMainFrame, text="WELCOME",font=("Algerian",22,'bold'),bg="#53eee5").place(x=1100,y=10)
            l1=Label(sMainFrame, text="TO",font=("Algerian",22,'bold'),bg="#53eee5").place(x=1100,y=40)

            Label(sMainFrame, text=shopname,font=("Algerian",22,'bold'),bg="#53eee5").place(x=1100,y=70)

        else:
            Label(sMainFrame, text="WELCOME",font=("Algerian",22,'bold'),bg="#53eee5").place(x=950,y=10)
            l1=Label(sMainFrame, text="TO",font=("Algerian",22,'bold'),bg="#53eee5").place(x=950,y=40)
            Label(sMainFrame, text=shopname,font=("Algerian",22,'bold'),bg="#53eee5").place(x=950,y=70)



        sc_x = ttk.Scrollbar(treeFrame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)

        sc_y = ttk.Scrollbar(treeFrame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)
        
        self.soldMain_tree = ttk.Treeview(treeFrame,xscrollcommand=sc_x,yscrollcommand=sc_y)

        self.soldMain_tree['columns'] = ("p_id","p_name","p_qty","p_price","t_price")

        sc_x.config(command=self.soldMain_tree.xview)
        sc_y.config(command=self.soldMain_tree.yview)

        self.soldMain_tree.column("#0", stretch=NO,width=0)
        self.soldMain_tree.column("p_id",minwidth=100,width=150,anchor=CENTER)
        self.soldMain_tree.column("p_name",minwidth=400,anchor=CENTER)
        self.soldMain_tree.column("p_qty",minwidth=130,anchor=CENTER)
        self.soldMain_tree.column("p_price",minwidth=130,anchor=CENTER)
        self.soldMain_tree.column("t_price",minwidth=130,anchor=CENTER)
        self.soldMain_tree.bind("<ButtonRelease-1>",self.soldMain_treeCursorData)

        self.soldMain_tree.heading("#0", text="")
        self.soldMain_tree.heading("p_id", text="PRODUCT ID", anchor=CENTER)
        self.soldMain_tree.heading("p_name", text="PRODUCT NAME", anchor=CENTER)
        self.soldMain_tree.heading("p_qty", text="PRODUCT QTY", anchor=CENTER)
        self.soldMain_tree.heading("p_price", text="PRODUCT PRICE", anchor=CENTER)
        self.soldMain_tree.heading("t_price", text="TOTAL PRICE", anchor=CENTER)

        self.soldMain_tree.pack(fill=BOTH,expand=True)


        

        

        img5  =Image.open(r"image\save2.png")
        img5 = img5.resize((140,50),Image.ANTIALIAS)
        self.insertlogo = ImageTk.PhotoImage(img5)
        save_btn = Button(sMainFrame,text="SAVE",image=self.insertlogo,font=('Times New Roman',18),bg="#E0C1FF",command=self.save_btn)
        save_btn.place(x=950,y=650)

        img6  =Image.open(r"image\print and save.png")
        img6 = img6.resize((180,60),Image.ANTIALIAS)
        self.printAndSavelogo = ImageTk.PhotoImage(img6)
        Button(sMainFrame,image=self.printAndSavelogo,borderwidth=0,command=self.printAndSave_btn).place(x=1100,y=650)

        #____________________________________________________________________________________________
        #_______________________________ BIND EVENTS ON MAIN FRAME __________________________________
        #button bind 
        sMainFrame.bind('<Control-Shift-B>',self.back)
        #sMainFrame.bind('<Control_L> <a>',self.add)
        sMainFrame.bind('<Control_L> <u>',self.update)
        sMainFrame.bind('<Control_L> <c>',self.clr)
        sMainFrame.bind('<Control_L> <d>',self.delete)
        sMainFrame.bind('<Control_L> <s>',self.save_btn)
        sMainFrame.bind('<Control-Shift-S>',self.printAndSave_btn)


        #entry bind
        self.p_name.bind('<Down>',self.downToTreeview)
        self.p_name.bind('<Up>',self.upToTreeview)

        self.p_name.bind('<Return>',self.add)
        self.p_qty.bind('<Return>',self.addtoMainTreeview)
        self.p_qty.bind('<Left>',self.MoveToNameField)
        self.p_price.bind('<Return>',self.addtoMainTreeview)
        self.p_price.bind('<Left>',self.MoveQtyField)

        self.cashPaid.trace('w',self.getChange)
        

        self.productframecount = 0
        #_______________________________________________________________________________________________
        #_____________________________________ METHOD SECTION __________________________________________

    
        
    def back(self,*args):
        self.root.withdraw()
        self.stock_w = Toplevel()
        obj = stock(self.stock_w)

    def MoveQtyField(self,*args):
        if self.p_price.get() == "" or self.p_price.get() == '0':
            self.p_qty.focus()

    def MoveToNameField(self,*args):
        if self.p_qty.get() == "" or self.p_qty.get()=='1':
            self.p_name.focus()

    def soldMain_treeCursorData(self,event=""):
        cursor_row = self.soldMain_tree.focus()
        content = self.soldMain_tree.item(cursor_row)
        row = content['values']
        self.MainCursordata = row
        self.productName.set(row[1])
        self.qty.set(row[2])
        self.price.set(row[3])
    

    def getChange(self,*args):
        if self.cashpaid_e.get() == "":
            self.changeRs.set(0)
   
        try:
            
            change = float(self.cashpaid_e.get()) - float(self.total_e.get())
            self.changeRs.set(change)
        except ValueError:
            messagebox.showinfo('info','insert correct string')

    def save_btn(self,*args):
        cursor.execute("select sum(total_price) from selling_table where sh_id=? and s_id=?",(self.shop_no[0],self.sellId[0]))
        self.total = cursor.fetchone()
        self.total_price.set(self.total[0])

    def clrsoldMain_tree(self):
        self.soldMain_tree.delete(*self.soldMain_tree.get_children()) 
        cursor.execute("SELECT p_id,p_name,qty,s_price,total_price FROM selling_table WHERE s_id=? AND sh_id = ?",(self.sellId[0],self.shop_no[0]))
        data = cursor.fetchall()

        count=0

        for i in data:
                self.soldMain_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]))
                count=count+1

        self.save_btn()

        #print(data)

    def clr(self,*args):
        self.p_name.delete(0,END)
        self.p_qty.delete(0,END)
        self.p_price.delete(0,END)
        self.qty.set(1)
        self.p_name.focus()

    def addtoMainTreeview(self,*args):
        if self.p_name.get()=="" or self.p_price.get=='0':
            messagebox.showinfo('info','all fields are required')


        else:
            cursor.execute("SELECT p_id FROM products WHERE p_name=? AND sh_id=? ",(self.p_name.get(),self.shop_no[0]))
            c = cursor.fetchone()
            if c == None:
                 messagebox.showinfo('info','plz insert correct product')

            else:
                cursor.execute("select *from selling_table where p_id=? AND s_id=? AND sh_id=?",(self.highlighlitedRow[0],self.sellId[0],self.shop_no[0]))
                ch = cursor.fetchall()
                if ch:
                    #if product already available
                    messagebox.showinfo('info','this product is already available')
                else:
                    
                    total_price = float(self.p_qty.get()) * float(self.p_price.get())

                    cursor.execute("select p_price from products where p_id=? AND sh_id=?",(self.highlighlitedRow[0],self.shop_no[0]))
                    product_price = cursor.fetchone()
                    
                    cursor.execute("select getdate()")
                    date = cursor.fetchone()

                    cursor.execute("INSERT INTO selling_table(sh_id,s_id,p_name,qty,p_price,s_price,total_price,date,p_id) VALUES(?,?,?,?,?,?,?,?,?)",
                                   (self.shop_no[0],self.sellId[0],self.p_name.get(),self.p_qty.get(),product_price[0],self.p_price.get(),total_price,date[0],self.highlighlitedRow[0])
                                   )
                    conn.commit()

                    self.clr()
                    
                    

                    self.clrsoldMain_tree()
                    
                    
                    '''print("==============================")
                    print("pro id",self.highlighlitedRow[0])
                    print("shop no = ",self.shop_no[0])
                    print("product name = ",self.p_name.get())
                    print('qty = ',self.p_qty.get())
                    print('s price = ',self.p_price.get())
                    print('p price = ',product_price[0])
                    print('date = ',date[0])
                    print('total price = ',total_price)'''

        
            
    def add(self,*args):
        if self.p_name.get() == "" or self.p_price.get()=="":
            messagebox.showinfo('info','plz select correct product')

        else:
            cursor.execute("SELECT *FROM products WHERE p_name = ? AND sh_id=?",(self.p_name.get(), self.shop_no[0]))
            ch = cursor.fetchall()
            if ch:
                self.productName.set(self.highlighlitedRow[1])
                self.productparentFrame.destroy()
        
            else:
                messagebox.showinfo("info","select correct product")
            

    def clrProduct_treeview(self,rowcount):

        proName = '%'+self.p_name.get()+'%'
        cursor.execute("SELECT p_id,p_name,p_qty,s_price FROM products WHERE p_name like ? AND sh_id = ?",(proName,self.shop_no[0]))
        data = cursor.fetchall()

        self.sold_tree.delete(*self.sold_tree.get_children())  #clr treeview

        self.sold_tree.tag_configure('highlight',background="blue",foreground="white",font=('Times New Roman',12,'bold'))

        self.count = 0
        for i in data:
            if rowcount == self.count:
                self.sold_tree.insert(parent="", index="end", iid=self.count, text="" , values=(i[0],i[1],i[2],i[3]),tags='highlight')
                
            else:
                self.sold_tree.insert(parent="", index="end", iid=self.count, text="" , values=(i[0],i[1],i[2],i[3]))

            self.count += 1

            
    
    def select(self,*args):
        if self.p_name.get() == "" and self.p_qty.get()=="":
            messagebox.showerror("error","all fields are required")

        else:
            if self.productframecount == 1:
                self.productframecount = 0
                self.productparentFrame.destroy()
                self.select()

            if self.p_name.get()=="":
                self.productparentFrame.destroy()
                
            if self.productframecount == 0:
                self.productparentFrame = LabelFrame(self.root,text="select product",font=('Algerian',12,'bold'),bd=10,relief=RIDGE)
                self.productparentFrame.place(x=100,y=310,width=800,height=400)

                self.productFrame = Frame(self.productparentFrame,bd=5,relief=RIDGE)
                self.productFrame.place(x=3,y=35,width=780,height=335)

                img  =Image.open(r"image\exit.png")
                img = img.resize((90,35),Image.ANTIALIAS)
                self.exit = ImageTk.PhotoImage(img)
                Button(self.productparentFrame, image=self.exit,command=self.exitbtn).place(x=690,y=0)
                

                sc_x = ttk.Scrollbar(self.productFrame, orient=HORIZONTAL)
                sc_x.pack(side=BOTTOM, fill=X)

                sc_y = ttk.Scrollbar(self.productFrame, orient=VERTICAL)
                sc_y.pack(side=RIGHT, fill=Y)
                
                self.sold_tree = ttk.Treeview(self.productFrame,xscrollcommand=sc_x,yscrollcommand=sc_y)

                self.sold_tree['columns'] = ("p_id","p_name","p_qty","p_price")

                self.sold_tree.column("#0",stretch=NO,width=0)
                self.sold_tree.column("p_id",minwidth=100,width=100,anchor=CENTER)
                self.sold_tree.column("p_name",minwidth=400,anchor=CENTER)
                self.sold_tree.column("p_qty",minwidth=100,anchor=CENTER)
                self.sold_tree.column("p_price",minwidth=150,anchor=CENTER)

                self.sold_tree.heading("#0",text="")
                self.sold_tree.heading("p_id",text="product id",anchor=CENTER)
                self.sold_tree.heading("p_name",text="product name",anchor=CENTER)
                self.sold_tree.heading("p_qty",text="QTY",anchor=CENTER)
                self.sold_tree.heading("p_price",text="price",anchor=CENTER)
                

                self.sold_tree.pack(fill=BOTH, expand=True)
                
                self.clrProduct_treeview(-1)
                
            #-------variables --------------   
            self.productframecount = 1
            self.rowCount = 0
            self.c = 0
            
    def downToTreeview(self,*args):
        if self.p_name.get() == "":  #product name is not empty self.count check the row of treeview is end row or not
            pass
           
        else:
            print("row count",self.rowCount)
            if self.rowCount == self.count:
                pass
            #cursor_row = self.sold_tree.focus()
            else:
                content = self.sold_tree.item(self.rowCount)
                row = content['values']
                
                self.highlighlitedRow = row  #store the value of selected row
                print("highlight row data = ",self.highlighlitedRow)

                self.p_id = self.highlighlitedRow[0]
                #self.productName.set(self.highlighlitedRow[1])
                #self.qty.set(self.highlighlitedRow[2])
                self.price.set(self.highlighlitedRow[3])
                

                self.clrProduct_treeview(self.rowCount)
                self.rowCount = self.rowCount+1
                self.c=self.c+1
            

    def upToTreeview(self,*args):
        
        #cursor_row = self.sold_tree.focus()
        if self.p_name.get() == "":
            pass
        else:
            if self.rowCount == 0:
                content = self.sold_tree.item(self.rowCount)
                row = content['values']
                self.clrProduct_treeview(self.rowCount)
            else:
                content = self.sold_tree.item(self.rowCount-1)
                row = content['values']

                self.highlighlitedRow = row  #store the value of selected row
                print("highlight row data=",self.highlighlitedRow)
                self.p_id = self.highlighlitedRow[0]
            
                #self.productName.set(self.highlighlitedRow[1])
                #self.qty.set(self.highlighlitedRow[2])
                self.price.set(self.highlighlitedRow[3])
                
                print("before :-",self.rowCount)
                self.clrProduct_treeview(self.rowCount-1)
                self.rowCount = self.rowCount-1
                print("after := ",self.rowCount)
                #self.c=self.c+1
            
    def update(self,*args):
        if self.p_qty.get()=="" or self.p_name.get()=="" or self.p_price.get()=="":
            messagebox.showinfo('info','all fields are required')
        else:
            sh_id = self.shop_no[0]
            sell_id = self.sellId[0]
            p_name = '%'+str(self.p_name.get())+'%'
    
            cursor.execute("SELECT *from selling_table WHERE sh_id=? AND s_id=? AND p_name like ? ",(sh_id,sell_id,p_name))
            ch = cursor.fetchall()
            if ch:
     
                cursor.execute("SELECT p_id from selling_table WHERE p_name like ? AND sh_id=? AND s_id=?",(self.p_name.get(),sh_id,sell_id))
                p_id = cursor.fetchone()
                #print("p_name = ",self.p_name.get(),"sh_id = ",sh_id,"sell_id = ",sell_id)        
                
                qty = self.p_qty.get()
                s_price =   self.p_price.get()
                total_price =   float(qty) * float(s_price)
                #print('qty =',qty,'sprice = ',s_price,'total_price = ',total_price)

                #print('p_id= ',p_id[0],'sh_id = ',sh_id,'sell_id = ',sell_id)
                
                cursor.execute("UPDATE selling_table SET qty=?,s_price=?, total_price=? WHERE p_id=? AND sh_id=? AND s_id=? ",
                                   (qty, s_price,total_price ,p_id[0],sh_id, sell_id)
                              )
                conn.commit()
                messagebox.showinfo('info','update')
            else:
                messagebox.showinfo('info',"this product can't update because this product is not inserted")
        self.clrsoldMain_tree()

    

    def delete(self,*args):
        if self.p_name.get()=="" or self.p_price.get=='0':
            messagebox.showinfo('info','all fields are required')
        else:
            cursor.execute("SELECT *FROM products WHERE p_name = ? AND sh_id=?",(self.p_name.get(), self.shop_no[0]))
            ch = cursor.fetchall()
            if ch:
                messagebox.showinfo('info','delete')
            else:
                messagebox.showinfo('info','plz.. select correct product')

    

    def printAndSave_btn(self,*args):
        messagebox.showinfo('info','print and save click')

    
    def exitbtn(self):
        self.productframecount = 0
        self.productparentFrame.destroy()


   
#______________________________________________________________________________________________________________
'''================================================ MAIN LOOP =============================================='''
    
if __name__ == '__main__':
    root=Tk()
  
    #obj = splash(root)
    obj = SoldClass(root)
    root.mainloop
