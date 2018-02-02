"""给定一个矩阵matrix，其中的值有正、有负、有0，返回子矩阵的最大累加和。"""
def maxSumOfSubMatrix(matrix):
	"""子矩阵的最大累加和
	"""
	if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
		return 0

	maxSum = float('-inf')

	row, col = len(matrix), len(matrix[0])
	for beg in range(row): # 从beg行开始遍历
		arr = [0] * col
		for i in range(beg, row):
			for j in range(col):
				arr[j] += matrix[i][j]

			maxSum = max(
				maxSum,
				maxSumOfSubArray(arr)
				)
	
	return maxSum


def maxSumOfSubArray(arr):
	if arr == None or len(arr) == 0:
		return 0

	maxSum = float('-inf')
	sum1 = 0
	for i in range(len(arr)):
		sum1 += arr[i]
		maxSum = max(maxSum, sum1)
		sum1 = 0 if sum1 < 0 else sum1

	return maxSum

if __name__ == '__main__':
	matrix = [
	[-90, 48, 78],
	[64, -40, 64],
	[-81, -7, 66]]
	print(maxSumOfSubMatrix(matrix)) # 209

	matrix = [
	[-1, -1, -1],
	[-1, 2, 2],
	[-1, -1, -1]]
	print(maxSumOfSubMatrix(matrix)) # 4