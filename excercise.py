import random
zufallszahl = random.randrange(0,100)
while True: 
    input_zahl= int(input("Gib eine Zahl zwischen 0 und 100 ein."))
    print(zufallszahl)
    if input_zahl == zufallszahl:
        print("Richtig!")
        break
    else:
        eindrittel = random.randrange(3)
        if eindrittel == 0:
            if input_zahl < zufallszahl:
                print("Zufallszahl ist größer")
            else: 
                print("Zufallszahl ist kleiner")
        elif eindrittel == 1:
            if zufallszahl % input_zahl == 0:
                print("Zufallszahl teilbar durch Inputzahl")
            else:
                print("Zufallszahl nicht teilbar durch Inputzahl")
        else:
            if input_zahl % zufallszahl == 0:
                print("Zufallszahl Vielfaches von Inputzahl")
            else:
                print("Zufallszahl kein Vielfaches von Inputzahl")
            