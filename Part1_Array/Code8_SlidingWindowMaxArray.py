"""给定一个数组arr 和 一整数w代表窗口大小。窗口从数组的最左侧滑向最右侧，每次仅向右滑动一个位置，
返回一个长度为 n-w+1的数组res，res[i]表示每一种窗口状态下的最大值"""

def getArrayOfMAX(arr, w):
	if arr == None or len(arr) == 0 or w < 1 or w > len(arr):
		return None

	res = []
	qmax = []
	for i in range(len(arr)):
		
		while len(qmax) != 0 and arr[qmax[-1]] <= arr[i]:
			qmax.pop(-1)
			
		qmax.append(i)

		if i - w == qmax[0]:
			qmax.pop(0)

		if i + 1 >= w:
			res.append(arr[qmax[0]])

	return res



if __name__ == '__main__':
	arr = [4, 3, 5, 4, 3, 3, 6, 7]
	w = 3
	print(getArrayOfMAX(arr, w))