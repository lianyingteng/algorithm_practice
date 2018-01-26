"""给定一个矩阵m, 从左上角开始每次只能向右或者向下走，
最终到达右下角位置，路径上所有的数字累加起来就是路径和，
返回所有的路径中最小的路径和。"""

def minPathSum_1(matrix):
	"""暴力递归
	"""
	if matrix == None:
		return None

	return process_1(matrix, 0, 0)

def process_1(arr, i, j):
	if i == len(arr) - 1 and j == len(arr[0]) - 1:
		return arr[i][j]

	if i == len(arr) - 1:
		return arr[i][j] + process_1(arr, i, j+1)
	elif j == len(arr[0]) - 1:
		return arr[i][j] + process_1(arr, i+1, j)
	else:
		return arr[i][j] + min(
			process_1(arr, i, j+1),
			process_1(arr, i+1, j))


def minPathSum_2(matrix):
	"""动态规划 （从下往上递推）

	i,j 到 右下角的最小路径和
	"""
	if matrix == None:
		return None

	row = len(matrix)
	col = len(matrix[0])

	bp = [] # 初始化 bp数组
	for _ in range(row):
		bp.append([0] * col)

	bp[row-1][col-1] = matrix[row-1][col-1]
	
	# 最后一列赋值
	for i in list(range(row-1))[::-1]:
		bp[i][col-1] = matrix[i][col-1] + bp[i+1][col-1]
	# 最后一行赋值
	for j in list(range(col-1))[::-1]:
		bp[row-1][j] = matrix[row-1][j] + bp[row-1][j+1]

	#其他位置赋值
	for i in list(range(row-1))[::-1]:
		for j in list(range(col-1))[::-1]:
			bp[i][j] = matrix[i][j] + min(bp[i+1][j], bp[i][j+1])

	return bp[0][0]


def minPathSum_3(matrix):
	"""动态规划 （从上往下递推）

	0，0 到 i,j的最小路径和
	"""
	if matrix == None:
		return None

	row = len(matrix)
	col = len(matrix[0])

	bp = []
	for i in range(row):
		bp.append([0] * col)

	bp[0][0] = matrix[0][0]
	# 第一列赋值
	for i in range(1, row):
		bp[i][0] = matrix[i][0] + bp[i-1][0]
	# 第一行赋值
	for j in range(1, col):
		bp[0][j] = matrix[0][j] + bp[0][j-1]
	
	# 其他位置
	for i in range(1, row):
		for j in range(1, col):
			bp[i][j] = matrix[i][j] + min(
				bp[i-1][j],
				bp[i][j-1])

	return bp[row-1][col-1]

def minPathSum_3_plus(matrix):
	"""动态规划（空间压缩技术）
	"""
	if matrix == None or len(matrix) == 0 or matrix[0] == None or len(matrix[0]) == 0:
		return None

	more = max(len(matrix), len(matrix[0])) # 行列数最大的那个为 more， 小的为less
	less = min(len(matrix), len(matrix[0]))

	rowMore = (more == len(matrix))
	bp = [0] * less
	bp[0] = matrix[0][0]
	for i in range(1, less):
		bp[i] = bp[i-1] + (
			matrix[0][i] if rowMore else matrix[i][0]
			)

	for i in range(1, more):
		bp[0] += (
			matrix[i][0] if rowMore else matrix[0][i]
			)

		for j in range(1, less):
			bp[j] = min(bp[j-1], bp[j]) + (
				matrix[i][j] if rowMore else matrix[j][i]
				)

	return bp[less-1]


"""
注意：
	1. 最终目的是想求最优解的《具体路经》，空间压缩方法是不能用的（这时需要完整的动态规划表）
	2. 最终目的是像求最优解的《值》，则可以使用空间压缩方法！
"""


if __name__ == '__main__':
	matrix = [
	[1, 3, 5, 9], 
	[8, 1, 3, 4], 
	[5, 0, 6, 1], 
	[8, 8, 4, 0]]

	print(minPathSum_1(matrix))
	print(minPathSum_2(matrix))
	print(minPathSum_3(matrix))
	print(minPathSum_3_plus(matrix))