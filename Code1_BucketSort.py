import sys
import copy
import random

def bucketSort(arr):
	if arr == None or len(arr) < 2:
		return None

	maxVal = -sys.maxsize
	for i in range(len(arr)):
		maxVal = maxVal if maxVal > arr[i] else arr[i]

	bucket = [0] * (maxVal + 1)
	for i in range(len(arr)):
		bucket[arr[i]] += 1

	i = 0
	for j in range(len(bucket)):
		while bucket[j] > 0:
			arr[i] = j; i += 1; bucket[j] -= 1
	

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
                bucketSort(arrCopy)

                if arr != arrCopy:
                        succeed = False
                        break
        print(arrCopy)

        print('nice!' if succeed == True else 'Fucking Fucked!')