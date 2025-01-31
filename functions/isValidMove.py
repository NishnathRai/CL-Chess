from .moveDiagram import moveDiagram
from .stepsCountDiagram import stepsCountDiagram
from .gameEngine import gameEngine

def isValidMove(f,t,board):
    if( board[int(f[0])][int(f[1])][1]!="Q" and  board[int(f[0])][int(f[1])][1]!="P" ):
        coin = board[int(f[0])][int(f[1])][1]
        return gameEngine( f, t, moveDiagram[coin] , stepsCountDiagram[coin] )
    elif (board[int(f[0])][int(f[1])][1]!="Q"):
        return gameEngine( f, t, moveDiagram["E"] , stepsCountDiagram["E"] )  or  gameEngine( f, t, moveDiagram["N"] , stepsCountDiagram["N"] )
    else:
        return gameEngine( f, t, moveDiagram["P"] , stepsCountDiagram["P"])