import tkinter as tk
import random
# from .back2 import calculations


"""
MainApp class code referenced from "Bryan Oakley" on https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
Creates a container that allows multiple frames to be stacked onto each other. 
"""
class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # container is created where all the frames are stacked on top of each other
        container = tk.Frame(self, bg="#FAF0E6")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        # dictionary of variables that allows access for classes to use
        self.shared = {
            "endNumber": tk.IntVar(),
            "firstNumber": tk.IntVar(),
            "rounds": tk.IntVar(),
            "finalCalc": tk.IntVar(),
            "counter": tk.IntVar()
        }

        # puts all of the pages in the same location, and is put in the stacking order
        self.frames = {}
        for F in (StartPage, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # starts with the start page
        self.show_frame("StartPage")

    # shows a frame with a given name
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


"""
Handles the Start Page 
"""
class StartPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.startPrompt = tk.Label(self, text="How Many Rounds?", fg="#BC8F8F", font=("Bahnschrift", 20, "bold"))
        self.startPrompt.pack()

        """Handles the texts for the amount of rounds"""
        # entry section for the amount of rounds
        self.startEntry = tk.Entry(self, font=("Bahnschrift", 15, "bold"), justify="center", fg="#BC8F8F",width=25, textvariable=self.controller.shared["rounds"])
        self.startEntry.pack()


        # button to verify the number for the entry button
        self.entryButtonVer = tk.Button(self, text="Verify", width="8", height="3", font=("Bahnschrift", 7, "bold"),command=self.buttonVerifyRounds, state="normal")
        self.entryButtonVer.pack()

        self.noticeErrorRounds = tk.Label(self, text="")
        self.noticeErrorRounds.pack()

        """First Number"""
        # asks for the first number in the range
        self.startRange1 = tk.Label(self, text="Beginning Number", fg="#BC8F8F", font=("Bahnschrift", 20, "bold"), width=25)
        self.startRange1.pack()

        # user input for the first number to use for multiplication
        self.startRangeEntry = tk.Entry(self, font=("Bahnschrift", 15, "bold"), justify="center", fg="#BC8F8F", width=25, textvariable=self.controller.shared["firstNumber"])
        self.startRangeEntry.pack()

        # button to verify the number for the first number in the range
        self.entryButtonRange1 = tk.Button(self, text="Verify", width="8", height="3",font=("Bahnschrift", 7, "bold"), command=self.buttonVerifyRange1, state="normal")
        self.entryButtonRange1.pack()

        self.noticeErrorRange1 = tk.Label(self, text="")
        self.noticeErrorRange1.pack()

        """Ending Number"""
        # creates a label for "Ending Number"
        self.startRange2 = tk.Label(self, text="Last Number", fg="#BC8F8F", font=("Bahnschrift", 20, "bold"), width=25)
        self.startRange2.pack()

        # creates a user input for the "Ending Number" section
        self.startEndEntry = tk.Entry(self, font=("Bahnschrift", 15, "bold"), justify="center", fg="#BC8F8F", width=25, textvariable=self.controller.shared["endNumber"])
        self.startEndEntry.pack()

        # button to verify the number for the second number in the range
        self.entryButtonRange2 = tk.Button(self, text="Verify", width="8", height="3", font=("Bahnschrift", 7, "bold"), command=self.buttonVerifyRange2,state="normal")
        self.entryButtonRange2.pack()

        self.noticeErrorRange2 = tk.Label(self, text="")
        self.noticeErrorRange2.pack()

        self.startButton = tk.Button(self, text="Start!", width="15", height="3", fg="#CD5C5C",font=("Bahnschrift", 15, "bold", "italic"), state="normal", command=lambda: controller.show_frame("PageTwo"))
        self.startButton.place(relx=0.5, rely=0.9, anchor="s")

    """
    Handes the verifying button for the amount of rounds 
    """
    def buttonVerifyRounds(self):
        try: # ensures the number inputted in an integer and greater than 0
            if int(self.controller.shared["rounds"].get()) <= 0:
                # sends an error message to the user
                self.noticeErrorRounds.config(text="Please Enter a Number > 0")
            if int(self.controller.shared["rounds"].get()) > 0:
                # assigns the rounds variable to the inputted value
                rounds = int(self.controller.shared["rounds"].get())

                # configures the button to say verified
                self.entryButtonVer.config(state="normal")
                self.noticeErrorRounds.config(text="Verified!")
                return rounds

        # if the inputted value is not an integer
        except ValueError:
            self.noticeErrorRounds.config(text="Please Enter in a Number!")
        except _tkinter.TclError:
            self.noticeErrorRounds.config(text="Please Enter in a Number!")

    """
    Handles the verifying button for the first number in the range
    """
    def buttonVerifyRange1(self):
        try: # ensures the number inputted in a integer and is greater than 0
            if int(self.controller.shared["firstNumber"].get()) <= 0:
                self.noticeErrorRange1.config(text="Please Enter a Number > 0")

            # if the input is an integer greater than zero
            if int(self.controller.shared["firstNumber"].get()) > 0:
                firstNumber = int(self.controller.shared["firstNumber"].get())
                # the verify button sends a "verified" message
                self.entryButtonRange1.config(state="normal")
                self.noticeErrorRange1.config(text="Verified!")

        # if the inputted value is not an integer
        except ValueError:
            self.noticeErrorRange1.config(text="Please Enter in a Number!")
        except _tkinter.TclError:
            self.noticeErrorRange1.config(text="Please Enter in a Number!")

    """
    Handles the verifying button for the second range input 
    """
    def buttonVerifyRange2(self):
        try: # ensures that the user inputs in a number greater than the first number in the range
            if int(self.controller.shared["endNumber"].get()) <= int(self.controller.shared["firstNumber"].get()):
                self.noticeErrorRange2.config(text="Please Enter in a Number Greater Than the First Number!")

            if int(self.controller.shared["endNumber"].get()) > int(self.controller.shared["firstNumber"].get()):
                # assigns the end range number the user inputted
                endNumber = int(self.controller.shared["endNumber"].get())

                # sends a verification message to the user
                self.noticeErrorRange2.config(text="Verified!")
                return endNumber

        # if the user does not input an integer
        except ValueError:
            self.noticeErrorRange2.config(text="Please Enter in a Number!")
        except _tkinter.TclError:
            self.noticeErrorRange2.config(text="Please Enter in a Number!")
"""
Handles the Second Page 
Utilizes the after method in tkinter to wait for the user input for three seconds. Will be using threading for voice recognition
"""
class PageTwo(tk.Frame):
    # constructor
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        # sample demo text
        self.secPage = tk.Label(self, text="Manages the Main Game Premise")
        self.secPage.pack()

        self.demoText = tk.Label(self, fg="#BC8F8F",text="RangeX x RangeY", font=("Bahnschrift", 50, "bold"))
        self.demoText.place(relx=0.5, rely=0.5, anchor="s")

        self.demoButton = tk.Button(self, text="Record", font=("Bahnschrift", 15, "bold"), fg="red", comand=self.recording())
        self.demoButton.place(relx=0.5, rely=0.6, anchor="s")

        self.nextButton = tk.Button(self, width="10", height="2", text="Next Page", command=lambda: controller.show_frame("PageThree"))
        self.nextButton.place(relx=0.5, rely=0.9, anchor="s")

    def recording(self):
        # sets up the recording process
        print("Recording")

"""
    # repeat for the amount of rounds inputted. Generates two random numbers with the given parameters 
    for i in range(rounds):
        def generate(self):
            # generates two random numbers in the range given
            rangeX = int(random.randint(self.firstNumber, endNumber + 1))
            rangeY = int(random.randint(self.firstnumber, endNumber + 1))
            print(rangeX)

            # calculates the answer
            finalCalc = rangeX * rangeY

            return rangeX, rangeY, finalCalc
        
    
"""

"""
Handles the end page 
"""
class PageThree(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.demotext = tk.Label(self, text="Your Score: ", font=("Bahnschrift", 50, "bold") )
        self.demotext.place(relx=0.5, rely=0.3, anchor="n")

        self.demoScore = tk.Label(self, text="10", font=("Bahnschrift", 30, "bold"))
        self.demoScore.place(relx=0.5, rely=0.5, anchor="s")



if __name__=="__main__":
    app = MainApp()
    app.geometry("800x800")
    app.title("Multiplyer")
    app.mainloop()


