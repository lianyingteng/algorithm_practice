"""用数组实现栈结构
"""
class Stack(object):
	def __init__(self):
		self.items = list()

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def clear(self):
		del self.items[:]

	def empty(self):
		return self.size() == 0

	def size(self):
		return len(self.items)

	def peak(self):
		return self.items[self.size() - 1]


class ArrayStack(object):
	def __init__(self, initSize):
		if initSize < 0:
			raise IllegalArgmentException("The init size is less than 0!")

		self.items = [0] * initSize
		self.size = 0

	def push(self, item):
		if self.size == len(self.items):
			raise ArrayIndexOutOfBoundsException("The stack is full!")

		self.items[self.size] = item
		self.size += 1

	def pop(self):
		if self.size == 0:
			raise ArrayIndexOutOfBoundsException("The stack is empty!")

		self.size -= 1
		
		return self.items[self.size]

	def peak(self):
		if self.size == 0:
			return None

		return self.items[self.size - 1]

		



