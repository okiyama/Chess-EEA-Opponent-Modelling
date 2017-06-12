import chess

class Test:
    """ One test we present to the real opponent to get information about how they play """

    def __init__(self, board):
        self.board = board or chess.Board()
        self.actualMove = None

    def getExpectedMove(self, opponent):
        return opponent.getMove(self.board)