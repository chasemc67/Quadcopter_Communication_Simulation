# An instance of an event in the simulation
# Will be put on an event priority queue

class Event():
	def __init__(node1, node2):
		self.valid = True
		self.left = node1
		self.right = node2