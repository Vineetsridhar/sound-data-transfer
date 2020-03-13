from decoder import binary, d

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

def send(num):
    print("Sending code: ")
    print(num)
   
    # TEST CODE WITH chatroom.py
    '''
    buffer = open('testBuff.txt', 'a')
    buffer.write(num)
    buffer.close()
    '''
def receive():
    
    '''Checks buffer every REF seconds'''
    
    buffer = open('buffer.txt', 'r')
    print("Incoming data: ")
    for line in buffer:
        chat = open('chathistory.txt', 'a')
        chat.write(line + '\n')
        chat.close()
        print(line)
    buffer.close()