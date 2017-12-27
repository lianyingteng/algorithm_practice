import random
import copy

def partition(arr, l, r):
	less, more = l-1, r
	
	while l < more:
		if arr[l] < arr[r]:
			less += 1
			arr[less], arr[l] = arr[l], arr[less]
			l += 1
		elif arr[l] > arr[r]:
			more -= 1
			arr[more], arr[l] = arr[l], arr[more]
		else:
			l += 1

	arr[more], arr[r] = arr[r], arr[more]

	return less+1, more


def subQuickSort(arr, l, r):
	if l >= r:
		return None

	randNum = l + int(random.random() * (r - l + 1))
	arr[r], arr[randNum] = arr[randNum], arr[r]
	[begin, end] = partition(arr, l, r)

	subQuickSort(arr, l, begin-1)
	subQuickSort(arr, end+1, r)


def quickSort(arr):
	if arr == None or len(arr) < 2:
		return None

	length = len(arr)
	subQuickSort(arr, 0, length-1)


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

                arr.sort()
                quickSort(arrCopy)

                if arr != arrCopy:
                        succeed = False
                        break
        print(arrCopy)

        print('nice!' if succeed == True else 'Fucking Fucked!')