"""给定一个数组1，3，2，4，3，计算所有小和
"""
import random
import copy

def minSum(arr):
	if arr == None or len(arr) < 2:
		return 0

	return subMergeSort(arr, 0, len(arr)-1)

def subMergeSort(arr, l, r):
	if l >= r: return 0
	mid = l + (r-l)//2
	return subMergeSort(arr, l, mid) + subMergeSort(arr, mid+1, r) + merge(arr, l, mid, r)

def merge(arr, l, mid, r):
	res = 0

	p1, p2 = l, mid+1
	helpArr = []

	while p1 <= mid and p2 <= r:
		if arr[p1] < arr[p2]:
			res += arr[p1] * (r-p2+1) ###
			helpArr.append(arr[p1]); p1+=1
		else:
			helpArr.append(arr[p2]); p2+=1

	while p1 <= mid:
		helpArr.append(arr[p1]); p1+=1
	while p2 <= r:
		helpArr.append(arr[p2]); p2+=1

	for i in range(len(helpArr)):
		arr[l+i] = helpArr[i]

	return res


def comparator(arr):
	if arr == None and len(arr) < 2:
		return 0
	
	res = 0
	for i in range(1, len(arr)):
		for j in range(i):
			res += arr[j] if arr[j] < arr[i] else 0

	return res

def generateRandomArray(maxLen, maxVal):
	arr = []
	length = int(maxLen * random.random() + 1)
	for _ in  range(length):
		arr.append(int(maxVal * random.random() + 1))
	return arr



if __name__ == '__main__':
	interNum = 5000
	maxLen = 100
	maxVal = 100
	succeed = True

	while interNum > 0:
		interNum -= 1

		arr = generateRandomArray(maxLen, maxVal)
		arrCopy = copy.copy(arr)

		if comparator(arr) != minSum(arrCopy):
			succeed = False
			break
	print(arrCopy)

	print('nice!' if succeed == True else 'Fucking Fucked!')