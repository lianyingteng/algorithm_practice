"""最长无重复子串的长度"""

def maxUnique(string):

	if string == None or string == "":
		return 0

	arr = list(string)
	hMap = [-1] * 256 # 字符编码范围

	maxLen = 0
	pre = -1
	for i in range(len(arr)):
		pre = max(
			pre, 
			hMap[ord(arr[i])]
			)

		maxLen = max(
			maxLen,
			i - pre
			)

		hMap[ord(arr[i])] = i

	return maxLen

string = "aabcb"
print(maxUnique(string))
