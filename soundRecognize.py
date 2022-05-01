"""
Due to too many hardware problems, this code will be used in the future to further expand the project. 
Instead of using user input, the program will use the user's voice for an answer when prompted. 
"""

import speech_recognition as sr
from front import rounds, firstNumber, endNumber
import tkinter as tk

import random

# global variables
finalCalc = 0
rangeX = 0
rangeY = 0
counter = 0

"""
numbersCalc generates two random numbers between 1 - 10 for the user to solve 
pre: none 
post: returns the final calculation of the two numbers 
"""
def numbersCalc(firstNumber, endNumber):
    print(firstNumber)
    global finalCalc
    global rangeX
    global rangeY

    # calculates two random numbers between the range of the first and end number
    rangeX = int(random.randrange(firstNumber, endNumber + 1, 1))
    rangeY = int(random.randrange(firstNumber, endNumber + 1, 1))

    # calculates the answer of the randomly generated numbers
    finalCalc = rangeX * rangeY

    # returns the two randomly generated numbers and the answer
    return (rangeX, rangeY, finalCalc)



"""
getAudio uses speech recognition 
pre: none 
post: returns the final mic input of the human   
"""
def getAudio():
    # instance of the class
    r = sr.Recognizer()

    # instance of microphone class
    micInput  = sr.Microphone()

    with sr.Microphone() as source:
        # IF BACKGROUND NOISE IS AN ISSUE: r.adjust_for_ambient_noise(source, duration=5)

        # listens to the source of input for the duration of 3 seconds
        print("Listening for 3 seconds: ")
        audio = r.listen(source, phrase_time_limit=3)

        try:
            global userAnswer
            # recognizes the audio input using Google API
            userAnswer = r.recognize_google(audio)

            # changes the string to an int
            userAnswer = int(userAnswer)

        # handles the errors if there is no input into the mic or other issues
        except UnboundLocalError:
            print("it did not work")
        except sr.UnknownValueError:
            print("No mic input detected")
        except sr.WaitTimeoutError:
            print("No mic input detected")
        except ValueError:
            print("Must be an Integer")

    # returns the answer of the user
    return userAnswer


def check(finalCalc, userAnswer):
    if finalCalc == userAnswer:
        print("correct")
        global counter
        counter += 1
    else:
        print("no")

def points(counter):
    print(counter)


for i in range(1, rounds):
    numbersCalc(firstNumber, endNumber)
    getAudio()
    check(finalCalc, userAnswer)
    points(counter)
