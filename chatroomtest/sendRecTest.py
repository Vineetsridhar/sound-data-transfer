from generatorTest import *

def new():
    try:
        file = open("buffer.txt")
        file2 = open("chathistory.txt")
    except IOError:
        file = open("buffer.txt", 'w')
        file2 = open("chathistory.txt", 'w')
        file.close()
        file2.close()

def clear(file):
    inF = open(file, "w")

def send(inp):
    print("Sending code: ")
    print(inp)
    call(inp)

def receive():
    buffer = open('buffer.txt', 'r')
    for line in buffer:
        print("Incoming data: ")
        chat = open('chathistory.txt', 'a')
        chat.write(line + '\n')
        chat.close()
        print(line)
    buffer.close()