"""转圈打印矩阵"""

def printEdge(matrix, tR, tC, dR, dC):

	if tR == dR:
		for i in range(tC, dC+1):
			print(matrix[tR][i])
	elif tC == dC:
		for i in range(tR, dR+1):
			print(matrix[tC][i])
	else:
		curR, curC = tR, tC
		while curC != dC: # 相等就不打印了，交给下一个while打印
			print(matrix[curR][curC], end=' ')
			curC += 1
		while curR != dR:
			print(matrix[curR][curC], end=' ')
			curR += 1
		while curC != tC:
			print(matrix[curR][curC], end=' ')
			curC -= 1
		while curR != tR:
			print(matrix[curR][curC], end=' ')
			curR -= 1


def spiralOrderPrintMatrix(matrix):

	tR, tC = 0, 0
	dR, dC = len(matrix)-1, len(matrix[0]) - 1

	while tR <= dR and tC <= dC:
		printEdge(matrix, tR, tC, dR, dC)
		tR += 1
		tC += 1
		dR -= 1
		dC -= 1


if __name__ == '__main__':
	matrix = [[1, 2, 3, 4], [5, 6, 7, 8],
	 [9, 10, 11, 12], [13, 14, 15, 16]]

	spiralOrderPrintMatrix(matrix)