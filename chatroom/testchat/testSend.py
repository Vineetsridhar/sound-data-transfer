from decoder import binary, d

def new():
    try:
        file = open("testBuff.txt")
        file2 = open("testHist.txt")
    except IOError:
        file = open("testBuff.txt", 'w')
        file2 = open("testHist.txt", 'w')
        file.close()
        file2.close()

def clear(file):
    inF = open(file, "w")

def send(num):
    print("Sending code: ")
    print(num)
    
    #Test Code with chatroom.py
    '''
    buffer = open('buffer.txt', 'a')
    buffer.write(num)
    buffer.close()
    '''
def receive():
    
    '''Checks buffer every REF seconds'''
    
    buffer = open('testBuff.txt', 'r')
    print("Incoming data: ")
    for line in buffer:
        chat = open('testHist.txt', 'a')
        chat.write(line + '\n')
        chat.close()
        print(line)
    buffer.close()