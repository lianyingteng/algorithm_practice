"""全排列问题 """
def printAllPermutation_1(string):
	if string == None:
		return None

	arr = list(map(lambda i: i, string))
	process_1(arr, 0)


def process_1(arr, index):
	if index == len(arr):
		print("".join(arr))
		return None

	for i in range(index, len(arr)):
		arr[i], arr[index] = arr[index], arr[i]
		process_1(arr, index + 1)
		arr[i], arr[index] = arr[index], arr[i]



def printAllPermutation_2(string):
	"""去重
	"""
	if string == None:
		return None

	arr = list(map(lambda i:i, string))
	process_2(arr, 0)


def process_2(arr, index):
	if index == len(arr):
		print("".join(arr))
		return None

	hset = set()
	for i in range(index, len(arr)):
		if arr[i] not in hset:
			hset.add(arr[i])

			arr[i], arr[index] = arr[index], arr[i]
			process_2(arr, index+1)
			arr[i], arr[index] = arr[index], arr[i]



if __name__ == '__main__':
	string = 'abc'
	printAllPermutation_1(string)
	print("#########")
	printAllPermutation_2(string)
	
	print()
	print('--------------')
	print()

	
	string = 'acc'
	printAllPermutation_1(string)
	print("#########")
	printAllPermutation_2(string)