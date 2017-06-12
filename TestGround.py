from CommandLineMoveGetter import CommandLineMoveGetter
from RandomTestGetter import RandomTestGetter
import chess

class TestGround:
    """ Just for testing things out, things in here will change rapidly """

    def playNormalChessGame(self):
        board = chess.Board()
        moveGetter = CommandLineMoveGetter()
        while True:
            move = moveGetter.getMove(board)
            board.push(move)

    def solveRandomTests(self):
        testGetter = RandomTestGetter()
        randomTest = testGetter.getNextTest(None, None)
        board = randomTest.board
        moveGetter = CommandLineMoveGetter()
        while True:
            move = moveGetter.getMove(board)
            randomTest.actualMove = move
            randomTest = testGetter.getNextTest(None, None)


if __name__ == "__main__":
    testGround = TestGround()
    # testGround.playNormalChessGame()
    testGround.solveRandomTests()