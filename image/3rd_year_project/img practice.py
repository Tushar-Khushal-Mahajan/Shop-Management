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
        self.p_name.bind('<Control-F4>',self.exitbtn)
        self.p_name.bind('<Control_L> <u>',self.update)  #update key bind
        self.p_qty.bind('<Return>',self.addtoMainTreeview)
        self.p_qty.bind('<Left>',self.MoveToNameField)
        self.p_qty.bind('<Control_L> <u>',self.update)   #update key bind
        self.p_price.bind('<Return>',self.addtoMainTreeview)
        self.p_price.bind('<Left>',self.MoveQtyField)
        self.p_price.bind('<Control_L> <u>',self.update)  #update key bind

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
        messagebox.showinfo('info','save')

    def change(self):
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

        self.change()

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
            p_name = '%'+self.p_name.get()+'%'
            cursor.execute("SELECT *FROM products WHERE p_name LIKE ? AND s_price=? AND sh_id=?",(p_name,self.p_price.get(),self.shop_no[0]))
            ch= cursor.fetchall()
            if ch:
                self.productName.set(self.highlighlitedRow[1])  # set the selected record into entry frame
                self.productparentFrame.destroy()       #after selection this frame destroys
        
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
        if self.p_name.get() == "" or self.p_price.get()=="":
            messagebox.showinfo('info','plz... select correct product')

        else:
            p_name = self.p_name.get()
            cursor.execute("SELECT *FROM products WHERE p_name = ? AND s_price=? AND sh_id=?",(p_name,self.p_price.get(),self.shop_no[0]))
            ch= cursor.fetchall()
            if ch:
                c = messagebox.askquestion('warning','do you want to delete this record')

                if c == 'yes':
                    messagebox.showinfo('info','delete successfully')
                    cursor.execute("DELETE selling_table WHERE s_id=? AND sh_id=?",(self.sellId[0],self.shop_no[0]))
                    conn.commit()
            else:
                messagebox.showinfo("info","plz... select correct product")

    

    def printAndSave_btn(self,*args):
        messagebox.showinfo('info','print and save click')

    
    def exitbtn(self,*args):
        self.productframecount = 0
        self.productparentFrame.destroy()


   
#______________________________________________________________________________________________________________
'''================================================ MAIN LOOP =============================================='''
    
if __name__ == '__main__':
    root=Tk()
  
    #obj = splash(root)
    obj = SoldClass(root)
    root.mainloop
