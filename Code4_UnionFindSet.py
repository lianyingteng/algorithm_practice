"""并查集"""

class Data(object):
	"""数据的类型与结构（支持任何类型）
	"""

class unionFindSets(object):
	"""并查集类
	"""
	def __init__(self):
		"""初始化结构"""
		self.fatherMap = dict()
		self.sizeMap = dict()

	def makeSets(self, datas):
		"""初始化并查集
		"""
		self.fatherMap.clear()
		self.sizeMap.clear()
		for each in datas:
			self.fatherMap[each] = each
			self.sizeMap[each] = 1


	def findFather(self, data):
		"""查找数据的父节点，查找过程中打平链
		"""
		father = self.fatherMap.get(data)
		if father != data:
			father = self.findFather(father)

		self.fatherMap[data] = father
		return father


	def union(self, a, b):
		"""合并a,b所在的两个集合
		"""
		if a == None or b == None:
			return None

		aFather = self.findFather(a)
		bFather = self.findFather(b)

		if aFather != bFather:
			aSize = self.sizeMap.get(aFather)
			bSize = self.sizeMap.get(bFather)
			if aSize > bSize:
				self.fatherMap[bFather] = aFather
				self.sizeMap[aFather] = aSize + bSize
			else:
				self.fatherMap[aFather] = bFather
				self.sizeMap[bFather] = aSize + bSize