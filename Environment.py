# An object containing a reference to the environment

class Environment():
	def __init__(self):
		#self.eventList = priorityQueue()
		self.nodeList = list() # list of nodes in environment

	def moveNodes(self):
		for node in self.nodeList:
			node.move(1)