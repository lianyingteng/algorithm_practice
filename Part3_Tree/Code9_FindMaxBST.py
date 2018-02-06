"""给定一颗二叉树的头结点head，已知其中所有节点的值都不一样，找到含有节点数最多的搜索二叉树，
并返回这颗子树的头结点。

要求： 时间复杂度 O(N)，额外空间复杂度O(h)"""

def biggestSubBST(head):
	return posOrder(head)[0]


def posOrder(head):
	"""返回四个信息

		最大搜索二叉树：头结点、 节点数、 最小值、 最大值
	"""
	if head == None:
		return None, 0, float('inf'), float('-inf')

	lBST, lSize, lMin, lMax = posOrder(head.left)
	rBST, rSize, rMin, rMax = posOrder(head.right)

	minVal = min(lMin, head.value)
	maxVal = max(rMax, head.value)

	if lBST == head.left and rBST == head.right and lMax < head.value and rMin > head.value:
		return head, (lSize + rSize + 1), minVal, maxVal

	if lSize > rSize:
		return lBST, lSize, lMin, lMax

	return rBST, rSize, rMin, rMax


class Node(object):
	"""二叉树的节点结构
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

"""对二叉树后序遍历的改写"""