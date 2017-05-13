from CommandLineMoveGetter import CommandLineMoveGetter
import chess

class TestGround:
	""" Just for testing things out, things in here will change rapidly """

	def playNormalChessGame(self):
		board = chess.Board()
		moveGetter = CommandLineMoveGetter()
		while True:
			move = moveGetter.getMove(board)
			board.push(move)


if __name__ == "__main__":
	testGround = TestGround()
	testGround.playNormalChessGame()