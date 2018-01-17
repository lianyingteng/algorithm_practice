"""
输入:
	正数数组costs - costs[i]表示i号项目的花费
	正数数组profits - profits[i]表示i号项目的纯利润
	正数k - 表示你不能并行、只能串行的最多做k个项目
	整数m - 表示你的初始资金

输出：
	你最后获得的最大钱数

说明：
	你每做完一个项目，马上获得的收益，可以支持你去做下一个项目
"""
class MyHeap(object):
	"""公共类"""

	def __init__(self):
		self.heap = []
		self.size = 0

	def push(self, pro):
		if self.size == 0:
			self.heap.append(pro)
		else:
			self.heap.append(pro)
			self.insertHeap()

		self.size += 1

	def pop(self):
		self.size -= 1
		self.heap[0], self.heap[self.size] = self.heap[self.size], self.heap[0]
		tmp = self.heap.pop(-1)
		self.heapify()
		return tmp

	def peak(self):
		return self.heap[0]

	def getSize(self):
		return self.size


class MaxHeapForProfits(MyHeap):
	"""利润大根堆
	"""
	def __init__(self):
		super(MaxHeapForProfits, self).__init__()

	def insertHeap(self):
		"""插入堆"""
		arr = self.heap
		index = self.size

		par_i = (index-1) // 2
		while par_i >= 0 and arr[index].p > arr[par_i].p:
			arr[index], arr[par_i] = arr[par_i], arr[index]
			index = par_i
			par_i = (index - 1) // 2

	def heapify(self):
		"""堆化"""
		arr = self.heap
		length = self.size
		index = 0

		left = 2 * index + 1
		while left < length:
			largest = left+1 if left+1 < length and arr[left+1].p > arr[left].p else left
			largest = index if arr[index].p >= arr[left].p else largest

			if largest == index:
				break

			arr[largest], arr[index] = arr[index], arr[largest]
			index = largest
			left = 2 * index + 1


class MinHeapForCosts(MyHeap):
	"""花费小根堆
	"""
	def __init__(self):
		super(MinHeapForCosts, self).__init__()

	def insertHeap(self):
		"""插入堆"""
		arr = self.heap
		index = self.size

		par_i = (index-1) // 2
		while par_i >= 0 and arr[index].c < arr[par_i].c:
			arr[index], arr[par_i] = arr[par_i], arr[index]
			index = par_i
			par_i = (index - 1) // 2
	

	def heapify(self):
		"""堆化"""
		arr = self.heap
		length = self.size
		index = 0

		left = 2 * index + 1
		while left < length:
			largest = left+1 if left+1 < length and arr[left+1].c < arr[left].c else left
			largest = index if arr[index].c <= arr[left].c else largest

			if largest == index:
				break

			arr[largest], arr[index] = arr[index], arr[largest]
			index = largest
			left = 2 * index + 1



class Project(object):
	"""项目（花费和利润）
	"""
	def __init__(self, cost, profit):
		self.c = cost
		self.p = profit


def findMaxIncome(costs, profit, k, m):
	"""找寻最大收入的解决方案
	"""
	project = []
	for i in range(len(costs)):
		project.append(Project(costs[i], profit[i]))

	maxProfitQ, minCostQ = MaxHeapForProfits(), MinHeapForCosts()
	# 将项目都放进代价 小根堆
	for i in range(len(project)):
		minCostQ.push(project[i])

	# 最多执行k次
	for _ in range(k):
		while (minCostQ.getSize != 0 and minCostQ.peak().c <= m):
			maxProfitQ.push(minCostQ.pop())

		if maxProfitQ.getSize() == 0:
			return m

		m += maxProfitQ.pop().p

	return m


if __name__ == '__main__':
	costs = [100, 200, 300, 400, 500, 10000]
	profit = [100, 120, 170, 200, 60, 100]
	k = 4
	m = 200

	print(findMaxIncome(costs, profit, k, m))