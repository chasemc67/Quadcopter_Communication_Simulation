# An object containing a reference to the environment

import math
import queue as q

import random

from Event import Event
from Node import Node
from helpers import *

class Environment():
	def __init__(self, size, numNodes, smin, smax, r, debug=False):
		self.eventList = q.PriorityQueue(maxsize=0)
		self.nodeList = list() # list of nodes in environment
		self.size = size
		self.clock = 0
		self.debug = debug

		for i in range(numNodes):
			self.nodeList.append(Node(smin, smax, r))
			self.nodeList[i].x = random.randint(1, size-1)
			self.nodeList[i].y = random.randint(1, size-1)
			self.nodeList[i].dx = random.randint(smin, smax)
			self.nodeList[i].dy = random.randint(smin, smax)

			directionX = random.randint(0,1)
			if directionX == 0:
				directionX = -1
			directionY = random.randint(0,1)
			if directionY == 0:
				directionY = -1

			self.nodeList[i].dx = self.nodeList[i].dx * directionX
			self.nodeList[i].dy = self.nodeList[i].dy * directionY


	def moveNodes(self, timeSteps):
		self.clock += timeSteps
		for node in self.nodeList:
			node.move(timeSteps)

	# returns number of time steps until a collision will happen
	# If both nodes stay on their current coarse
	#def getTimeTillCollisionEvent(self, Node1, Node2):
	#	intersectionPoint = self.lineIntersection(Node1.getLineSegmemnt(), Node2.getLineSegmemnt())
	#	
	#	if self.getTimeUntilNodeReachesPoint(Node1, intersectionPoint) < math.inf and self.getTimeUntilNodeReachesPoint(Node2, intersectionPoint) < math.inf:
	#		return abs(self.getTimeUntilNodeReachesPoint(Node1, intersectionPoint))
	#	else:
	#		return math.inf


	def getTimeUntilNodeReachesPoint(self, Node, Point):
		if Point[0] == math.inf:
			return math.inf

		if Point[0] > Node.x and Node.dx < 0 and Point[0]:
			return math.inf
		elif Point[0] < Node.x and Node.dx > 0:
			return math.inf
		else:	
			return abs(Point[0] - Node.x) / Node.dx		
	
	def getTimeTillWallIsHit(self, Node):
		# Take the min of intersecting with each wall
		wallList = list()
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, 0), (0, self.size-1))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, 0), (self.size-1, 0))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((self.size-1, 0), (self.size-1, self.size-1))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, self.size-1), (self.size-1, self.size-1))))))
		return min(wallList)

	# Returns the intersction point, still need to check
	# If that intersection will happen in future
	def lineIntersection(self, line1, line2):
	    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

	    def det(a, b):
	        return a[0] * b[1] - a[1] * b[0]

	    div = det(xdiff, ydiff)
	    if div == 0:
	       return (math.inf, math.inf)

	    d = (det(*line1), det(*line2))
	    x = det(d, xdiff) / div
	    y = det(d, ydiff) / div
	    return x, y

	def queueNextEvents(self):
		self.eventList = q.PriorityQueue(maxsize=0)
		if self.nodeList[0].communicating == False:
			self.eventList.put(Event(predictTimeToEnter(self.nodeList[0], self.nodeList[1]), self.nodeList[0], self.nodeList[1], "enter"))
		else:
			self.eventList.put(Event(predictTimeToExit(self.nodeList[0], self.nodeList[1]), self.nodeList[0], self.nodeList[1], "exit"))

		self.eventList.put(Event(self.getTimeTillWallIsHit(self.nodeList[0]), self.nodeList[0], None, "bounce"))
		self.eventList.put(Event(self.getTimeTillWallIsHit(self.nodeList[1]), self.nodeList[1], None, "bounce"))

		if self.debug:
			self.eventList.put(Event(1, None, None, "debug"))

	def handleEvent(self, event):
		if event.type == "bounce":
			print("Wall Event")
			event.node1.bounceOffWall()
		elif event.type == "debug":
			temp = self.eventList.get()
			self.eventList.put(temp)
			print("Next event in " + str(temp.eventTime) + " of type: " + temp.type)
			print("Node1: " + str(self.nodeList[0].x) + ", " + str(self.nodeList[0].y))
			print("Node2: " + str(self.nodeList[1].x) + ", " + str(self.nodeList[1].y))
		elif event.type == "enter":
			print("Enter Event")
			event.node1.communicating = True
			event.node2.communicating = True
		elif event.type == "exit":
			print("Exit Event")
			event.node1.communicating = False
			event.node2.communicating = False
		else:
			print("Cannot handle event of type: " + str(event.type))

