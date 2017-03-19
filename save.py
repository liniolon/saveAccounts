#!/usr/bin/python3 
"""
programmer : Amir Kouhkan 
website : www.amirkouhkan.ir
E-mail : amirkouhkan1@gmail.com 

This script it's so biegner, you can developed it and make it most usefull :D
"""
import sqlite3

def createDatabase():
    global db
    db = sqlite3.connect('save.db')
    print("Database is created successfully")
    db.close()

def createTable():
    #createDatabase()
    #con = db.connect('save.db')
    db = sqlite3.connect('save.db')
    print("Connected to the database...")
    db.execute('create table tbl_save(id int primary key, username text, password text, website text)')
    print("Table is created successfully")
    db.close()

def insertAccounts():
#     createDatabase()
    db = sqlite3.connect('save.db')
    # con = db.connect('save.db')
    print("Connected to database ...")
    # cursor = con.cursor()
    ID = int(input("Enter an id for this account: "))
    username = input("Enter username of this account: ")
    password = input("Enter password of this account: ")
    website = input("Enter websites account: ")
    db.execute('insert into tbl_save (id,username,password,website) values (?,?,?,?)',(ID,username,password,website))
    db.commit()
    print("The account's information is added successfully")
    db.close()

def deleteAccount():
    db = sqlite3.connect('save.db')
    #createDatabase()
    #con  = db.connect('save.db')
    ID = int(input("Enter an ID for delete account: "))
    db.execute('delete from tbl_save where id={0}'.format(ID))
    db.commit()
    print("The account information is deleted successfully")
    db.close()

def updateAccount():
    db = sqlite3.connect('save.db')
    #createDatabase()
    #con = db.connect('save.db')
    ID = int(input("Enter an id for update account information: "))
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    website = input("Enter new website")
    db.execute('update tbl_save set username="{1}",password="{2}",website="{3}" where id={0}'.format(ID,username,password,website))
    db.commit()
    print("The account information is updated")
    db.close()

def showAccount():
    db = sqlite3.connect('save.db')
    #createDatabase()
    #con = db.connect('save.db')
    row = db.execute('select * from tbl_save')
    #row.fetchall()
    for rows in row:
        print(rows)
    db.close()

def searchAccount():
    try:
        db =sqlite3.connect('save.db')
        set_type = input("Enter type of search by name or ID: (name,id)")
        if(set_type == "id" or set_type=="ID"):
            ID  = int(input("Enter an id for search: "))
            search = db.execute('select * from tbl_save where id ={0}'.format(ID))
            for i in search:
                print(i)
        elif(set_type == "name" or set_type == " NAME"):
            name = input("Enter name of website: ")
            search = db.execute('select * from tbl_save where website = "{0}"'.format(name))
            for i in search:
                print(i)
        db.close()
    except:
        print("The value is not founded")

def main():
    print('''Welcome To Save Account Information Application

If you use for first time you must be create the database. 
    1. Create Database
    2. Create Table 
    3. Insert a account
    4. Delete a account
    5. Update a account 
    6. Show Accounts
    7. Search in Database
    8. Exit''')
    key_number = int(input("Enter number: "))
    while True:
        if key_number == 1:
            createDatabase()
            key_number = int(input("Do you want to continue?(1-7 / 8)"))
        elif key_number == 2:
            createTable()
            key_number = int(input("Do you want to continue?(1-7 / 8)")) 
        elif key_number == 3:
            insertAccounts()
            key_number = int(input("Do you want to continue?(1-7 / 8)"))
        elif key_number == 4:
            deleteAccount()
            key_number = int(input("Do you want to continue?(1-7 / 8)"))
        elif key_number == 5:
            updateAccount()
            key_number = int(input("Do you want to continue?(1-7 / 8)"))
        elif key_number == 6:
            showAccount()
            key_number = int(input("Do you want to continue?(1-7 / 8)"))
        elif key_number == 7:
            searchAccount()
            key_number = int(input("Do you want to continue?(1-7 / 8)"))
        elif key_number == 8:
            break

if __name__=="__main__":
    main()

