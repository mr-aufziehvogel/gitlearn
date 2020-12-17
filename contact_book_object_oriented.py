contact_list = []
class Contactbook:
    def __init__(self, name, address, email, telephonenumber):
        self.name = name
        self.address = address
        self.email = email
        self.telephonenumber = telephonenumber

def adddetails():
    name = input("Enter name: ")
    address = input("Enter address: ")
    email = input("Enter email: ")
    telephonenumber = input("Enter number: ")
    contact_list.append(Contactbook(name, address, email, telephonenumber))

def what_do_you_want_to_do():
    print ("To add contact press 1")
    print ("To edit contact press 2")
    print ("To delete contact press 3")
    print ("To end press 4")
    print ("To show contact press 5")

def delete_contact():
    id = input("Enter contact id you want to delete: ")
    
    try:
        del contact_list[int(id)]
        print ("The contact " + id + " is deleted")
    except IndexError:
        print("This id does not exist")

def show():
    i = 0
    for x in contact_list:
        print (contact_list[i].name)
        print (contact_list[i].address)
        print (contact_list[i].email)
        print (contact_list[i].telephonenumber)
        print ("Contact id is  %d" %i)
        i += 1

def edit_contact():

while True:    
    what_do_you_want_to_do()
    choice = input("Enter your choice: ")
    if choice == "1":
        adddetails()
    elif choice == "5":
        show()
    elif choice == "3":
        delete_contact()    
    elif choice == "4":
        print("You chose to end the program")
        break
        



