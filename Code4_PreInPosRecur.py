"""二叉树的先序、中序、后序遍历的实现
	（递归形式和非递归形式）	
"""
class Node(object):
	"""二叉树节点表示
	"""
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None


### 非递归实现

def preOrderUnRecur(head):
	"""先序遍历
	"""
	if head == None:
		return None

	stack = []
	stack.append(head)
	while len(stack) != 0:
		cur = stack.pop(-1)
		print(cur.value, end=' ')

		if cur.right != None:
			stack.append(cur.right)
		if cur.left != None:
			stack.append(cur.left)


def inOrderUnRecur(head):
	"""中序遍历
	"""
	if head == None:
		return None

	stack = []
	cur = head
	while len(stack) != 0 or cur != None:

		if cur != None:
			stack.append(cur)
			cur = cur.left
		else:
			cur = stack.pop(-1)
			print(cur.value, end=' ')
			cur = cur.right


def posOrderUnRecur(head):
	"""后序遍历
	"""
	if head == None:
		return None

	help1 = []
	help1.append(head)
	stack = []
	while len(help1) != 0:
		head = help1.pop()
		stack.append(head)

		if head.left != None:
			help1.append(head.left)
		if head.right != None:
			help1.append(head.right)

	while len(stack) != 0:
		print(stack.pop().value, end=' ')



### 递归实现

def preOrderRecur(head):
	"""先序遍历
	"""
	if head == None:
		return None

	print(head.value, end=' ')
	preOrderRecur(head.left)
	preOrderRecur(head.right)


def inOrderRecur(head):
	"""中序遍历
	"""
	if head == None:
		 return None

	inOrderRecur(head.left)
	print(head.value, end=' ')
	inOrderRecur(head.right)


def posOrderRecur(head):
	"""后序遍历
	"""
	if head == None:
		return None

	posOrderRecur(head.left)
	posOrderRecur(head.right)
	print(head.value, end=' ')



if __name__ == '__main__':
	head = Node(5)
	head.left = Node(3)
	head.right = Node(8)
	head.left.left = Node(2)
	head.left.right = Node(4)
	head.left.left.left = Node(1)
	head.right.left = Node(7)
	head.right.left.left = Node(6)
	head.right.right = Node(10)
	head.right.right.left = Node(9)
	head.right.right.right = Node(11)

	print("pre order: ")
	preOrderRecur(head)
	print()
	preOrderUnRecur(head)
	print()

	print("in order: ")
	inOrderRecur(head)
	print()
	inOrderUnRecur(head)
	print()


	print("pos order: ")
	posOrderRecur(head)
	print()
	posOrderUnRecur(head)
	print()