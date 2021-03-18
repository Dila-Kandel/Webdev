from tkinter import*
import sqlite3
import tkinter.messagebox
from yttyui import*
class ultis():
    def close():
        print('Product: close method is called')
        close = tkinter.messagebox.askyesno('WAREHOUSE INVENTORY SYSTEM', 'really ..... want to close the inventory ')
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
            productList.insert(END, PId.get(), PName.get(), PPrice.get(), PCompany.get(), PQty.get(), PContact.get())
            showinproductlist()
        else:
            tkinter.messagebox.askyesno('WARE HOUSE INVENTORY', 'Really...... do you enter PId')
        return


    def showinproductlist():
        productList.delete(0, END)
        for row in p.show():
            productList.insert(END, row, str(' '))


    def productRec():
        global pd
        searchPd = productList.curselection()[0]
        pd = productList.get(searchPd)

        self.textPID.delete(0, END)
        self.textPID.insert(End, pd[0])

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
            productList.insert(END, PId.get(), PName.get(), PPrice.get(), PCompany.get(), PQty.get(), PContact.get())
