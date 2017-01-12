import Sys

from Drawer import Drawer
from Environment import Environment
from Node import Node
from Event import Event

def main():
	# Get command line arguments
	args = sys.argv

	if len(argv) < 7:
		print("Usage:")
		print("python main.py smin smax r seed duration")
		print("Optional:")
		print("python main.py smin smax r seed duration drawingEnabled")
		exit()

	smin = argv[2]
	smax = argv[3]
	r = argv[4]
	seed = argv[5]
	duration = argv[6]
	drawingEnabled = False

	if len(argv) > 7 and argv[7] == "true":
		drawingEnabled = True


	env = Environment()
	output = Drawer(10, 10)

	env.nodeList = list();
	env.nodeList.append(Node())
	env.nodeList.append(Node())

	env.nodeList[1].x = 7
	env.nodeList[1].y = 7
	env.nodeList[1].dx = -1
	env.nodeList[1].dy = -1

	for i in range(10):
		output.draw(env.nodeList)
		env.moveNodes()



main()