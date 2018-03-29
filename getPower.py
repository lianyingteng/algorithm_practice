def getResult(k, N):  # k ** N
	
	res = 1
	tmp = k

	while N > 0:
		if (N & 1) != 0:
			res = res * tmp
		N >>= 1

		tmp = tmp * tmp

	return res

k = 5
N = 7
print(getResult(k, N))
print(k ** N)
