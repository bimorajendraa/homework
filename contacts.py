import sqlite3

connect = sqlite3.connect("contactsdb.db")
cursor = connect.cursor()

name = input("Name: ")
phone = input("Phone: ")
address = input("Address: ")

insert_contact = "INSERT INTO contacts(name, phone, address) VALUES ('{0}',{1},'{2}')"

cursor.execute(insert_contact.format(name,phone,address))

connect.commit()

