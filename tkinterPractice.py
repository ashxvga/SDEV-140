"""
import tkinter as tk

mainWindow = tk.Tk()

#frame1
frame1 = tk.LabelFrame(mainWindow, text= "Frame 1", padx = 10, pady = 10)

#add frame to window
frame1.grid(row = 0, column = 0, columnspan = 10, rowspan = 10)

#create label
fname = tk.Label(frame1,  text = "Firstname")

#add label to fname
fname.grid(row = 2, column= 0)

#create a textbox
enterfname = tk.Entry()

mainWindow.mainloop()
"""
from tkinter import *

#make window
mainWindow = Tk()

#change title of the window
mainWindow.title("Student Application")

#change background color
mainWindow.configure(bg = "blue")

#frame1
frame1 = LabelFrame(mainWindow, text= "Frame 1", padx = 10, pady = 10)

#add frame to window
frame1.grid(row = 0, column = 0, columnspan = 10, rowspan = 10)

#create label
fname = Label(frame1,  text = "Firstname")
lname = Label(frame1,  text = "Lastname")
age = Label(frame1, text = "Age")

#add label to fname
fname.grid(row = 2, column= 0)
#add label to lname
lname.grid(row= 5, column = 0)
#add label to age
age.grid(row = 8, column = 0)

#create a textbox
enterfname = Entry(frame1, width = 20)
enterlname = Entry(frame1, width = 20)
enterAge =   Entry(frame1, width = 20)

#add textbox to frame
enterfname.grid(row = 2, column = 5)
enterlname.grid(row = 5, column = 5)
enterAge.grid(row = 8, column = 5)

#frame2
frame2 = LabelFrame(mainWindow, text = "Frame 2", padx = 10, pady = 10)

#add frame2 to mainwindow
frame2.grid(row = 0, column = 25, columnspan = 10, rowspan = 10)

#create buttons with a function - create a function to call
def calcAge():
  yourAge = int(enterAge.get()) + 5
  #creates a label to display the age when the buton is clicked
  buttonLabel = Label(frame2, text = yourAge)
  buttonLabel.grid(row = 0, column = 35)
  
#create a button
calcButton = Button(frame2, text = "Calculate Age", command = calcAge)
calcButton.grid(row = 0, column = 30)

mainWindow.mainloop()