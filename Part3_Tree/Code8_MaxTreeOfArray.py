"""给定一个没有重复元素的数组arr，写出生成这个数组的MaxTree的函数 P22

要求： 时间复杂度 O(N)，额外空间复杂度 O(N)

MaxTree的定义：
1) 数组必须没有重复元素
2) MaxTree是一颗二叉树，数组的每一个值对应一个二叉树的节点
3) 包含MaxTree树在内且在其中的每一颗子树上，值最大的节点都是树的头
"""
def getMaxTree(arr):
	"""主程序
	"""
	if arr == None or len(arr) == 0:
		return None

	nArr = []
	for i in range(len(arr)):
		nArr.append(Node(arr[i]))

	stack = []
	lBigMap, rBigMap = dict(), dict() # 左右两段第一大值map

	# 找到每个数左侧第一个比它大的数
	for i in range(len(nArr)):
		curNode = nArr[i]
		while len(stack) != 0 and stack[-1].value < curNode.value:
			popStackSetMap(stack, lBigMap)
		stack.append(cur)

	while len(stack) != 0:
		popStackSetMap(stack, lBigMap)

	# 找个每个数的右侧第一个比它大的数
	for i in list(range(len(nArr)))[::-1]:
		curNode = nArr[i]
		while len(stack) != None and stack[-1].value < curNode.value:
			popStackSetMap(stack, rBigMap)
		stack.append(curNode)

	while len(stack) != 0:
		popStackSetMap(stack, rBigMap)

	# 生成maxTree树
	head = None
	for i in range(len(nArr)):
		curNode = nArr[i]
		leftMax = lBigMap[curNode]
		rightMax = rBigMap[curNode]

		if leftMax == None and rightMax == None:
			head = curNode

		elif leftMax == None:
			if rightMax.left == None:
				rightMax.left = curNode
			else:
				rightMax.right = curNode

		elif rightMax == None:
			if leftMax.left == None:
				leftMax.left = curNode
			else:
				leftMax.right = curNode

		else:
			parent = leftMax if leftMax.value < rightMax.value else rightMax
			if parent.left == None:
				parent.left = curNode
			else:
				parent.right = curNode

	return head

def popStackSetMap(stack, bigMap):
	"""设置 大值 map
	"""
	popNode = stack.pop(-1)
	if len(stack) == 0:
		bigMap[popNode] = None
	else:
		bigMap[popNode] = stack[-1]


class Node(object):
	"""二叉树节点结构
	"""
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None 


"""建树原则
1) 每一个数的父节点是它左边第一个比它大的数和它右边第一个比它大的数中，较小的那一个。
2) 如果一个数左侧和右侧都没有比它大的数，那么这个数是maxTree的头结点
"""