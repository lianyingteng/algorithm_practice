"""给定两个字符串str1和str2，判断两个字符串是否互为变形词

变形词： 字符种类一样，字符出现的次数也一样
"""
def isDeformation(str1, str2):

	if str1 == None or str2 == None or len(str1) != len(str2):
		return False

	# 假设出现的字符编码值在0-255之间
	helpArr = [0] * 256
	for i in str1:
		helpArr[ord(i)] += 1

	for i in str2:
		helpArr[ord(i)] -= 1
		if helpArr[ord(i)] < 0:  # 
			return False

	return True


if __name__ == '__main__':
	str1 = '123'
	str2 = '231'
	print(isDeformation(str1, str2))

	str1 = '123'
	str2 = '238'
	print(isDeformation(str1, str2))