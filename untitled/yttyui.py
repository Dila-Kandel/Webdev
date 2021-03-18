from tkinter import*
import sqlite3
import tkinter.messagebox

class product:
    def __init__(self, root):
        p=Database()
        p.conn()
        self.root=root
        self.root.title('sell and purchases')
        self.root.geometry('1325x690')
        self.root.config(bg='yellow')

        global pd



        PId=StringVar()
        PName=StringVar()
        PQty=StringVar()
        PPrice=StringVar()
        PContact=StringVar()
        PCompany=StringVar()

        def close():
            print('Product: close method is called')
            close = tkinter.messagebox.askyesno('WAREHOUSE INVENTORY SYSTEM',
                                                'really ..... want to close the inventory ')
            if close > 0:
                root.destroy()
                return

        def clear():
            self.textPID.delete(0, END)
            self.textPPrice.delete(0, END)
            self.textPCompany.delete(0, END)
            self.textPName.delete(0, END)
            self.textPContact.delete(0, END)
            self.textPQTY.delete(0, END)

        def Inserts():
            if (len(PId.get()) != 0):
                p.insert(PId.get(), PName.get(), PPrice.get(), PCompany.get(), PQty.get(), PContact.get())
                productList.delete(0, END)
                productList.insert(END, PId.get(), PName.get(), PPrice.get(), PCompany.get(), PQty.get(),
                                   PContact.get())
                showinproductlist()
            else:
                tkinter.messagebox.askyesno('WARE HOUSE INVENTORY', 'Really...... do you enter PId')
            return

        def showinproductlist():
            productList.delete(0, END)
            for row in p.show():
                productList.insert(END, row, str(' '))

        def productRec():

            searchPd = productList.curselection()[0]
            pd = productList.get(searchPd)

            self.textPID.delete(0, END)
            self.textPID.insert(END, pd[0])

            self.textPQTY.delete(0, END)
            self.textPQTY.insert(End, pd[4])

            self.textPName.delete(0, END)
            self.textPName.insert(End, pd[1])
            self.textPPrice.delete(0, END)
            self.textPPrice.insert(End, pd[2])
            self.textPContact.delete(0, END)
            self.textPContact.insert(End, pd[5])
            self.textPCompany.delete(0, END)
            self.textPCompany.insert(End, pd[3])

        def delete():
            if (len(PId.get()) != 0):
                p.delete(pd[0])
                clear()
                showinproductlist()

        def search():
            productList.delete(0, END)
            for row in p.search(PId.get(), PName.get(), PPrice.get(), PCompany.get(), PQty.get(), PContact.get()):
                productList.insert(END, row, str(' '))

        def update():
            if (len(PId.get()) != 0):
                p.delete(pd[0])
                p.insert(PId.get(), PName.get(), PPrice.get(), PCompany.get(), PQty.get(), PContact.get())
                productList.delete(0, END)
                productList.insert(END, PId.get(), PName.get(), PPrice.get(), PCompany.get(), PQty.get(),
                                   PContact.get())
        mainFrame=Frame(self.root,bg='red')
        mainFrame.grid()
        headFrame=Frame(mainFrame, bd=10,padx=10,pady=50,bg='blue',relief= RIDGE)
        headFrame.pack(side=TOP)
        self.Itite=Label(headFrame,font=('arial',30,'bold'),text='कन्डेल उत्पादन ',bg='white')
        self.Itite.grid()
        operatinFrame=Frame(mainFrame,bd=1,width=1300,height=60,padx=20,pady=20,bg='white',relief=RIDGE)
        operatinFrame.pack(side=BOTTOM)
        bodyFrame=Frame(mainFrame,bd=2,width=1290,height=400,padx=30,pady=20,bg='white',relief=RIDGE)
        bodyFrame.pack(side=BOTTOM)
        leftBody=LabelFrame(bodyFrame,bd=2,padx=10,pady=10,bg='yellow',width=600,
                                height=380,font=('arial',10,'bold'),text='product items details')
        leftBody.pack(side=LEFT)
        rightBody = LabelFrame(bodyFrame, bd=2, padx=10, pady=10, bg='yellow', width=300,
                              height=380, font=('arial', 10, 'bold'), text='product information')
        rightBody.pack(side=RIGHT)
        self.lebelPID=Label(leftBody,font=('arial',15,'bold'),text='product Id:',padx=2,pady=2,bg='white',fg='blue')
        self.lebelPID.grid(row=0,column=0,sticky=W)
        self.textPID=Entry(leftBody,font=('arial',20,'bold'),textvariable=PId,width=35)
        self.textPID.grid(row=0, column=1, sticky=W)


        self.lebelPName = Label(leftBody, font=('arial', 15, 'bold'), text='product Name:', padx=2, pady=2, bg='white',
                              fg='blue')
        self.lebelPName.grid(row=1, column=0, sticky=W)
        self.textPName = Entry(leftBody, font=('arial', 20, 'bold'), textvariable=PName, width=35)
        self.textPName.grid(row=1, column=1, sticky=W)

        self.lebelPPrice= Label(leftBody, font=('arial', 15, 'bold'), text='product Price:', padx=2, pady=2, bg='white',
                              fg='blue')
        self.lebelPPrice.grid(row=2, column=0, sticky=W)
        self.textPPrice = Entry(leftBody, font=('arial', 20, 'bold'), textvariable=PPrice, width=35)
        self.textPPrice.grid(row=2, column=1, sticky=W)

        self.lebelPCompany = Label(leftBody, font=('arial', 15, 'bold'), text='Mgf. Company:', padx=2, pady=2, bg='white',
                              fg='blue')
        self.lebelPCompany.grid(row=3, column=0, sticky=W)
        self.textPCompany = Entry(leftBody, font=('arial', 20, 'bold'), textvariable=PCompany, width=35)
        self.textPCompany.grid(row=3, column=1, sticky=W)

        self.lebelPQTY = Label(leftBody, font=('arial', 15, 'bold'), text='product qt:', padx=2, pady=2, bg='white',
                              fg='blue')
        self.lebelPQTY.grid(row=4, column=0, sticky=W)
        self.textPQTY = Entry(leftBody, font=('arial', 20, 'bold'), textvariable=PQty, width=35)
        self.textPQTY.grid(row=4, column=1, sticky=W)


        self.lebelPContact = Label(leftBody, font=('arial', 15, 'bold'), text='Company contact:', padx=2, pady=2, bg='white',
                              fg='blue')
        self.lebelPContact.grid(row=5, column=0, sticky=W)
        self.textPContact = Entry(leftBody, font=('arial', 20, 'bold'), textvariable=PContact, width=35)
        self.textPContact.grid(row=5, column=1, sticky=W)

        scroll= Scrollbar(rightBody)
        scroll.grid(row=0,column=1,sticky='ns')
        productList=Listbox(rightBody,width=40,height=16,font=('arial',10,'bold'),yscrollcommand=scroll.set)
        productList.bind('<<ListboxSelect>>',productRec)
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)

        self.ButtonSave=Button(operatinFrame,text='Save',font=('arial',20,'bold'),height=1,width=10,bd=4,command=Inserts)
        self.ButtonSave.grid(row=0,column=0)

        self.ButtonShow = Button(operatinFrame, text='Show Data', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=showinproductlist)
        self.ButtonShow.grid(row=0, column=1)

        self.ButtonSearch = Button(operatinFrame, text='Search', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=search)
        self.ButtonSearch.grid(row=0, column=2)

        self.ButtonUpdate = Button(operatinFrame, text='Update', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=update)
        self.ButtonUpdate.grid(row=0, column=3)

        self.ButtonReset=Button(operatinFrame,text='Reset',font=('arial',20,'bold'),height=1,width=10,bd=4,command=clear)
        self.ButtonReset.grid(row=0,column=4)

        self.ButtonClose = Button(operatinFrame, text='Close', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=close)
        self.ButtonClose.grid(row=0, column=5)

        self.ButtonDelete = Button(operatinFrame, text='Delete', font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=delete)
        self.ButtonDelete.grid(row=0, column=6)


