import math
from copy import deepcopy
from pawn import Orientation, Pawn, translate_x, translate_y
from functools import reduce
import console
from board import *
from enum import IntEnum

class State(IntEnum):
    RUNNING = 0,
    VICTORY = 1,
    QUIT = 2,

steps = []

    # algoritmo de backtraking
def backtracking(board, pawns, fences, previus_pawn = None):
    player_turn = 0
    current_pawn = pawns[player_turn]

    if is_a_victory(current_pawn):
        return True

    pawn_right = move_right(current_pawn, fences)
    pawn_up = move_up(current_pawn, fences)
    pawn_down = move_down(current_pawn, fences)
    pawn_left = move_left(current_pawn, fences)

    if pawn_right != current_pawn and pawn_right != previus_pawn and no_repeat_steps(steps, pawn_right):
        pawns[player_turn] = pawn_right

        steps.append(pawn_right)
        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn) :
            return True
 
    if pawn_up != current_pawn and pawn_up != previus_pawn and no_repeat_steps(steps, pawn_up):
        pawns[player_turn] = pawn_up
        steps.append(pawn_up)

        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn):
            return True

    if pawn_down != current_pawn and pawn_down != previus_pawn and no_repeat_steps(steps, pawn_down):
        pawns[player_turn] = pawn_down
        steps.append(pawn_down)

        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn):
            return True

    if pawn_left != current_pawn and pawn_left != previus_pawn and no_repeat_steps(steps, pawn_left):
        pawns[player_turn] = pawn_left
        steps.append(pawn_left)

        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn):
            return True

    return False

def backtracking_2(board, pawns, fences, previus_pawn = None):
    player_turn = 0
    current_pawn = pawns[player_turn]

    if is_a_victory(current_pawn):
        return True

    pawn_right = move_right(current_pawn, fences)
    pawn_down = move_down(current_pawn, fences)
    pawn_up = move_up(current_pawn, fences)
    pawn_left = move_left(current_pawn, fences)

    if pawn_right != current_pawn and pawn_right != previus_pawn and no_repeat_steps(steps, pawn_right):
        pawns[player_turn] = pawn_right

        steps.append(pawn_right)
        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn) :
            return True
 
    if pawn_up != current_pawn and pawn_up != previus_pawn and no_repeat_steps(steps, pawn_up):
        pawns[player_turn] = pawn_up
        steps.append(pawn_up)

        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn):
            return True

    if pawn_down != current_pawn and pawn_down != previus_pawn and no_repeat_steps(steps, pawn_down):
        pawns[player_turn] = pawn_down
        steps.append(pawn_down)

        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn):
            return True

    if pawn_left != current_pawn and pawn_left != previus_pawn and no_repeat_steps(steps, pawn_left):
        pawns[player_turn] = pawn_left
        steps.append(pawn_left)

        display(pawns, fences)
        if backtracking(board, pawns, fences, current_pawn):
            return True

    return False


def BFS(board, pawns, fences):
    player_turn = 0
    current_pawn = pawns[player_turn]

    n=len(board)
    padres=[[None for i in range(n)] for i in range(n)]
    visitado=[[False for i in range(n)] for i in range(n)]
    # print(visitado)
    cola=[current_pawn]
    visitado[current_pawn.x][current_pawn.y]=True
    print(current_pawn.x, " ", current_pawn.y)
    
    while len(cola)>0:
        u=cola[0]
        cola=cola[1:]
        for v in board[u.x]:
            if not visitado[v]:
                # print(v) #secuencia de visita
                cola.append(v)
                padres[v]=u
                visitado[v]=True
    return None



def no_repeat_steps(steps, pawn):
    for step in steps:
        if step == pawn:
            return False
    return True
    
#estado objetivo
def is_a_victory(pawn):
    victory = False
    if pawn.goal == Orientation.WEST:
        victory = pawn.x == BASE_LINE_SIZE - 1
    return victory

# reglas de movimientos
def move_right(pawn, fences):
    if not is_crossable_right(pawn, fences):
        return pawn
    return translate_x(pawn, 2)


def move_left(pawn, fences):
    if not is_crossable_left(pawn, fences):
        return pawn
    return translate_x(pawn, -2)


def move_up(pawn, fences):
    if not is_crossable_up(pawn, fences):
        return pawn
    return translate_y(pawn, -2)


def move_down(pawn, fences):
    if not is_crossable_down(pawn, fences):
        return pawn
    return translate_y(pawn, 2)



def display(pawns, fences):
    board = get_board(pawns, fences)
    console.display_game(board)