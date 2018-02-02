"""有一个机器按自然数序列的方式吐出球（1，2，3……），你有一个袋子，袋子最多只能装下K个球。
设计一种选择方式，当吐到第N号球时，之前每个球被装进袋子的概率都是 k/N。
"""
import random

class ReservoirSampling(object):
	def __init__(self, bagSize):
		self.bagSize = bagSize
		self.bag = [None] * bagSize

	def rand(self, max1):
		return int(random.random() * max1 + 1)

	def add(self, num):

		if num <= self.bagSize:
			self.bag[num-1] = num

		else:

			if self.rand(num) <= k: # num号球进袋子
				self.bag[self.rand(k) - 1] = num

"""算法过程

	1. 处理1~k号球，直接进袋子。
	2. 处理num (num>k)号球时，以k/num的概率决定是否将第i号球
		决定进 -> 从袋中随机扔掉一个，num进袋子
		不决定进 -> num扔掉
"""

if __name__ == '__main__':
	k = 6
	num = 100

	pool = ReservoirSampling(k)
	for i in range(1, num):
		pool.add(i)
		print(pool.bag)