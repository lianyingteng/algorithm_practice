"""Dijkstra算法（适用于：没有负权值的边）

Dijkstra算法是一种单源最短路径，针对的是非负权边。所谓的
单源最短路径： 指定一个出发顶点，计算从该源顶点出发到其他
所有顶点的最短路径
"""
import sys
def dijkstra1(node):

	distanceMap = dict()
	distanceMap[node] = 0
	selectedNodes = set()

	minNode = getMinDistanceAndUnselectedNode(distanceMap, selectedNodes)
	while minNode != None:
		distance = distanceMap.get(minNode)
		for edge in minNode.edges:
			toNode = edge.end
			if distanceMap.get(toNode) == None:
				distanceMap[toNode] = distance + edge.weight

			distanceMap[toNode] = min(distanceMap[toNode], distance + edge.weight)

		selectedNodes.add(minNode)
		minNode = getMinDistanceAndUnselectedNode(distanceMap, selectedNodes)

	return distanceMap

def getMinDistanceAndUnselectedNode(distanceMap, selectedNodes):
	"""得到距离最近并且没有选过的节点
	"""
	minNode = None
	minDistance = sys.maxSize
	for node, distance in distanceMap.items():
		if node not in selectedNodes and distance < minDistance:
			minNode = node
			minDistance = distance

	return minNode