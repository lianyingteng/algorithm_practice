"""图的深度优先遍历

（一个节点的某条路，走到不能再走，退回上级再走）一条路走到黑
"""
def DFS(node):
	"""迭代实现
	"""
	if node == None: return None

	stack, sSet = list(), set()
	stack.append(node)
	while len(stack) != 0:
		cur = stack.pop(-1)

		if cur not in sSet:
			sSet.add(cur)
			for each in cur.nexts:
				stack.append(each)