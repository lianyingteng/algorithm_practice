"""查找前k个最小的数，用堆排序实现 【注：没有BFPRT好】
"""

def getMinKNumsByHeap(arr, k):
	"""通过建立k个元素大根堆 找到无序数组中 前k个最小的数
	"""
	if k < 1 or k > len(arr):
		return None

	KHeap = [0] * k
	for i in range(k):
		heapInsert(KHeap, arr[i], i)

	for i in range(k, len(arr)):
		if arr[i] < KHeap[0]:
			KHeap[0] = arr[i]
			heapity(KHeap, 0, k)

	return KHeap

def heapInsert(arr, val, index):
	"""向堆中插入元素， 然后将其调整为大根堆
	"""
	arr[index] = val

	while index != 0:  ####
		parent = (index-1) // 2

		if arr[parent] < arr[index]:
			arr[parent], arr[index] = arr[index], arr[parent]
			index = parent
		else:
			break

def heapity(arr, index, heapSize):
	"""堆化
	"""
	lchild = 2 * index + 1
	rchild = 2 * index + 2

	while lchild < heapSize:
		largest = rchild if rchild < heapSize and arr[rchild] > arr[lchild] else lchild
		if 	arr[largest] > arr[index]:
			arr[largest], arr[index] = arr[index], arr[largest]
			index = largest

			lchild = 2 * index + 1
			rchild = 2 * index + 2
		else:
			break



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

