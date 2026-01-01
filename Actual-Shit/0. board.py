print ("Enter 'q' to quit\n")

board = [
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "]
]

F_Row = int(input("From Row : \n"))
F_Col = int(input("From Col : \n"))
board [F_Row-1] [F_Col-1] = "♚"


print (board)


T_Row = int(input("To Row : \n"))
T_Col = int(input("To Col : \n"))
    

def swapPOS(T_Row, T_Col) :
    board [T_Row-1][T_Col-1] = "♚"
    board [F_Row-1] [F_Col-1] = " "
    print (board)


swapPOS(T_Row, T_Col)