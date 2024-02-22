import tkinter
from tkinter import *
from PIL import Image, ImageTk

#The first window is the main - where the user identifies as employer or employee 
mainWindow = Tk()
mainWindow.title("Salary Calculator: Easy Pay")
mainWindow.geometry("500x500")
mainWindow.configure(bg= "white")

employerImageIcon = Image.open("/Users/ashleyvega/Downloads/3324336-200.png")
employerIcon = ImageTk.PhotoImage(employerImageIcon)
employerImageLabel = tkinter.Label(image = employerIcon)
employerImageLabel.image = employerIcon
mainWindow.mainloop()
#Employeer window
"""
For the second window - employer window
employerNameLabel = Label(mainWindow, text = "Employee Name: ")
employerNameLabel.pack()
"""
