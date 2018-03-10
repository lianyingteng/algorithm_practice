"""给定数组 arr， arr中所有的值都为正数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个整数aim代表要找的钱数，求换钱的有多少种方法？"""

def methodNum_1(arr, aim):
	"""暴力递归
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return -1

	return process(arr, len(arr) - 1, aim)


def process(arr, index, aim):
	if aim < 0 or index < 0:
		return 0

	if aim == 0:
		return 1

	if index == 0:
		return 1 if aim % arr[0] == 0 else 0

	return process(arr, index-1, aim) + process(arr, index, aim - arr[index])


def methodNum_2(arr, aim):
	"""动态规划
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return -1

	row, col = len(arr), aim+1

	dp = []
	for _ in range(row):
		dp.append([0] * col)

	# 初始化第一行
	dp[0][0] = 1 # aim == 0 -> return 1
	for i in range(1, col):
		dp[0][i] = 1 if i % arr[0] == 0 else 0

	# 其他位置
	for i in range(1, row):
		dp[i][0] = 1 # aim == 0 -> return 1
		for j in range(1, col):
			tmp = dp[i][j-arr[i]] if j - arr[i] >= 0 else 0
			dp[i][j] = tmp + dp[i-1][j]

	return dp[row-1][col-1]



def methodNum_3(arr, aim):
	"""动态规划（空间压缩）
	"""
	if arr == None or len(arr) == 0 or aim < 0:
		return 0

	row, col = len(arr), aim + 1
	dp = [0] * col
	dp[0] = 1
	for i in range(1, col):
		dp[i] = 1 if i%arr[0] == 0 else 0

	for i in range(1, row):
		for j in range(1, col):
			
			dp[j] = dp[j] + (dp[j-arr[i]]  if j-arr[i] >= 0 else 0)

	return dp[-1]


if __name__ == '__main__':
	arr = [5, 10, 25, 1]
	aim = 500

	print(methodNum_1(arr, aim))
	print(methodNum_2(arr, aim))
	print(methodNum_3(arr, aim))
