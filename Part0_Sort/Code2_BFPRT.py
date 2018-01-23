"""BFPRT: 在无序数组中找到前k个最小的数, K从 1 到 N"""

def getMinKNumsByBFPRT(arr, k):
	"""得到前k个最小的数
	"""
	if k < 1 or k > len(arr):
		return None

	minKth = getMinKthByBFPRT(arr, k)

	res = []
	for i in range(len(arr)):
		if arr[i] < minKth:
			res.append(arr[i])
	while len(res) < k:
		res.append(minKth)

	return res

def getMinKthByBFPRT(arr, k):
	"""得到第k个小的数
	"""
	arrCopy = copy.copy(arr)
	return select(arrCopy, 0, len(arrCopy)-1, k-1)

def select(arr, begin, end, index):
	""""BFPRT主程序
	"""
	if begin == end:
		return arr[begin]

	pivot = getMedianOfMedians(arr, begin, end)
	pivotRange = partition(arr, begin, end, pivot)

	if index >= pivotRange[0] and index <= pivotRange[1]:
		return arr[index]
	elif index < pivotRange[0]:
		return select(arr, begin, pivotRange[0]-1, index)
	else:
		return select(arr, pivotRange[1]+1, end, index)

def getMedianOfMedians(arr, begin, end):
	"""得到数组中位数的中位数
	"""
	num = end - begin + 1
	offset = 0 if num%5==0 else 1

	mArr = [0] * (num//5 + offset)
	for i in range(len(mArr)):
		beginI = begin + i * 5
		endI = min(end, beginI+4)
		mArr[i] = getMedian(arr, beginI, endI)

	return select(mArr, 0, len(mArr)-1, len(mArr)//2)


def getMedian(arr, begin, end):
	"""通过插入排序得到，中位数
	"""
	insertSort(arr, begin, end)
	sum1 = begin + end  ###
	mid = (sum1 // 2) + (sum1 % 2)
	return arr[mid]

def insertSort(arr, begin, end):
	"""插入排序
	"""
	for un_i in range(begin+1, end+1):
		o_i = un_i - 1
		while o_i >= 0 and arr[o_i] > arr[o_i + 1]:
			arr[o_i], arr[o_i+1] = arr[o_i+1], arr[o_i]
			o_i -= 1

def partition(arr, begin, end, p):
	"""划分过程
	"""
	less = begin - 1
	more = end + 1
	cur = begin  ####

	while cur < more:
		if arr[cur] < p:
			less += 1
			arr[less], arr[cur] = arr[cur], arr[less]
			cur += 1
		elif arr[cur] > p:
			more -= 1
			arr[more], arr[cur] = arr[cur], arr[more]
		else:
			cur += 1

	return less + 1, more - 1


def generateRandomArray(maxLen, maxVal):
	length = int(random.random() * maxLen) + 1

	arr = []
	for _ in range(length):
		arr.append(int(random.random() * maxVal) + 1)
	return arr


import copy
import random

if __name__ == '__main__':
	iterNum = 5000
	maxLen = 100
	maxVal = 100
	succeed = True

	for _ in range(iterNum):
		arr = generateRandomArray(maxLen, maxVal)
		arrCopy = copy.copy(arr)
		k = int(random.random() * len(arr)) + 1
		
		res1 = getMinKNumsByBFPRT(arr, k)
		res1.sort()
		arrCopy.sort()
		res2 = arrCopy[:k]

		if res1 != res2:
			succeed = False
			break

	print("nice" if succeed == True else "fucking fucked!")