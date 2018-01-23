"""Kruskal算法： 加边法 （实现：并查集+堆结构）

初始最小生成树边数为0，每迭代一次就选择一条满足不成环的最小代价边，
加入到最小生成树的边集合里，知道选取n-1条边。
"""
def kruskalMSI(graph):
	"""算法程序
	"""
	union_find = UnionFindSet()
	union_find.preprocessing(graph.nodes.values())
	
	min_heap = MinHeap()
	for edge in graph.edges:
		min_heap.push(edge)

	result = set()
	while min_heap.getSize() == 0:
		edge = min_heap.pop()
		if not union_find.isSameSet(edge.start, edge.end):
			result.add(edge)
			union_find.union(edge.start, edge.end)

	return result



class MinHeap(object):
	"""小根堆结构： 比较信息 - 边的权重
	"""
	def __init__(self):
		self.heap, self.size = [], 0

	def push(self, edge):
		self.heap.append(edge)
		if self.size != 0:
			self.insertHeap()
		self.size += 1

	def pop(self):
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		tmp = self.heap.pop(-1)
		self.size -= 1
		self.heapify()
		return tmp

	def peak(self):
		return self.heap[0]

	def getSize(self):
		return self.size

	def insertHeap(self):
		"""插入堆
		"""
		index = self.size
		parent = (index - 1) >> 1
		while parent >= 0 and self.heap[parent].weight > self.heap[index].weight:
			self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
			index = parent
			parent = (index - 1) >> 1

	def heapify(self):
		"""堆化
		"""
		arr = self.heap
		length = self.size
		index = 0

		left = index * 2 + 1
		while left < length:
			mini_est = left + 1 if left+1 < length and arr[left+1].weight < arr[left].weight else left
			mini_est = index if arr[index].weight <= arr[mini_est].weight else mini_est
			
			if mini_est == index:
				break

			arr[mini_est], arr[index] = arr[index], arr[mini_est]
			index = mini_est
			left = 2 * index + 1


class UnionFindSet(object):
	"""并查集结构
	"""
	def __init__(self):
		self.fatherMap = dict()
		self.sizeMap = dict()

	def preprocessing(self, edges):
		self.fatherMap.clear()
		self.sizeMap.clear()

		for each in edges:
			self.fatherMap[each] = each
			self.sizeMap[each] = 1

	def findFather(self, edge):
		father = self.fatherMap[edge]

		if father != edge:
			father = self.findFather(father)

		self.fatherMap[edge] = father
		return father

	def union(self, a, b):
		if a == None or b == None:
			return None

		aFather = self.fatherMap[a]
		bFather = self.fatherMap[b]

		if aFather != bFather:
			aSize = self.sizeMap[aFather]
			bSize = self.sizeMap[bFather]
			if aSize > bSize:
				self.fatherMap[bFather] = aFather
				self.sizeMap[aFather] = aSize + bSize
			else:
				self.fatherMap[aFather] = bFather
				self.sizeMap[bFather] = aSize + bSize

	def isSameSet(self, a, b):
		return self.findFather(a) == self.findFather(b)
