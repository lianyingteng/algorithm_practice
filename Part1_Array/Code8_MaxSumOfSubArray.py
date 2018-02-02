"""给定一个数组arr，返回子数组的最大累加和"""
def maxSum(arr):
	if arr == None or len(arr) == 0: return 0

	maxSum = float('-inf')
	sum1 = 0
	for i in range(len(arr)):
		sum1 += arr[i]
		maxSum = max(maxSum, sum1)
		sum1 = 0 if sum1 < 0 else sum1

	return maxSum

if __name__ == '__main__':
	arr = [1, -2, 3, 5, -2, 6, -1] # 12
	print(maxSum(arr))