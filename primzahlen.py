limit = input("Which range? ")
for i in range(int(limit)+1):
    for j in range(2,int(limit)+1):
        if i == j:
            print(i)
            continue
        elif i % j == 0:
            break
        elif i % j != 0:
            pass

# number = input("welche zahl?")
# number = int(number)
# for i in range(0,number):
#     for teiler in range(2, i):
#         if i == number:
#             print(number)
#         elif number % i != 0:
#             continue
#         else:
#             break