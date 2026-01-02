def printBOARD(board) :
    for number in range (1, 9) :
        print ("---"*11, end = "\n")
        for letter in range (1, 9) :
            if letter == 8 :
                print (f"|   ", end="|")
            else :
                print (f"|   ", end="")
        print ()
    print ("---"*11)

printBOARD()

print ("\n\n")