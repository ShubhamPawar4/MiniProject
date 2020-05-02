"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError

    if any(None in row for row in board):
        XCount=sum(row.count("X") for row in board)
        OCount=sum(row.count("O") for row in board)

        if XCount == OCount:
            return "X"
        else:
            return "O"
    else:
        return



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    x= set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                x.add((i,j))
    return x


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError
    i , j = action
    if i<3 and j<3 and board[i][j]==EMPTY:
        playername=player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = playername
        return new_board
    else:
        raise Exception('Invalid action')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return "X"
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return "O"
    if board[0][0] == board[1][1] == board[2][2] == "X":
            return "X"
    if board[0][0] == board[1][1] == board[2][2] == "O":
            return "O"
    if board[0][2] == board[1][1] == board[2][0] == "X":
            return "X"
    if board[0][2] == board[1][1] == board[2][0] == "O":
            return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
   # raise NotImplementedError
    if winner(board)!=None:
        return True
    if any(None in row for row in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
   # raise NotImplementedError
    w = winner(board)
    if w=="X":
        return 1
    if w=="O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #raise NotImplementedError
    if terminal(board):
        return None
    if player(board)=="X":
        best_val=-1
        best_move = (-1,-1)
        c=sum(row.count(EMPTY) for row in board)
        if c==9:
            return best_move
        for action in actions(board):
            move_value = MIN_VALUE(result(board,action))
            if move_value == 1:
                best_move = action
                break
            if move_value > best_val:
                best_move = action
        return best_move
    
    if player(board) == "O":
        best_val=1
        best_move = (-1,-1)
        for action in actions(board):
            move_value = MAX_VALUE(result(board,action))
            if move_value == -1:
                best_move=action
                break
            if move_value < best_val:
                best_move = action
        return best_move

def MIN_VALUE(board):
    if terminal(board):
        return utility(board)
    v=1
    for action in actions(board):
        v = min(v, MAX_VALUE(result(board,action)))
        if v == -1:
            break
    return v


def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v=-1
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board,action)))
        if v == 1:
            break
    return v
