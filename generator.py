import pyaudio
import numpy as np
import time
p = pyaudio.PyAudio()
import sys
from mapping import MyMapping

def generate_wave(f, duration, volume=0.5, fs=44100):
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
    stream.write(samples)
    stream.stop_stream()
    stream.close()

def generate_sequence(f, data):
    duration = 8
    #sample_length = duration/len(data)
    sample_length = 1/35 #Smallest sample rate my speaker can handle
    print(sample_length)
    generate_wave(f, 1)
    time.sleep(0.50)
    for num in data:
        if num:
            print(1)
            time.sleep(sample_length/2.5)
            generate_wave(f, sample_length/1)
            time.sleep(sample_length/3.5)
            generate_wave(f, sample_length/1)
            time.sleep(sample_length/2.5)
        else:
            print(0)
            time.sleep(sample_length/2.5)
            generate_wave(f, sample_length)
            time.sleep(sample_length/2.5)
            

def createBinary(data):
    mapping = MyMapping(True)
    mapping = mapping.mapping
    ret = ""
    for item in data:
        ret += mapping[item]
    return ret

data = createBinary(sys.argv[2])
print(data)
generate_sequence(int(sys.argv[1]), [int(n) for n in data])
