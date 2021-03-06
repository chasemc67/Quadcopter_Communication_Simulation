# Module for drawing the simulation out in the terminal using ascii art
# Works on MacOS, untested on other systems.

import os
import sys
import time
import math

class Drawer():
	# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
	# redOnWhite = '\x1b[1;31;47m' 
	# blueOnWhite = '\x1b[1;34;47m' 
	def __init__(self, x, y, enabled):
		self.width = x
		self.height = y
		self.enabled = enabled

	def clear(self):
		print("Clearing")
		os.system('cls' if os.name == 'nt' else 'clear')

	def nodeAtPosition(self, nodeList, posX, posY):
		for node in nodeList:
			if math.ceil(node.x) == posX and math.ceil(node.y) == posY:
				if node.communicating == True:
					return 2
				else:
					return 1
		return 0

	def draw(self, nodeList):
		if self.enabled == True:
			self.clear()
			for y in range(self.height):			
				for x in range(self.width):
					if (self.nodeAtPosition(nodeList, x, y) == 2):
						sys.stdout.write('\x1b[1;31;47mo \x1b[0m')	
					elif (self.nodeAtPosition(nodeList, x, y) == 1):
						sys.stdout.write('\x1b[1;34;47mo \x1b[0m')	
					else:
						sys.stdout.write('\x1b[1;34;47m  \x1b[0m')
					sys.stdout.flush()
				sys.stdout.write('\n')
				sys.stdout.flush()
			time.sleep(0.1)
