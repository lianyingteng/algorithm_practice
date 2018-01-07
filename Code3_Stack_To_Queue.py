"""使用栈结构实现一个队列结构：栈转换成队列"""

class Stack_To_Queue(object):
	"""两个栈结构实现队列
		
		栈结构：先进后出
		队列结构：先进先出
	"""
	def __init__(self):

		self.stackPush = []
		self.stackPop = []

	def add(self, item):

		self.stackPush.append(item)

	def poll(self):
		if len(self.stackPop) == 0 and len(self.stackPush) == 0:
			raise ArrayIndexOutOfBoundsException("The queue is empty!")

		if len(self.stackPop) != 0:
			return self.stackPop.pop(-1)

		while len(self.stackPush) == 0:
			self.stackPop.append(self.stackPush.pop(-1))

		return self.stackPop.pop(-1)

	def peak(self):
		if len(self.stackPop) != 0:
			return self.stackPop[-1]

		if len(self.stackPush) != 0:
			return self.stackPush[0]

		raise ArrayIndexOutOfBoundsException("The queue is empty!")





