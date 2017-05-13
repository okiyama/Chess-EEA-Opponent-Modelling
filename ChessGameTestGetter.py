import TestGetter
import chess

class ChessGameTestGetter(TestGetter):
	""" Gets the next test such that the opponent plays a normal game of chess """

	def getNextTest(self, opponents, testSet):
		currTest = testSet[-1]
		opponentMove = currTest.move
		boardCopy = chess.Board.copy()
		boardCopy.push(opponentMove)
		
		return boardCopy