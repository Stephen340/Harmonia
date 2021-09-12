# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:31:47 2021

@author: stjoh
"""

from playsound import playsound
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

pianoList = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C","C#","D","D#","E","F","F#","G"]

#return the major triad when called
def majorTriad(note):
    chord = ""
    if note <= 12:
        chord += pianoList[note]
        chord += " - "
        chord += pianoList[note+4]
        chord += " - "
        chord += pianoList[note+7]
    return chord

#return the minor triad when chosen
def minorTriad(note):
    chord = ""
    if note <= 12:
        chord += pianoList[note]
        chord += " - "
        chord += pianoList[note+3]
        chord += " - "
        chord += pianoList[note+7]
    return chord
    
#variable used for the minor/major toggle
major = True

#set piano to use major triads
def changeTypemaj():
    global major
    if major == False:
        major = True
        
#set piano to use minor triads
def changeTypemin():
    global major
    if major == True:
        major = False

#The configuration of the display text
toDisplay = ""
notesLabel = tk.Label(root, text=toDisplay, font = ("Helvetica", 20))
notesLabel.grid(columnspan=3, column=0, row=2)

'''
    The following functions were all made to be a part of the actual piano.
    Upon clicking a button on the piano, the sound of the respective key's
    harmony will play. The function for the button will also call the functions
    for the harmony display, and set the text to the screen.
'''
def isClickedc():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\c.wav')
        toDisplay = majorTriad(0)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\cm.wav')
        toDisplay = minorTriad(0)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        

def isClickedcs():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\cs.wav')
        toDisplay = majorTriad(1)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\pm.wav')
        toDisplay = minorTriad(1)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
    
        
def isClickedd():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\d.wav')
        toDisplay = majorTriad(2)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\dm.wav')
        toDisplay = minorTriad(2)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
              
def isClickedds():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\ds.wav')
        toDisplay = majorTriad(3)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\um.wav')
        toDisplay = minorTriad(3)
    notesLabel.config(text = toDisplay)
    notesLabel.update()

def isClickede():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\e.wav')
        toDisplay = minorTriad(4)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\em.wav')
        toDisplay = minorTriad(4)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        
def isClickedf():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\f.wav')
        toDisplay = majorTriad(5)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\fm.wav')
        toDisplay = minorTriad(5)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        
def isClickedfs():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\fs.wav')
        toDisplay = majorTriad(6)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\xm.wav')
        toDisplay = minorTriad(6)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
                
def isClickedg():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\g.wav')
        toDisplay = majorTriad(7)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\gm.wav')
        toDisplay = minorTriad(7)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
                
def isClickedgs():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\gs.wav')
        toDisplay = majorTriad(8)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\ym.wav')
        toDisplay = minorTriad(8)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        
def isClickeda():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\a.wav')
        toDisplay = majorTriad(9)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\am.wav')
        toDisplay = minorTriad(9)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        
def isClickedbf():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\bf.wav')
        toDisplay = majorTriad(10)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\bb.wav')
        toDisplay = minorTriad(10)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        
def isClickedb():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\b.wav')
        toDisplay = majorTriad(11)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\bm.wav')
        toDisplay = minorTriad(11)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        
def isClickedbc():
    if(major):
        playsound(r'C:\\Users\stjoh\Documents\triads\cc.wav')
        toDisplay = majorTriad(12)
    else:
        playsound(r'C:\\Users\stjoh\Documents\riadds\zm.wav')
        toDisplay = minorTriad(12)
    notesLabel.config(text = toDisplay)
    notesLabel.update()
        
 
    
             
        
        


#The beginning of the actual display for the piano, using TKinter
canvas = tk.Canvas(root, width=1400, height=700)

canvas.grid(columns=20,columnspan= 3,rowspan= 4)

#Set the piano into the display
piano = Image.open("piano.png")
piano_resize = piano.resize((960, 480))
newPiano = ImageTk.PhotoImage(piano_resize)
piano_label = tk.Label(image=newPiano)
piano_label.image = newPiano
piano_label.grid(columnspan = 3, column=0, row=1)


#Set the instructions for the program
instructions = tk.Label(root, text="Click a piano key and then either major or minor", font = ("Helvetica", 17))
instructions.grid(columnspan=3, column=0, row=3)

#The name of the program
notesLabel = tk.Label(root, text="", font = ("Helvetica", 20))
notesLabel.grid(columnspan=3, column=0, row=2)

#Set the title
title = tk.Label(root, text="Harmonia", width =40, font = ("Rockwell", 25))
title.grid(columnspan=3, column=0, row=0)

#Image setting for the logo of the program
logo = Image.open("Capture.PNG")
logo = logo.resize((300, 147))
newLogo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = newLogo)
logo_label.grid(columnspan=3,column=0,row=0)

#button for the major switch
button = Image.open("majorButton.png")
button = button.resize((200,45))
buttonImg = ImageTk.PhotoImage(button)

#button for the minor switch
button1 = Image.open("minorButton.png")
button1 = button1.resize((200,45))
buttonImg1 = ImageTk.PhotoImage(button1)

#Follow actions when major button is clicked
major_btn = tk.Button(root, text="Major", width=200, height=45, image=buttonImg,command=changeTypemaj)
major_btn.grid(column=0, row = 2)

#Follow actions when minor button is clicked
minor_btn = tk.Button(root, text="Minor", width=200, height=45, image=buttonImg1,command=changeTypemin)
minor_btn.grid(column=2, row = 2)

# Piano key Buttons
def hide_button(widget):
    widget.pack_forget()


#These are all of the actual buttons for the keys, they will call different commands
#to call respective harmonies
buttonC1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedc).place(x=224,y=410)
buttonD1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedd).place(x=292,y=410)
buttonE1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickede).place(x=361,y=410)
buttonF1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedf).place(x=429,y=410)
buttonG1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedg).place(x=497,y=410)
buttonA1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickeda).place(x=566,y=410)
buttonB1 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedb).place(x=635,y=410)

buttonC2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedbc).place(x=704,y=410)
buttonD2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedd).place(x=773,y=410)
buttonE2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickede).place(x=842,y=410)
buttonF2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedf).place(x=910,y=410)
buttonG2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedg).place(x=978,y=410)
buttonA2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickeda).place(x=1046,y=410)
buttonB2 = tk.Button(activebackground='gray',activeforeground='red',width=8,height=8,command=isClickedb).place(x=1115,y=410)

buttonCS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedcs).place(x=273, y=249)
buttonDS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedds).place(x=341, y=249)
buttonFS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedfs).place(x=478, y=249)
buttonGS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedgs).place(x=546, y=249)
buttonAS1 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedbf).place(x=614, y=249)

buttonCS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedcs).place(x=753, y=249)
buttonDS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedds).place(x=822, y=249)
buttonFS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedfs).place(x=958, y=249)
buttonGS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedgs).place(x=1026, y=249)
buttonAS2 = tk.Button(activebackground='gray',activeforeground='red',bg = 'black', width=4,height=10,command=isClickedbf).place(x=1094, y=249)



root.mainloop()
