from tkinter import *
from decoder import *
from sendRec import *

def insert():
    s = entry.get()
    if(s != ""):
        send(binary(d, name) + binary(d, "... ")  + binary(d, s))
    entry.delete(0, END)
    label4 = Label(frame, text = "Message sent!")
    label4.pack()
    root.after(1000, label4.destroy)
    
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
    #root.resizable(0,0)
    canvas = Canvas(root, height= 155, width= 500)
    canvas.pack()
    title = Label(root, text = "Send a message")
    title.place(x=210,y=10)
    frame = Frame(root)
    frame.place(x=55, y = 40)
    entry = Entry(frame, width=65)
    entry.pack()
    button = Button(frame, text="Enter", command = insert)
    button.pack()
    button = Button(frame, text="Leave", command = root.destroy)
    button.pack()
    root.mainloop()