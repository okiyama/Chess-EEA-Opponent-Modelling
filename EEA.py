from Test import Test
from CommandLineMoveGetter import CommandLineMoveGetter
from RandomTestGetter import RandomTestGetter

class EEA:
    def __init__(self):
        """ Initializes EEA to have a random set of tests and opponent models """
        self.realOpponent = CommandLineMoveGetter()
        self.currentTest = Test(None)
        self.currentTest.getExpectedMove(self.realOpponent)
        self.testSet = [self.currentTest]

    def run(self):
        done = False
        # opponentEvolver = OpponentEvolver(self.testSet) #Will this pass reference correctly? Want it to auto-update
        testGetter = RandomTestGetter(self.testSet)
        while not done:
            # opponentEvolver.evolve(self.currentTest)
            self.currentTest = testGetter.getNextTest(None, self.testSet)
            self.currentTest.getExpectedMove(self.realOpponent)
            self.testSet.append(self.currentTest)
            done = True


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
    eea.run()