"""在数组中找到一个局部最小的位置
	
给定一个无序数组，任意相邻两数均不相等，返回一个局部最小位置
"""
def getLessIndex(arr):
	"""返回局部最小值索引
	"""
	if arr == None or len(arr) < 2:
		return -1

	if arr[0] < arr[1] or arr[len(arr)-1] < arr[len(arr)-2]:
		return 0 if arr[0] < arr[1] else len(arr)-1

	left, right = 1, len(arr) - 2 ###
	while left < right:
		mid = left + (right - left) >> 1
		if arr[mid] > arr[mid + 1]:
			left = mid + 1
		elif arr[mid] > arr[mid - 1]:
			right = mid - 1
		else:
			return mid

	return -1


if __name__ == '__main__':
	arr = [6, 5, 3, 4, 6, 7, 8]
	print(arr)

	index = getLessIndex(arr)
	print("Index: %d, value: %d"%(index, arr[index]))