import math
import game

from board import *
from pawn import Orientation, Pawn


def run():
	center = math.floor(BASE_LINE_SIZE / 2)

	#estado incial
	fences = build()
	pawns = [Pawn(0, center, Orientation.WEST), Pawn(BASE_LINE_SIZE - 3, center + 6, Orientation.EAST)]
	board = get_board(pawns, fences)

	game.init_game(board, pawns, fences)

	# game.display_result_route()

if __name__ == "__main__":
    run()
