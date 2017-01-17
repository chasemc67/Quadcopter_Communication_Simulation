# An instance of an event in the simulation
# Will be put on an event priority queue

class Event():
	def __init__(self, eventTime, node1, node2, eventType):
		self.valid = True
		self.node1 = node1
		self.node2 = node2
		self.eventTime = eventTime
		self.type = eventType

	# http://stackoverflow.com/questions/10045405/overloading-comparator-of-priority-queue-in-python
	def __lt__(self, other):
		return self.eventTime < other.eventTime

