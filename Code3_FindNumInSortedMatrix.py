"""在行列都排好序的矩阵中找数"""

def isContains(m, K):
	if m == None or len(m) == 0:
		return -1

	curR, curC = 0, len(m[0]) - 1
	while curR <= len(m)-1 and curC >= 0:
		if m[curR][curC] > K:
			curC -= 1
		elif m[curR][curC] < K:
			curR += 1
		else:
			return (curR, curC)
	return -1



if __name__ == '__main__':
	matrix = [
	[0, 1, 2, 3, 4, 5, 6], 
	[10, 12, 13, 15, 16, 17, 18], 
	[23, 24, 25, 26, 27, 28, 29],
	[44, 45, 46, 47, 48, 49, 50], 
	[65, 66, 67, 68, 69, 70, 71], 
	[96, 97, 98, 99, 100, 111, 122],
	[166, 176, 186, 187, 190, 195, 200],
	[233, 243, 321, 341, 356, 370, 380]
	]

	K = 356
	print(isContains(matrix, K))