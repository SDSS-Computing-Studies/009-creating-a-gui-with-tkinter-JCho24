import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("Example")



dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
label1 = tk.Label(window, text = " Pochacco!")

label2 = tk.Label(window, text = "  A cuddly little puppy! This is from the same    ", bg = "#87CEEB")
label3 = tk.Label(window, text = "creators who brought you Keropi and Kero Kero", bg = "#87CEEB")

label.grid(row = 1, column = 3, rowspan = 5)
label1.grid(row = 3, column = 4)
label2.grid(row = 6, column = 1, columnspan = 7)
label3.grid(row = 7, column = 1, columnspan = 7)

window.mainloop()

