"""将单链表按某值划分成左边小，中间相等、右边大的形式"""

class Node(object):
	def __init__(self, val):
		self.value = val
		self.next = None



def listPartition2(head, pivot):
	"""最优解：额外空间复杂度O(1)的解法"""
	sH, sT = None, None # 小的头和尾
	eH, eT = None, None # 等的头和尾
	bH, bT = None, None # 大的头和尾

	tmp = None # 暂存下一个结点

	# 将每个结点分给这三个链表
	while head != None:
		tmp = head.next
		head.next = None
		if head.value < pivot: # 填到小于区
			if sH == None:
				sH, sT = head, head
			else:
				sT.next = head
				sT = head

		elif head.value > pivot: # 填到大于区
			if bH == None:
				bH, bT = head, head
			else:
				bT.next = head
				bT = head

		else:
			if eH == None: # 填到等于区
				eH, eT = head, head
			else:
				eT.next = head
				eT = head

		head = tmp
	
	# 小于尾 与 等于头 相连
	if sT != None:
		sT.next = eH
		eT = sT if eT == None else eT

	if eT != None:
		eT.next = bH

	return sH if sH != None else (eH if eH != None else bH)




def listPartition1(head, pivot):
	"""数组的划分方法应用于链表的划分
	"""
	if head == None: return head

	# 求链表的长度
	length = 0
	cur = head
	while cur != None:
		length += 1
		cur = cur.next

	# 将所有结点暂存在数组中
	arr = [None] * length
	cur = head
	for i in range(length):
		arr[i] = cur
		cur = cur.next

	# 数组的划分思想
	arrPartition(arr, pivot)

	# 将数组串成一个新的链表
	for i in range(1, length):
		arr[i-1].next = arr[i]

	arr[i].next = None

	return arr[0]

def arrPartition(arr, pivot):
	"""数组的划分过程
	"""
	less, more = -1, len(arr)
	cur = 0

	while cur < more:
		if arr[cur].value < pivot:
			less += 1
			arr[cur], arr[less] = arr[less], arr[cur]
			cur += 1
		elif arr[cur].value > pivot:
			more -= 1
			arr[more], arr[cur] = arr[cur], arr[more]
		else: 
			cur += 1

def generateLinkedList(arr):
	"""由数组生成单链表
	"""
	if arr == None:
		raise IndexError("The array is empty!")

	head = Node(0)
	cur = head
	for each in arr:
		cur.next = Node(each)
		cur = cur.next

	cur.next = None

	return head.next

def printLinkedList(head):
	"""打印单链表
	"""
	if head == None: return Node

	cur = head
	print("LinkedList is: ", end=' ')
	while cur != None:
		print(cur.value, end=' ')
		cur = cur.next

	print()


if __name__ == '__main__':

	pivot = 5
	arr = [7, 9, 1, 8, 5, 2, 5]
	head1 = generateLinkedList(arr)

	printLinkedList(head1)
	
	#printLinkedList(listPartition1(head1, pivot))
	printLinkedList(listPartition2(head1, pivot))


