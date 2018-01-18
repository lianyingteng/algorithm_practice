"""较为直观打印二叉树"""
import sys
class Node(object):
	"""二叉树节点"""
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None


def printTree(head):
	"""打印二叉树"""
	length = 16 # 每个节点打印所占位数

	inOrderRecur(head, 0, 'H', length)


def inOrderRecur(head, deep, label, length):
	"""中序遍历（递归）"""
	if head == None:
		return None

	inOrderRecur(head.right, deep+1, 'v', length)

	str1 = "%s%d%s"%(label, head.value, label)
	len_l = (length - len(str1)) // 2
	len_r = length - len(str1) - len_l
	str1 = "%s%s%s%s"%(" "*(deep*length), " "*len_l, str1, " "*len_r)
	print(str1)

	inOrderRecur(head.left, deep+1, '^', length)



if __name__ == '__main__':
	head = Node(1)
	head.left = Node(-222222222)
	head.right = Node(3)
	head.left.left = Node(88)
	head.right.left = Node(55555555)
	head.right.right = Node(66)
	head.left.left.right = Node(777)
	printTree(head)

	head = Node(1)
	head.left = Node(2)
	head.right = Node(3)
	head.left.left = Node(4)
	head.right.left = Node(5)
	head.right.right = Node(6)
	head.left.left.right = Node(7)
	printTree(head)

	head = Node(1)
	head.left = Node(1)
	head.right = Node(1)
	head.left.left = Node(1)
	head.right.left = Node(1)
	head.right.right = Node(1)
	head.left.left.right = Node(1)
	printTree(head)

