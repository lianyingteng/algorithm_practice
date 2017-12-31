"""将一个小字符串abcabc扩展为一个大的字符串abcabcabc，要求大字符串包含小字符串两次"""
def getStartIndex(str1):

	nextArr = [-1, 0]
	cn = 0
	while len(nextArr) < len(str1)+1:
		if str1[len(nextArr)-1] == str1[cn]:
			cn += 1
			nextArr.append(cn)
		elif cn > 0:
			cn = nextArr[cn]
		else:
			nextArr.append(cn)

	return nextArr[-1]


def answer(str1):
	if str1 == None or len(str1) == 0: return ""
	if len(str1) == 1: return str1 + str1
	if len(str1) == 2: 
		return (str1 + str1[0]) if str1[0] == str1[1] else (str1 + str1)

	return str1 + str1[getStartIndex(str1):]

if __name__ == '__main__':
	str1 = "a"
	print(answer(str1))

	str1 = "aa"
	print(answer(str1))

	str1 = "ab"
	print(answer(str1))

	str1 = "abcdabcd"
	print(answer(str1))

	str1 = "abracadabra"
	print(answer(str1))
	
