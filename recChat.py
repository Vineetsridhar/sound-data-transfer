from tkinter import *
from decoder import *
from sendRec import *

def refresh():
    text.delete("1.0", END)
    receive()
    textchat()
    text.yview(END)
    clear('buffer.txt')
    print("Chat Refreshed!")
    root.after(REF, refresh)
    
def textchat():
    chat = open("chathistory.txt", "r")
    for line in chat:
        text.insert(END, alpha(d, line) + '\n')
    chat.close()    

new()

root = Tk()
root.resizable(0,0)
canvas = Canvas(root, height= 800, width= 600)
canvas.pack()
title = Label(root, text = "Receiving Messages")
title.place(x=230,y=41)
frame = Frame(root)
frame.place(x=48, y = 110)
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)
text = Text(frame, yscrollcommand=scroll.set, height=40, width=63)
text.pack()
scroll.config(command=text.yview)

REF = 5000

root.after(1000, refresh)
root.mainloop()






