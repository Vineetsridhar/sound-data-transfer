from getAmplitudeTest import *
import sys, os
import pyaudio
import wave
from array import array
import time
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = "output.wav"
THRESHOLD = 10000

def is_silence(data):
        return max(data) < THRESHOLD
    
def sound():
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []
    data = array('h')
    data.append(0)
    while is_silence(data):
        data_chunk = array('h', stream.read(CHUNK))
        if sys.byteorder == 'big':
            data_chunk.byteswap()
        data.extend(data_chunk)


    stream.stop_stream()
    stream.close()
    print("Waiting one second")
    time.sleep(1)

    print("Recording")
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)


    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    getAmp()
    #sound()

sound()
    

