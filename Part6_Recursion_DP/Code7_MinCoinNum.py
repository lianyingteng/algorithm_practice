"""给定数组arr，arr中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，
再给定一个整数aim代表要找的钱数，求组成aim的最少货币数？"""

def minCoinNum_1(arr, aim):
	"""暴力递归
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return -1

	#return process_1(arr,0,aim) 
	return process(arr, len(arr)-1, aim)

def process(arr, index, aim): # arr[0 - index] 这些货币，得到aim的最小货币数
	
	# 当目标钱数aim=0时，返回0张钱
	if aim == 0:
		return 0

	# 当目标钱数aim<0时，表示换不开，返回无穷大
	if aim < 0:
		return float('inf')

	# 当只用 arr[0] 面值的钱时， aim是arr[0]整数倍时 - 可以换开； aim不是arr[0]整数倍时 - 换不开（返回无穷大）
	if index == 0:
		return aim // arr[index] if (aim % arr[index] == 0) else float('inf')

	"""
	process(arr, index, aim) 表示用 arr[0], arr[1], ..., arr[index] 这些面值的钱 可以 换取 aim 的最小货币数
	它的值来源于下面两种情况：
		1. process(arr, index-1, aim) 表示 不用 arr[index], 只用 arr[0] 到 arr[index-1]这些面值的钱 
			可以 换取 aim 的最小货币数
		2. process(arr, index, aim - arr[index]) 表示用 arr[index]，也就是用 arr[0] 到 arr[index]这些面值的钱
			可以 换取 aim-arr[index] 的最小货币数
	所以
	process(arr, index, aim)的值 等于
	min(
		process(arr, index-1, aim), 
		1 + process(arr, index, aim - arr[index])
		)
	"""  
	return min(
		process(arr, index-1, aim), 
		1 + process(arr, index, aim - arr[index])
		)


def process_1(arr, index, aim): # arr[index:] 这些货币，得到aim的最小货币数
	if index == len(arr):
		return float('inf')

	tmp = float('inf')
	for i in range(index, len(arr)):
		if aim == arr[i]:
			return 1
		elif aim < arr[i]:
			continue
		else:
			tmp = min(tmp, 1 + process_1(arr, i, aim-arr[i]))

	return tmp



def minCoinNum_2(arr, aim):
	"""动态规划 P192  核心： dp[i][j] = min( dp[i-1][j], dp[i][j-arr[i]] + 1)
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return -1

	row, col = len(arr), aim + 1
	dp = []
	for _ in range(row):
		dp.append([0] * col)

	# 第一行
	for i in range(1, col):
		dp[0][i] = i//arr[0] if i%arr[0] == 0 else float('inf')

	for i in range(1, row):
		for j in range(1, col):
			dp[i][j] = min(
				dp[i-1][j],
				1 + dp[i][j-arr[i]]
				) if j - arr[i] >= 0 else float('inf')


	return dp[row - 1][col - 1] if dp[row-1][col-1] != float('inf') else -1

def minCoinNum_3(arr, aim):
	"""动态规划（空间压缩）P193
	"""
	if arr == None or len(arr) == None or aim < 0:
		return -1

	row, col = len(arr) - 1, aim + 1
	dp = [float('inf')] * col
	dp[0] = 0
	for i in range(1, col):
		if i % arr[0] == 0:
			dp[i] = i // arr[0]

	for i in range(1, row):
		dp[0] = 0
		for j in range(1, col):
			tmp = float('inf') if j - arr[i] < 0 or dp[j - arr[i]] == float('inf') else dp[j - arr[i]] + 1
			dp[j] = min(dp[j], tmp)

	return dp[-1]


if __name__ == '__main__':
	arr = [5, 4, 3, 2]
	aim = 23
	print(minCoinNum_1(arr, aim))
	print(minCoinNum_2(arr, aim))
	print(minCoinNum_3(arr, aim))
