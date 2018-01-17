"""堆排序"""

import random
import copy

def heapify(arr, index, length):
	"""堆化
	"""
	left = 2 * index + 1
	while left < length:
		largest = left + 1 if (left+1) < length and arr[left+1] > arr[left] else left
		largest = index if arr[index] >= arr[largest] else largest

		if largest == index:
			break

		arr[largest], arr[index] = arr[index], arr[largest]
		index = largest
		left = 2 * index + 1


def insertHeap(arr, index):
	"""index位置元素插入堆
	"""
	par_i = (index - 1) // 2
	while par_i >= 0 and arr[index] > arr[par_i]:
		arr[par_i], arr[index] = arr[index], arr[par_i]
		index = par_i
		par_i = (index - 1) // 2


def heapSort(arr):
	"""堆排序
	"""
	if arr == None or len(arr) < 2:
		return arr

	length = len(arr)
	for i in range(1, length):
		insertHeap(arr, i)

	length -= 1
	arr[0], arr[length] = arr[length], arr[0]

	while length > 1:
		heapify(arr, 0, length)
		length -= 1
		arr[0], arr[length] = arr[length], arr[0]



def generateRandomArray(max_len, max_val):
	"""生成随机数组
	"""
	length = int(random.random() * max_len + 1)

	arr = []
	for _ in range(length):
		arr.append(int(random.random() * max_val + 1))

	return arr


if __name__ == '__main__':
	iterNum = 5000
	max_len = 100
	max_val = 100
	succeed = True

	while iterNum > 0:
		iterNum -= 1

		arr = generateRandomArray(max_len, max_val)
		arr_copy = copy.copy(arr)

		arr.sort()
		heapSort(arr_copy)

		if arr != arr_copy:
			succeed = False
			break

	print(arr_copy)
	print("today is a beatiful day!" if succeed else "What's the Fucked!")

