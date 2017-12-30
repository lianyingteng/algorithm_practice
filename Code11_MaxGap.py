"""最大间隔问题： 无序数组，返回排完序之后相邻两数的最大差值！要求：时间复杂度O(n)
"""
import sys
import random
import copy
def generateRandomArray(maxLen, maxSize):
	arr = []
	for _ in range(int(random.random() * maxLen + 1)):
		arr.append(int(random.random() * maxSize + 1))
	return arr
	
def maxGap(arr):
	length = len(arr)
	maxVal, minVal = -sys.maxsize, sys.maxsize
	for i in range(length):
		maxVal, minVal = max(maxVal, arr[i]), min(minVal, arr[i])
	
	if maxVal == minVal: return 0  ###【重点】

	bNum = length + 1 
	mins = [maxVal] * bNum
	maxs = [minVal] * bNum
	hasNum = [False] * bNum
	for i in range(length):
		bid = (arr[i]-minVal) * length // (maxVal-minVal) ### 
		mins[bid] = min(mins[bid], arr[i])
		maxs[bid] = max(maxs[bid], arr[i])
		hasNum[bid] = True

	res = 0
	lastMax = maxs[0]
	for bid in range(1, bNum):
		if hasNum[bid]:
			res = max(res, mins[bid]-lastMax)
			lastMax = maxs[bid]

	return res


def comparator(arr):
	arr.sort()
	res = 0
	for i in range(1, len(arr)):
		res = max(res, arr[i]-arr[i-1])

	return res

if __name__ == '__main__':
	iterNum = 5000
	maxLen = 100
	maxSize = 100
	succeed = True

	while iterNum > 0:
		iterNum -= 1

		arr = generateRandomArray(maxLen, maxSize)
		arr_copy = copy.copy(arr)

		res = maxGap(arr)
		res1 = comparator(arr_copy)

		if res != res1:
			succeed = False
			break

	print('nice!' if succeed == True else 'Fucking Ficked!')












