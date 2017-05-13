class TestGetter:
	""" Interface for getting tests. Useful because I'd like to both be able to evolve a next test as well as play a normal game of chess with the user """
	#I thought about using abstract base class for this but it feels like overkill
	def getNextTest(self, opponents, previousTest): raise NotImplementedError