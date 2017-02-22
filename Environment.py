# An object containing a reference to the environment

import math
import queue as q

import random

from Event import Event
from Node import Node
from helpers import *

from statistics import variance

class Environment():
	# if debug is true, an event will be placed to draw the board
	# at each time interval.
	# Otherwise the board is only drawn at events
	def __init__(self, size, numNodes, smin, smax, r, debug=False):
		self.eventList = q.PriorityQueue(maxsize=0)
		self.nodeList = list() # list of nodes in environment
		self.size = size
		self.clock = 0
		self.debug = debug

		self.communicationEvents = list()
		self.averageComms = list() # tuples of (time, CommPercent)
		self.startComm = 0

		# flag that gets flipped when sim should end early
		self.endEarly = False

		# create nodes in environment with random values
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

		# check if newly created nodes are within comm distance
		if getEquclidianDist((self.nodeList[0].x, self.nodeList[0].y), (self.nodeList[1].x, self.nodeList[1].y)) < self.nodeList[0].radius:
			self.nodeList[0].communicating = True
			self.nodeList[1].communicating = True


	# move nodes and advance clock some number of steps
	def moveNodes(self, timeSteps):
		self.clock += timeSteps
		for node in self.nodeList:
			node.move(timeSteps)


	# get time until node reaches some point
	# returns infinity if node won't reach point on current trajectory
	def getTimeUntilNodeReachesPoint(self, Node, Point):
		if Point[0] == math.inf:
			return math.inf

		if Point[0] > Node.x and Node.dx < 0 and Point[0]:
			return math.inf
		elif Point[0] < Node.x and Node.dx > 0:
			return math.inf
		else:	
			return abs(Point[0] - Node.x) / Node.dx		
	
	# Gets time until a noe will intersect a wall
	def getTimeTillWallIsHit(self, Node):
		# Take the min of intersecting with each wall
		wallList = list()
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, 0), (0, self.size-1))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, 0), (self.size-1, 0))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((self.size-1, 0), (self.size-1, self.size-1))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, self.size-1), (self.size-1, self.size-1))))))
		while min(wallList) <= 0:
			wallList.remove(min(wallList))
		return min(wallList)

	# Returns the intersction point, still need to check
	# If that intersection will happen in future
	def lineIntersection(self, line1, line2):
	    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

	    def det(a, b):
	        return a[0] * b[1] - a[1] * b[0]

	    div = det(xdiff, ydiff)
	    if div == 0:
	       return (math.inf, math.inf)

	    d = (det(*line1), det(*line2))
	    x = det(d, xdiff) / div
	    y = det(d, ydiff) / div
	    return x, y

	# create a new priority queue and queue up the future events
	def queueNextEvents(self):
		self.eventList = q.PriorityQueue(maxsize=0)
		if self.nodeList[0].communicating == False:
			if (predictTimeToEnter(self.nodeList[0], self.nodeList[1])) != math.inf:
				self.eventList.put(Event(predictTimeToEnter(self.nodeList[0], self.nodeList[1]), self.nodeList[0], self.nodeList[1], "enter"))
		else:
			if (predictTimeToExit(self.nodeList[0], self.nodeList[1])) != math.inf:
				self.eventList.put(Event(predictTimeToExit(self.nodeList[0], self.nodeList[1]), self.nodeList[0], self.nodeList[1], "exit"))

		self.eventList.put(Event(self.getTimeTillWallIsHit(self.nodeList[0]), self.nodeList[0], None, "bounce"))
		self.eventList.put(Event(self.getTimeTillWallIsHit(self.nodeList[1]), self.nodeList[1], None, "bounce"))

		# if debug is true (we're drawing every frame)
		# then add an event in every frame, since we only draw events
		if self.debug:
			self.eventList.put(Event(1, None, None, "debug"))

	# Get the % of total sim time communication has happened
	def getCommsPercent(self):
		total = 0
		for i in self.communicationEvents:
			total += (i[1] - i[0])

		# if startComm != 0, then there is currently communication hapening
		if self.startComm != 0:
			total += (self.clock - self.startComm)
		return ((total / self.clock) * 100)

	# check if variance in communication averages is less than some threshold
	# returns false if < 10 averages in list to calc variance on
	def isVarianceLessThanThresh(self, threshold):
		if len(self.averageComms) < 10:
			return False

		#create list of last 10 averages
		last10 = list()
		lenAvgs = len(self.averageComms)
		for i in range(10):
			last10.append(self.averageComms[lenAvgs-(i+1)][1])

		if variance(last10) < threshold:
			return True
		else:
			return False

	# Switch case for handling events
	# also appends a comm average here if its been enough time since the last one
	def handleEvent(self, event):
		if len(self.averageComms) > 0:
			if self.clock > ((self.averageComms[len(self.averageComms)-1][0]) + 10):
				self.averageComms.append((self.clock, self.getCommsPercent()))
		else:
			self.averageComms.append((self.clock, self.getCommsPercent()))

		if event.type == "bounce":
			event.node1.bounceOffWall()
		elif event.type == "debug":
			temp = self.eventList.get()
			self.eventList.put(temp)
		elif event.type == "enter":
			event.node1.communicating = True
			event.node2.communicating = True
			self.startComm = self.clock
		elif event.type == "exit":
			event.node1.communicating = False
			event.node2.communicating = False
			self.endComm = self.clock
			self.communicationEvents.append((self.startComm, self.endComm))
			self.startComm = 0
			self.endComm = 0
		elif event.type == "end":
			if self.nodeList[0].communicating:
				self.endComm = self.clock
				self.communicationEvents.append((self.startComm, self.endComm))
				self.startComm = 0
				self.endComm = 0
		else:
			print("Cannot handle event of type: " + str(event.type))

		# Check for end early condition
		# 2 is magic number here for end variance
		if self.isVarianceLessThanThresh(2):
			self.endEarly = True


	# For debugging purposes.
	# Prints out the currente event queue without destroying it
	def printEventQueue(self):
		tq1 = q.PriorityQueue(maxsize=0)
		print("==================================")
		print("Printing Event Queue: ")
		while( not self.eventList.empty()):
			temp = self.eventList.get()
			tq1.put(temp)
			print("Event: ")
			print("time: " + str(temp.eventTime))
			print("type: " + str(temp.type))
			print("")
		while(not tq1.empty()):
			temp = tq1.get()
			self.eventList.put(temp)

		print("==================================")
