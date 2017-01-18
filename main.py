# A Simulate two moving nodes, who can communicate when 
# within some distance.

# Written by Chase McCarty, January 2017

import sys

from Drawer import Drawer
from Environment import Environment
from Node import Node
from Event import Event
import math
import random

import queue as q

from helpers import *

#debug
import time

def getLineSegmemnt(Node):
	startPoint = (Node.x, Node.y)
	endPoint = (Node.x + (40*Node.dx), Node.y + (40*Node.dy))
	return (startPoint, endPoint)



def main():
	args = sys.argv
	if len(args) < 6:
		print("Usage:")
		print("python main.py smin smax r seed duration")
		print("Optional:")
		print("python main.py smin smax r seed duration drawingEnabled")
		exit()

	smin = int(args[1])
	smax = int(args[2])
	r = int(args[3])
	seed = int(args[4])
	duration = int(args[5])
	drawingEnabled = False

	if len(args) > 6 and args[6] == "true":
		drawingEnabled = True

	random.seed(seed)

	env = Environment(40, 2, smin, smax)
	output = Drawer(40, 40)

	env.eventList = q.PriorityQueue(maxsize=0)
	env.eventList.put(Event(env.getTimeTillCollisionEvent(env.nodeList[0], env.nodeList[1]), env.nodeList[0], env.nodeList[1], "node intersect"))
	env.eventList.put(Event(env.getTimeTillWallIsHit(env.nodeList[0]), env.nodeList[0], None, "wall"))
	env.eventList.put(Event(env.getTimeTillWallIsHit(env.nodeList[1]), env.nodeList[1], None, "wall"))

	for i in range(100):
		output.draw(env.nodeList)
		nextEvent = env.eventList.get()
		print("Next Event: " + nextEvent.type + " in: " + str(nextEvent.eventTime))
		print("Node1: " + str(env.nodeList[0].x) + ", " + str(env.nodeList[0].y))
		print("Node2: " + str(env.nodeList[1].x) + ", " + str(env.nodeList[1].y))
		env.moveNodes(nextEvent.eventTime)
		if nextEvent.type == "wall":
			nextEvent.node1.bounceOffWall()

		env.moveNodes(1)

		env.eventList = q.PriorityQueue(maxsize=0)
		env.eventList.put(Event(env.getTimeTillCollisionEvent(env.nodeList[0], env.nodeList[1]), env.nodeList[0], env.nodeList[1], "node intersect"))
		env.eventList.put(Event(env.getTimeTillWallIsHit(env.nodeList[0]), env.nodeList[0], None, "wall"))
		env.eventList.put(Event(env.getTimeTillWallIsHit(env.nodeList[1]), env.nodeList[1], None, "wall"))
		
		time.sleep(0.5)

		



main()