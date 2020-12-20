from os import system, name 
import mariadb
import sys

contactlist = []
# database connection code
try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="python_db"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
# database connection cursor
cursor = conn.cursor()

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

class Contacts:
    def __init__(self, name, mail, phone, address):
        self.name = name
        self.mail = mail
        self.phone = phone
        self.address = address

def show():
    cursor.execute("SELECT * FROM employees")
    myresult = cursor.fetchall()
    print(myresult)
    i = 0
    # for _ in contactlist:
    #     print("\nID: " + str(i))
    #     print("Name: " + contactlist[i].name)
    #     print("Mail: " + contactlist[i].mail)
    #     print("Telefon: " + contactlist[i].phone)
    #     print("Adresse: " + contactlist[i].address)
    #     i += 1

def create():
    name = input("Name? ")
    mail = input("Mail? ")
    while True:
        phone = input("Telefonnummer? ")
        if phone.isnumeric() == True:
            break
    address = input("Adresse? ")
    clear()
    contactlist.append(Contacts(name,mail,phone,address))
    print("Name: " + contactlist[-1].name)
    print("Mail: " + contactlist[-1].mail)
    print("Telefon: " + contactlist[-1].phone)
    print("Adresse: " + contactlist[-1].address + "\n")
    try:
        cursor.execute(
            "INSERT INTO employees (name,email,telephone,address) VALUES (?, ?, ?, ?)", 
        (name, mail, phone, address))
    except mariadb.Error as e:
        print(f"Error: {e}")
    conn.commit() 

def edit():
    id = input("Welchen Kontakt bearbeiten? ")
    print("\nName: " + contactlist[-1].name)
    print("Mail: " + contactlist[-1].mail)
    print("Telefon: " + contactlist[-1].phone)
    print("Adresse: " + contactlist[-1].address + "\n")
    if contactlist[int(id)] != "":
        while True:
            which_edit = input("1. Name\n2. Mail\n3. Telefonnummer\n4.Adresse\n5. Zurück\nAuswahl: ")
            if which_edit == "1":
                while True:
                    id_name = input("Neuer Name? ")
                    if id_name != "":
                        contactlist[int(id)].name = id_name
                        break
            elif which_edit == "2":
                while True:
                    id_mail = input("Neue Mail? ")
                    if id_mail != "":
                        contactlist[int(id)].mail = id_mail
                        break
            elif which_edit == "3":
                while True:
                    id_phone = input("Neue Telefonnummer? ")
                    if id_phone != "":
                        contactlist[int(id)].phone = id_phone
                        break
            elif which_edit == "4":
                while True:
                    id_address = input("Neue Adresse? ")
                    if id_address != "":
                        contactlist[int(id)].address = id_address
                        break
            elif which_edit == "5":
                pass
            break
    else:
        print("Dieser Kontakt existiert nicht.")


def delete():
    dn = input("Welcher name? ")
    try:
        cursor.execute(
            "DELETE FROM employees WHERE name = ?", (deletename, )
        )
    except mariadb.Error as e:
        print(f"Error: {e}")
    conn.commit() 
while True:
    print("\n1. Anzeigen")
    print("2. Erstellen")
    print("3. Bearbeiten")
    print("4. Löschen")
    print("5. Beenden")
    choice = input("Was möchtest du tun? ")
    if choice == "1":
        show()
    elif choice == "2":
        create()
    elif choice == "3":
        edit()
    elif choice == "4":
        delete()
    elif choice == "5":
        exit()