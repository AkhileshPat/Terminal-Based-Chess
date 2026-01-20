class Board :

    """DEFINE A BOARD WHICH CONTAINS AN 8×8 GRID, AND METHODS LIKE "GET PIECE" (TO GET INFO ABOUT IT'S POSITION ON THE 8×8 GRID), "MOVE THE PIECE" (WHICH TAKES MOVE AS AN INPUT, AND MOVE FURTHER WILL HAVE TWO COMPONENTS VIZ, THE ROW & COLUMN)"""""

    #   METHOD TO INITIALIZE
    #   CREATE A 2D LIST TO STORE THE MOVES, OTHER COMPONENTS OF A BOARD (VIZ. PIECES INFO, STRUCTURE TO MAKE A MOVE)
    #    board = [   [" "*8 for _ in range (8)]*8]
    def __init__ (self) :
        self.board = [
            ["bR", "bKN", "bB", "bQ", "bK", "bB", "bKN", "bR"],     #8
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],       #7
            [" ", " ", " ", " ", " ", " ", " ", " "],               #6
            [" ", " ", " ", " ", " ", " ", " ", " "],               #5
            [" ", " ", " ", " ", " ", " ", " ", " "],               #4
            [" ", " ", " ", " ", " ", " ", " ", " "],               #3
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],       #2
            ["wR", "wKN", "wB", "wQ", "wK", "wB", "wKN", "wR"]]     #1

    #   METHOD THAT TAKES 3 INPUT (ROW, COL) TO LOCATE THE PIECE
    def get_piece (self, row, col) :
        return self.board[row][col]
    
    def set_piece (self, row, col, piece) :
        self.board[row][col] = piece

    #   METHOD THAT TAKES 4 INPUT (FROM_ROW, FROM_COL, TO_ROW, TO_COL)
    def move (self, from_row, from_col, to_row, to_col) :
        piece = self.get_piece(from_row, from_col)
        if piece == " " :
            return False
        else : 
            self.set_piece(to_row, to_col)
            self.set_piece(from_row, from_col) = ""
            return True
        
board = Board ()

print (board)