class Database:
    def conn(self):
        print('Database: connection method is called \n')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        query='CREATE TABLE if not exists product(id integer primary key,pid text,pname text,price text, qty text,company text,contact text)'
        cur.execute(query)
        con.commit()
        con.close()
        print('connection: method is finished \n ')

    def insert(self,pid,name, price, company, qty,contact ):
        print('Database: insert method is called \n')
        con = sqlite3.connect('inventory.db')
        cur = con.cursor()
        query='INSERT into product VALUES(?,?,?,?,?,?)'
        cur.execute(query,(pid,name, price, company, qty,contact))
        con.commit()
        con.close()
        print('database: insert method is finished \n ')
    def show(self):
        print('Database: show method is called \n')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        query='select * from product'
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print('Database: show method is finished \n')
        return rows
    def delete(self,pid):
        print('Database: delete method is called ')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute('delete from product where pid=?',(pid,))
        con.commit()
        con.close()
        print('Database: delete method is finished')

    def search(self,pid='',name='', price='', qty='', company='',contact=''):
        print('Database: search method is called')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute('select * from product where pid=? or pname=? or price=? or qty=? or company=? or contact=?',(pid,name, price, qty, company,contact))
        rows=cur.fetchall()
        con.close()
        print('Database: search menthod is finished \n')
        return rows
    def update(self,pid='',name='', price='', qty='', company='',contact=''):
        print('Database: update method is clled \n')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute('update product set where pid=?or pname=? or price=? or qty=? or company=? or contact=?',(pid,name, price, qty, company,contact))
        con.commit()
        con.close()
        print("Database : uptate method is finished \n")




if __name__ == "__main__":
    root = Tk()
    application = product(root)
    root.mainloop()