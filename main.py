from functions.printBoard import printBoard
from functions.askUserToGiveInput import askUserToGiveInput

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
    askUserToGiveInput(turn)
    break



