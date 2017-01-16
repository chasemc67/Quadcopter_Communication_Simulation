# A node in the simulation

class Node():
	def __init__(self):
		self.x = 4
		self.y = 5
		self.dx = 1
		self.dy = 1
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