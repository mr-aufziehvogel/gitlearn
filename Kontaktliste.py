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
    for _ in contactlist:
        print("\nID: " + str(i))
        print("Name: " + contactlist[i].name)
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
    if contactlist[id] != "":
        while True:
            which_edit = input("1. Name\n2. Mail\n3. Telefonnummer\n4.Adresse\n5. Zurück\nAuswahl: ")
            if which_edit == "1":
                while True:
                    id = input("Neuer Name? ")
                    if id != "":
                        contactlist[int(id)].name = id
                        break
            elif which_edit == "2":
                id = input("Neue Mail? ")
                if id != "":
                    contactlist[int(id)].mail = id
                    break
            elif which_edit == "3":
                id = input("Neue Telefonnummer? ")
                if id != "":
                    contactlist[int(id)].phone = id
                    break
            elif which_edit == "4":
                id = input("Neue Adresse? ")
                if id != "":
                    contactlist[int(id)].address = id
                    break
            elif which_edit == "5":
                pass
            break
    else:
        print("Dieser Kontakt existiert nicht.")


def delete():
    id = input("Welcher Kontakt(ID)? ")
    try:
        del contactlist[int(id)]
    except IndexError:
        print("Dieser Kontakt existiert nicht.")

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