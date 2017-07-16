from __future__ import division

def calculatePi(n):

	divisor = 1
	output = 4

	for i in range(n):
		divisor = divisor + 2
		output = output - (4/divisor)
		divisor = divisor + 2
		output = output + (4/divisor)

	return output 

print calculatePi(10000000)