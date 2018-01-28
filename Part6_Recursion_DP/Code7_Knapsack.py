"""给定两个数组w和v，两个数组长度相等，w[i]表示第i件商品的重量，v[i]表示第i见商品的价值。
再给定一个整数bag，要求你挑选商品的重量加起来一定不能超过bag，返回满足这个条件下，你能获
得的最大价值！"""
def maxValue1(w, v, bag):
	"""暴力递归
	"""
	if w == None or len(w) == 0 or v == None or len(v) == 0 or bag < 0:
		return None

	return process1(w, v, 0, 0, bag)

def process1(w, v, i, already, bag):
	if already > bag:
		return float('-inf')

	if i == len(w): ####
		return 0

	return max(
		process1(w, v, i+1, already, bag),
		v[i] + process1(w, v, i+1, already+w[i], bag),
		)


def maxValue2(w, v, bag):
	"""动态规划
	"""
	if w == None or len(w) == 0 or v == None or len(v) == 0 or bag < 0:
		return None

	row, col = len(w) + 1, bag + 1
	dp = []
	for _ in range(row):
		dp.append([0] * col)

	# 其他位置
	for i in list(range(row-1))[::-1]: # 从后向前
		for j in range(col):
			dp[i][j] = dp[i+1][j]
			if j + w[i] <= bag:
				dp[i][j] = max(
					dp[i][j],
					v[i] + dp[i+1][j+w[i]]
					)
				
	return dp[0][0]





###############


if __name__ == '__main__':
	w = [3, 2, 4, 7]
	v = [5, 6, 3, 19]
	bag = 0
	while bag <= sum(w):
		bag += 1
		print(maxValue1(w, v, bag), end=' ')
		print(maxValue2(w, v, bag))
