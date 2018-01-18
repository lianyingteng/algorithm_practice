"""在二叉树中找到一个节点的后继节点
	
后继节点：中序遍历时，该节点的下一个节点
"""
class Node(object):
	"""二叉树的节点结构"""
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None
		self.parent = None


def getNextNode(node):
	"""得到后继节点"""
	if node == None:
		return None

	if node.right != None:
		return getLeftMost(node.right)

	cur = node
	parent = node.parent
	while parent != None and parent.left != node:
		node = parent
		parent = node.parent

	return parent


def getLeftMost(node):
	"""得到右子树最左节点"""
	cur = node
	while cur.left != None:
		cur = cur.left

	return cur



if __name__ == '__main__':

	head = Node(6)
	head.parent = None
	head.left = Node(3)
	head.left.parent = head
	head.left.left = Node(1)
	head.left.left.parent = head.left
	head.left.left.right = Node(2)
	head.left.left.right.parent = head.left.left
	head.left.right = Node(4)
	head.left.right.parent = head.left;
	head.left.right.right = Node(5)
	head.left.right.right.parent = head.left.right
	head.right = Node(9)
	head.right.parent = head
	head.right.left = Node(8)
	head.right.left.parent = head.right
	head.right.left.left = Node(7)
	head.right.left.left.parent = head.right.left
	head.right.right = Node(10)
	head.right.right.parent = head.right

	test = head.left.left
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.left.left.right;
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.left
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.left.right
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.left.right.right
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.right.left.left
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.right.left
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.right
	print("%d next: %d"%(test.value, getNextNode(test).value))
	test = head.right.right # 10's next is null
	print("%d next:"%(test.value), end=' ')
	print(getNextNode(test))
