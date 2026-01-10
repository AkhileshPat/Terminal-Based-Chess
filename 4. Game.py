class Game : 

    def __init__(self, board, aes_board) :
        self.board = [[None for _ in range (8)] for _ in range (8)]
        self.aes_board = {"K" : "♔", "Q" : "♕", "R" : "♖", "B" : "♗", "N" : "♘", "P" : "♙", 
         "k" : "♚", "q" : "♛", "r" : "♜", "b" : "♝", "n" : "♞", "p" : "♟"}
        for number in range (1, 9) :
            print ("---"*11, end = "\n")
            for letter in range (1, 9) :
                if letter == 8 :
                    print (f"|   ", end="|")
                else :
                    print (f"|   ", end="")
        print ()
        print ("---"*11)

    def misc(self, board, turn, color, piece) :
        self.board = board
        self.turn = turn
        self.color = color
        self.piece = piece
        turn = 1 if piece.color == "white" else 0
                        
        return board, turn, color, piece

    # while __init__().turn == 1 :

PrintBoard = Game(board, aes_board)