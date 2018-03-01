"""使用栈结构实现一个队列结构：栈转换成队列"""

class Stack_To_Queue(object):
	"""两个栈结构实现队列
		
		栈结构：先进后出
		队列结构：先进先出
	"""
	def __init__(self):
		self.stack = []
		self.help = []

	def push(self, item):

		self.stack.append(item)

	def pop(self):

		if len(self.stack) == 0 and len(self.help) == 0:
			raise Exception("The queue is empty")

		if len(self.help) == 0:
			while len(self.stack) != 0:
				self.help.append(self.stack.pop(-1))

		return self.help.pop(-1)

	def peak(self):

		if len(self.stack) == 0 or len(self.help) == 0:
			raise Exception("The queue is empty")

		if len(self.help) == 0:
			while len(self.stack) != 0:
				self.help.append(self.stack.pop(-1))

		return self.help[-1]





