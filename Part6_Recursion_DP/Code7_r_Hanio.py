"""汉诺塔问题"""
def hanio(n):
	if n > 0: 
		process(n, 'left', 'mid', 'right')

def process(n, start, help1, end):
	if n == 1:
		print("%d from %s to %s"%(n, start, end))
		return None

	process(n-1, start, end, help1)
	print("%d from %s to %s"%(n, start, end))
	process(n-1, help1, start, end)

if __name__ == '__main__':
	n = 5
	hanio(n)
