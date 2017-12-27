import random

def generateRandomArray(length):
	arr = []
	for _ in range(length):
		arr.append(int(random.random() * 3))

	return arr


def partition(arr, l, r, p):
	less, more = l-1, r+1

	while l < more:
		if arr[l] < p:
			less += 1; arr[less], arr[l] = arr[l], arr[less]; l += 1
		elif arr[l] > p:
			more -= 1; arr[more], arr[l] = arr[l], arr[more]
		else:
			l += 1
	return less+1, more-1


if __name__ == '__main__':

        arr = generateRandomArray(10)
        print(arr)

        left, right = partition(arr, 0, len(arr)-1, 1)
        print(arr)
        print(left, right)