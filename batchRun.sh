#!/bin/bash
rm results.txt
for i in `seq -w 10`; do echo 'Sim : '$i; python main.py 1 2 10 $RANDOM 1000; done