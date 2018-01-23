"""manacher算法： 返回字符串中最长回文串的长度
"""
import sys

def manacherArray(str1):
	manacherArr = []

	index = 0
	for i in range(len(str1) * 2 + 1):
		manacherArr.append('#' if i%2 == 0 else str1[index])
		if i%2 != 0: index += 1

	return manacherArr


def maxLcpsLength(str1):
	if str1 == None or len(str1) == 0:
		return 0

	mcArr = manacherArray(str1)
	mcLength = len(mcArr)
	R, C = -1, -1   # 最右回文右边界R, 及其对应的回文中心C
	maxmum = -sys.maxsize
	pArr = [0] * mcLength  # 从每个字符出发，最长回文半径
	for i in range(mcLength):
		pArr[i] = min(R-i, pArr[2*C-i]) if R > i else 1
		while i + pArr[i] < mcLength and i - pArr[i] > -1:
			if mcArr[i+pArr[i]] == mcArr[i-pArr[i]]:
				pArr[i] += 1
			else:
				break

		if i+pArr[i] > R:
			R = i + pArr[i]
			C = i

		maxmum = max(maxmum, pArr[i])

	return maxmum - 1


if __name__ == '__main__':
	str1 = "abc12344321ab"
	print(maxLcpsLength(str1))