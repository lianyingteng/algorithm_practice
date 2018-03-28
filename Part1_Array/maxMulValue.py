def getMaxMul(arr):

	if arr == None or len(arr) < 3:
		return None


	max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
	min1, min2 = float('inf'), float('inf')

	for i in range(len(arr)):

		if arr[i] > max1:
			max3 = max2
			max2 = max1
			max1 = arr[i]

		elif arr[i] > max2:
			max3 = max2
			max2 = arr[i]

		elif arr[i] > max3:
			max3 = arr[i]


		if arr[i] < min1:
			min2 = min1
			min1 = arr[i]

		elif arr[i] < min2:
			min2 = arr[i]


	return max(
		max1 * max2 * max3,
		max1 * min1 * min2
		)


"""
3个数的最大乘积

给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1) 
输入描述:
无序整数数组A[n]

输出描述:
满足条件的最大乘积

输入例子1:
3 4 1 2

输出例子1:
24

最大乘积为最大的三个数字乘积或者最大一个数字和最小两个数字乘积，负负得正。

注意此题需要用long

第一种方法是排序，取得最值

第二种方法是使用五个变量
"""
