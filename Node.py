# A node in the simulation

class Node():
	def __init__(self):
		self.x = 4
		self.y = 5
		self.dx = 1
		self.dy = 1
		self.radius = 4
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

	def getLineSegmemnt(self):
		startPoint = (self.x, self.y)
		endPoint = (self.x + (40*self.dx), self.y + (40*self.dy))
		return (startPoint, endPoint)

	def getFatLineSegemnets(self):
		startPoint = (self.x, self.y)
		if self.dx = 0:
			s1 = ((self.x + self.radius), self.y)
			s2 = ((self.x - self.radius), self.y)
		else:
			s1 = (self.x, (self.y + self.radius))
			s2 = (self.x, (self.y - self.radius))

		e1 = ((s1[0] + (40*self.dx)), (s1[1] + (40*self.dy)))
		e2 = ((s2[0] + (40*self.dx)), (s2[1] + (40*self.dy)))

		return ((s1, e1), (s2, e2))

	def bounceOffWall(self):
		self.dx = -self.dx
		self.dy = -self.dy