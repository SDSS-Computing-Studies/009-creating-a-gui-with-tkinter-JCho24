import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")



dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
searchbyname = tk.Button(window,text = "Seach By Name")
entry = tk.Entry(window)
clientdatabase = tk.Label(window,text = "Client Database")


name = Label(window, text = "Name")
typee = Label(window, text = "Type")
breed = Label(window, text = "Breed")
owner = Label(window, text = "Owner")
birthdate = Label(window, text = "Birthdate")


entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)
entry5 = tk.Entry(window)


previous = tk.Button(window,text = "< Previous")
saveentry = tk.Button(window,text = " Save Entry ", bg = "#808080")
nextt = tk.Button(window,text = "Next >")


label.grid(row = 1, column = 1, rowspan = 3)
searchbyname.grid(row = 1, column = 4)
entry.grid(row = 1, column = 5)
clientdatabase.grid(row = 2, column = 3)
name.grid(row = 4, column = 1)
typee.grid(row = 4, column = 2)
breed.grid(row = 4, column = 3)
owner.grid(row = 4, column = 4)
birthdate.grid(row = 4, column = 5)
entry1.grid(row = 5, column = 1)
entry2.grid(row = 5, column = 2)
entry3.grid(row = 5, column = 3)
entry4.grid(row = 5, column = 4)
entry5.grid(row = 5, column = 5)
previous.grid(row = 6, column = 1, sticky = W)
saveentry.grid(row = 6, column = 3)
nextt.grid(row = 6, column = 5, sticky = E)


window.mainloop()