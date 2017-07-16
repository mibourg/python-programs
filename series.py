from __future__ import division

#Arithmetic sequences
#tn = a + (n - 1)d
def findNumberAt(number_list, position):
	a = number_list[0]
	d = number_list[1] - number_list[0]
	return a + (position - 1) * d

def findPositionOf(number_list, number):
	a = number_list[0]
	d = number_list[1] - number_list[0]
	return (number - a + d) / d

#Sn = (n/2)(2a + (n - 1)d) OR Sn = (n/2)(a + tn)
def findSumUpToPosition(number_list, position):
	a = number_list[0]
	d = number_list[1] - number_list[0]
	return (position / 2) * (2 * a + (position - 1) * d)

def findSumUpToNumber(number_list, number):
	position = findPositionOf(number_list, number)
	return findSumUpToPosition(number_list, position)

#Geometric sequences
def findNumberAtGeometric(number_list, position):
	a = number_list[0]
	r = number_list[1] / number_list[0]
	return a * r**(position-1)

def findPostionOfGeometric(number_list, number):
	a = number_list[0]
	r = number_list[1] / number_list[0]
	comparison = number - a 
	position = 1
	while r**(position) != comparison:
		position = position + 1
	return position + 1

