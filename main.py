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

#debug
import time


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

	debug = True

	if len(args) > 6 and args[6] == "true":
		drawingEnabled = True

	random.seed(seed)

	env = Environment(40, 2, smin, smax, r, debug=False)
	output = Drawer(40, 40)

	env.queueNextEvents()
	env.printEventQueue()

	output.draw(env.nodeList)
	while env.clock < duration:
		
		nextEvent = env.eventList.get()
		if env.clock + nextEvent.eventTime > duration:
			env.moveNodes(duration - env.clock)
			continue

		env.moveNodes(nextEvent.eventTime)
		env.handleEvent(nextEvent)


		env.queueNextEvents()
		#time.sleep(0.5)

		output.draw(env.nodeList)

	env.handleEvent(Event(1, None, None, "end"))

	print("Comm list: ")
	print(env.communicationEvents)



main()