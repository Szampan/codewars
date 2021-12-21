# Tic-Tac-Toe Checker

def is_draw(board):
    for i in board:
        if 0 in i:
            return False
    return True
        
def get_winner(board):
    for mark in (1,2):
        rotated = [list(i) for i in list(zip(*board[::-1]))]
        diag_1 = [board[i][i] for i in range(len(board))]
        diag_2 = [rotated[i][i] for i in range(len(rotated))]
        
        if [mark]*3 in (board + rotated + [diag_1] + [diag_2]):
            return mark
        
def is_solved(board):
    winner = get_winner(board)
    if winner:
        return winner 
    elif is_draw(board):
        return 0
    return -1