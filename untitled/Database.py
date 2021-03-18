from tkinter import*
import sqlite3
import tkinter.messagebox
from ultis import*
class Database:
    def conn(self):
        print('Database: connection method is called \n')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        query='CREATE TABLE if not exists product(pid integer primary key,pname text,price text, qty text,company text,contact text)'
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
        pritnt('Database: search method is called')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute('slect * from product where pid=? or name=? or price=? or qty=? or company=? or \
                     contact=?',(pid,name, price, qty, company,contact))
        rows=cur.fetchall()
        con.close()
        print('Database: search menthod is finished \n')
        return rows
    def update(self,pid='',name='', price='', qty='', company='',contact=''):
        print('Database: update method is clled \n')
        con=sqlite3.connect('inventory.db')
        cur=con.cursor()
        cur.execute('update product set where pid=?or name=? or price=? or qty=? or company=? or \
                     contact=?',(pid,name, price, qty, company,contact))
        con.commit()
        con.close()
        print("Database : uptate method is finished \n")
