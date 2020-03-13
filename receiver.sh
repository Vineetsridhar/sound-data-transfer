#!/bin/bash


while [ 1 ]; do
	echo "Waiting to receive..."
	da=$(date +%S)
	while  ((da % 15 != 0)) ; do
		da=$(date +%S)
		echo $da
	done
	echo "Receiving...."
	./controller.sh
done

