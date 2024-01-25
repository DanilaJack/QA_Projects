from tkinter import messagebox
from turtle import *
from random import *
import turtle
import time
import tkinter as tk


def click(num):
    # SetUp
    setup(800, 500)
    title("Turtle Race")
    bgcolor("forestgreen")
    speed(0)

    # TitleOnPage
    penup()
    goto(-100, 205)
    color("white")
    write("TURTLE RACE", font=("Arial", 20, "bold"))

    # Racing area
    goto(-350, 200)
    pendown()
    color("chocolate")
    begin_fill()
    for i in range(2):
        forward(700)
        right(90)
        forward(400)
        right(90)
    end_fill()

    # Finish - white squares
    gap_size = 20
    shape("square")
    penup()
    color("white")

    for i in range(10):
        goto(250, (180 - (i * gap_size * 2)))
        stamp()

    turtles = []
    for i in range(int(num)):
        new_turtle = Turtle()
        turtles.append(new_turtle)

    yaxis = 150
    turtle_gap = 300/int(num)
    for i in range(int(num)):
        turtles[i].color("cyan")
        turtles[i].shape("turtle")
        turtles[i].shapesize(1.5)
        turtles[i].penup()
        turtles[i].goto(-300, yaxis)
        yaxis -= turtle_gap
        turtles[i].pendown()


    # Pause before start
    time.sleep(1)

    stop = False
    for j in range(300):
        for i in range(int(num)):
            turtles[i].forward(randint(1,10))
            if turtles[i].xcor() >= 250:
                max_i = i
                stop = True
        if stop == True:
            messagebox.showinfo(title="Winner", message=f"Player {max_i+1} Won")
            break


window = tk.Tk()
window.geometry("600x100")
window.title("Desicion Pop-Up")
window.configure(bg="pink")

label1 = tk.Label(window, text="Enter number of participants (from 2 to 10):", font=("Arial", 12))
label1.place(x=20, y=20)
entry1 = tk.Entry(window, width=5)
entry1.place(x=330, y=20)
btn1 = tk.Button(window, text="Start", bg="lime", command=lambda: click(entry1.get()))
btn1.place(x=370, y=20)
window.mainloop()
time.sleep(2)
