class MoveGetter:
	""" Interface to gets moves by presenting a board to an opponent, either an AI or a human """

	def getMove(self, board): raise NotImplementedError