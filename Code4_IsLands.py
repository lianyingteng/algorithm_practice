"""岛屿问题： 给定一个矩阵，返回岛屿的个数"""

def countIslands(m):
	"""返回岛的个数
	"""
	if m == None or len(m) == 0:
		return 0

	res = 0
	row_Num = len(m)
	col_Num = len(m[0])
	for i in range(row_Num):
		for j in range(col_Num):
			if m[i][j] == 1:
				infect(m, i, j, row_Num, col_Num)
				res += 1

	return res


def infect(arr, i, j, row, col):
	"""感染过程
	"""
	if i < 0 or i >= row or j < 0 or j >= col or arr[i][j] != 1:
		return None

	arr[i][j] = 2

	infect(arr, i-1, j, row, col)
	infect(arr, i+1, j, row, col)
	infect(arr, i, j-1, row, col)
	infect(arr, i, j+1, row, col)





if __name__ == '__main__':
	m1 = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 1, 1, 1, 0, 1, 1, 1, 0],
		[0, 1, 1, 1, 0, 0, 0, 1, 0],
		[0, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
		]


	print(countIslands(m1))


	m2 = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0], 
		[0, 1, 1, 1, 1, 1, 1, 1, 0],
		[0, 1, 1, 1, 0, 0, 0, 1, 0],
		[0, 1, 1, 0, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
		]

	print(countIslands(m2))