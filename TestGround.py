from CommandLineMoveGetter import CommandLineMoveGetter #TODO: Why do I have to do it like this? I want to just import like I did in my other project
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