import tkinter as tk 
from tkinter import *

window = tk.Tk()

nF = Frame()

num1 = tk.Entry(nF,text = " ", width = 20)
multiply = Label(nF, text = "x")
num2 = tk.Entry(nF,text = " ", width = 20)
equals = tk.Button(nF,text="=")
num3 = tk.Entry(nF,text = " ", width = 20)


nF.pack()
num1.pack(side = LEFT)
multiply.pack(side = LEFT)
num2.pack(side = LEFT)
equals.pack(side = LEFT)
num3.pack(side = LEFT)


window.mainloop()