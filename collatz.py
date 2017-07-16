def main(x):
	iterations = 0
	while x != 1:
		print x
		if x % 2 == 0:
			x = x / 2
		else:
			x = 3 * x + 1
		iterations = iterations + 1
	return '\n' + str(iterations)

print main(6 * 10**1000000)
