'''*****IMPORT MODULES****'''
from tkinter import *
from functools import partial
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import re




'''////////////////////////////////////////'''

class Sold:
    def __init__(self,root):
        self.root = root
        self.root.state("zoomed")
        '''----------------------- shop name and shop no ----------------------------'''
        conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
        cursor = conn.cursor()
        
        cursor.execute("SELECT sh_id FROM shop WHERE sh_status='yes' ")
        self.shop_no = cursor.fetchone()
        cursor.execute("SELECT sh_name FROM shop WHERE sh_id={} ".format(self.shop_no[0]))
        self.shop_name = cursor.fetchone()
        cursor.execute("INSERT INTO sell_id(abc) VALUES('{}')".format('abc'))
        conn.commit()
        cursor.execute("SELECT s_id FROM sell_id order by s_id desc")
        self.sellId = cursor.fetchone()

        conn.close()
        
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

        self.shop_name = StringVar()
        
        self.total_price.set(0)
        #----------------------------set date and day------------
        conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
        cursor=conn.cursor()

        cursor.execute(""" select date_format(sysdate(),'%y-%m-%d') """)
        date = cursor.fetchall()
        self.getDate=date[0]

        cursor.execute(""" select dayname(sysdate()) """)
        day = cursor.fetchall()
        self.getDay=day[0]

        cursor.execute(""" select sh_name from shop where sh_status='yes' """)
        shname = cursor.fetchone()
        self.shop_name=shname[0]
        
        shname_len = len(shname[0])
        self.qty.set(1)
        
        conn.close()
        
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
        self.total_e = Entry(sMainFrame, bd=5,state='disable',textvariable=self.total_price,relief=RIDGE,font=('Times New Roman',18,'bold'))
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

        self.cashpaid_e.bind('<F1>',lambda event="":self.p_name.focus())

        img1  =Image.open(r"image\add.jpg")
        img1 = img1.resize((120,35),Image.ANTIALIAS)
        self.addbtn = ImageTk.PhotoImage(img1)
        Button(sMainFrame,image=self.addbtn,borderwidth=0,command=self.sold_treeview_to_main_treeview).place(x=550,y=45)

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

                Label(sMainFrame, text=self.shop_name,font=("Algerian",22,'bold'),bg="#53eee5").place(x=1100,y=70)

        else:
                Label(sMainFrame, text="WELCOME",font=("Algerian",22,'bold'),bg="#53eee5").place(x=950,y=10)
                l1=Label(sMainFrame, text="TO",font=("Algerian",22,'bold'),bg="#53eee5").place(x=950,y=40)
                Label(sMainFrame, text=self.shop_name,font=("Algerian",22,'bold'),bg="#53eee5").place(x=950,y=70)



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
        self.soldMain_tree.bind("<ButtonRelease-1>",self.sell_treeview_focus)

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
        Button(sMainFrame,text="SAVE",image=self.insertlogo,font=('Times New Roman',18),bg="#E0C1FF",command=self.save_btn).place(x=950,y=650)

        img6  =Image.open(r"image\print and save.png")
        img6 = img6.resize((180,60),Image.ANTIALIAS)
        self.printAndSavelogo = ImageTk.PhotoImage(img6)
        Button(sMainFrame,image=self.printAndSavelogo,borderwidth=0,command=self.printAndSave_btn).place(x=1100,y=650)

        #----------------------------------------------------------------------------------------------
        self.productmainframeOpen = False
        self.productName.trace('w',self.pro_nameEnter)
        self.cashPaid.trace('w',self.cash_paid)
        
        self.count_sell_treeviewValues=0
        self.count_down_cursor_value=0
        self.highlightrow= None

        self.target = -1

        
        #____________________________________________________________________________________________
        #_______________________________ BIND EVENTS ON MAIN FRAME __________________________________
        
        self.p_name.bind('<Down>',self.p_nameDown)
        self.p_name.bind('<Up>',self.p_nameUp)
        self.p_name.bind('<Return>',self.p_nameEnter)
        
        self.p_qty.bind('<Return>',self.sold_treeview_to_main_treeview)
        self.p_price.bind('<Return>',self.sold_treeview_to_main_treeview)

        #global button binding
        self.p_name.bind('<Control-Shift-B>',self.back)
        self.p_qty.bind('<Control-Shift-B>',self.back)
        self.p_price.bind('<Control-Shift-B>',self.back)
        self.cashpaid_e.bind('<Control-Shift-B>',self.back)

        #local btn binding
        '''PRODUCT NAME ENTRY BIND'''
        self.p_name.bind('<Control_L> <a>',self.sold_treeview_to_main_treeview),self.p_name.bind('<Control_L> <u>',self.update)
        self.p_name.bind('<Control_L> <d>',self.delete),self.p_name.bind('<Control_L> <c>',self.clr)
        '''PRODUCT QTY ENTRY BIND'''
        self.p_qty.bind('<Control_L> <a>',self.sold_treeview_to_main_treeview),self.p_qty.bind('<Control_L> <u>',self.update)
        self.p_qty.bind('<Control_L> <d>',self.delete),self.p_qty.bind('<Control_L> <c>',self.clr)
        '''PRODUCT PRICE ENTRY BIND'''
        self.p_price.bind('<Control_L> <a>',self.sold_treeview_to_main_treeview),self.p_price.bind('<Control_L> <u>',self.update)
        self.p_price.bind('<Control_L> <d>',self.delete),self.p_price.bind('<Control_L> <c>',self.clr)
        '''PRODUCT CASH PAID ENTRY BIND'''
        self.cashpaid_e.bind('<Control_L> <a>',self.sold_treeview_to_main_treeview),self.cashpaid_e.bind('<Control_L> <u>',self.update)
        self.cashpaid_e.bind('<Control_L> <d>',self.delete),self.cashpaid_e.bind('<Control_L> <c>',self.clr)
        self.cashpaid_e.bind('<Control_L> <s>',self.save_btn),self.cashpaid_e.bind('<Control_L> <p>',self.printAndSave_btn)

        #_______________________________________________________________________________________________
        #_____________________________________ METHOD SECTION __________________________________________

    def update(self,*args):
        if self.p_name.get()=="" or self.p_qty.get()=="" or self.p_price.get()=="":
                messagebox.showinfo("Message","All Fields are required..")

        else:
                try:
                        total_price =float(self.p_qty.get()) * float(self.p_price.get())
                        
                        conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
                        cursor=conn.cursor()

                        
                        cursor.execute(" UPDATE selling_table SET qty='{}',s_price='{}',total_price='{}' WHERE p_id='{}' AND sh_id='{}' AND s_id='{}' ".format(
                                self.p_qty.get(), self.p_price.get() , total_price,self.main_focus_row[0], self.shop_no[0],self.sellid.get() 
                            ))
                        conn.commit()
                        conn.close()
                        self.refresh_mainTreeview_data()

                except Exception:
                        messagebox.showinfo("Info","Plz select correct product")
                
    def delete(self,*args):
        if self.p_name.get()=="" or self.p_qty.get()=="" or self.p_price.get()=="":
                messagebox.showinfo("Message","All Fields are required..")
        else:
                try:
                        conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
                        cursor=conn.cursor()

                        cursor.execute(" DELETE FROM selling_table WHERE p_id='{}' AND sh_id='{}' AND s_id='{}' ".format(
                                self.main_focus_row[0],self.shop_no[0],self.sellid.get() 
                            ))
                        conn.commit()
                        conn.close()
                        self.refresh_mainTreeview_data()
                except Exception:
                        messagebox.showinfo("Info","Plz select correct product")

    def clr(self,*args):
        self.p_name.delete(0,END)
        self.qty.set(1)
        self.p_price.delete(0,END)
        self.p_name.focus()
        
        
    def back(self,*args):
        print("back..")
        '''self.root.withdraw()
        self.stock_w = Toplevel()
        obj = stock(self.stock_w)'''

      
    def sell_treeview_focus(self,*args):
        self.clr()
        cursor_row = self.soldMain_tree.focus()
        content = self.soldMain_tree.item(cursor_row)
        self.main_focus_row = content['values']
        try:
                self.productName.set(self.main_focus_row[1])
                self.qty.set(self.main_focus_row[2])
                self.price.set(self.main_focus_row[3])
        except Exception:
                self.productName.set("")
                self.qty.set(1)
                self.price.set(0)

    def cash_paid(self,*args):
        if self.total_e.get() == "" or self.total_e.get() == None:
                pass

        elif self.total_e.get()=='0':
                messagebox.showinfo("Message","Plz Select Product First..")
                self.cashPaid.set(0)

        else:
                try:
                        cash_paid = float(self.cashpaid_e.get())
                        total = float(self.total_e.get())
                        
                        change =  cash_paid -  total
                        self.changeRs.set(change)
                except Exception:
                        if self.cashpaid_e.get() == "":
                                self.changeRs.set(0)
                        elif self.cashpaid_e.get()=='+' or self.cashpaid_e.get()=='-':
                                if self.cashpaid_e.get()=='-':
                                        self.cashPaid.set('-')
                                else:
                                        self.cashPaid.set('+')
                        else:
                                self.cashPaid.set(0)
                                self.changeRs.set(0)
                                messagebox.showinfo("Message","Plz Enter Number Values Only..")
                    
    def go_to_CreaditPage(self):
        print('creadit page opened')

    
    def save_btn(self,*args):
        if self.total_e.get() == "" or self.total_e.get() == None or self.total_e.get()=='0':
                messagebox.showinfo("Message","Plz Select Product First..")
                self.p_name.focus()

        elif self.cashpaid_e.get() == '0':
                messagebox.showinfo("Message","Plz receive payment first..")
                self.cashpaid_e.focus()   

        elif float(self.change_e.get()) >= 0:
                messagebox.showinfo("message","saved")
        else:
                ch = messagebox.askquestion("question","this payment is -ve do you want to go to this payment in creadit")
                if ch == 'yes':
                        self.go_to_CreaditPage()
                else:
                        print('saved')
                self.p_name.focus()

    def printAndSave_btn(self,*args):
        print("print and save")

    #=======================================================
    def pro_nameEnter(self,*args):
        if self.p_name.get()== "":
                self.productmainframeOpen = False
                self.target=-1
                self.productmainframe.destroy()
    
            
        elif self.productmainframeOpen == False:
                self.productmainframe = LabelFrame(self.root,text="select product",font=('Algerian',12,'bold'),bd=10,relief=RIDGE)
                self.productmainframe.place(x=100,y=310,width=800,height=400)

                self.productFrame = Frame(self.productmainframe,bd=5,relief=RIDGE)
                self.productFrame.place(x=3,y=35,width=780,height=335)

                #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
                self.count_down_cursor_value = 0
                #-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
                
                img  =Image.open(r"image\exit.png")
                img = img.resize((90,35),Image.ANTIALIAS)
                self.exit = ImageTk.PhotoImage(img)
                Button(self.productmainframe, image=self.exit,command=self.exitbtn).place(x=690,y=0)


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

                #self.sold_tree_insert(-1)
                self.sold_tree_insert()

                self.productmainframeOpen = True
            
        else:
                #self.sold_tree_insert(0)
                self.sold_tree_insert()
            
            

    #----------------------------product frame functions------------------------------
    def exitbtn(self):
            self.productmainframeOpen = False
            self.target=-1 #new line add
            self.productmainframe.destroy()

    def sold_tree_insert(self):
        
            proName = '%'+self.p_name.get()+'%'

            conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
            cursor=conn.cursor()

            cursor.execute("SELECT p_id,p_name,p_qty,s_price FROM products WHERE p_name like '{}' AND sh_id = '{}'  ".format(proName,self.shop_no[0]))
            self.soldTree_data = cursor.fetchall()

            cursor.execute(" SELECT count(p_name)as count FROM products WHERE p_name like '{}' AND sh_id = '{}' ".format(proName,self.shop_no[0]))
            c= cursor.fetchone()
            self.count_sell_treeviewValues = c[0]        
            conn.close()

            #print(self.count_sell_treeviewValues)
            
            self.sold_tree.delete(*self.sold_tree.get_children())  #clr treeview

            self.sold_tree.tag_configure('focus',background="blue",foreground="white", font=('Times New Roman',12,'bold'))
            self.sold_tree_insert_refresh()
        
                
    def sold_tree_insert_refresh(self):
            count = 0
            for i in self.soldTree_data:
               
                    if self.target == count:
                            self.sold_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3]),tags=('focus',))

                            self.content =self.sold_tree.item(self.target)
                            
                            self.highlightrow = self.content['values']
                            
                    else:
                            self.sold_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3]))
                    count = count + 1
        

    def p_nameUp(self,*args):
            if self.p_name.get() == "":
                    pass
            
            elif self.target != 0 and self.target != -1:
                    self.target = self.target-1
                    self.sold_tree_insert()
            
            else:
                    self.target = self.count_sell_treeviewValues-1
                    self.sold_tree_insert()
            
    
    def p_nameDown(self,event=""):
            if self.p_name.get() == "":
                    pass

            elif self.target < self.count_sell_treeviewValues-1:
                    self.target = self.target+1
                    self.sold_tree_insert()
            else:
                    self.target = 0
                    self.sold_tree_insert()
            

    def p_nameEnter(self,*args):
            if self.p_name.get()=="" or self.highlightrow == None or self.target == -1:
                    pass

            else:
                    
                    '''data fiill in the text boxes'''
                    p_name = self.highlightrow[1] 
                    p_price = self.highlightrow[3]
                        
                    self.price.set(p_price)
                    self.productName.set(p_name)
                    self.exitbtn()
             


    def sold_treeview_to_main_treeview(self,*args):
            if self.p_name.get()=="":
                    messagebox.showinfo("message","product name is required.")
            else:
                    sh_id = self.shop_no[0]
                    s_id  = self.sellId[0]
                    p_name = self.highlightrow[1]
                    p_qty = self.p_qty.get()
                    #p_price = p_price[0]
                    s_price = self.p_price.get()
                    total_price = float(s_price) * float(p_qty)
                    date = self.getDate[0]
                    p_id = self.highlightrow[0]
                    #_______________________________________________
                    conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
                    cursor=conn.cursor()
                    cursor.execute(" SELECT p_price,p_qty FROM products WHERE p_id='{}' AND sh_id='{}' ".format(p_id,sh_id))
                    price_qty = cursor.fetchone()
                    conn.close()
                    
                    #------------------------------------------------

                    p_price = price_qty[0]
                    main_pro_qty = price_qty[1]
                    #________________________________________________
                    conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
                    cursor=conn.cursor()

                    #cursor.execute(" SELECT p_qty FROM products WHERE sh_id='{}' AND p_id='{}' ".format(sh_id,p_id))
                    
                    try:
                            if int(p_qty) < int(main_pro_qty):
                                    cursor.execute(" insert into selling_table values({},{},'{}',{},{},{},{},'{}',{})".format(
                                            sh_id,s_id,p_name,p_qty,p_price,s_price,total_price,date,p_id
                                        ))
                                    conn.commit()
                                    conn.close()
                            else:
                                    messagebox.showinfo("message","qty not available")
                        
                    except Exception:
                            messagebox.showinfo("message","product already available")
                    self.refresh_mainTreeview_data()

    def refresh_mainTreeview_data(self):
            sh_id = self.shop_no[0]
            s_id  = self.sellId[0]
            
            conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
            cursor=conn.cursor()     
            cursor=conn.cursor()
            cursor.execute(" SELECT p_id,p_name,qty,s_price,total_price FROM selling_table WHERE s_id='{}' AND sh_id='{}' ".format(
                    s_id,sh_id
                ))
            data = cursor.fetchall()
            
            conn.close()
            #------------------------------------------------
            self.soldMain_tree.delete(*self.soldMain_tree.get_children()) #clear treeview
            count = 0
            for i in data:
                    self.soldMain_tree.insert(parent="", index="end", iid=count, text="" , values=(i[0],i[1],i[2],i[3],i[4]))
                    count = count + 1

            self.clr()

            conn = mysql.connector.connect(host='localhost', database='shopmanagement', user='root', password='Tushar()mysql[123]')
            cursor=conn.cursor()
            cursor.execute(" SELECT SUM(total_price) FROM selling_table WHERE sh_id='{}' AND s_id='{}' ".format(sh_id,s_id))
            all_total_price = cursor.fetchone()
            conn.close()

            if all_total_price[0] == None:
                    self.total_price.set(0)
            else:
                    self.total_price.set(all_total_price[0])

            self.cash_paid()
        
        
        
               
       

if __name__ == '__main__':
        root  = Tk()
        obj = Sold(root)
        root.mainloop()
