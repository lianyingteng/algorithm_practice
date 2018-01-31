"""给定一个整型矩阵matrix，其中的值只有0和1两种。求其中取值全为1的子矩阵中，
最大矩形1的数量？  P26

时间复杂度 O(N*M)
"""

def maxRecSize(matrix):
	"""最大矩形size
	"""
	if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
		return None

	maxArea = 0
	row, col = len(matrix), len(matrix[0])
	height = [0] * col # 以每行作为结尾时，连续1的数量 (高度数组)
	for i in range(row):
		for j in range(col):
			height[j] = height[j] + 1 if matrix[i][j] == 1 else 0

		maxArea = max(
			maxArea, 
			maxAreaBasedOnHeight(height)
			)

	return maxArea

def maxAreaBasedOnHeight(height):
	"""基于行的height数组的 maxArea
	"""
	maxArea = 0

	stack = []
	for i in range(len(height)):
		cur = height[i]

		while len(stack) != 0 and cur <= height[stack[-1]]:
			maxArea = max(
				maxArea,
				popAndCalcArea(stack, height, i)
				)
		stack.append(i)

	while len(stack) != 0:
		maxArea = max(
				maxArea,
				popAndCalcArea(stack, height, len(height))
				)
		
	return maxArea


def popAndCalcArea(stack, height, i):
	"""stack 弹出 并计算当前弹出的 area
	"""
	popIndex = stack.pop(-1)
	k = stack[-1] if len(stack) != 0 else -1
	return (i - k - 1) * height[popIndex]


if __name__ == '__main__':
	matrix = [
	[1, 0, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 1, 0]]

	print(maxRecSize(matrix))