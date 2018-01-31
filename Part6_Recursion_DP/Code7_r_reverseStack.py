"""给你一个栈，请你逆序这个栈，不能申请额外的数据结构，只能使用递归函数。如何实现？"""

def reverseStack(stack):
	"""栈的逆序
	"""
	if len(stack) == 0: # 栈空了
		return None

	i = findAndPopStackLow(stack)
	reverseStack(stack)
	stack.append(i) # 压栈

def findAndPopStackLow(stack):
	"""找到并弹出栈中最后一个元素
	"""
	i = stack.pop(-1)
	if len(stack) == 0:
		return i

	res = findAndPopStackLow(stack)
	stack.append(i)
	return res


if __name__ == '__main__':
	stack = [1, 2, 3, 4, 5, 6]
	reverseStack(stack)
	print(stack)
