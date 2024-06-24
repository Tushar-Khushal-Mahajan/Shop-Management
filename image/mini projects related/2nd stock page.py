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


class stock:
    def __init__(self,root):
        self.root = root

        self.root = root
        self.root.geometry("1550x1000")
        self.root.resizable(False,False) #hide the title bar

        cursor = conn.cursor()
        cursor.execute("SELECT sh_id FROM shop WHERE sh_status='yes' ")
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
        cursor.execute("SELECT sh_name FROM shop WHERE sh_status='yes' ")
        shop_name = cursor.fetchone()
    
        sh_name = shop_name[0]
        '''
            ===============================================================================================
        '''

        img1  =Image.open(r"image\bg.png")
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
        Button(topframe,text="click",command=self.logo,image=self.photoimg1,borderwidth=0).place(x=0,y=0)
        
        Label(topframe, text=sh_name,bg="lightyellow",fg="red",font=("Algerian",30)).pack(side=TOP , fill=X,padx=100,pady=25)

        img2  =Image.open(r"image\home1.png")
        img2 = img2.resize((125,50),Image.ANTIALIAS)
        self.homelogo = ImageTk.PhotoImage(img2)
        Button(btnframe,image=self.homelogo ,text="HOME",command=self.home,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=3,height=50,width=125)

        img3  =Image.open(r"image\stock.png")
        img3 = img3.resize((125,50),Image.ANTIALIAS)
        self.stocklogo = ImageTk.PhotoImage(img3)
        Button(btnframe,image=self.stocklogo ,text="STOCK",command=self.stock,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=55,height=50,width=125)
        
        img4  =Image.open(r"image\sold.png")
        img4 = img4.resize((125,50),Image.ANTIALIAS)
        self.soldlogo = ImageTk.PhotoImage(img4)
        Button(btnframe,image=self.soldlogo, text="SOLD", command=self.sold,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=108,height=50,width=125)

        img5  =Image.open(r"image\creadit.png")
        img5 = img5.resize((125,50),Image.ANTIALIAS)
        self.creaditlogo = ImageTk.PhotoImage(img5)
        Button(btnframe,image=self.creaditlogo, text="CREDIT", command=self.creadit,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=160,height=50,width=125)

        img6  =Image.open(r"image\order goods.png")
        img6 = img6.resize((125,50),Image.ANTIALIAS)
        self.orderlogo = ImageTk.PhotoImage(img6)
        Button(btnframe,image=self.orderlogo, text="ORDER GOODS",command=self.order,font=('Sitka Small Semibold',11,'bold'),bd=5,relief=GROOVE).place(x=2,y=213,height=50,width=125)

        img7  =Image.open(r"image\accounting.png")
        img7 = img7.resize((125,50),Image.ANTIALIAS)
        self.acclogo = ImageTk.PhotoImage(img7)
        Button(btnframe,image=self.acclogo,text="ACCOUNTING", command=self.accounting,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=266, height=50,width=125)

        img8  =Image.open(r"image\notes.png")
        img8 = img8.resize((125,50),Image.ANTIALIAS)
        self.noteslogo = ImageTk.PhotoImage(img8)
        Button(btnframe,image=self.noteslogo, text="NOTES",command=self.notes,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=319,height=50,width=125)

        img9  =Image.open(r"image\log out.png")
        img9 = img9.resize((125,50),Image.ANTIALIAS)
        self.logoutlogo = ImageTk.PhotoImage(img9)
        Button(btnframe,image=self.logoutlogo,text="LOG OUT", command=self.log_out,font=('Sitka Small Semibold',12,'bold'),bd=5,relief=GROOVE).place(x=2,y=372, height=50,width=125)

        '''========================BIND GLOBAL ROOT BUTTONS=========================='''
        self.root.focus()

        self.root.bind('<Control-Shift-H>',self.home)
        self.root.bind('<Control-Shift-S>',self.stock)
        self.root.bind('<F2>',self.sold)
        self.root.bind('<Control-Shift-C>',self.creadit)
        self.root.bind('<Control-Shift-O>',self.order)
        self.root.bind('<Control-Shift-A>',self.accounting)
        self.root.bind('<Control-Shift-N>',self.notes)
        self.root.bind('<Control-Shift-L>',self.log_out)

        '''=========================================================================='''
            
        self.stock_w_open = False
        self.searchCount = 0
        
    def logo(self):
        pass

    def home(self,*args):
        if self.stock_w_open == True:
            self.stock_frame.destroy()
            self.stock_w_open = False

    def stock(self,*args):
        if self.stock_w_open == False:
            self.stock_frame = Frame(self.root,bg='white',bd=10,relief=RIDGE)
            self.stock_frame.place(x=250,y=100,width=920,height=500) 
            

            Label(self.stock_frame, text="STOCK AVAILABLE ON SHOP",font=("Sitka Small Semibold",15,"bold")).pack(side=TOP,fill=X)

            self.o_frame = Frame(self.stock_frame,bd=10,relief=RIDGE)
            self.o_frame.place(x=0,y=30,width=900,height=250)

            self.stock_btm_frame = Frame(self.stock_frame,bg='red',bd=10,relief=RIDGE)
            self.stock_btm_frame.place(x=0,y=280,width=900,height=200)

            stock_left_frame = Frame(self.stock_btm_frame, bd=10,relief=RIDGE)
            stock_left_frame.place(x=1,y=0,width=660,height=180)
       
        
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

            
            
            self.stock_w_open = True

            '''===================================== BINDING BUTTONS============================='''
            
            
            #local button binds
            EntryBoxList = [self.product,self.qty,self.p_price,self.s_price]
            for i in EntryBoxList:
                i.bind('<Control_L><i>',self.stock_insert)
                i.bind('<Control_L><u>',self.stock_update)
                i.bind('<Control_L><d>',self.stock_delete)
                i.bind('<Control_L><c>',self.stock_clere)
                i.bind('<Control_L><r>',self.refresh)
                i.bind('<Control_L><s>',self.search)
                i.bind('<Control_L><h>',self.highStockFun)
                i.bind('<Control_L><l>',self.lowStockFun)
            
            '''=================================================================================='''


    def sold(self,*args):
        print("sold class object hear")
        print(args)

    def creadit(self,*args):
        print("creadit class object hear")

    def order(self,*args):
        print("order class object hear")

    def accounting(self,*args):
        print("accounting class object hear")

    def notes(self,*args):
        print("notes class object hear")

    def log_out(self,*args):
        self.c=messagebox.askquestion("warning","ARE YOU SURE TO LOG OUT YOUR SHOP AC.")
        if self.c == "yes":
            messagebox.showinfo("info","LOG OUT SUCCESSFULLY")

            cursor = conn.cursor()
            cursor.execute("UPDATE shop set sh_status='no' WHERE sh_status='yes'")
            conn.commit()

            '''self.root.withdraw()
            self.Register_w = Toplevel()
            obj = Register(self.Register_w)'''
            print("log out successfully")

        else:
            #nothing
            pass

    #___________________________________________________________________________________________
    '''=====================================stock w functions ================================'''
    def stock_insert(self,*args):
        if self.product.get()=='' or self.qty.get()=='' or self.p_price.get()=='' or self.s_price.get()=='':
            messagebox.showerror("error", "all fields are required")

        else:
            cursor = conn.cursor()
          
            sh_id=self.shop_no[0]
            
            cursor.execute("select *from products where p_name ='{}' ".format(self.p_name.get()))
            avl = cursor.fetchone()

            if avl:
                messagebox.showerror('error', "product already available")

            else:
                cursor.execute("""INSERT INTO products(sh_id, p_name, p_qty, p_price, s_price) VALUES('{}','{}','{}','{}','{}')""".format
                            (sh_id,self.p_name.get(),self.qty.get(),self.p_price.get(), self.s_price.get() ))
                conn.commit()
                self.stock_clere()
                #messagebox.showinfo('INFO','insert successfully')
                self.clr_treeview()


    def stock_update(self,*args):
        if self.product.get()=='' or self.qty.get()=='' or self.p_price.get()=='' or self.s_price.get()=='':
            messagebox.showerror("error", "all fields are required")

        else:
            cursor = conn.cursor()
            cursor.execute("UPDATE products set p_name='{}', p_qty='{}', p_price='{}', s_price='{}' where p_id ='{}' ".format(
                        self.p_name.get(),self.qty.get(),self.p_price.get(), self.s_price.get(),self.p_id
                ))            
            conn.commit();
            self.stock_clere()
            #messagebox.showinfo('INFO','update successfully')
            self.clr_treeview()
            

    def stock_delete(self,*args):
            if self.product.get()=='' or self.qty.get()=='' or self.p_price.get()=='' or self.s_price.get()=='':
                messagebox.showerror("error", "all fields are required")

            else:
                self.ch = messagebox.askquestion("warning","ARE YOU SURE TO DELETE THIS RECORD...")
                if self.ch == "yes":
                    cursor = conn.cursor()
                    cursor.execute("DELETE from products WHERE p_id='{}'".format(self.p_id))
                    conn.commit()
                    self.stock_clere()
                    self.clr_treeview()
                    
                else:
                    #nothing
                    pass

    def refresh(self,*args):
        self.clr_treeview()
        
                
    def stock_clere(self,*args):
        self.product.focus()
        self.product.delete(0,END)
        self.qty.delete(0,END)
        self.p_price.delete(0 ,END)
        self.s_price.delete(0,END)


    def search(self,*args):
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

            self.option.trace('w',self.search_OptionMenu_Click)
            
            #Button(self.stock_search_frame, text="SEARCH",image= self.rsearchlogo,borderwidth=0,command=self.itemSearch).place(x=200, y=40,width=40)

        else:
            self.stock_search_frame.destroy()
            self.searchCount=0
            

    def highStockFun(self,*args):
        cursor = conn.cursor()
        
        sh_id = self.shop_no[0]
        
        cursor.execute("SELECT p_id,p_name,p_qty,p_price,s_price FROM products where sh_id='{}' and p_qty>='{}' order by p_qty desc".format(sh_id,18))
        data = cursor.fetchall()
        self.order_tree.delete(*self.order_tree.get_children())  #clere treeview

        self.order_tree.tag_configure('highstock',background="lime", font=('Times New Roman',12,'bold'))

        count = 0
        for i in data:
            self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]),tags=('highstock',))
            count += 1

    def lowStockFun(self,*args):
        cursor = conn.cursor()
       
        sh_id = self.shop_no[0]
        cursor.execute("SELECT p_id,p_name,p_qty,p_price,s_price FROM products where sh_id='{}' and p_qty<='{}' order by p_qty asc".format(sh_id,10))
        data = cursor.fetchall()
        self.order_tree.delete(*self.order_tree.get_children())  #clere treeview

        self.order_tree.tag_configure('lowstock',background="DarkOrange", font=('Times New Roman',12,'bold'))

        count = 0
        for i in data:
            self.order_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]),tags=('lowstock',))
            count += 1
    #___________________________________________________________________________________________

    def clr_treeview(self):
        self.order_tree.delete(*self.order_tree.get_children())  #clere treeview

       
        sh_id = self.shop_no
        cursor.execute("SELECT p_id,p_name,p_qty,p_price,s_price FROM products where sh_id='{}' order by p_qty asc".format(sh_id[0]))
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
        
    
    def stock_cursor(self, event=""):
        try:
            cursor_row = self.order_tree.focus()
            content = self.order_tree.item(cursor_row)
            row = content['values']
            self.p_id = row[0]
            self.p_name.set(row[1])
            self.ss_price.set(row[4])
            self.sp_price.set(row[3])
            self.sqty.set(row[2])
            
        except Exception:
            pass
        self.product.focus()
        
    
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
        cursor.execute("""SELECT p_name FROM products WHERE sh_id='{}' """.format(self.shop_no[0]))
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
        

        
    def itemSearch(self,):
        if self.option.get() == "Search By" or self.searchEntry.get() == "":
            messagebox.showerror("Error","all fields are required");
            

        else:
            check_selection = self.str_out.get()
            entry_value = '%'+self.searchEntry.get()+'%'
            
            
            if check_selection == 'By ID':   #if the user intrested to search a product by its id 
                cursor = conn.cursor()
                cursor.execute("""SELECT *FROM products WHERE p_id like '{}'  AND sh_id ='{}' """.format(entry_value,self.shop_no[0]))
                data = cursor.fetchall()

                
                
            else:     #if the user intrested to search a product by its id
                
                cursor = conn.cursor()
                cursor.execute("""SELECT *FROM products WHERE p_name like '{}' AND sh_id='{}' ORDER BY p_qty asc """.format(entry_value,self.shop_no[0]))
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
                self.order_tree.delete(*self.order_tree.get_children())  #clere treeview'''
    



if __name__ == '__main__':
    root = Tk()
    obj = stock(root)

    root.mainloop()
