from helpers import *

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


test()




