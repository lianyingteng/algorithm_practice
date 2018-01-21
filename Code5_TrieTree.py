"""前缀树结构

优点： 最大限度的减少无谓的字符串比较，查词效率比哈希表高

性质：
	1. 根结点不包含字符，除根结点外每个节点只包含一个字符
	2. 从根结点到某一结点，路径上经过的字符连接起来为该节点对应的字符串
	3. 每个节点的所有子节点的字符都不相同
"""
class TrieTreeNode(object):
	"""前缀树结构
	"""
	def __init__(self):
		self.via = 0   # 经由数
		self.end = 0   # 结尾数
		self.nexts = [None] * 26  #  下级节点


class Trie(object):
	"""前缀树的操作
	"""
	def __init__(self):
		self.root = TrieTreeNode()

	def insert(self, str1):
		"""添加字符串
		"""
		if str1 == None or len(str1) == 0:
			return None

		node = self.root
		for each in str1:
			index = ord(each) - ord('a')
			if node.nexts[index] == None:
				node.nexts[index] = TrieTreeNode()

			node = node.nexts[index]
			node.via += 1

		node.end += 1


	def delete(self, str1):
		"""删除字符串
		"""
		if str1 == None or len(str1) == 0 or self.search(str1) == False:
			return None

		node = self.root
		for each in str1:
			index = ord(each) - ord('a')
			node.nexts[index].via -= 1
			if node.nexts[index].via == 0:
				node.nexts[index] = None
				return None

			node = node.nexts[index]

		node.end -= 1


	def search(self, str1):
		"""查询字符串
		"""
		if str1 == None or len(str1) == None:
			return False

		node = self.root
		for each in str1:
			index = ord(each) - ord('a')
			if node.nexts[index] == None:
				return False

			node = node.nexts[index]

		return node.end != 0


	def prefixNumber(self, prefix):
		"""返回前缀数量
		"""
		if prefix == None or len(prefix) == 0:
			return 0

		node = self.root
		for each in prefix:
			index = ord(each) - ord('a')
			if node.nexts[index] == None:
				return 0

			node = node.nexts[index]

		return node.via


if __name__ == '__main__':
	trie = Trie()
	print(trie.search("zuo")) # False
	trie.insert("zuo") 
	print(trie.search("zuo")) # True
	trie.delete("zuo");
	print(trie.search("zuo")) # False
	trie.insert("zuo")
	trie.insert("zuo")
	trie.delete("zuo")
	print(trie.search("zuo")) # True
	trie.delete("zuo")
	print(trie.search("zuo")) # False
	trie.insert("zuo")
	trie.insert("zuoac")
	trie.insert("zuoab")
	trie.insert("zuoad")
	trie.insert("zuoa")
	print(trie.search("zuoa")) # True
	print(trie.prefixNumber("zuo")) # 5






