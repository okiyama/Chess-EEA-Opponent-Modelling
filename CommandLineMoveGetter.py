from MoveGetter import MoveGetter

class CommandLineMoveGetter(MoveGetter):

	def getMove(self, board):
		print(board)
		self.printLegalMoves(board)
		print(self.getMoveFromCLI(board))

	def printLegalMoves(self, board):
		for index, move in enumerate(board.legal_moves):
			print(str(index) + ": ", end="")
			print(move)

	def getMoveFromCLI(self, board):
		selection = input("Select a move")
		while(int(selection) < 0 or int(selection) >= len(board.legal_moves)):
			selection = input("Select a move")

		return board.legal_moves[selection]