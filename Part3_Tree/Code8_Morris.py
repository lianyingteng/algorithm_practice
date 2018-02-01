"""
给定一颗二叉树的头结点head，完成二叉树的先序、中序和后序遍历。
如果二叉树的节点数为N，要求时间复杂度为O(N)，额外空间复杂度为O(1)。
"""
def morrisPre(head):
	"""Morris先序遍历
	"""
	if head == None: return None

	cur = head
	while cur != None:
		tmp = cur.left
		if tmp != None:
			while tmp.right != None and tmp.right != cur:
				tmp = tmp.right

			if tmp.right == None:
				print(cur.value, end=' ')
				tmp.right = cur
				cur = cur.left
				continue

			if tmp.right == cur:
				tmp.right = None
		else:
			print(cur.value, end=' ')

		cur = cur.right


def morrisIn(head):
	"""Morris中序遍历
	"""
	if head == None: return None

	cur = head
	while cur != None:
		tmp = cur.left
		if tmp != None:
			while tmp.right != None and tmp.right != cur:
				tmp = tmp.right

			if tmp.right == None:
				tmp.right = cur
				cur = cur.left
				continue

			if tmp.right == cur:
				tmp.right = None

		print(cur.value, end=' ')
		cur = cur.right


def morrisPos(head):
	"""Morris后序遍历
	"""
	if head == None: return None

	cur = head
	while cur != None:
		tmp = cur.left
		if tmp != None:
			while tmp.right != None and tmp.right != cur:
				tmp = tmp.right

			if tmp.right == None:
				tmp.right = cur
				cur = cur.left
				continue

			if tmp.right == cur:
				tmp.right = None
				printEdge(cur.left)

		cur = cur.right

	printEdge(head)


def printEdge(head):
	"""逆序打印右边界
	"""
	tail = reverseEdge(head)

	cur = tail
	while cur != None:
		print(cur.value, end=' ')
		cur = cur.right

	reverseEdge(tail)


def reverseEdge(cur):
	"""逆序操作
	"""
	pre = None
	nex = None
	while cur != None:
		nex = cur.right
		cur.right = pre
		pre = cur
		cur = nex

	return pre


class Node(object):
	"""二叉树的节点结构
	"""
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

"""Morris遍历

实质： 通过底层节点（叶子节点）指向None的空闲指针，指回上层的某个节点

过程：
	1. 假设头结点为head，让head的《左子树中最右节点》的right指针指向head。
	然后在其左子树中重复该步骤，直到遇到叶子结点（无左子树），记为node，进入步骤2
	
	2. 从node开始通过每个节点的right指针进行移动，并以此打印。 假设当前移动到的节点
	记为cur
		1) cur《左子树中最右节点》的right指针指向cur（说明第二次到达cur）
			令cur《左子树中最右节点》的right指针指向None; 
			通过右指针移动 cur = cur.right

		2) cur《左子树中最右节点》的right指针指向None（说明第一次到达cur）
			重复1步骤，即：
			令cur《左子树中最右节点》的right指针指向cur
			通过左指针移动 cur = cur.left

	3. cur移动到空，整个过程结束
"""

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
	morrisPre(head)
	print()

	print("in order: ")
	morrisIn(head)
	print()

	print("pos order: ")
	morrisPos(head)
	print()