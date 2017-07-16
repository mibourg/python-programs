from math import sqrt
import numpy as np  
import matplotlib.pyplot as plt

def quadraticFormula(a, b, c):
	d = b**2 - 4*a*c

	if d < 0:
		return "There are no possible solutions. (0 roots)"

	elif d == 0:
		x = (-b + sqrt(d))/(2*a)
		return str(x)

	else:
		x1 = (-b + sqrt(d))/(2*a)
		x2 = (-b - sqrt(d))/(2*a)
		return str(x1) + "\n" + str(x2)

def quadraticFormulaEq(equation):
	parts = equation.split()
	if len(parts) == 1:
		a = parts[0].split("x")[0]
		b = 0
		c = 0
		return quadraticFormula(float(a), float(b), float(c))

	elif len(parts) == 3:
		a = parts[0].split("x")[0]

		if 'x' in parts[2]:
			c = 0
			if parts[1] == '+':
				b = parts[2].split("x")[0]
			else:
				b = "-" + parts[2].split("x")[0]

		else:
			b = 0
			if parts[1] == '+':
				c = parts[2]
			else:
				c = "-" + parts[2]

		return quadraticFormula(float(a), float(b), float(c))

	else:
		a = parts[0].split("x")[0]

		if parts[1] == '+':
			b = parts[2].split("x")[0]
		else:
			b = "-" + parts[2].split("x")[0]

		if parts[3] == '+':
			c = parts[4]
		else:
			c = "-" + parts[4]

		return quadraticFormula(float(a), float(b), float(c))

def plotEquation(equation, min_x, max_x):
	x = np.linspace(min_x, max_x)
	y = eval(equation)
	fig, ax = plt.subplots()
	plt.show(ax.plot(x,y))

def generalToVertex(a, b, c):
	a = float(a)
	b = float(b)
	c = float(c)
	in_parenthesis = str(b/(2*a))
	out_parenthesis = str((((4*a**2*c)-(b**2*a))/(4*a**2)))

	if in_parenthesis[0] == "-" and out_parenthesis[0] == "-":
		out_parenthesis = out_parenthesis.replace("-", "")
		in_parenthesis = in_parenthesis.replace("-", "")
		return str(a) + "(x - " + in_parenthesis + ")^2 - " + out_parenthesis

	elif in_parenthesis[0] == "-" and out_parenthesis[0] != "-":
		in_parenthesis = in_parenthesis.replace("-", "")
		return str(a) + "(x - " + in_parenthesis + ")^2 + " + out_parenthesis

	elif in_parenthesis[0] != "-" and out_parenthesis[0] == "-":
		out_parenthesis = out_parenthesis.replace("-", "")
		return str(a) + "(x + " + in_parenthesis + ")^2 - " + out_parenthesis

	else:
		return str(a) + "(x + " + in_parenthesis + ")^2 + " + out_parenthesis

def generalToVertexEq(equation):
	parts = equation.split()
	if len(parts) == 1:
		a = parts[0].split("x")[0]
		b = 0
		c = 0
		
		return generalToVertex(a, b, c)

	elif len(parts) == 3:
		a = parts[0].split("x")[0]

		if 'x' in parts[2]:
			c = 0
			if parts[1] == '+':
				b = parts[2].split("x")[0]
			else:
				b = "-" + parts[2].split("x")[0]

		else:
			b = 0
			if parts[1] == '+':
				c = parts[2]
			else:
				c = "-" + parts[2]

		return generalToVertex(a, b, c)

	else:
		a = parts[0].split("x")[0]

		if parts[1] == '+':
			b = parts[2].split("x")[0]
		else:
			b = "-" + parts[2].split("x")[0]

		if parts[3] == '+':
			c = parts[4]
		else:
			c = "-" + parts[4]

		return generalToVertex(a, b, c)




