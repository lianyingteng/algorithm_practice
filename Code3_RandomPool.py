"""设计RandomPool结构

	功能： 不重复插入、删除、等概率随机返回
"""
import random

class RandomPool(object):

	def __init__(self):

		self.keyIndexMap = dict()
		self.indexKeyMap = dict()
		self.size = 0

	def insert(self, key):

		if self.keyIndexMap.get(key) == None:
			self.size += 1
			self.keyIndexMap[key] = self.size
			self.indexKeyMap[self.size] = key


	def delete(self, key):

		if self.keyIndexMap.get(key) != None:
			deleteIndex = self.keyIndexMap[key]
			lastKey = self.indexKeyMap[self.size]
			
			self.keyIndexMap[lastKey] = deleteIndex
			self.keyIndexMap.pop(key)

			self.indexKeyMap[deleteIndex] = lastKey
			self.indexKeyMap.pop(self.size)

			self.size -= 1

	
	def getRandom(self):
		if self.size == 0:
			raise IndexError("The structure is empty!")

		randNum = int(random.random() * self.size + 1)
		return self.indexKeyMap[randNum]


