"""分别实现反转单链表和反转双链表的函数"""

def reverseSingleList(head):
	if head == None or head.next == None:
		return head

	pre, nex = None, None
	while head != None:
		nex = head.next
		head.next = pre
		pre = head
		head = nex

	return pre

def printSimpleLinkedList(head):
	print("The single List is : ", end=' ')
	if head == None:
		print(head)

	cur = head
	while cur != None:
		print(cur.value, end=' ')
		cur = cur.next
	print()

class SingleNode(object):
	def __init__(self, val):
		self.value = val
		self.next = None


#############################################

def reverseDoubleList(head):
	pre, nex = None, None
	while head != None:
		nex = head.next
		head.next = pre
		head.last = nex
		pre = head
		head = nex

	return pre


def printDoubleLinkedList(head):
	print("The Double List is : ", end=' ')

	end = None
	while head != None:
		print(head.value, end=' ')
		end = head
		head = head.next

	print('||', end=' ')
	while end != None:
		print(end.value, end=' ')
		end = end.last
	print()

class DoubleNode(object):
	def __init__(self, val):
		self.value = val
		self.next = None
		self.last = None




if __name__ == '__main__':
	head1 = SingleNode(1)
	head1.next = SingleNode(2)
	head1.next.next = SingleNode(3)
	head1.next.next.next = SingleNode(4)
	printSimpleLinkedList(head1)
	printSimpleLinkedList(reverseSingleList(head1))


	head2 = DoubleNode(1)
	head2.next = DoubleNode(2)
	head2.next.last = head2
	head2.next.next = DoubleNode(3)
	head2.next.next.last = head2.next
	head2.next.next.next = DoubleNode(4)
	head2.next.next.next.last = head2.next.next
	printDoubleLinkedList(head2)
	printDoubleLinkedList(reverseDoubleList(head2))


	