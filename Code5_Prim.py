"""Prim算法（加点法）

以任意一个顶点开始，选最小的代价边，解锁新的顶点，重复该过程，直到所有顶点都解锁
"""
def primMSI(graph):
	"""算法过程
	"""
	result = set()

	node_set = set()
	min_heap = MinHeap()

	node = graph.nodes.values()[0] # 从一个顶点开始
	node_set.add(node)
	for edge in node.edges:
		min_heap.push(edge)

	while min_heap.getSize() != 0:
		edge = min_heap.pop()
		toNode = edge.end

		if toNode not in node_set:
			node_set.add(toNode)
			result.add(edge)

			for edge in toNode.edges:
				min_heap.push(each)

	


class MinHeap(object):

	def __init__(self):
		self.heap = []
		self.size = 0

	def push(self, edge):
		self.heap.append(edge)
		if self.size != 0:
			self.__insertHeap()

		self.size += 1	


	def pop(self):
		self.size -= 1
		self.heap[0], self.heap[self.size] = self.heap[self.size], self.heap[0]
		tmp = self.heap.pop(-1)
		self.__heapify()
		return tmp


	def getSize(self):
		return self.size 


	def __insertHeap(self):
		"""插入堆
		"""
		arr = self.heap
		index = self.size

		par_i = (index - 1) >> 1
		while par_i >= 0 and arr[par_i].weight > arr[index].weight:
			arr[par_i], arr[index] = arr[index], arr[par_i]
			index = par_i
			par_i = (index - 1) >> 1


	def __heapify(self):
		"""堆化
		"""
		arr = self.heap
		index = 0
		length = self.size

		left = 2 * index + 1
		while left < length:
			mini_est = left + 1 if (left+1) < length and arr[left+1].weight < arr[left].weight else left
			mini_est = index if arr[index].weight <= arr[mini_est] else mini_est

			if mini_est == index:
				break

			arr[index], arr[mini_est] = arr[mini_est], arr[index]
			index = mini_est
			left = 2 * index + 1




