def random_word():
    import random 
    lines = open(r"C:\Users\haseebshahdin\Desktop\Python\3letterwords.txt").readlines() 
    word = random.choice(lines)
    return word


def length():
    return len(random_word())

the_word = random_word()

splitted_word = list(the_word)
splitted_word.remove('\n')
splitted_word = ['A', 'A', 'B']
print (the_word)
print (splitted_word)
h = ['','','']
i = 0
print (h)
once_correct1 = False
once_correct2 = False
once_correct3 = False
while i < 6:
    if h == splitted_word:
        print('You win')
        break    
    elif i == 6:
        print ('you lose')
        break
        
    for x in splitted_word:
        guess = input("Input a guess:")
        print (x)
        if i == 6:
           
            break
        elif h == splitted_word:
            
            break    
        elif guess == splitted_word[0]:
            if once_correct1 == False:
                h[0]= guess
            else:
                pass
           
        
    
        elif guess == splitted_word[1]:
            if once_correct2 == False:
                h[1] = guess
            else:
                pass    
            
       
        elif guess == splitted_word[2]:
            if once_correct3 == False:
                h[2] = guess
            else:
                pass  
            

        elif guess != splitted_word[2] or splitted_word[1] or guess != splitted_word[0]:  
            print ('try again') 
        i = i + 1
        print (i)
        print (len(h))
        print (h)
        
        

