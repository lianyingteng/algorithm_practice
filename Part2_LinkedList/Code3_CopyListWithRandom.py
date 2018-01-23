class Node(object):
	def __init__(self, val):
		self.value = val
		self.next = None
		self.rand = None


def copyListWithRandom2(head):
	"""最优解法： 额外空间复杂度O(1)
	"""
	if head == None: return None

	# 整合
	cur = head
	tmp = None
	while cur != None:
		tmp = cur.next
		cur.next = Node(cur.value)
		cur.next.next = tmp
		cur = tmp

	# 设置copy结点的rand指针
	cur = head
	curCopy = None
	while cur != None:
		tmp = cur.next.next
		curCopy = cur.next
		curCopy.rand = cur.rand.next if cur.rand != None else None
		cur = tmp

	# 拆分
	copyHead = head.next
	cur = head
	while cur != None:
		tmp = cur.next.next
		curCopy = cur.next
		cur.next = tmp
		curCopy.next = tmp.next if tmp != None else None

		cur = tmp

	return copyHead




def copyListWithRandom1(head):
	"""普通解法： 额外空间复杂度O(N)
	"""
	if head == None: return None

	dict1 = dict()
	cur = head
	while cur != None:
		dict1[cur] = Node(cur.value)
		cur = cur.next

	cur = head
	while cur != head:
		dict1[cur].next = dict1[cur.next]
		dict1[cur].rand = dict1[cur.rand]

		cur = cur.next

	return dict1[head]