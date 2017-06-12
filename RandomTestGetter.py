from TestGetter import TestGetter
from Test import Test
import chess.pgn
import random

class RandomTestGetter(TestGetter):
    def __init__(self):
        self.file = open('games/Kasparov.pgn', 'r')

        #Ideally instead of doing this, we'd have some way to randomly seek to one game quickly and load it
        self.games = self.loadAllGames(self.file)

    def getNextTest(self, opponents, previousTest):
        game = self.loadRandomGame()
        numMovesToSkip = random.randint(0, len(list(game.main_line())))

        for i in range(numMovesToSkip):
            game = game.variations[0]
        board = game.board()
        return Test(board)

    def loadRandomGame(self):
        return random.choice(self.games)

    def loadAllGames(self, file):
        toRet = []
        currGame = chess.pgn.read_game(file)

        #100 games is plenty for now
        while currGame and len(toRet) < 100:
            toRet.append(currGame)
            currGame = chess.pgn.read_game(file)

        return toRet