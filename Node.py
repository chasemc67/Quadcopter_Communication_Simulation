# A node in the simulation

import random

class Node():
	def __init__(self, smin, smax, radius):
		self.x = 4
		self.y = 5
		self.dx = 1
		self.dy = 1
		self.radius = radius

		self.smin = smin
		self.smax = smax

		self.communicating = False

	def move(self, timeSteps):
		self.x = self.x + (timeSteps * self.dx)
		self.y = self.y + (timeSteps * self.dy)

	def setRandomSpeed(smin, smax):
		# X axis and y-axis speeds are chosen randomly 
		# Between args smin and smax
		return random.randint(smin, smax)

	def getLineSegmemnt(self):
		startPoint = (self.x, self.y)
		endPoint = (self.x + (60*self.dx), self.y + (60*self.dy))
		return (startPoint, endPoint)


	def bounceOffWall(self):
		self.dx = random.randint(self.smin, self.smax)
		self.dy = random.randint(self.smin, self.smax)

		directionX = random.randint(0,1)
		if directionX == 0:
			directionX = -1
		directionY = random.randint(0,1)
		if directionY == 0:
			directionY = -1

		self.dx = self.dx * directionX
		self.dy = self.dy * directionY		

		if self.x >= 38:
			self.dx = -abs(self.dx)
		if self.y >= 38:
			self.dy = -abs(self.dy)

		if self.x <= 1:
			self.dx = abs(self.dx)
		if self.y <= 1:
			self.dy = abs(self.dy)


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

	def toString(self):
		return ("\nNode: \nx: " + str(self.x) + "\ny: " + str(self.y) + "\ndx: " + str(self.dx) + "\ndy: " + str(self.dy) + "\nrad: " + str(self.radius) + "\ncomm: " + str(self.communicating) + "\n\n")

