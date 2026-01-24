from Square import Square 

class Piece :

    """REPRESENTS THE OVERALL SITUATION OF A PIECE IN TERMS OF IT'S COLOR, AND POSITION (VIZ. IN TERMS OF ROW, COL, AND COLOR)"""

    #   INITIALIZE THE PIECE IN TERMS OF ITS COLOR, POSITION, ETC.  
    def __init__ (self, row, col, color):
        self.row = row
        self.col = col
        self.color = color


    #   RETURN THE STATE (POSITION IN TERMS OF ROW & COLUMNS) OF THE PIECE
    def position(self, row, col):
        return self.row, self.col
    

    #   RETURN THE COLOR OF THE PIECE
    def color(self, color):
        return self.color

########################################################################

class Pawn (Piece):

    """Docstring for Pawn piece, which includes its position and color, and a method to get its legal moves based on the current board state."""

    #   INIT METHOD FOR INITIALIZING PAWN WITH SQUARE & IT'S SQUARE
    def __init__(self, square, color):
        self.square = square
        self.color = color

    #   GETTER METHOD TO GET / COMPUTE / CALCULATE POSSIBLE LEGAL MOVES
    def get_legal_moves(self, board):
        
        moves = []

        #   DEFINE THE DIRECTIONS BASED ON THE COLOR
        direction = -1 if self.color == "white" else 1
        row = self.square.row
        col = self.square.col

        #   COMPUTE STATE OF THE SQUARE AHEAD (EMPTY OR CONTAINS A PIECE) AND APPEND IT TO THE "MOVES" ARRAY
        one_forward = Square(row + direction, col)
        if board.get_piece(one_forward) is None:
            moves.append(one_forward)

            #   COMPUTE STATE OF TWOS SQUARES AHEAD IF & ONLY IF ONE_FORWARD_SQUARE IS VALID
            start_row = 6 if self.color == "white" else 1
            if row == start_row:
                two_forward = Square(row + 2 * direction, col)
                if board.get_piece(two_forward) is None:
                    moves.append(two_forward)

        #   COMPUTE THE DIRECTIONS POSSIBLE FOR PAWN
        for dc in (-1, 1):
            new_col = col + dc
            if 0 <= new_col < 8:
                target = Square(row + direction, new_col)
                piece = board.get_piece(target)
                if piece and piece.color != self.color:
                    moves.append(target)

        return moves


########################################################################

class Sliding_Piece (Piece): 
    
    """Sliding_Pieces, which represents pieces that can move multiple squares in straight lines (like Rooks, Bishops, and Queens)."""

    # CREATE AN EMPTY ARRAY / LIST NAMED DIRECTIONS TO LATER MANNUALY ASSIGN DIRECTIONS FOR EACH PIECE
    directions = []

    # JUST LIKE FOR PAWN, CREATE A METHOD NAMED GET_LEGAL_MOVES WITH BOARD AS INPUT PARAMETER TO COMPUTE POSSIBLE LEGAL MOVES 
    # FOR INDIVIDUAL PIECES (SELF.PIECE)
    def get_legal_moves (self, board) :

        # CREATE AN EMPTY ARRAY / LIST NAMED MOVES TO ADD THE POSSIBLE SET OF MOVES FOR EACH PIECE
        moves = []

        # LOOP AND ITERATE THROUGH EVERY POSSIBLE COMBINATION (ROW, COLUMN) FROM THE DIRECTIONS LIST
        for dr, dc in self.directions: 
            r = self.square.row + dr
            c = self.square.col + dc

        # LOOP (WHILE) AND APPEND MOVES IN THE MOVES LIST FOR THE REQUESTED DIRECTION (AND UPDATE THE ROWS AND COLUMNS BASED ON THE DIRECTIONS)
            while 0 <= r < 8 and 0 <= c < 8 :
                target = Square (r, c)
                piece = board.get_piece(target)

                if piece is None :
                    moves.append(target)
                else : 
                    if piece.color != self.color :
                        moves.append(target)
                    break
            
                r += dr
                c += dc

        return moves

########################################################################

class Rook (Sliding_Piece) :

    #   ASSIGNING DIRECTIONS FOR THE ROOK
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

########################################################################

class Bishop(Sliding_Piece):
    
    #   ASSIGNING DIRECTIONS FOR THE BISHOP
    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]

########################################################################

class Queen(Sliding_Piece):
    
    #   ASSIGNING DIRECTIONS TO QUEEN (ROOK + BISHOP)
    directions = [(1,1), (1,-1), (-1,1), (-1,-1), (1,0), (-1,0), (0,1), (0,-1)]

########################################################################

class Knight(Piece):
    offsets = [
        (2,1),(2,-1),(-2,1),(-2,-1),
        (1,2),(1,-2),(-1,2),(-1,-2)
    ]

    def get_legal_moves(self, board):
        moves = []
        for dr, dc in self.offsets:
            r = self.square.row + dr
            c = self.square.col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                target = Square(r, c)
                piece = board.get_piece(target)
                if piece is None or piece.color != self.color:
                    moves.append(target)
        return moves

########################################################################

class King(Piece):

    OFFSETS = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    def get_legal_moves(self, board):
        moves = []

        r = self.square.row
        c = self.square.col

        for dr, dc in self.OFFSETS:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < 8 and 0 <= nc < 8:
                target = Square(nr, nc)
                piece = board.get_piece(target)

                if piece is None or piece.color != self.color:
                    moves.append(target)

        return moves

########################################################################