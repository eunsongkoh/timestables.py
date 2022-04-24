import speech_recognition as sr
import tkinter as tk

# global variables
finalCalc = 0
userAnswer = 0
counter = 0

"""
startPage.py is part of main.py but is displayed on a different file on github for readbility reasons. 
Creates the window and the start page for timestables.py
Asks for the amount of rounds the user would like to practice their multiplication tables
It then asks for the range they would like to practice 
Lines 15-36 referenced from: https://www.youtube.com/watch?v=MKgDQjZwI2o "Python - Create Multiple Window Frames with TKinter ( The easiest way )" By: codefoxx

stackFrames(frame)
Allows frames to be stacked on top of each other 
"""
def stackFrames(frame):
    frame.tkraise()

# creates an instance of tkinter
window = tk.Tk()

# sets the window size
window.geometry("900x800")

# ensures that the frame expands with the window
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# creates the different frames included in the program
startFrame = tk.Frame(window, bg="#FAF0E6")
frame2 = tk.Frame(window, bg="#FAF0E6")
frame3 = tk.Frame(window, bg="#FAF0E6")

# allows the frame to mold into the size of the window
startFrame.grid(row=0, column=0, sticky='nsew')
frame2.grid(row=0, column=0, sticky='nsew')
frame3.grid(row=0, column=0, sticky='nsew')

# opens the startFrame frame
stackFrames(startFrame)

# frame 1 code
startTitle = tk.Label(
    startFrame,
    text="TimesTables.py",
    fg="#CD5C5C",
    bg="#FAF0E6",
    font=("Bahnschrift", 50, "bold", "italic")
)

startPrompt = tk.Label(
    startFrame,
    text="How Many Rounds?",
    fg="#BC8F8F",
    bg="#FAF0E6",
    font=("Bahnschrift", 20, "bold")
)

startEntry = tk.Entry(
    startFrame,
    font=("Bahnschrift", 15, "bold"),
    justify="center",
    fg="#BC8F8F",
    bg="#FAF0E6",
    width=25
)
# assigns the value inputted by the user for the amount of rounds
roundsAnswer = startEntry.get()
rounds = int(roundsAnswer)

# the starting range label
startRange1 = tk.Label(
    startFrame,
    text="Beginning Number",
    fg="#BC8F8F",
    bg="#FAF0E6",
    font=("Bahnschrift", 20, "bold"),
    width=25
)

# user input for the first number to use for multiplication
startRangeEntry = tk.Entry(
    startFrame,
    font=("Bahnschrift", 15, "bold"),
    justify="center",
    fg="#BC8F8F",
    bg="#FAF0E6",
    width=25
)
# assigns the user input of the first number in the range
firstAnswer = startRangeEntry.get()
firstNumber = int(firstAnswer)

# creates a label for "Ending Number"
startRange2 = tk.Label(
    startFrame,
    text="Ending Number",
    fg="#BC8F8F",
    bg="#FAF0E6",
    font=("Bahnschrift", 20, "bold"),
    width=25
)

# creates a user input for the "Ending Number" section
startEndEntry = tk.Entry(
    startFrame,
    font=("Bahnschrift", 15, "bold"),
    justify="center",
    fg="#BC8F8F",
    bg="#FAF0E6",
    width=25
)
# assigns the end value for the multiplication
endAnswer = startEndEntry.get()
endNumber = int(endAnswer)

# Start Button
startButton = tk.Button(
    startFrame,
    text="Start!",
    width="15",
    height="3",
    fg="#CD5C5C",
    font=("Bahnschrift", 15, "bold", "italic"),
    command=lambda: stackFrames(frame2)
)

# packing and placement of startFrame
startTitle.pack(ipadx=20, ipady=20)
startPrompt.pack()
startEntry.pack()
startRange1.pack()
startRangeEntry.pack()
startRange2.pack()
startEndEntry.pack()
startButton.place(relx=0.5, rely=0.9, anchor="s")
