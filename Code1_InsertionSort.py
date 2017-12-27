import random
import copy

def insertionSort(arr, length):
	"""
	插入排序
	"""
	if arr == None or length < 2:
		return None

	for un_i in range(1, length):
		o_i = un_i - 1
		while o_i >= 0 and arr[o_i] > arr[o_i+1]:
			arr[o_i], arr[o_i+1] = arr[o_i+1], arr[o_i]
			o_i -= 1


def generateRandomArray(maxSize, maxValue):

	arr = []
	length = int(maxSize*random.random()+1)

	for _ in range(length):
		arr.append(int(maxValue*random.random() + 1))

	return arr


if __name__ == '__main__':
	interNum = 5000
	maxSize = 100
	maxValue = 1000
	succeed = True

	while interNum > 0:
		interNum -= 1
		arr = generateRandomArray(maxSize, maxValue)
		arrCopy = copy.copy(arr)

		arr.sort()
		insertionSort(arrCopy, len(arrCopy))

		if arr != arrCopy:
			succeed = False
			break

	print('nice!' if succeed == True else 'Fucking Fucked!')

	print(arr)
	print(arrCopy)

