"""有一个源源不断地吐出整数的数据流，假设你有足够的空间
来保存吐出的数。请设计一个名叫 MedianHolder 的结构，该
结构可以随时取得之前吐出所有数的中位数。
"""
import heapq
import random
import copy

class MedianHolder(object):
	def __init__(self):
		self.min_heap, self.max_heap = MinHeap(), MaxHeap()

	def __modifyTwoHeapSize(self):
		"""调整两个堆的大小"""
		if self.min_heap.size - self.max_heap.size == 2:
			self.max_heap.push(self.min_heap.pop())

		elif self.max_heap.size - self.min_heap.size == 2:
			self.min_heap.push(self.max_heap.pop())

		else:
			pass


	def addNumber(self, val): ### **
		"""向结构中添加元素"""

		if self.max_heap.size == 0:
			self.max_heap.push(val)
			return None

		if self.max_heap.peak() >= val:
			self.max_heap.push(val)
		else:
			if self.min_heap.size == 0:
				self.min_heap.push(val)
				return None

			if self.min_heap.peak() > val:
				self.max_heap.push(val)
			else:
				self.min_heap.push(val)

		self.__modifyTwoHeapSize()
		

	def getMedian(self):
		"""得到吐出的所有数的中值"""

		max_size, min_size = self.max_heap.size, self.min_heap.size

		if max_size + min_size == 0:
			return None

		if max_size + min_size == 1: # **
			return self.max_heap.peak() if max_size == 1 else self.min_heap.peak()

		max_top, min_top = self.max_heap.peak(), self.min_heap.peak()

		if (max_size + min_size) % 2 == 0:
			return (max_top + min_top) / 2
		
		return max_top if max_size > min_size else min_top


class MinHeap(object):
	"""使用heapq模块 实现小根堆"""
	def __init__(self):
		self.heap = []
		self.size = 0

	def push(self, value):
		self.size += 1
		heapq.heappush(self.heap, value)

	def pop(self):
		self.size -= 1
		return heapq.heappop(self.heap)

	def peak(self):
		return self.heap[0]


class MaxHeap(object):
	"""使用heapq模块 实现大根堆"""
	def __init__(self):
		self.heap = []
		self.size = 0

	def push(self, value):
		heapq.heappush(self.heap, -value) # 压入相反数
		self.size += 1

	def pop(self):
		self.size -= 1
		return -heapq.heappop(self.heap) # 弹出相反数

	def peak(self):
		return -self.heap[0] # 返回相反数
	
#######################################################
"""下面部分为对数器部分
"""
def generateRandomArray(max_len, max_val):
	length = int(random.random() * max_len + 1)

	return [int(random.random() * max_val + 1) for i in range(length)]


def getMedianForArray(arr):
	new_arr = copy.copy(arr)
	new_arr.sort()
	length = len(new_arr)
	mid = (length - 1) // 2

	if length % 2 == 0:
		return (new_arr[mid] + new_arr[mid+1]) / 2
	else:
		return new_arr[mid]


if __name__ == '__main__':


	max_len = 50
	max_val = 100
	iter_num = 50000
	succeed = True

	while iter_num > 0:
		iter_num -= 1

		median_holder = MedianHolder()

		arr = generateRandomArray(max_len, max_val)
		for i in arr:
			median_holder.addNumber(i)

		if median_holder.getMedian() != getMedianForArray(arr):
			succeed = False
			break

	print("today is a beatiful day!" if succeed else "What's the Fuck!")
	print(arr)
	arr.sort()
	print(arr)
	print(median_holder.getMedian())
	print(getMedianForArray(arr))