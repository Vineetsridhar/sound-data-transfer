# sound-data-transfer

Sending messages wirelessly through sound. Text is converted into binary and then sent through speakers. 
The receiver can then listen for this message and decode it converting the binary message back into text. 

## Usage for command line interface:
### Sender
```
python3 generator [frequency] [message]
i.e 
python3 generator 10000 "Hello how are you"
```
### Receiver 
```
./controller.sh [recording duration]
i.e
./controller.sh 5
```
Will wait for starting sound and then begin recording for [duration] seconds.
Will then call the getAmplitude fuction which parses the data, extracts the bits, and returns the value

## Usage for chatroom
```
cd chatroomtest
chmod 744 chatroom.sh
./chatroom.sh
```
