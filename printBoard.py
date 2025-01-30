from generateBoard import generateBoard

def printBoard(board):
    board = generateBoard( board )
    s = f"""
                                    a   b   c   d   e   f   g   h
                                  ┌───┬───┬───┬───┬───┬───┬───┬───┐
                                8 │ {board[0][0]} │ {board[0][1]} │ {board[0][2]} │ {board[0][3]} │ {board[0][4]} │ {board[0][5]} │ {board[0][6]} │ {board[0][7]} │ 8
                                  ├───┼───┼───┼───┼───┼───┼───┼───┤
                                7 │ {board[1][0]} │ {board[1][1]} │ {board[1][2]} │ {board[1][3]} │ {board[1][4]} │ {board[1][5]} │ {board[1][6]} │ {board[1][7]} │ 7
                                  ├───┼───┼───┼───┼───┼───┼───┼───┤
                                6 │ {board[2][0]} │ {board[2][1]} │ {board[2][2]} │ {board[2][3]} │ {board[2][4]} │ {board[2][5]} │ {board[2][6]} │ {board[2][7]} │ 6
                                  ├───┼───┼───┼───┼───┼───┼───┼───┤
                                5 │ {board[3][0]} │ {board[3][1]} │ {board[3][2]} │ {board[3][3]} │ {board[3][4]} │ {board[3][5]} │ {board[3][6]} │ {board[3][7]} │ 5
                                  ├───┼───┼───┼───┼───┼───┼───┼───┤
                                4 │ {board[4][0]} │ {board[4][1]} │ {board[4][2]} │ {board[4][3]} │ {board[4][4]} │ {board[4][5]} │ {board[4][6]} │ {board[4][7]} │ 4
                                  ├───┼───┼───┼───┼───┼───┼───┼───┤
                                3 │ {board[5][0]} │ {board[5][1]} │ {board[5][2]} │ {board[5][3]} │ {board[5][4]} │ {board[5][5]} │ {board[5][6]} │ {board[5][7]} │ 3
                                  ├───┼───┼───┼───┼───┼───┼───┼───┤
                                2 │ {board[6][0]} │ {board[6][1]} │ {board[6][2]} │ {board[6][3]} │ {board[6][4]} │ {board[6][5]} │ {board[6][6]} │ {board[6][7]} │ 2
                                  ├───┼───┼───┼───┼───┼───┼───┼───┤
                                1 │ {board[7][0]} │ {board[7][1]} │ {board[7][2]} │ {board[7][3]} │ {board[7][4]} │ {board[7][5]} │ {board[7][6]} │ {board[7][7]} │ 1
                                  └───┴───┴───┴───┴───┴───┴───┴───┘
    """
    print(s)