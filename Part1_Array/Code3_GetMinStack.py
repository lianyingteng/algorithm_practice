"""实现一个特殊的栈，操作：pop、push、getMin"""

class Stack1(object):
	"""实现1： 两个栈同步压入和弹出,minStack压入时稍费时间、但是弹出时操作稍省时间"""

	def __init__(self):

		self.stack = []
		self.help = []

	def isEmpty(self, obj):
		if len(obj) == 0:
			return True

		return False

	def push(self, item):
		self.stack.append(item)

		if len(self.help) == 0 or self.help[-1] >= item:
			self.help.append(item)
		else: 
			self.help.append(self.help[-1])

	def pop(self):
		if self.isEmpty(self.stack):
			raise ArrayIndexOutOfBoundsException("The Stack is empty!")

		self.help.pop(len(self.help) - 1)

		return self.stack.pop(len(self.stack) - 1)

	def getMin(self):
		if len(self.stack) == 0:
			raise ArrayIndexOutOfBoundsException("The Stack is empty!")

		return self.help[-1]


class Stack2(object):
	"""实现2： minStack压入时稍省空间，但是弹出操作稍费时间"""
	def __init__(self):

		self.stack = []
		self.minStack = []
		self.size = 0

	def push(self, item):
		self.stack.append(item)
		self.size += 1

		if len(self.minStack) == 0 or self.minStack[-1] >= item:
			self.minStack.append(item)

	
	def pop(self):
		if self.size == 0:
			raise ArrayIndexOutOfBoundsException("The stack is empty!")

		popVal = self.stack.pop()
		self.size -= 1

		if popVal == self.minStack[-1]:
			self.minStack.pop()

		return popVal


	def getMin(self):
		if self.size == 0:
			raise ArrayIndexOutOfBoundsException("The stack is empty!")

		return self.minStack[-1]







