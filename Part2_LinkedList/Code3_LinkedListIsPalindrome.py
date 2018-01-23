"""判断一个链表是否为回文结构"""

class Node(object):
	def __init__(self, data):
		self.value = data
		self.next = None


class isPalindrome(object):

	def __init__(self, head):
		self.head = head


	# 方法一：额外空间复杂度O(N) 每个元素依次进栈
	def isPalindrome1(self):
		cur = self.head
		stack = []

		while cur != None:
			stack.append(cur.value)
			cur = cur.next

		cur = self.head
		while cur != None:
			if cur.data != stack.pop(-1):
				return False

		return True


	# 方法二： 只有一半元素进栈，额外空间复杂度O(N/2)
	def isPalindome2(self):
		fast, slow = self.head, self.head
		while fast.next != None and fast.next.next != None:
			fast = fast.next.next
			slow = slow.next

		stack = []
		while slow.next != None:
			slow = slow.next
			stack.append(slow.value)

		cur = self.head
		while len(stack) != 0:
			if stack.pop() != cur.value:
				return False
			cur = cur.next

		return True


	# 方法三：不需要任何额外空间，额外空间复杂度O(1) 【最优解】
	def isPalindome3(self):
		if self.head == None or self.head.next == None:
			return True

		slow, fast = self.head, self.head
		while fast.next != None and fast.next.next != None:
			slow, fast = slow.next, fast.next.next # 此时的slow指向中间结点

		# 反转右半部分链表 （slow指向最后一个位置）
		cur = slow.next
		slow.next = None
		tmp = None
		while cur != None:
			tmp = cur.next
			cur.next = slow
			slow = cur
			cur = tmp

		tmp = slow # 暂存最后一个结点（还原链表时用到）
		# 检测是否为回文
		cur = self.head
		res = True
		while cur != None and slow != None:
			if cur.value != slow.value:
				res = False
				break
			cur, slow = cur.next, slow.next

		# 还原链表
		slow = tmp
		cur = slow.next
		slow.next = None
		tmp = None
		while cur != None:
			tmp = cur.next
			cur.next = slow
			slow = cur
			cur = tmp

		return res