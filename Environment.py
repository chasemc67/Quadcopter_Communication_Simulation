# An object containing a reference to the environment

import math
import queue as q

class Environment():
	def __init__(self, size):
		self.eventList = q.PriorityQueue(maxsize=0)
		self.nodeList = list() # list of nodes in environment
		self.size = size
		self.clock = 0

	def moveNodes(self, timeSteps):
		self.clock += timeSteps
		for node in self.nodeList:
			node.move(timeSteps)

	# returns number of time steps until a collision will happen
	# If both nodes stay on their current coarse
	def getTimeTillCollisionEvent(self, Node1, Node2):
		intersectionPoint = self.lineIntersection(Node1.getLineSegmemnt(), Node2.getLineSegmemnt())
		
		if self.getTimeUntilNodeReachesPoint(Node1, intersectionPoint) < math.inf and self.getTimeUntilNodeReachesPoint(Node2, intersectionPoint) < math.inf:
			return self.getTimeUntilNodeReachesPoint(Node1, intersectionPoint)
		else:
			return math.inf


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
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, 0), (0, self.size))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, 0), (self.size, 0))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((self.size, 0), (self.size, self.size))))))
		wallList.append(abs(self.getTimeUntilNodeReachesPoint(Node, self.lineIntersection(Node.getLineSegmemnt(), ((0, self.size), (self.size, self.size))))))
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