"""切金条问题： 最小分割代价（哈夫曼树）

	贪心问题
"""
import heapq

class MinHeap(object):
	"""小根堆接口"""
	def __init__(self):
		self.heap = []
		self.size = 0

	def push(self, val):
		self.size += 1
		heapq.heappush(self.heap, val)

	def pop(self):
		self.size -= 1
		return heapq.heappop(self.heap)

	def getSize(self):
		return self.size


def lessMoney(arr):
	if len(arr) == 1:
		return arr[0]

	heap = MinHeap()
	for i in arr:
		heap.push(i)

	sum1 = 0
	while heap.getSize() > 1:
		tmp = heap.pop() + heap.pop()
		sum1 += tmp
		heap.push(tmp)

	return sum1

if __name__ == '__main__':
	arr = [3, 5, 2, 7, 0, 1, 6, 4]
	print(lessMoney(arr))