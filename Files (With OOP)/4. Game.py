import itertools

from Board import board

from Square import square
class Game : 

    def __init__(self, board, turn) :

        self.board = board

        self.turn = turn

        return True
            
    def player_turns(self) :

        self.turn
        
        if self.turn == "white" :
            self.turn = "black"
        
        else :
            self.turn = "white"

        return self.turn

    def in_check (self, color) :
        print()



# ---------------------------------------------------------------------------------


# 2.] Toggle the color (Of the pieces)
# 1.] Get the squares (of attack) for a piece from a position
# 3.] If king lies in the squares => Check else Pass


# ---------------------------------------------------------------------------------


# Now you need to work out if (0, 2) is in check. 
# The way I would do this is work out for each type of piece, 
# where one could be, to put this position in check. 
# You could store this as a list of differences from the current king location, 
# and for each of those you check if the thing 
# that's in them is the piece that can cause check.


# ---------------------------------------------------------------------------------


# movements = {
#     "P": [(1,-1), (1,1)],
#     "R": [*[(0, i), (0, -i), (i, 0), (-i, 0)] for i in range(7)],
# }


# ---------------------------------------------------------------------------------


# Here are movements for a pawn and rook. 
# If there is a pawn on (0, 2)+(1, 1) or (0, 2)+(1,-1)
# and those positions are inside the grid, the pawn is checking (0, 2).


# ---------------------------------------------------------------------------------


# I think you are making this more complicated than it is. Here are the steps I would use:
# Find the king positions.
# Loop through all 8 directions from that location in a nested loop.
# When you reach a white piece (uppercase letter), break that direction.
# When you reach end of board, break that direction.
# If you reach a black piece (lowercase) you have 4 options to check:
# a. Piece is orthogonally from king and is a rook
# b. Piece is diagonally from king and is a bishop
# c. Piece is 1 square away diagonally from king and is a pawn
# d. Any direction and piece is a queen
# If any of a-d is True, then return True (king is in check). If the entire loop ends, return False.
# If you need I can give you the code for my checker.


# ---------------------------------------------------------------------------------