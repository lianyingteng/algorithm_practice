"""折纸问题：给定一个输入参数N，代表纸条都从下边向上方连续对折N次，请从上到下打印所有折痕的方向。"""

def printAllFolds(n):
	"""主进程"""
	pocessing(1, n, True)

def pocessing(start, end, dowm):
	"""递归子进程"""
	if start > end:
		return None

	pocessing(start+1, end, True)
	print("dowm" if dowm else "up", end=' ')
	pocessing(start+1, end, False)

if __name__ == '__main__':
	n = 3
	printAllFolds(n)
	print()