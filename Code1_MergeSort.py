import random
import copy


def merge(arr, l, mid, r):
	helpArr = []
	p1, p2 = l, mid+1

	while (p1 <= mid and p2 <= r):
		if arr[p1] < arr[p2]:
			helpArr.append(arr[p1])
			p1 += 1
		else:
			helpArr.append(arr[p2])
			p2 += 1

	while p1 <= mid: 
		helpArr.append(arr[p1])
		p1 += 1

	while p2 <= r: 
		helpArr.append(arr[p2])
		p2 += 1

	for i in range(len(helpArr)):
		arr[l+i] = helpArr[i]


def subMergeSort(arr, l, r):
	if l >= r:
		return None

	mid = l + ((r-l)>>1)
	subMergeSort(arr, l, mid)
	subMergeSort(arr, mid+1, r)
	merge(arr, l, mid, r)


def mergeSort(arr):

	if arr == None or len(arr) < 2:
		return None

	subMergeSort(arr, 0, len(arr)-1)



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
                mergeSort(arrCopy)

                if arr != arrCopy:
                        succeed = False
                        break
        print(arrCopy)

        print('nice!' if succeed == True else 'Fucking Fucked!')