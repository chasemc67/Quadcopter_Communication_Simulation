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

#def getLineSegmemnt(Node):
	#startPoint = (Node.x, Node.y)
	#endPoint = (Node.x + (40*Node.dx), Node.y + (40*Node.dy))
	#return (startPoint, endPoint)



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

	debug = True

	if len(args) > 6 and args[6] == "true":
		drawingEnabled = True

	random.seed(seed)

	env = Environment(40, 2, smin, smax, r, debug=True)
	output = Drawer(40, 40)

	env.queueNextEvents()

	output.draw(env.nodeList)
	while env.clock < duration:
		
		nextEvent = env.eventList.get()
		#print("Events: ")
		
		#while not env.eventList.empty():
		#	print("Next Event: ")
		#	print("time: " + str(nextEvent.eventTime))
		#	print("type: " + str(nextEvent.type))
		#	print("")
		#	env.eventList.get()
		
		env.moveNodes(nextEvent.eventTime)
		env.handleEvent(nextEvent)

		
		#tempEvent = env.eventList.get()
		#while tempEvent.eventTime == nextEvent.eventTime:
		#	env.handleEvent(tempEvent)
		#env.eventList.put(tempEvent)

		env.queueNextEvents()
		time.sleep(0.5)

		#print nodelist
		for node in env.nodeList:
			print("Node: ")
			print("x: " + str(node.x))
			print("y: " + str(node.y))
			print("dx: " + str(node.dx))
			print("dy: " + str(node.dy))
			print("comm: " + str(node.communicating))
			print("")

		output.draw(env.nodeList)

		



main()