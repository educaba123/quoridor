import math
import game
import time


from board import *
from pawn import Orientation, Pawn


def run():
	center = math.floor(BASE_LINE_SIZE / 2)

	#estado incial
	fences = build()
	pawns = [Pawn(0, center, Orientation.WEST), Pawn(BASE_LINE_SIZE - 3, center + 6, Orientation.EAST)]
	board = get_board(pawns, fences)


	# tiempos
	t0=time.time()
	game.backtracking(board, pawns, fences)
	t00=time.time()
	tiempo_1 = t00-t0

	t1=time.time()
	game.backtracking_2(board, pawns, fences)
	t11=time.time()
	tiempo_2 = t11-t1

	t2=time.time()
	game.BFS(board, pawns, fences)
	tiempo_3 = time.time()-t2

	print('BackTracking: ', tiempo_1)
	print('BackTracking 2: ', tiempo_2)
	print('BFS: ', tiempo_3)


if __name__ == "__main__":
    run()
