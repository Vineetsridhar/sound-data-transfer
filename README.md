# sound-data-transfer

Data is almost always wirelessly transmitted through radio waves whether that be via Wifi or bluetooth (And for good reason). I attemped to create a data transfer algorithm that used sound waves instead of radio waves. 

## Limitations
  1. Data transfer is fairly slow
  2. Limited to very certain characters
  3. The application is just listening for any sound rather than a specific frequency. Very easy for data to get corrupted. FFT could be a potential solution to this
  4. Sound doesn't travel very far unless you've got great speakers 
  5. Code is kind of messy and inconsistent. I was semi-new to programming when I wrote it.

## Potential improvements
  1. Better hardware would help a lot. My microphone could only detect certain frequencies and my speakers weren't made to turn on and off so quickly
  2. Every character in the language is encoded to be the same space, however information theory/entropy could be used to shorten the lengths of characters that appear more frequently. This would improve the overall rate of transfer.
  3. If I could use a Fast Fourier Transform to get the frequencies of the sound data coming in, I could filter out all other noises, and only listen for the sender. I could also potentially send data in parallel using multiple frequencies therefore increasing the rate of transfer.    

## Demonstration of the project
https://www.youtube.com/watch?v=el1mwSr1VAY

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
