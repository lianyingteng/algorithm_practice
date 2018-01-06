"""用数组实现队列结构
"""
class ArrayQueue(object):
	if __init__(self, initSize):
		if initSize < 0:
			raise IllegalArgmentException("The init size is less than 0")

		self.items = [0] * initSize
		self.size = 0
		self.first = 0
		self.last = 0

	def push(self, item):
		if self.size == len(self.items):
			raise ArrayIndexOutOfBoundsException("The queue is full!")
		
		self.size += 1
		self.items[self.last] = item
		self.last = 0 if self.last == len(self.items) - 1 else self.last + 1

	def pull(self):
		if self.size == 0:
			raise ArrayIndexOfBoundsException("The queue is empty!")

		self.size -= 1
		tmp = self.first
		self.first = 0 if self.first == len(self.items) - 1 else self.first + 1

		return self.items[tmp]

	def peak(self):
		if self.size == 0:
			raise ArrayIndexOfBoundsException("The queue is empty!")

		return self.items[self.first]

