"""
补充问题： 给定一个数组arr, arr中所有的值都为正数。《每个值仅代表一张钱的面值》，
再给定一个整数aim代表要找的钱数，求组成aim的最少货币数。
"""
def minCoinNum_1(arr, aim):
	"""暴力递归
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return -1

	return process(arr, len(arr)-1, aim)


def process(arr, index, aim): # arr[0 - index] 合成 aim 的最少货币数
	if aim < 0 or index < 0: 
		return float('inf')
	
	if aim == 0: 
		return 0

	if index == 0:
		return 1 if aim == arr[0] else float('inf')

	tmp = min(
		process(arr, index-1, aim),
		1 + process(arr, index-1, aim - arr[index])
		)

	return tmp


def minCoinNum_2(arr, aim):
	"""动态规划
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return -1

	row, col = len(arr), aim + 1

	dp = []
	for _ in range(row):
		dp.append([0] * col)

	# 第一行初始化
	for i in range(1, col):
		dp[0][i] = 1 if i == arr[0] else float('inf')

	# 其他位置
	for i in range(1, row):
		for j in range(1, col):
			tmp =  dp[i-1][j-arr[i]] + 1 if j - arr[i] >= 0 else float('inf')
			dp[i][j] = min(dp[i-1][j], tmp)

	return dp[row-1][col-1]


def minCoinNum_3(arr, aim):
	"""动态规划（空间压缩）
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return -1

	row, col = len(arr), aim+1

	dp = [float('inf')] * col
	dp[0] = 0
	if arr[0] <= aim: # 初始化第一行
		dp[arr[0]] = 1

	# 其他位置
	for i in range(1, row):
		dp[0] = 0
		for j in list(range(1, col))[::-1]:
			tmp = dp[j-arr[i]] + 1 if j-arr[i] >= 0 else float('inf')
			dp[j] = min(dp[j], tmp)

	return dp[col-1]


if __name__ == '__main__':
	arr = [5, 2, 3, 5]
	aim = 10
	print(minCoinNum_1(arr, aim))
	print(minCoinNum_2(arr, aim))
	print(minCoinNum_3(arr, aim))