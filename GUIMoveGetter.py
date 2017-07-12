from MoveGetter import MoveGetter
import chess, chess.svg, webbrowser, os

class GUIMoveGetter(MoveGetter):

    def getMove(self, board):
        self.displayBoard(board)
        move = self.getMoveFromGUI(board)
        self.closeDisplay()
        return move


    def displayBoard(self, board):
        """
        Display the given board by opening up a webbrowser and showing the svg
        """
        boardAsSvg = chess.svg.board(board)
        filePath = self.saveSvg(boardAsSvg)
        fullPath = "file://" + os.path.dirname(os.path.abspath(__file__)) + "\\" + filePath
        webbrowser.open(fullPath)

    def saveSvg(self, svg):
        filePath = "board.svg"
        toWrite = open(filePath, "w")
        toWrite.write(svg)
        toWrite.close()
        return filePath

    def getMoveFromGUI(self, board):
        pass

    def closeDisplay(self):
        pass
