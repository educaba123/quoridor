import os
from board import Item

# limpiar mostrar la tabla a analizar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# mostar tabla
def display_game(board):
    border = get_top_border(board)


    print(border)
    for row in board:
        line = "| "
        for cell in row:
            if cell == Item.PAWN_1:
                line += "X "
            elif cell == Item.PAWN_2:
                line += "Y "
            elif cell == Item.FENCE:
                line += "* "
            elif cell == Item.SQUARE:
                line += "- "
            else:
                line += "  "
        line += "| "
        print(line)
    print(border)

# borde de la tabla
def get_top_border(board):
    border = "-"
    for x in board:
        border += "--"
    border += "-"
    return border
