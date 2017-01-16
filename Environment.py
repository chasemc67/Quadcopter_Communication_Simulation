# An object containing a reference to the environment

import math

class Environment():
	def __init__(self):
		#self.eventList = priorityQueue()
		self.nodeList = list() # list of nodes in environment

	def moveNodes(self):
		for node in self.nodeList:
			node.move(1)

	# returns number of time steps until a collision will happen
	# If both nodes stay on their current coarse
	def getTimeTillCollisionEvent(self, Node1, Node2):
		try:
			intersectionPoint = self.lineIntersection(Node1.getLineSegmemnt(), Node2.getLineSegmemnt())
		except:
			print("Intersection failed")
			return math.inf
		if intersectionPoint[0] > Node1.x and Node1.dx < 0:
			return math.inf
		elif intersectionPoint[0] < Node1.x and Node1.dx > 0:
			return math.inf
		else:	
			return abs(intersectionPoint[0] - Node1.x) / Node1.dx

	# Returns the intersction point, still need to check
	# If that intersection will happen in future
	def lineIntersection(self, line1, line2):
	    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
	    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

	    def det(a, b):
	        return a[0] * b[1] - a[1] * b[0]

	    div = det(xdiff, ydiff)
	    if div == 0:
	       raise Exception('lines do not intersect')

	    d = (det(*line1), det(*line2))
	    x = det(d, xdiff) / div
	    y = det(d, ydiff) / div
	    return x, y