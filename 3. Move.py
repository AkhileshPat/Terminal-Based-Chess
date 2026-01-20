class Move :
    def __init__ (self, from_sq, to_sq) :
        if from_sq == " " :
            return print("Invalid Move (Square Contains No Piece)")
        self.from_square = from_sq
        self.to_square = to_sq
    
    #   TAKES TWO SQUARES AS AN INPUT, SWITCHES THEM
    def move (self, from_sq, to_sq, board) :
        self.to_square = from_sq
        self.from_square = " "
        board[to_sq] = board[from_sq]
        board[from_sq] = " "
        return (board[to_sq], board[from_sq])