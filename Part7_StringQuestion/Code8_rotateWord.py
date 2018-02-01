"""给定一个字符串，请在单词之间做逆序调整"""
def reverseWord(str1):
	if str1 == None or len(str1) == 0:
		return None

	arr = list(str1)
	reverse(arr, 0, len(arr) - 1)

	l, r = -1, -1
	for i in range(len(arr)):
		if arr[i] != ' ':
			l = i if i == 0 or arr[i-1] == ' ' else l
			r = i if i == len(arr) - 1 or arr[i+1] == ' ' else r

		if l != -1 and r != -1:
			reverse(arr, l, r)
			l, r = -1, -1

	return arr


def reverse(arr, l, r):
	"""数组反转
	"""
	while l <= r:
		arr[l], arr[r] = arr[r], arr[l]
		l += 1
		r -= 1



if __name__ == '__main__':
	str1 = "I am a student" # -> student a am I
	print("%s\n\t-> %s"%(
		str1,
		''.join(reverseWord(str1))
		)
	)