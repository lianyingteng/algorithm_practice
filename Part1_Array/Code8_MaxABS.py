"""给定一个长度为N的整型数组arr，可以将其划分成左右两部分arr[0···k], arr[k+1···N-1]
k的取值是[0, n-2)，求这些划分中方案中，左部分最大-右部分最大的绝对值中的最大值。
"""
def maxAbs1(arr):
	"""预处理数组法 
	
	时间复杂度O(n)，额外空间O(N)
	"""
	if arr == None or len(arr) == 0:
		return 0

	length = len(arr)

	lmax, rmax = [0] * length, [0] * length
	lmax[0] = arr[0]
	rmax[length-1] = arr[length-1]

	for i in range(1, len(arr)):
		lmax[i] = max(lmax[i-1], arr[i])

	for j in list(range(len(arr)-1))[::-1]:
		rmax[j] = max(rmax[j+1], arr[j])

	res = 0
	for i in range(length-1):
		res = max(
			res,
			abs(lmax[i] - rmax[i+1])
			)

	return res


def maxAbs2(arr):
	"""最优解

	时间复杂度O(n)，额外空间O(N)
	"""
	if arr == None or len(arr) == 0:
		return 0

	maxVal = float('-inf')
	for i in range(len(arr)):
		maxVal = max(
			maxVal,
			arr[i]
			)

	return maxVal - min(arr[0], arr[-1])


if __name__ == '__main__':
	arr = [2, 7, 3, 1, 1]
	print(maxAbs1(arr))
	print(maxAbs2(arr))