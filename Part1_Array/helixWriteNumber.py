def getMatrix(n):

	matrix = []
	for _ in range(n):
		matrix.append([0] * n)

	count = 1
	for i in range(n//2 + 1):

		for j in range(i, n-i):  # 上方行
			matrix[i][j] = count
			count += 1

		for j in range(i+1, n-i-1):  # 右侧列
			matrix[j][n-i-1] = count
			count += 1

		for j in list(range(i+1, n-i))[::-1]:  # 下方行
			matrix[n-i-1][j] = count
			count += 1

		for j in list(range(i+1, n-i))[::-1]: # 左侧列
			matrix[j][i] = count
			count += 1


	for each in matrix:
		print(each)


getMatrix(5)


"""
螺旋填数

从键盘输入一个整数（1~20）

则以该数字为矩阵的大小，把1,2,3…n*n 的数字按照顺时针螺旋的形式填入其中。例如：

输入数字2，则程序输出：

1 2

4 3

输入数字3，则程序输出：

1 2 3

8 9 4

7 6 5

输入数字4，则程序输出：

1  2   3   4

12  13  14  5

11  16  15  6

10   9  8   7
"""

