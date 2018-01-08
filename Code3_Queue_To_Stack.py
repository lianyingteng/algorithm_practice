"""队列结构实现堆结构"""

class Queue_To_Stack(object):
	"""两个队列实现一个栈结构
	"""
	def __init__(self):

		self.qData = []
		self.qHelp = []

	def push(self, item):
		self.qData.append(item)

	def pop(self):
		if len(self.qData) == 0:
			raise IndexError("The stack is empty!")

		while len(self.qData) != 1:
			self.qHelp.append(self.qData.pop())

		res = self.qData.pop()
		self.qData, self.qHelp = self.qHelp, self.qData
		return res

	def peak(self):
		if len(self.qData) == 0:
			raise IndexError("The stack is empty!")

		while len(self.qData) != 1:
			self.qHelp.append(self.qData.pop())

		res = self.qData.pop()
		self.qHelp.append(res)
		self.qData, self.qHelp = self.qHelp, self.qData
		
		return res


	