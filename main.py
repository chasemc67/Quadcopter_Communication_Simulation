from Drawer import Drawer
from Environment import Environment
from Node import Node
from Event import Event


env = Environment()
output = Drawer(10, 10)

env.nodeList = list();
env.nodeList.append(Node())
env.nodeList.append(Node())

env.nodeList[1].x = 7
env.nodeList[1].y = 7
env.nodeList[1].dx = -1
env.nodeList[1].dy = -1

for i in range(10):
	output.draw(env.nodeList)
	env.moveNodes()
