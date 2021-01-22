# for rows in range(0,20):
#     print("*" * rows)
# for rows in range(20,0,-1):
#     print("*" * rows)


# i = 0
# for rows in range(20):
#     print(*range(0,i))
#     i += 1

# liste = []
# i = 0
# for rows in range(10):
#     for _ in range(i,i+rows):
#         i += 1
#         liste.append(i)
#     print(''.join(str(liste)).strip('[]').replace(", "," "))
#     liste = []

# liste = []
# i = 1
# for rows in range(10):
#     for _ in range(i,i+rows):
#         i += 1
#         liste.append(i)
#     for _ in range(i+rows,i,-1):
#         print(_-2, end=" ")
# #    print(''.join(str(liste)).strip('[]').replace(", "," "))
#     print("")
#     liste = []

# for row in range(1,6):
#     for _ in range(1,row+1):
#         print(_, end = " ")
#     print(" ")

# for row in range(1,7):
#     for _ in range(1,7,1):
#         for a in range(7-_,1,-1):
#             print(_, end = " ")
#         print(" ")

# z = 5
# for row in range(z):
#     for desc in range(z-row,0,-1):
#         print(z, end = " ")
#     print(" ")

# z = 5
# for row in range(z):
#     for desc in range(z-row,0,-1):
#         print(z-row, end = " ")
#     print(" ")

# z = 5
# for row in range(z,0,-1):
#     for desc in range(0,row,1):
#         print(desc, end = " ")
#     print(" ")

# z = 5
# for row in range(z,0,-1):
#     for desc in range(row,0,-1):    
#         print(desc, end = " ")
#     print(" ")

# z = 8
# for row in range(0,z):
#     for col in range(0,row):
#         print(col*row, end=" ")
#     print(" ")

# z = 8
# for row in range(1,z):
#     for col in range(row,z):
#         print(col, end=" ")
#     print(" ")

# z = 8
# for row in range(1,z):
#     for col in range(row,z):
#         print(col, end=" ")
#     print(" ")

# z = 6
# i = 0
# for row in range(0,z):
#     for col in range(z-1,0,-1):
#         if col >= row+1:
#             print(col, end=" ")
#         else:
#             print(" ", end=" ")
#     for col in range(1,z):
#         if col >= row+1:
#             print(col, end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# z = 6
# i = 0
# for row in range(0,z):
#     for col in range(z-1,row,-1):
#         print(col, end=" ")
#     for col in range(0,row):
#         print("   ", end=" ")
#     for col in range(row+1,z):
#         print(col, end=" ")
#     print("")

# for row in range(0,10,1):
#     for col in range(0,row):
#         print(row*2-1, end=" ")
#     print(" ")


# for row in range(1,6):
#     for _ in range(row-1):
#         print(row, end=" ")
#     for _ in range(row,6):
#         print(_, end=" ")
#     print(" ")

list = []
for row in range(1,6):
    for _ in range(1,row+1):
        # print(_, end=" ")
        list.append(_)
    txt = str(list)[1:-1]
    print("{:>10}".format(txt. replace(',', '')))
    list = []
    # print(" ")

# z = 5
# for row in range(0,z):
#     for desc in range(row,0,-1):    
#         print(2 ** (desc-1), end = " ")
#     print(" ")

# z = 8
# for row in range(0,z):
#     for _ in range(1,row):
#         print(_, end=" ")
#     for _ in range(row-2,0,-1):
#         print(_, end=" ")
#     print(" ")

# z = 8
# for row in range(0,z):
#     for _ in range(0,row):
#         print(2 ** _, end=" ")
#     for _ in range(row-2,0-1,-1):
#         print(2 ** _, end=" ")
#     print(" ")

# z = 6
# i = 1
# for row in range(0,z):
#     for col in range(row*2-1):
#         print(i,end=" ")
#         i += 1
#     print(" ")

# z = 6
# i = 1
# for row in range(0,z):
#     for col in range(row):
#         print(i,end=" ")
#         i += 1
#     print(" ")

# z = 5
# for row in range(0,z):
#     for col in range(z,z-row-1,-1):
#         print(2 * col, end=" ")
#     print(" ")


# i=0
# for row in range(1,10):
#     c = -1
#     for _ in range(i+row+c,i,-1):
#         c -= 2
#         i += 1
#         print(_, end=" ")
#     print("")


# liste = []
# rows = 1
# i = 0
# end = 1
# while rows < 10:
#     while i < end:
#         i += 1
#         liste.append(i)
#     print(''.join(str(liste)).strip('[]').replace(", "," "))
#     liste = []
#     rows += 1
#     end = i + rows