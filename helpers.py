import math

from Node import Node

import matplotlib.pyplot as plt
import numpy as np


# expects each point to be an (x,y) tuple
def getEquclidianDist(point1, point2):
	return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))


# Predicts the time until 2 nodes will be within comm distance
def predictTimeToEnter(Node1, Node2):
	dr = (Node2.x - Node1.x, Node2.y - Node1.y)
	dv = (Node2.dx - Node1.dx, Node2.dy - Node1.dy)

	drdr = (dr[0] * dr[0]) + (dr[1] * dr[1])
	dvdv = (dv[0] * dv[0]) + (dv[1] * dv[1])
	dvdr = (dr[0] * dv[0]) + (dr[1] * dv[1])

	sig = Node1.radius

	d = (dvdr * dvdr) - (dvdv * (drdr - sig*sig))

	if dvdr >= 0:
		return math.inf
	if d < 0:
		return math.inf

	if (-(dvdr + math.sqrt(d))/dvdv) < 0:
		return math.inf

	return (-(dvdr + math.sqrt(d))/dvdv)

def predictTimeToExit(Node1, Node2):
	time = 0

	# Clone Nodes, and offset so we don't worry about negatives
	N1 = Node(0, 0, 4)
	N1.x = Node1.x + Node1.radius*100
	N1.y = Node1.y + Node1.radius*100
	N1.dx = Node1.dx 
	N1.dy = Node1.dy
	N1.radius = Node1.radius
	N2 = Node(0, 0, 4)
	N2.x = Node2.x + Node1.radius*100
	N2.y = Node2.y + Node1.radius*100
	N2.dx = Node2.dx
	N2.dy = Node2.dy
	N2.radius = Node2.radius

	if (predictTimeToEnter(N1, N2) == math.inf):
		if (getEquclidianDist((N1.x, N1.y), (N2.x, N2.y)) > Node1.radius):
			return math.inf
		time = (Node1.radius * 5)
	else:
		time = predictTimeToEnter(N1, N2) + (Node1.radius * 5)

	N1.move(time)
	N2.move(time)

	# Reverse Node path
	N1.dx = -N1.dx
	N1.dy = -N1.dy
	N2.dx = -N2.dx
	N2.dy = -N2.dy

	return time - predictTimeToEnter(N1, N2)
	

def createCommLengthsFromIntervals(commIntervals):
	intervals = list()
	for i in commIntervals:
		intervals.append(i[1] - i[0])

	return intervals

def plotComms(values):
	plt.hist(values)
	plt.title("Communication Lengths")
	plt.xlabel("Value")
	plt.ylabel("Frequency")

	plt.show()

def getAvgEncounerTime(values):
	total = 0
	for i in values:
		total += i
	return (total / len(values))
