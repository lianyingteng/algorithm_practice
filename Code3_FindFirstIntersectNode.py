"""寻找两个单链表相交的第一个结点的问题"""

def getIntersectNode(head1, head2):
	"""分三种情况：
		1. 都无环
		2. 都有有环
		3. 一个有环一个无环
	"""
	if head1 == None or head2 == None: return None

	loop1 = getLoopNode(head1)
	loop2 = getLoopNode(head2)

	if loop1 == None and loop2 == None:
		return noLoop(head1, head2)

	if loop1 != None and loop2 != None:
		return bothLoop(head1, loop1, head2, loop2)

	return None

def getLoopNode(head):
	"""得到单链表入环的第一个结点， 无环返回 None
	"""
	if head.next == None or head.next.next == None: return None

	fast = head.next.next
	slow = head.next
	while fast != slow:
		if fast.next == None or fast.next.next == None:
			return None
		fast = fast.next.next
		slow = slow.next

	fast = head
	while fast != slow:
		fast, slow = fast.next, slow.next

	return fast

def noLoop(head1, head2):
	"""两个无环单链表相交的第一个结点， 不相交返回None
	"""
	# 计算两个链表的长度差值，并且暂存 两个单链表的最后一个结点
	cur1, cur2 = head1, head2
	diff = 0
	while cur1.next != None:
		diff += 1
		cur1 = cur1.next
	while cur2.next != None:
		diff -= 1
		cur2 = cur2.next

	# 比较最后一个结点是否相同
	if cur1 != cur2:
		return None

	# cur1 存 长链表头结点； cur2 存 短链表头结点
	cur1 = head1 if diff > 0 else head2
	cur2 = head1 if cur1 == head2 else head2
	diff = abs(diff)

	while diff != 0:
		diff -= 1
		cur1 = cur1.next

	while cur1 != cur2:
		cur1, cur2 = cur1.next, cur2.next

	return cur1

def bothLoop(head1, loop1, head2, loop2):
	"""判断两个有环单链表的第一个相交结点
	"""
	if loop1 == loop2:
		cur1, cur2 = head1, head2
		diff = 0
		while cur1 != loop1: ###
			diff += 1
			cur1 = cur1.next
		while cur2 != loop2: ###
			diff -= 1
			cur2 = cur2.next

		cur1 = head1 if diff > 0 else head2 # long
		cur2 = head1 if cur1 == head2 else head2
		diff = abs(diff)
		while diff != 0:
			diff -= 1
			cur1 = cur1.next

		while cur1 != cur2:
			cur1, cur2 = cur1.next, cur2.next

		return cur1

	else:
		cur1 = loop1.next
		while cur1 != loop1:
			if cur1 == loop2:
				return loop2
			cur1 = cur1.next

		return None


class Node(object):
	def __init__(self, val):
		self.value = val
		self.next = None


if __name__ == '__main__':
	# 1->2->3->4->5->6->7->null
	head1 = Node(1)
	head1.next = Node(2)
	head1.next.next = Node(3)
	head1.next.next.next = Node(4)
	head1.next.next.next.next = Node(5)
	head1.next.next.next.next.next = Node(6)
	head1.next.next.next.next.next.next = Node(7)

	# 0->9->8->6->7->null
	head2 = Node(0)
	head2.next = Node(9)
	head2.next.next = Node(8)
	head2.next.next.next = head1.next.next.next.next.next; # 8->6
	print(getIntersectNode(head1, head2).value)

	# 1->2->3->4->5->6->7->4...
	head1 = Node(1)
	head1.next = Node(2)
	head1.next.next = Node(3)
	head1.next.next.next = Node(4)
	head1.next.next.next.next = Node(5)
	head1.next.next.next.next.next = Node(6)
	head1.next.next.next.next.next.next = Node(7)
	head1.next.next.next.next.next.next = head1.next.next.next # 7->4
	# 0->9->8->2...
	head2 = Node(0)
	head2.next = Node(9)
	head2.next.next = Node(8)
	head2.next.next.next = head1.next # 8->2
	print(getIntersectNode(head1, head2).value)

	# 0->9->8->6->4->5->6..
	head2 = Node(0)
	head2.next = Node(9)
	head2.next.next = Node(8)
	head2.next.next.next = head1.next.next.next.next.next # 8->6
	print(getIntersectNode(head1, head2).value);