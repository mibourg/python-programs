import time
def findGreatestCommonDivisor(a, b):
	while a != b:
		if a > b:
			a = a - b
			return findGreatestCommonDivisor(a, b)
		elif a <= b:
			b = b - a
			return findGreatestCommonDivisor(a, b)
	return a

print findGreatestCommonDivisor(541, 1044)
