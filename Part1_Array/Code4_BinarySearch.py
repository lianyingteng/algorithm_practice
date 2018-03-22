"""找到有序数组中第一个大于或等于k的数"""

def findNumberIndex(arr, target):
	"""二分找数"""
	if arr == None or len(arr) == 0:
		return -1

	l, r = 0, len(arr) - 1
	res = -1
	while r > l:
		mid = l + ((r-l)>>1)
		if arr[mid] >= target:
			r = mid - 1
			res = mid if arr[mid] == target else res
		else:
			l = mid + 1

	return l if arr[l] == target else res 


if __name__ == '__main__':
	arr = [1, 3, 5, 8, 10, 10, 10, 10, 10, 10, 10, 14, 16, 19, 21, 43]
	k = 14

	ind = findNumberIndex(arr, k)
	print("index: %d, value: %d"%(ind, arr[ind]) if ind != -1 else None)
