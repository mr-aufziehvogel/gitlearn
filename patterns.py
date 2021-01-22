rows = 20
n = []
nminus1 = [1]
for row in range(0, rows+2):
    for column in range(0,row+1):
        if column == 0 or column == row:
            n.append(1)
        else:
            n.append(nminus1[column-1] + nminus1[column])
    print(*n)
    nminus1 = n
    n = []
