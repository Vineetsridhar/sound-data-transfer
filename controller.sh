#!/bin/bash

#while [ 1 ]; do
	$(python3 sound.py $1)
	
	#echo $(python3 getPitch.py output.wav)
	echo $(python3 getAmplitude.py)
#done
