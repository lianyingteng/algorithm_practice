"""跳表结构（空间换时间 链表+二分法的结合）

跳表的由来： 链表的插入和删除操作时间复杂度是O(1)，但是查询操作时间复杂度O(N)，
	为了提高计算速度，就有了跳表的概念

跳表的性质：
	1) 有很多层结构组成
	2) 每一层都是一个有序的链表
	3) 最底层的链表包含所有元素
	4) 如果一个元素出现在leve i的链表中，则它在level i之下的链表中也都会出现
	5）每个节点包含两个指针 a.指向同一链表中下一个元素的指针 b.指向下面一层的元素的指针

注意： 一个数能够到第几层是通过概率决定的


代码未完成！！！！！！！！！！！！！
"""
class SkipListNode(object):
	"""跳表的节点结构
	"""
	def __init__(self, value):
		self.value = value
		self.nextNodes = []


class SkipList(object):
	"""跳表
	"""
	global PROBABILITY 
	PROBABILITY = 0.5

	def __init__(self):
		self.size = 0
		self.maxLevel = 0
		self.head = SkipListNode(None)
		self.head.nextNodes.append(None)

	def getHead(self):
		return self.head

	def add(self, newValue):
		"""添加新的元素
		"""
		if not self.contains(newValue):
			self.size += 1

			level = 0
			while random.random() < PROBABILITY:
				level += 1

			while level > self.maxLevel: # 包含level
				self.head.nextNodes.append(None)
				self.maxLevel += 1

			newNode = SkipListNode(newValue)
			current = self.head
			while level >= 0:
				current = self.findNext(newValue, current, level)
				newNode.nextNodes.append()
				level -= 1




	def contains(self, value):
		node = self.find(value)
		return node != None and node.value != None and self.equal(node.value, value)

	def equalTo(self, a, b):
		return a == b



"""跳表与红黑树的比较

1. skiplist的复杂度和红黑树一样，但是实现起来更加简单
2. 在并发环境下，红黑树进行插入和删除操作的时候，需要一些rebalance操作，需要大量的锁
	skiplist需要锁相对较少
"""