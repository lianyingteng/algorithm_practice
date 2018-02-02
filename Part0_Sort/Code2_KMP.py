"""给定两个字符串str1 和 match，长度分别是N和M。实现一个算法，
如果字符串str1中含有子串match，则返回match在str1中的开始位置，不含有则返回-1
"""
def getNextArray(match):
	"""基于match串生成next数组
	"""
	if len(match) == 1:
		return [-1]

	nextArr = [-1, 0]
	cn = 0  # cn 表示前一个字符最长匹配前缀的下一个字符位置(前一个字符最长匹配前缀的长度)
	while len(nextArr) < len(match):
		if match[len(nextArr)-1] == match[cn]:
			cn += 1
			nextArr.append(cn)
		elif cn > 0:
			cn = nextArr[cn]
		else:
			nextArr.append(0)

	return nextArr


def getIndexOf(st1, match):
	"""KMP算法
	"""
	if str1 == None or match == None or len(match) < 1 or len(str1) < len(match):
		return -1

	nextArr = getNextArray(match)

	i1, i2 = 0, 0
	while i1 < len(str1) and i2 < len(match):
		if str1[i1] == match[i2]:
			i1 += 1; i2 += 1
		elif nextArr[i2] == -1:
			i1 += 1
		else:
			i2 = nextArr[i2]

	return (i1 - len(match)) if i2 == len(match) else -1



if __name__ == '__main__':
	str1 = "abcabcababaccc"
	match = "acc"
	print(getIndexOf(str1, match))