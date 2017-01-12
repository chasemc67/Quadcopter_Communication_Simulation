# A Simulate two moving nodes, who can communicate when 
# within some distance.

# Written by Chase McCarty, January 2017

import sys

from Drawer import Drawer
from Environment import Environment
from Node import Node
from Event import Event

def main():
	args = sys.argv
	if len(args) < 7:
		print("Usage:")
		print("python main.py smin smax r seed duration")
		print("Optional:")
		print("python main.py smin smax r seed duration drawingEnabled")
		exit()

	smin = args[2]
	smax = args[3]
	r = args[4]
	seed = args[5]
	duration = args[6]
	drawingEnabled = False

	if len(args) > 7 and args[7] == "true":
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