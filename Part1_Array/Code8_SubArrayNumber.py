"""给定数组arr和整数num，返回有多少个子数组满足如下情况：
max(arr[i...j]) - min(arr[i...j]) <= num

要求时间复杂度: O(N)
"""
def getNum_1(arr, num):
	"""普通解法 o(N^2)
	"""
	if arr == None or len(arr) == 0 or num <= 0:
		return None

	res = 0
	length = len(arr)
	for i in range(length):
		for j in range(i, length):
			tempArr = arr[i:j+1]
			res = res + 1 if max(tempArr) - min(tempArr) <= num else res

	return res


def getNum_2(arr, num):
	"""最优解法 O(N)
	"""
	if arr == None or len(arr) == 0 or num <= 0:
		return None

	l, r = 0, 0
	qmax, qmin = [], []
	res = 0

	while l < len(arr):
		while r < len(arr):
			# qmax
			while len(qmax) != 0 and arr[qmax[-1]] <= arr[r]:
				qmax.pop(-1)
			qmax.append(r)

			# qmin
			while len(qmin) != 0 and arr[qmin[-1]] >= arr[r]:
				qmin.pop(-1)
			qmin.append(r)

			if arr[qmax[0]] - arr[qmin[0]] > num:
				break
			else:
				r += 1

		if len(qmax) != 0 and qmax[0] == l:
			qmax.pop(0)
		if len(qmin) != 0 and qmin[0] == l:
			qmin.pop(0)

		res += (r - l)
		l += 1

	return res

"""双端队列 实现 窗口最大值和最小值的更新结构
"""


if __name__ == '__main__':

	arr = [1,2,3,4,5,6,7,8,9]
	num = 6
	print(getNum_1(arr, num))
	print(getNum_2(arr, num))
