"""问题1: 

	给定一个整数N，返回斐波那契数列的第N项？
"""

def fibonacci_1(n):
	"""暴力递归 时间复杂度 O(2^n)
	"""
	if n < 0:
		raise ValueError("The n is illegal!")

	if n < 3:
		return 1

	return fibonacci_1(n - 1) + fibonacci_1(n - 2)


def fibonacci_2(n):
	"""动态规划 时间复杂度 O(n)
	"""
	if n < 0:
		raise ValueError("The n is illegal!")

	if n < 3:
		return 1

	a, b = 1, 1
	for _ in range(3, n+1):
		tmp = a + b
		a = b
		b = tmp

	return tmp


def fibonacci_3(n):
	"""矩阵乘法 时间复杂度 O(logn) P184
	"""
	pass


"""问题2: 

	给定整数N，代表台阶数，一次可以跨2个或者1个台阶，返回有多少种走法？
"""

def treppe_1(n):
	"""暴力递归
	"""
	if n < 1:
		raise ValueError("The input is illegal! ")

	if n < 3 : 
		return n

	return treppe_1(n-1) + treppe_1(n-2)


def treppe_2(n):
	"""动态规划
	"""
	if n < 1:
		raise ValueError("The input is illegal! ")

	if n < 3 : 
		return n

	a, b = 1, 2
	for _ in range(3, n+1):
		tmp = a + b
		a = b
		b = tmp

	return tmp


"""问题3: 

	假设农场中成熟的母牛每年只会生1头小母牛，并且永远不会死。 第一年农场有一只成熟的母牛，
	从第二年开始，母牛开始生小母牛。每只小母牛3年之后成熟又可以生小母牛。给定整数N，求N年
	后牛的数量？
"""
def cow_1(n):
	"""暴力递归
	"""
	if n < 1:
		raise ValueError("The input is illegal!")

	if n <= 3: return n

	return cow_1(n-1) + cow_1(n-3)


def cow_2(n):
	"""动态规划
	"""
	if n < 1:
		raise ValueError("The input is illegal!")

	if n <= 3: return n

	prepre = 1
	pre = 2
	res = 3
	for i in range(4, n+1):
		tmp = res
		res = res + prepre
		prepre = pre
		pre = tmp

	return res

if __name__ == '__main__':
	n = 13
	print(fibonacci_1(n))
	print(fibonacci_2(n))
	print("-------")
	print(treppe_1(n))
	print(treppe_2(n))
	print("-------")
	print(cow_1(n))
	print(cow_2(n))
