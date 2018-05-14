### Simulates Communication Frequency and Duration for Nodes Moving in a Bounded Space

This code simulates two nodes, with a given communication radius, moving randomly in an enclosed space.
batch runs can be invoked, which will generate statistics on commuication duration and frequency, under different parameters.


For speed an efficiency, the simulation pre-calculates time signatures where events will start, and skips to those places.  
Rather than the alternative of calculating every single simulation frame.  
This allows the simulations to be incredibly fast.  

![quadsim](https://user-images.githubusercontent.com/6922982/39973101-406b904e-56d0-11e8-83b1-2cbfb326e925.gif)

#### Usage:
##### For a single run:
```
./run for a single run
```

##### For batched runs (default is 10):
```
./batchRun for 10 runs
```
##### Custom parameters:
```
python main.py smin smax r seed duration drawingEnabled
```
where:  
smin and smax represent the minimum and maximum values for the position of the node,  
r represents the communication radius of the node,  
seed is a seed for the random number generator,  
duration is the simulation duration in seconds,  
drawingEnabled is a toggle for whether an ascii art simulation is drawn to the terminal,  


##### Usage Example with Values:
```
python main.py 0 10 3 104141 100 true
```
