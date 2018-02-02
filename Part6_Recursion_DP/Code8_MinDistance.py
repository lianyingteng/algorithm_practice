"""一条直线上有居民点，邮局只能建在居民点上。给定一个有序数组arr，每个值表示居民点的一维坐标，
在给定一个整数num，表示邮局的数量。选择num个居民点建立num个邮局，使所有的居民点到邮局的总距离最短
，返回最短距离。

例：arr=[1, 2, 3, 4, 5, 1000], num = 2
邮局建在3， 1000上， 最短距离6
"""
def minDistance(arr, num):
	""" 动态规划 P509
	"""
	if arr == None or len(arr) == 0 or num < 1 or len(arr) < num:
		return 0

	w = []
	for _ in range(len(arr)+1): w.append([0] * (len(arr)+1))

	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			w[i][j] = w[i][j-1] + arr[j] - arr[(i+j)//2]

	dp = []
	for _ in range(num): dp.append([0] * len(arr))

	for j in range(1, len(arr)):
		dp[0][j] = w[0][j]

	for i in range(1, num):
		for j in range(i+1, len(arr)):
			dp[i][j] = float('inf')
			for k in range(j+1):
				dp[i][j] = min(
					dp[i][j],
					dp[i-1][k] + w[k+1][j]
					)

	return dp[num-1][len(arr)-1]



if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5, 1000] # 6
	num = 2
	print(minDistance(arr, num))