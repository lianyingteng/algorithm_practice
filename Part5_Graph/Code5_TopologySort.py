"""拓扑排序算法
定义：将有向图中的顶点以线性的方式进行排序
适用范围：有向无环图
"""
def topologySort(graph):

	inMap = dict()  # 节点与其入度hashmap
	zeroInQueue = []  # 0 入度节点

	for node in graph.nodes.values():
		inMap[node] = node.in_degree
		if node.in_degree == 0:
			zeroInQueue.append(node)

	result = []
	while len(zeroInQueue) != 0:
		cur = zeroInQueue.pop(0)
		result.append(cur)

		for each in cur.nexts:
			inMap[each] -= 1
			if inMap[each] == 0:
				zeroInQueue.append(each)


	return result