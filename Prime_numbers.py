starting_number = input("Enter your start number: ")
ending_number = input("Enter your end number: ")
sn = int(starting_number)
en = int(ending_number) + 1

for i in range(sn, en):
    for j in range(2,i+1):
        if i == j:
            print(i)
        elif i % j == 0:
            break

        


