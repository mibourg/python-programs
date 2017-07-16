from __future__ import division

def calculatePi(n):

	op = "+"
	output = 3
	
	for i in range(2, n, 2):
		if op == "-":
			output = output - (4/(i * (i + 1) * (i + 2)))
			op = "+"
		else:
			output = output + (4/(i * (i + 1) * (i + 2)))
			op = "-"

	return output

print calculatePi(10000000)