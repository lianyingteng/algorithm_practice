class Node(object):
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None



"""返回二叉树两个节点的最近公共祖先"""
def lowestAncestor(head, o1, o2):
	if head == None or head == o1 or head == o2:
		return head

	left = lowestAncestor(head.left, o1, o2)
	right = lowestAncestor(head.right, o1, o2)

	if left != None and right != None:
		return head

	return left if left != None else right
