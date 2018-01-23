"""打印两个有序链表的公共部分"""

class Node(object):
	def __init__(self, data):
		self.value = data
		self.next = None


def printCommonPart(head1, head2):
	print("打印公共部分：")

	while head1 != None and head2 != None:
		if head1.value < head2.value:
			head1 = head1.next
		elif head1.value > head2.value:
			head2 = head2.next
		else:
			print(head1.value, end=' ')
			head1 = head1.next
			head2 = head2.next

	print()

