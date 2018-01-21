"""程序设计中图的表示（类表示）"""


################ 图的程序表示（如下） ################

class Graph(object):
	"""定义图
	"""
	def __init__(self):
		self.nodes = dict() # 点集
		self.edges = set() # 边集


class Node(object):
	"""图的节点表示
	"""
	def __init__(self, value):
		self.value = value   # 节点值
		self.in_degree = 0   # 入度
		self.out_degree = 0   # 出度
		self.nexts = []   # 下级节点集合
		self.edges = []   # 该节点出发的所有边集合


class Edge(object):
	"""图中边的表示
	"""
	def __init__(self, weight, start, end):
		self.weight = weight
		self.start = start
		self.end = end



################ 图的生成（见下） ################

class GraphGenerator(object):
	"""图的生成：给定一个图的矩阵表示
		[
			[权重，从哪来，到哪去]，
			[权重，从哪来，到哪去]，
			……

		]
	"""
	def generateGraph(self, matrix):
		graph = Graph()
		for weight, beg_node, end_node in matrix:

			if graph.nodes.get(beg_node) == None:
				graph.nodes[beg_node] = Node(beg_node)
			if graph.nodes.get(end_node) == None:
				graph.nodes[end_node] = Node(end_node)

			beg_node = graph.nodes[beg_node]
			end_node = graph.nodes[end_node]
			edge = Edge(weight, beg_node, end_node)

			beg_node.out_degree += 1
			beg_node.edges.append(edge)
			beg_node.nodes.append(end_node)
			end_node.in_degree += 1

			graph.edges.add(edge)

		return graph