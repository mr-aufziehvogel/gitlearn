from os import system, name 

contactlist = []

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
    pass

def create():
    name = input("Name? ")
    mail = input("Mail? ")
    phone = input("Telefonnummer? ")
    address = input("Adresse? ")
    contactlist.append(Contacts(name,mail,phone,address))
    clear()
    print("Name: " + contactlist[-1].name)
    print("Mail: " + contactlist[-1].mail)
    print("Telefon: " + contactlist[-1].phone)
    print("Adresse: " + contactlist[-1].number)

def edit():
    pass

def delete():
    pass

while True:
    print("1. Anzeigen")
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