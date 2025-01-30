mapOfSymbols = {
    "WE": '♖',  # White Rook
    "WN": '♘',  # White Knight
    "WB": '♗',  # White Bishop
    "WQ": '♕',  # White Queen
    "WK": '♔',  # White King
    "WP": '♙',  # White Pawn
    "BE": '♜',  # Black Rook
    "BN": '♞',  # Black Knight
    "BB": '♝',  # Black Bishop
    "BQ": '♛',  # Black Queen
    "BK": '♚',  # Black King
    "BP": '♟',  # Black Pawn
    "E": '.'    # Empty square (optional)
}


def generateBoard(board):
    generatedBoard = []
    for i in range(8):
        aRow = []
        for j in range(8):
            aRow.append( mapOfSymbols[ str(board[i][j]) ] )
        generatedBoard.append( aRow )
    return generatedBoard