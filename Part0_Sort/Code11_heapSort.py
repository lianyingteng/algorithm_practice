"""查找前k个最小的数，用堆排序实现 【注：没有BFPRT好】
"""

def getMinKNumsByHeap(arr, k):
	"""通过建立k个元素大根堆 找到无序数组中 前k个最小的数
	"""
	if arr == None or k <= 0 or len(arr) <= k:
		return arr

	res = [arr[0]]
	for i in range(1, k):
		res.append(arr[i])
		insertHeap(res, i)

	for i in range(k, len(arr)):
		if res[0] > arr[i]:
			res[0] = arr[i]
			heapify(res, 0, k)

	return res


def insertHeap(arr, index):
	parent = (index-1) >> 1
	while parent >= 0 and arr[parent] < arr[index]:
		arr[parent], arr[index] = arr[index], arr[parent]
		index = parent
		parent = (index-1) >> 1


def heapify(arr, index, length):

	left = 2 * index + 1
	while left < length:
		largest = left+1 if left+1 < length and arr[left+1] > arr[left] else left
		largest = index if arr[index] >= arr[largest] else largest

		if largest == index:
			break

		arr[index], arr[largest] = arr[largest], arr[index]
		index = largest
		left = 2 * index + 1



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
		
		res1 = getMinKNumsByHeap(arr, k)
		res1.sort()
		arrCopy.sort()
		res2 = arrCopy[:k]

		if res1 != res2:
			succeed = False
			break

	print("nice" if succeed == True else "fucking fucked!")
	print(res1)
	print(res2)

