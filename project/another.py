from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Initialize the main window
win = Tk()
win.title("QUIZ COMPETITION")
win.iconbitmap("E:\\Khushi-College\\Python-practice\\Hackerrank\\NIIT_PACKAGE\\Custom-Icon-Design-Pretty-Office-10-Test-paper.512-_1_.ico")
win.maxsize(width=1000, height=400)
win.minsize(width=1000, height=400)

# Initialize the total score variable
total_score = 0

# Create a Notebook widget
a = ttk.Notebook(win)

# Create frames for each question
f1 = ttk.Frame(a)
f2 = ttk.Frame(a)
f3 = ttk.Frame(a)
f4 = ttk.Frame(a)
f5 = ttk.Frame(a)

# Function to update the score display
def update_score():
    global total_score
    total_score_label.config(text=f"Total Score: {total_score}")

# Define functions for correct and incorrect answers for each question
def right1():
    global total_score
    total_score += 1
    Label(f1, text="Correct", font=("Arial", 20, "bold"), background="green", fg="black").grid(row=1, column=2)
    update_score()

def wrong1():
    Label(f1, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="black").grid(row=1, column=2)

def right2():
    global total_score
    total_score += 1
    Label(f2, text="Correct", font=("Arial", 20, "bold"), background="green", fg="black").grid(row=1, column=2)
    update_score()

def wrong2():
    Label(f2, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="black").grid(row=1, column=2)

def right3():
    global total_score
    total_score += 1
    Label(f3, text="Correct", font=("Arial", 20, "bold"), background="green", fg="black").grid(row=1, column=2)
    update_score()

def wrong3():
    Label(f3, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="black").grid(row=1, column=2)

def right4():
    global total_score
    total_score += 1
    Label(f4, text="Correct", font=("Arial", 20, "bold"), background="green", fg="black").grid(row=1, column=2)
    update_score()

def wrong4():
    Label(f4, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="black").grid(row=1, column=2)

def right5():
    global total_score
    total_score += 1
    Label(f5, text="Correct", font=("Arial", 20, "bold"), background="green", fg="black").grid(row=1, column=2)
    update_score()

def wrong5():
    Label(f5, text="Incorrect", font=("Arial", 20, "bold"), background="red", fg="black").grid(row=1, column=2)

# Function to display the final score
def show_final_score():
    messagebox.showinfo("Final Score", f"Your total score is: {total_score}")

# Function to setup the quiz
def quiz():
    a.add(f1, text="Q1")
    a.add(f2, text="Q2")
    a.add(f3, text="Q3")
    a.add(f4, text="Q4")
    a.add(f5, text="Q5")

    Label(f1, text="Total keywords in python?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(f1, text="33", font=("Arial", 10, "bold"), bg="yellow", command=right1).grid(row=3, column=1)
    Button(f1, text="30", font=("Arial", 10, "bold"), bg="yellow", command=wrong1).grid(row=3, column=2)
    Button(f1, text="31", font=("Arial", 10, "bold"), bg="yellow", command=wrong1).grid(row=3, column=3)

    Label(f2, text="Output of 2**3?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(f2, text="6", font=("Arial", 10, "bold"), bg="yellow", command=wrong2).grid(row=3, column=1)
    Button(f2, text="8", font=("Arial", 10, "bold"), bg="yellow", command=right2).grid(row=3, column=2)
    Button(f2, text="9", font=("Arial", 10, "bold"), bg="yellow", command=wrong2).grid(row=3, column=3)

    Label(f3, text="Output of np.arange(1,5)?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(f3, text="[1,2,3,4]", font=("Arial", 10, "bold"), bg="yellow", command=right3).grid(row=3, column=1)
    Button(f3, text="[0,1,2,3,4]", font=("Arial", 10, "bold"), bg="yellow", command=wrong3).grid(row=3, column=2)
    Button(f3, text="[1,2,3,4,5]", font=("Arial", 10, "bold"), bg="yellow", command=wrong3).grid(row=3, column=3)

    Label(f4, text="Keywords used to declare a function in python?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(f4, text="def", font=("Arial", 10, "bold"), bg="yellow", command=right4).grid(row=3, column=1)
    Button(f4, text="ref", font=("Arial", 10, "bold"), bg="yellow", command=wrong4).grid(row=3, column=2)
    Button(f4, text="function", font=("Arial", 10, "bold"), bg="yellow", command=wrong4).grid(row=3, column=3)

    Label(f5, text="Output of 2*12?", font=("Arial", 30, "bold")).grid(row=2, column=2)
    Button(f5, text="24", font=("Arial", 10, "bold"), bg="yellow", command=right5).grid(row=3, column=1)
    Button(f5, text="28", font=("Arial", 10, "bold"), bg="yellow", command=wrong5).grid(row=3, column=2)
    Button(f5, text="33", font=("Arial", 10, "bold"), bg="yellow", command=wrong5).grid(row=3, column=3)

# Add the quiz to the notebook
quiz()

# Add a label to display the total score
total_score_label = Label(win, text="Total Score: 0", font=("Arial", 20, "bold"), background="blue", fg="white")
total_score_label.pack(side=TOP)

# Add a button to show the final score
Button(win, text="Show Final Score", font=("Arial", 20, "bold"), command=show_final_score).pack(side=BOTTOM)

# Pack the notebook
a.pack(expand=1, fill="both")

# Run the main loop
win.mainloop()
