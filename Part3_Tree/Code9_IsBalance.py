"""给定二叉树的头结点head，判断这棵二叉树是否为平衡二叉树

平衡二叉树的性质：
	要么是空树
	要么任何一个节点的左右子树高度差的绝对值不超过1
"""

def isBalance(head):
	"""判断以head为头的树是否为平衡二叉树
	"""
	if head == None: return True

	isB, height = posOrder(head, 1)
	return isB


def posOrder(node, level):
	"""返回两个信息 是否是平衡二叉树、最深到哪一层

	node 表示 头结点； level 表示 当前头结点所在的层数
	"""
	if node == None: 
		return True, level

	lIsB, lH = posOrder(node.left, level+1)
	if not lIsB:
		return False, lH

	rIsB, rH = posOrder(node.right, level+1)
	if not rIsB:
		return False, rH

	if abs(lH - rH) > 1:
		return False, max(lH, rH)

	return True, max(lH, rH)