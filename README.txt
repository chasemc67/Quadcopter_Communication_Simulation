The first assignment in Cmput 479

Simulate two moving nodes, who can communicate when within some distance.

Uses python 3

Drawer compatible with MacOS, untested on other systems.

usage:
./run for a single run
or 
./batchRun for 10 runs
or 
python main.py smin smax r seed duration drawingEnabled

where:
smin and smax represent the minimum and maximum values for the position of the node,

r represents the communication radius of the node

seed is a seed for the random number generator

duration is the simulation duration in seconds

drawingEnabled is a toggle for whether an ascii art simulation is drawn to the terminal

usage example with values:
python main.py 0 10 3 104141 100 true