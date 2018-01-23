def factorial(n):
	"""递归求阶乘
	"""
	if n == 1: 
		return n

	return n * factorial(n-1)


def factorial1(n):
	"""非递归
	"""
	result = 1
	for i in range(1, n+1):
		result *= i

	return result

if __name__ == '__main__':
	n = 6
	print(factorial(n))
	print(factorial1(n))

