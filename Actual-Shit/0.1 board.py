print ("Enter 'q' to quit\n")

board = [
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 [" ", " ", " ", " ", " ", " ", " ", " "],
 ["R ", "N ", " ", " ", " ", " ", " ", " "]
]

F_Row = int(input("From Row : \n"))
F_Col = int(input("From Col : \n"))
board [F_Row-1] [F_Col-1] = "♚"

# Here replace F_Row and F_Col with "square_to_position.py" output values


print (board)


T_Row = int(input("To Row : \n"))
T_Col = int(input("To Col : \n"))
    
# Here replace T_Row and T_Col with "square_to_position.py" output values


def swapPOS(T_Row, T_Col) :
    board [T_Row-1][T_Col-1] = "♚"
    board [F_Row-1] [F_Col-1] = " "
    # print (board)


swapPOS(T_Row, T_Col)