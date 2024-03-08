"""
Tic Tac Toe Player
"""

import math
import copy
import random

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

    nMoves_X = 0
    nMoves_O = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                nMoves_X += 1
            elif board[i][j] == O:
                nMoves_O += 1

    if not terminal(board) and nMoves_X == nMoves_O:
        return X
    elif nMoves_X > nMoves_O:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_moves.add((i, j))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("This action is not valid.")

    elif terminal(board):
        raise Exception("Sorry, the game is over.")

    copy_board = copy.deepcopy(board)
    copy_board[action[0]][action[1]] = player(board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if (board[i][0] == X and board[i][1] == X and board[i][2] == X):
            return X
        elif (board[i][0] == O and board[i][1] == O and board[i][2] == O):
            return O

    for j in range(3):
        if (board[0][j] == X and board[1][j] == X and board[2][j] == X):
            return X
        elif (board[0][j] == O and board[1][j] == O and board[2][j] == O):
            return O

    if (board[0][0] == X and board[1][1] == X and board[2][2] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O):
        return O

    if (board[2][0] == X and board[1][1] == X and board[0][2] == X):
        return X
    elif (board[2][0] == O and board[1][1] == O and board[0][2] == O):
        return O
    
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    n_emptyCells = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                n_emptyCells += 1
    if n_emptyCells == 9:
        starting_position = random.choice([(0, 0), (1, 1), (2, 2)])
        return (starting_position[0], starting_position[1])

    if player(board) == X:
        bestScore = -1
        bestAction = None

        for action in actions(board):
            minScore = minValue(result(board, action))
            if minScore > bestScore:
                bestScore = minScore
                bestAction = action

    elif player(board) == O:
        bestScore = 1
        bestAction = None

        for action in actions(board):
            maxScore = maxValue(result(board, action))
            if maxScore < bestScore:
                bestScore = maxScore
                bestAction = action

    return bestAction


def minValue(board):
    if terminal(board):
        return utility(board)
    else:
        bestScore = 1
        for action in actions(board):
            bestScore = min(bestScore, maxValue(result(board, action)))
        return bestScore


def maxValue(board):
    if terminal(board):
        return utility(board)
    else:
        bestScore = -1
        for action in actions(board):
            bestScore = max(bestScore, minValue(result(board, action)))
        return bestScore
