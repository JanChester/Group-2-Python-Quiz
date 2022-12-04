from tkinter import *

Questions = ["What is a correct syntax to output \"Hello World\" in Python?",
             "What is the correct file extension for Python files?",
             "What is the correct way to create a function in Python?",
             "Which operator is used to multiply numbers?",
             "Which operator can be used to compare two values?",
             "How do you start writing an if statement in Python?",
             "Which statement is used to stop a loop?",
             "Which of the following keywords lets you test a block of code for errors?",
             "It is the class being inherited from, also called base class.",
             "What is the ability of the class to inherit more than one class?"]

Options = [["print(\"Hello World\")", "p(\"Hello World\")", "system.out.print(\"Hello World\")"],
           [".pyth", ".py", ".python"],
           ["def myFunction():", "create myFunction():", "function myFunction():"],
           ["%", "#", "*"],
           ["=", "==", "<>"],
           ["if (x > y)", "if x > y:", "if x > y then:"],
           ["stop", "return", "break"],
           ["except", "try", "if"],
           ["Derived class", "Child class", "Parent class"],
           ["Multi-level inheritance", "Hybrid inheritance", "Multiple inheritance"]]

Answers = [1, 2, 1, 3, 2, 2, 3, 2, 3, 3]

userScore = 0
questionTotal = 10
questionNo = 1


def next():
    global userScore, questionNo
    if val1.get() == 1:
        selected_option = 1
    elif val2.get() == 1:
        selected_option = 2
    elif val3.get() == 1:
        selected_option = 3
    else:
        selected_option = -1

    if Answers[questionNo-1] == selected_option :
        userScore += 1

    questionNo += 1

    if questionNo > questionTotal:
        root.grid_forget()
        score.grid(row = 2, column = 2, ipadx = 640, ipady = 100, pady = 150)
        score.config(text="Score: "+ str(userScore), font = ("Arial", 50), bg = 'red', fg = 'white')
        exitBtn1.grid(row = 3, column = 2)
        exitBtn1.config(text="Exit", font = ("Arial", 50), command = Win.destroy, bg = 'red', fg = 'white')

    else:
        val1.set(0)
        val2.set(0)
        val3.set(0)
        question.config(text=Questions[questionNo-1])
        option1.config(text=Options[questionNo-1][0])
        option2.config(text=Options[questionNo-1][1])
        option3.config(text=Options[questionNo-1][2])


def check(option):
    if option == 1:
        val2.set(0)
        val3.set(0)
    elif option == 2:
        val1.set(0)
        val3.set(0)
    else:
        val2.set(0)
        val1.set(0)


def startQuiz():
    homeScreen.grid_forget()
    root.grid(row = 2, column = 2)


Win = Tk()
Win.geometry("1000x500")
Win.configure(bg='blue')
Win.title("PYTHON QUIZ")

homeScreen = Frame(bg = 'red')
homeScreen.grid(row = 2, column = 2, ipady = 100, pady = 50, padx = 5)
welcome = Label(homeScreen, width = 39, font=("Arial", 50), text="PYTHON QUIZ", bg = 'red', fg = 'white')
welcome.grid(row = 2, column = 2, ipady = 90, pady = 10)
playBtn = Button(homeScreen, width = 40, height = 2, font=("Arial", 20), text="Start Quiz", command=startQuiz, bg='light blue')
exitBtn = Button(homeScreen, width = 40, height = 2, font=("Arial", 20), text="Exit", command=Win.destroy, bg='light blue')
playBtn.grid(row = 3, column = 2, ipady = 10, pady = 10, padx = 5)
exitBtn.grid(row = 4, column = 2, ipady = 10, pady = 10, padx = 5)

root = Frame(Win, bg='red')
root.grid(row = 2, column = 2)
root.grid_forget()

question = Label(root, width = 67, font = ("Arial", 30), text = Questions[0], bg = 'blue', fg = 'white')
question.grid(row = 1, column = 1, ipady = 50, pady = 10)

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root, width = 30, font = ("Arial", 20), variable=val1, text=Options[0][0], command=lambda: check(1), bg='light blue')
option1.grid(row = 2, column = 1, ipadx = 500, ipady = 42, pady = 10)

option2 = Checkbutton(root, width = 30,  font = ("Arial",20), variable=val2, text=Options[0][1], command=lambda: check(2), bg='light blue')
option2.grid(row = 3, column = 1, ipadx = 500, ipady = 42, pady = 10)

option3 = Checkbutton(root, width = 30, font = ("Arial", 20), variable=val3, text=Options[0][2], command=lambda: check(3), bg='light blue')
option3.grid(row = 4, column = 1, ipadx = 500, ipady = 42, pady = 10)

nextBtn = Button(root, width = 20, font = ("Arial", 20), text="Next", command=next, bg='light blue')
nextBtn.grid(row = 5, column = 1, ipadx = 400, ipady = 30, padx = 10, pady = 35)

score = Label(Win)
exitBtn1 = Button(Win)
score.grid_forget()
exitBtn1.grid_forget()

Win.mainloop()