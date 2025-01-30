from functions.printBoard import printBoard
from functions.askUserToGiveInput import askUserToGiveInput
from functions.makeCoinFtoT import makeCoinFtoT
from functions.printGameOver import printGameOver
from functions.printWinPlayer import printWin

# Initial board
board = [
    ['WE', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WE'],  # White pieces
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],  # White Pawns
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],  # Empty row
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],  # Empty row
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],  # Empty row
    ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],  # Empty row
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],  # White Pawns
    ['BE', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BE']   # Black pieces
]

# Turn and GameOver Flage
turn = "White"
gameOver = False

# loop until the game is Over
while not gameOver:
    printBoard(board)
    f,t = askUserToGiveInput(turn,board)
    if(board[int(t[0])][int(t[1])][1]=="K"):
        break
    makeCoinFtoT(f,t,board)
    turn = "Black" if turn=="White" else "White"

# printing game Over
printGameOver()

#print win
printWin(turn)

