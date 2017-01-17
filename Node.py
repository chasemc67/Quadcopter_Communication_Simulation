# A node in the simulation

import random

class Node():
	def __init__(self, smin, smax):
		self.x = 4
		self.y = 5
		self.dx = 1
		self.dy = 1
		self.radius = 4

		self.smin = smin
		self.smax = smax
		#self.x = rand()
		#self.y = rand()
		#self.dx = rand()  # X movement speed
		#self.dy = rand()  # Y movement speed
		#self.commDistance = communicationDistance # r

	def move(self, timeSteps):
		self.x = self.x + (timeSteps * self.dx)
		self.y = self.y + (timeSteps * self.dy)

	def hitWall(self):
		return
		# randomize angle and speed or whateve

	def setRandomSpeed(smin, smax):
		# X axis and y-axis speeds are chosen randomly 
		# Between args smin and smax
		return random.randint(smin, smax)

	def getLineSegmemnt(self):
		startPoint = (self.x, self.y)
		endPoint = (self.x + (40*self.dx), self.y + (40*self.dy))
		return (startPoint, endPoint)

	def getFatLineSegemnets(self):
		# This will give us the line segments,
		# Can then find where the intersect with a segment perpendicular
		# To the node trajectory to find the start point
		startPoint = (self.x, self.y)
		if self.dx == 0:
			s1 = ((self.x + self.radius), self.y)
			s2 = ((self.x - self.radius), self.y)
		else:
			s1 = (self.x, (self.y + self.radius))
			s2 = (self.x, (self.y - self.radius))

		e1 = ((s1[0] + (40*self.dx)), (s1[1] + (40*self.dy)))
		e2 = ((s2[0] + (40*self.dx)), (s2[1] + (40*self.dy)))

		l1 = (s1, e1)
		l2 = (s2, e2)

		# Get a perpendicular segment
		# And find intersection with fat lines to get start point
		n1 = Node()
		n1.x = self.x
		n1.y = self.y
		n1.dx = -self.dy
		n1.dy = self.dx
		perpSeg = n1.getLineSegmemnt()

		return (l1, l2)



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


