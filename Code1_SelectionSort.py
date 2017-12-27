import random 
import copy

def selectionSort(arr, length):
	"""
	选择排序
	"""
	for i in range(length-1):
		min_i = i
		for j in range(i+1, length):
			if arr[min_i] > arr[j]:
				min_i = j
		arr[i], arr[min_i] = arr[min_i], arr[i]

def generateRandomArray(maxLength, maxValue):
	arr = []
	length = int(maxLength * random.random() + 1)

	for _ in range(length):
		arr.append(int(maxValue*random.random() + 1))

	return arr


if __name__ == '__main__':
	interNum = 5000
	maxLength = 100
	maxValue = 100
	succeed = True

	while interNum > 0:
		interNum -= 1
		arr = generateRandomArray(maxLength, maxValue)
		arrCopy = copy.copy(arr)

		arr.sort()
		selectionSort(arrCopy, len(arrCopy))

		if arr != arrCopy:
			succeed = False
			break

	print('nice!' if succeed == True else 'Fucking Fucked!')

	arr = generateRandomArray(maxLength, maxValue)
	print(arr)
	selectionSort(arr,len(arr))
	print(arr)
