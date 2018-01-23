"""图的深度优先遍历

（一个节点的某条路，走到不能再走，退回上级再走）一条路走到黑
"""
def dfs(node):
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



def dfs(node):
	"""课程代码
	"""
	if node == None: return None

	stack, h_set = list(), set()
	stack.append(node)
	h_set.add(node)
	print(node.value)
	while len(stack) != 0:
		cur = stack.pop(-1)

		for each in cur.nexts:
			if each not in h_set:
				stack.append(cur)
				stack.append(each)
				h_set.add(each)

				print(each.value)

				break


