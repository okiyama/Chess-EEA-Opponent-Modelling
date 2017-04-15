import chess

class Test:
	""" One test we present to the real opponent to get information about how they play """

	def __init__(self, board):
		self.board = board
		self.actualMove = None