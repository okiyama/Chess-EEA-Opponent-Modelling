import os
import chess, chess.pgn
from pprint import pprint

"""
Given a folder of PGN files, processes them into a series of python-chess PGN game files
These files are saved on a per-player basis and the pickle file will hold an array of python-chess PGN games
"""
def processRawGames(gamesFolder):
    files = os.listdir(gamesFolder)
    # for gameFile in files:
    currGameFile = open(gamesFolder + "/" + "KingBase2016-03-A00-A39.pgn", "r")
    game = chess.pgn.read_game(currGameFile)
    while(game):
        print(game)
        game = chess.pgn.read_game(currGameFile)


# def processRawGames(gamesFolder):
#     files = os.listdir(gamesFolder)
#     for gameFile in files:
#         currGameFile = open(gamesFolder + "/" + gameFile, "r")
#         currLine = currGameFile.readline()
#         endLineCount = 0
#         whitePlayer = ""
#         blackPlayer = ""
#         while(endLineCount < 2):
#             if(currLine == ""):
#                 endLineCount += 1
#             else:
#                 if("White " in currLine):
#                     whitePlayer = currLine
#                 elif("Black " in currLine):
#                     blackPlayer = currLine

#             print(whitePlayer)
#             print(blackPlayer)
#             currLine = currGameFile.readline()
            
if __name__ == "__main__":
    processRawGames("Raw_Games")