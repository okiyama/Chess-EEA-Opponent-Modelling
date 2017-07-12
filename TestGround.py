from CommandLineMoveGetter import CommandLineMoveGetter
from RandomTestGetter import RandomTestGetter
from GUIMoveGetter import GUIMoveGetter
import chess, time, chess.uci

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
        moveGetter = GUIMoveGetter()
        while True:
            move = moveGetter.getMove(board)
            randomTest.actualMove = move
            randomTest = testGetter.getNextTest(None, None)
            return

    def openUCIengine(self, location):
        engine = chess.uci.popen_engine(location)
        engine.uci()
        engine.uciok.wait(10)
        print(engine.name)
        print(engine.author)
        print(engine.options)

if __name__ == "__main__":
    testGround = TestGround()
    # testGround.playNormalChessGame()
    testGround.solveRandomTests()
    # testGround.openUCIengine("./stockfish-8-win/Windows/stockfish_8_x64.exe")
