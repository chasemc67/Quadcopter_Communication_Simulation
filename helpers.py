import math

from Node import Node


# expects each point to be an (x,y) tuple
def getEquclidianDist(point1, point2):
	return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))


# Predicts the time until 2 nodes will be within comm distance
def predictTimeToEnter(Node1, Node2):
	dr = (Node2.x - Node1.x, Node2.y - Node1.y)
	dv = (Node2.dx - Node1.dx, Node2.dy - Node1.dy)

	drdr = (dr[0] * dr[0]) + (dr[1] * dr[1])
	dvdv = (dv[0] * dv[0]) + (dv[1] * dv[1])
	dvdr = (dr[0] * dv[0]) + (dr[1] * dv[1])

	sig = Node1.radius

	d = (dvdr * dvdr) - (dvdv * (drdr - sig*sig))

	if dvdr >= 0:
		return math.inf
	if d < 0:
		return math.inf

	if (-(dvdr + math.sqrt(d))/dvdv) < 0:
		return math.inf

	return (-(dvdr + math.sqrt(d))/dvdv)

def predictTimeToExit(Node1, Node2):
	time = 0

	# Clone Nodes, and offset so we don't worry about negatives
	N1 = Node(0, 0, 4)
	N1.x = Node1.x + Node1.radius*1000
	N1.y = Node1.y + Node1.radius*1000
	N1.dx = Node1.dx 
	N1.dy = Node1.dy
	N2 = Node(0, 0, 4)
	N2.x = Node2.x + Node1.radius*1000
	N2.y = Node2.y + Node1.radius*1000
	N2.dx = Node2.dx
	N2.dy = Node2.dy

	if (predictTimeToEnter(N1, N2) == math.inf):
		if (getEquclidianDist((N1.x, N1.y), (N2.x, N2.y)) > Node1.radius):
			return math.inf
		time = (Node1.radius * 5)
	else:
		time = predictTimeToEnter(N1, N2) + (Node1.radius * 5)

	N1.move(time)
	N2.move(time)

	# Reverse Node path
	N1.dx = -N1.dx
	N1.dy = -N1.dy
	N2.dx = -N2.dx
	N2.dy = -N2.dy

	return time - predictTimeToEnter(N1, N2)

def test():
	print("Starting test")
	Node1 = Node(0, 0, 4)
	Node1.x = 3
	Node1.y = 6
	Node1.dx = 1
	Node1.dy = 2
	Node2 = Node(0, 0, 4)
	Node2.x = 11
	Node2.y = 6
	Node2.dx = -1
	Node2.dy = 2

	assert(predictTimeToEnter(Node1, Node2) == 2.0)
	assert(predictTimeToExit(Node1, Node2) == 6.0)


	Node1 = Node(0, 0, 4)
	Node1.x = 3
	Node1.y = 6
	Node1.dx = -1
	Node1.dy = 2
	Node2 = Node(0, 0, 4)
	Node2.x = 11
	Node2.y = 6
	Node2.dx = 1
	Node2.dy = 2

	assert(predictTimeToEnter(Node1, Node2) == math.inf)
	assert(predictTimeToExit(Node1, Node2) == math.inf)


	Node1 = Node(0, 0, 4)
	Node1.x = 3
	Node1.y = 6
	Node1.dx = 1
	Node1.dy = 2
	Node2 = Node(0, 0, 4)
	Node2.x = 11
	Node2.y = 6
	Node2.dx = -1
	Node2.dy = 2

	Node1.move(3)
	Node2.move(3)

	assert(predictTimeToEnter(Node1, Node2) == math.inf)
	assert(predictTimeToExit(Node1, Node2) == 3.0)


	print("Test passed")


#test()




