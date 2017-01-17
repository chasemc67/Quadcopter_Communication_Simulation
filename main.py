# A Simulate two moving nodes, who can communicate when 
# within some distance.

# Written by Chase McCarty, January 2017

import sys

from Drawer import Drawer
from Environment import Environment
from Node import Node
from Event import Event
import math

#debug
import time

def getLineSegmemnt(Node):
	startPoint = (Node.x, Node.y)
	endPoint = (Node.x + (40*Node.dx), Node.y + (40*Node.dy))
	return (startPoint, endPoint)



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


	env = Environment(40)
	output = Drawer(40, 40)

	Node1 = Node()
	Node1.x = 10
	Node1.y = 38
	Node1.dx = 1
	Node1.dy = -1

	Node2 = Node()
	Node2.x = 19
	Node2.y = 38
	Node2.dx = -1
	Node2.dy = -1


	env.nodeList = list();
	env.nodeList.append(Node1)
	env.nodeList.append(Node2)

	for i in range(50):
		output.draw(env.nodeList)
		env.moveNodes(1)

		eventList = list()
		timeToNodeIntersect = env.getTimeTillCollisionEvent(Node1, Node2)
		timeToNode1Wall = env.getTimeTillWallIsHit(Node1)
		timeToNode2Wall = env.getTimeTillWallIsHit(Node2)

		print("timeToNodeIntersect: " + str(timeToNodeIntersect))
		print("timeToNode1Wall: " + str(timeToNode1Wall))
		print("timeToNode2Wall: " + str(timeToNode2Wall))

		eventList.append(env.clock+timeToNodeIntersect)
		eventList.append(env.clock+timeToNode1Wall)
		eventList.append(env.clock+timeToNode2Wall)

		print("Next Event in: " + str(min(eventList) - env.clock))
		time.sleep(0.5)

		



main()