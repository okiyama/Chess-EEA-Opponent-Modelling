#Main method for running EEA to model opponents in Chess
#TODO: It would be cool and smart if things like number of opponents, time for evolution and what not were in a config file

#python chess: https://python-chess.readthedocs.io/en/v0.17.0/

class EEA(object):
	def __init__(self):
		""" Initializes EEA to have a random set of tests and opponent models """
		self.realOpponent = CommandLineMoveGetter()
		self.currentTest = Test()
		self.currentTest.getExpectedMove(self.realOpponent)
		self.testSet = TestSet(self.currentTest)

	def run(self):
		done = false
		opponentEvolver = OpponentEvolver(self.testSet) #Will this pass reference correctly? Want it to auto-update
		testEvolver = TestEvolver(self.)
		while not done:
			opponentEvolver.evolve(self.currentTest)
			self.currentTest = testEvolver.findBestTest(opponentEvolver.getOpponentModels())
			self.currentTest.getExpectedMove(self.realOpponent)
			done = true


"""
Generate initial random set of opponents
Generate initial random test
Get the actual move from the real opponent

Loop:
	Present all opponents with the test, give them time to evolve to find agreement
	Find a test that maximizes disagreement among the models given some amount of time
	Get the actual move from the real opponent
goto loop
"""

if (__name__ == "__main__"):
	eea = EEA()
	eea.initialize()
	eea.run()