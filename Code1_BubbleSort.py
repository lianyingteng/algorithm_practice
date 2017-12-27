import random

def bubbleSort(arr, length):
	"""
	冒泡排序
	"""

	if arr == None or length < 2:
		return None

	while length > 0:
		length -= 1

		for i in range(length):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]


def generateUnOrderArr(length):
	arr = []

	for _ in range(length):
		arr.append(int(random.random()*100))

	return arr



if __name__ == '__main__':
	i = 0
	chios = True
	while i < 5000:
		i += 1

		arr = generateUnOrderArr(int(random.random() * 100))
		arrCopy = arr.copy()

		arr.sort()
		bubbleSort(arrCopy, len(arrCopy))

		if arr != arrCopy:
			chios = False
			break

	print("yes" if chios == True else "err")
	print(arr)
	print(arrCopy)



