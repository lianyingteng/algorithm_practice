"""打印一个字符串所有子序列(不改变次序)"""

def printAllSubSequence(string):
	if string == None:
		return None

	process(string, 0, "")


def process(string, index, pre):
	if index == len(string):
		if pre != "":
			print(pre)
		return None

	process(string, index + 1, pre + string[index])
	process(string, index + 1, pre)


if __name__ == '__main__':
	
	string = '123'
	printAllSubSequence(string)