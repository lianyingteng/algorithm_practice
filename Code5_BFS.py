"""图的宽度优先遍历

（通过距离组织，离我近的先打印，离我远的后打印，但是不能重复打印）
"""

def bfs(node):

	if node == None: return None

	queue, qSet = list(), set()
	queue.append(node)
	
	while len(queue) != 0:
		cur = queue.pop(0)
		print(cur.value)

		if cur not in qSet:
			qSet.add(cur)
			for nex in cur.nexts:
				queue.append(nex)

