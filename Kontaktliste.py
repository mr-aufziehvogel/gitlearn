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
    i = 0
    for cons in contactlist:
        print("ID: " + i)
        print("\nName: " + contactlist[i].name)
        print("Mail: " + contactlist[i].mail)
        print("Telefon: " + contactlist[i].phone)
        print("Adresse: " + contactlist[i].address)
        i += 1

def create():
    name = input("Name? ")
    mail = input("Mail? ")
    phone = input("Telefonnummer? ")
    address = input("Adresse? ")
    clear()
    contactlist.append(Contacts(name,mail,phone,address))
    print("Name: " + contactlist[-1].name)
    print("Mail: " + contactlist[-1].mail)
    print("Telefon: " + contactlist[-1].phone)
    print("Adresse: " + contactlist[-1].address + "\n")

def edit():
    id = input("Welchen Kontakt bearbeiten? ")
    print("\nName: " + contactlist[-1].name)
    print("Mail: " + contactlist[-1].mail)
    print("Telefon: " + contactlist[-1].phone)
    print("Adresse: " + contactlist[-1].address + "\n")
    while True:
        which_edit = input("1. Name\n2. Mail\n3. Telefonnummer\n4.Adresse\n")
        if which_edit == "1"
            input = ("Neuer Name? ")
            contactlist[id].name = input
        elif which_edit == "2"
            contactlist[id].mail = input
        elif which_edit == "3"
            input = ("Neue Telefonnummer? ")
            contactlist[id].number = input
        elif which_edit == "4"
            input = ("Neue Adresse? ")
            contactlist[id].address = input


def delete():
    pass

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