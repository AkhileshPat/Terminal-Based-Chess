board = {"K" : "♔", "Q" : "♕", "R" : "♖", "B" : "♗", "N" : "♘", "P" : "♙", 
         "k" : "♚", "q" : "♛", "r" : "♜", "b" : "♝", "n" : "♞", "p" : "♟"}

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

printBOARD(board)
print ("\n\n")