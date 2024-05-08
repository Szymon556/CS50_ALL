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
    # czyli jeżeli cała tablica jest pusta to X zaczyna, wychodze z założenia że X jest pierwszy więc tylko go sprawdzam czy jest w tablicy

    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    if x_count > o_count:
        return "O"
    else:
        return "X"


def actions(board):

    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = []


    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.append((i,j))
    return set(actions_set)



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Czy akcja jest poprawna dla mojej tablicy?
    i,j = action
    cell = board[i][j]
    if cell != EMPTY or i <0 or i>3 or j < 0 or j>3:
        raise
    # Skpiuj tablice, bo jak wiadomo kilka zmiennych może mieć referencje do tego samego obiektu
    board_copy = copy.deepcopy(board)
    # Ustaw czyja tura jest teraz
    turn = player(board)
    board_copy[i][j] = turn
    return board_copy




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_terms = [
        [board[0][0],board[0][1],board[0][2]], # wiersz pierwszy
        [board[1][0],board[1][1],board[1][2]], # wiersz drugi
        [board[2][0],board[2][1],board[2][2]], # wiersz trzeci
        [board[0][0],board[1][0],board[2][0]], # kolumna pierwsza
        [board[0][1],board[1][1],board[2][1]], # kolumna druga
        [board[0][2],board[1][2],board[2][2]], # kolumna trzecia
        [board[0][0],board[1][1],board[2][2]], # od lewa do prawa
        [board[0][2],board[1][1],board[2][0]], # od prawa do lewa

    ]
    for state in win_terms:
        if state[0] != None and state[0] == state[1] and state[0] == state[2]:
            return state[0] # i to jest nasz zwycięzca
    return None # nikt nie wygrał


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_result = winner(board)
    # czyli jesli nikt nie wygral sprawdz czy tablica jest zapelniona
    if winner_result == None:
        for i in board:
            for j in i:
                # jeżeli jaka kolwiek komórka jest nie zapełniona to oznacza że gra w toku
                if j == None:
                    return False
        # jeżeli nie ma żadnej pustej komórki a nikt nie wygrał to zwróć True jako że to koniec gry
        return True
    # w przeciwnym razie jeżeli mamy zwycięzce to koniec gry
    return True





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win_player = winner(board)
    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        v,move = max_value(board)
        return move
    else:
        v,move = max_value(board)
        return move




def min_value(board):
    if terminal(board):
        return utility(board), None  # Nie ma ruchu, gdy gra się zakończyła
    v = float('inf')
    best_move = None
    for action in actions(board):
        score, _ = max_value(result(board, action))
        if score < v:
            best_move = action
            v = score
            if v == -1:
                break  # Przerywamy pętlę, jeśli znajdziemy najlepszy możliwy wynik
    return v, best_move

def max_value(board):
    if terminal(board):
        return utility(board), None  # Nie ma ruchu, gdy gra się zakończyła
    v = float('-inf')
    best_move = None
    for action in actions(board):
        score, _ = min_value(result(board, action))
        if score > v:
            best_move = action
            v = score
            if v == 1:
                break  # Przerywamy pętlę, jeśli znajdziemy najlepszy możliwy wynik
    return v, best_move

