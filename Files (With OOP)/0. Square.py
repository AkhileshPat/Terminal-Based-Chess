class Square :

    """REPRESENTS THE OVERALLL SQUARE OF THE BOARD (VIZ. IN TERMS OF ROW & COL)"""

    #   INITIALIZE THE POSITION (VIZ. ROW & COL)
    def __init__(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8) :
            raise ValueError ("Index Out Of Bound")
        self.row = row
        self.col = col

    #   REPRESENT A SQUARE 
    @staticmethod
    def from_algebraic (notation) :
        file = ord(notation[0].lower()) - ord('a')
        rank = 8 - int(notation[1])
        return Square(rank, file)
    
    def __eq__(self, other):
        return isinstance(other, Square) and \
               self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))
    