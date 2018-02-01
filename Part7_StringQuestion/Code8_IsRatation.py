"""判断两个字符串是否互为旋转词"""

def isRatation(a, b):
	if a == None or b == None or len(a) != len(b):
		return False

	a2 = a + a
	return getIndexOf(a2, b) != -1


def getIndexOf(str1, match):
	"""KMP算法
	"""
	nextArr = getNextArr(match)

	i1, i2 = 0, 0
	while i1 < len(str1) and i2 < len(match):
		if str1[i1] == match[i2]:
			i1 += 1; i2 += 1
		elif nextArr[i2] == -1:
			i1 += 1
		else:
			i2 = nextArr[i2]

	return i1 - len(match) if i2 == len(match) else -1



def getNextArr(match):
	"""得到next数组
	"""
	if len(match) == 1:
		return [-1]

	nextArr = [-1, 0]
	cn = 0 # cn 表示前一个字符最长匹配前缀的下一个字符位置
	while len(nextArr) < len(match):
		if match[len(nextArr)-1] == match[cn]:
			cn += 1
			nextArr.append(cn)

		elif cn > 0:
			cn = nexArr[cn]

		else:
			nextArr.append(0)

	return nextArr


if __name__ == '__main__':
	a, b = 'cdab', 'abcd' # true
	print(isRatation(a, b))
	print('-----')

	a, b = '1ab2', 'ab12' # false
	print(isRatation(a, b))
	print('-----')

	a, b = '2ab1', 'ab12' # true
	print(isRatation(a, b))
	print('-----')