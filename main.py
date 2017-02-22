# A Simulate two moving nodes, who can communicate when 
# within some distance.

# Written by Chase McCarty, January 2017

import sys

from Drawer import Drawer
from Environment import Environment
from Node import Node
from Event import Event
import math
import random

import queue as q

from helpers import *


def main():
	args = sys.argv
	if len(args) < 6:
		print("Usage:")
		print("python main.py smin smax r seed duration")
		print("Optional:")
		print("python main.py smin smax r seed duration drawingEnabled")
		exit()

	smin = int(args[1])
	smax = int(args[2])
	r = int(args[3])
	seed = int(args[4])
	duration = int(args[5])
	drawingEnabled = False

	if len(args) > 6 and args[6].lower() == "true":
		drawingEnabled = True

	random.seed(seed)

	env = Environment(40, 2, smin, smax, r, drawingEnabled)
	output = Drawer(40, 40, drawingEnabled)

	env.queueNextEvents()
	#env.printEventQueue()

	output.draw(env.nodeList)
	while env.clock < duration and env.endEarly == False:
		
		nextEvent = env.eventList.get()
		if env.clock + nextEvent.eventTime > duration:
			env.moveNodes(duration - env.clock)
			continue

		env.moveNodes(nextEvent.eventTime)
		env.handleEvent(nextEvent)

		tempEvent = env.eventList.get()
		while(tempEvent.eventTime == nextEvent.eventTime):
			env.handleEvent(tempEvent)
			tempEvent = env.eventList.get()


		env.queueNextEvents()

		output.draw(env.nodeList)

	env.handleEvent(Event(1, None, None, "end"))

	
	comms = createCommLengthsFromIntervals(env.communicationEvents)
	print("Average Encounter time: " + str(getAvgEncounerTime(comms)))
	#print("All averages: " + str(env.averageComms))
	print("Percent of time spent communicationg: " + str(env.getCommsPercent()) + '%')
	print("Total simulation time: " + str(env.clock))
	plotComms(comms)


main()