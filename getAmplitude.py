from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import math
from mapping import MyMapping

def filter(audio, threshold):
    audio = np.copy(audio)
    ind = audio < threshold
    audio[ind] = 0        
    return audio

def getNumberPerTimeInterval(data, times, rate, threshold, numBits, duration):
    interval = duration / numBits
    intervalFrequency = interval / 4

    numPeaks = [0] * int(round(L)*(1/interval))
    timeFound = 0
    for soundVal, time in zip(data, np.arange(times)/rate):
        if soundVal > threshold and time - timeFound > intervalFrequency:
            timeFound = time
            numPeaks[int(time/interval)] += 1
    return numPeaks

def getNumber(data, N, rate, threshold, minInterval, maxInterval):
    ret = []
    timeFound = 0
    for val, time in zip(data, np.arange(N)/rate):
        if val > threshold:
            diff = time - timeFound
            if diff > minInterval and diff < maxInterval:
                ret[-1] = 1
            elif diff > maxInterval:
                ret.append(0)
                timeFound = time
    return ret



def showPlots(data, times, rate):
    plt.plot(np.arange(times) / rate, data)
    plt.show()

def showMultiplePlots(data, data2, times, rate):
    f = plt.figure(1)
    plt.plot(np.arange(times)/rate, data)
    g = plt.figure(2)
    plt.plot(np.arange(times)/rate, data2)
    
    plt.show()

def getThreshold(data, times, rate, intervalF=0.1, sampleSize=6):
    timeFound = 0
    maxes = []
    for val, time in zip(data, np.arange(times)/rate):
        if time - timeFound > intervalF:
            timeFound = time
            maxes.append(val)
        else:
            if maxes:
                maxes[-1] = max(maxes[-1], val) 
    return sum(sorted(maxes)[-sampleSize:])/sampleSize

def translateData(binary):
    mapping = MyMapping()
    mapping = mapping.mapping
    ret = ""
    if len(binary) % 6 != 0:
        print("Corruption occured: {}".format(len(binary) % 6 ))
        
    for i in range(0, len(binary), 6):
        key = "".join(map(str, binary[i:i+6]))
        if key in mapping:
            ret += mapping[key]
        
    print(ret)
    

rate, audio = wavfile.read('output.wav')
N = audio.shape[0]
L = N / rate
#THRESHOLD = getThreshold(audio, N, rate, 0.25)
#THRESHOLD -= THRESHOLD / 10 * 2
THRESHOLD = 5000
#print(THRESHOLD, audio)
vals = filter(audio, THRESHOLD)
#getStartPoint(vals, N, rate)
binary = getNumber(audio, N, rate, THRESHOLD, 0.02, 0.04)
[print(x, end="") for x in binary]
print()
translateData(binary)
showMultiplePlots(vals,audio, N, rate)
#showPlots(audio, N, rate)

    
