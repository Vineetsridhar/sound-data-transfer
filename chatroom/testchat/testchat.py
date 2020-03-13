from tkinter import *
from decoder import *
from testSend import *

'''
Chatroom uses local testHist.txt for textchat and a testBuff.txt to get outside binary
'''

def textchat():
    chat = open("testHist.txt", "r")
    for line in chat:
        text.insert(END, alpha(d, line) + '\n')
    chat.close()

def insert():
    s = entry.get()
    if(s != ""):
        
        chat = open("testHist.txt", "a")
        chat.write(binary(d, name) + binary(d, "... ")  + binary(d, s) + '\n')
        chat.close()
        
        send(binary(d, name) + binary(d, "... ")  + binary(d, s))
    entry.delete(0, END)

def refresh():
    '''Refreshes server every REF seconds'''
    
    text.delete("1.0", END)
    receive()
    textchat()
    text.yview(END)
    clear('testBuff.txt')
    print("Chat refreshed!")
    root.after(REF, refresh)

def define():
    global name
    name = entry2.get()
    if(name == ""):
        label3 = Label(frame2, text = "No username provided")
        label3.pack()
    else:
        new()
        root2.destroy()
        
name = ""

'''Entry Window'''
root2 = Tk()
root2.resizable(0,0)
canvas2 = Canvas(root2, height = 101, w = 200)
canvas2.pack()
frame2 = Frame(root2)
frame2.place(x=28,y=18)
title2 = Label(frame2, text = "Welcome to our messenger")
title2.pack()
entry2 = Entry(frame2)
entry2.pack()
button2 = Button(frame2, text = "Enter chatroom", command = define)
button2.pack()
root2.mainloop()

if(name != ""):
    '''Messenger Window'''
    root = Tk()
    root.resizable(0,0)
    canvas = Canvas(root, height= 800, width= 600)
    canvas.pack()
    title = Label(root, text = "Welcome to the chatroom!")
    title.place(x=210,y=41)
    frame = Frame(root)
    frame.place(x=85, y = 110)
    scroll = Scrollbar(frame)
    scroll.pack(side=RIGHT, fill=Y)
    text = Text(frame, yscrollcommand=scroll.set, height=30, width=50)
    text.pack()
    scroll.config(command=text.yview)
    label = Label(frame, text=" ")
    label.pack()
    entry = Entry(frame, width=65)
    entry.pack()
    button = Button(frame, text="Enter", command = insert)
    button.pack()
    space = Label(frame, text = "")
    space.pack()
    button = Button(frame, text="Leave", command = root.destroy)
    button.pack()

    REF = 5000
    
    root.after(500, refresh)
    root.mainloop()





 