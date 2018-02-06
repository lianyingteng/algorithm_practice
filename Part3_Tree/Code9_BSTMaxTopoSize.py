"""给定一棵二叉树的头结点head，已知所有节点的值都不一样，
返回其中最大的且符合搜索二叉树条件的最大拓扑结构的大小P119"""

####################《递归》########################
def bstTopoSize1(head):
	"""时间复杂度 O(N^2)

	给定头结点，返回该头节点下的最大拓扑大小
	"""
	if head == None:
		return 0

	max1 = maxTopo(head, head)
	max1 = max(bstTopoSize1(head.left), max1)
	max1 = max(bstTopoSize1(head.right), max1)
	return max1

def maxTopo(head, node):
	"""node及其子树可以为 以head为头的BST 提供多少节点拓扑
	"""

	if head != None and node != None and isBSTNode(head, node, node.value):
		return maxTopo(head, node.left) + maxTopo(head, node.right) + 1

	return 0

def isBSTNode(head, node, value):
	"""判断node是否可以构成 以head为头的BST 的拓扑
	"""
	if head == None:
		return False

	if head == node:
		return True

	return isBSTNode(head.left if head.value > value else head.right
		, node, value)



class Node(object):
	"""二叉树的节点结构
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None