def printLevel(m, tR, tC, dR, dC, toDown):
	if toDown:
		while tR != dR + 1:
			print(m[tR][tC], end=' ')
			tR += 1
			tC -= 1
	else:
		while dR != tR - 1:
			print(m[dR][dC], end=' ')
			dR -= 1
			dC += 1


def zigzagPrintMatrix(matrix):
	tR, tC = 0, 0
	dR, dC = 0, 0
	endR, endC = len(matrix)-1, len(matrix[0])-1
	toDown = False

	while tR != endR + 1:
		printLevel(matrix, tR, tC, dR, dC, toDown)
		tR = tR+1 if tC == endC else tR
		tC = tC if tC == endC else tC+1
		dC = dC+1 if dR == endR else dC
		dR = dR if dR == endR else dR+1

		toDown = not toDown





if __name__ == '__main__':
	
	matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
	zigzagPrintMatrix(matrix)