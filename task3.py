import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")



dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
label1 = tk.Label(window, text = " Pochacco!")

label2 = tk.Label(window, text = "  A cuddly little puppy! This is from the same    ", bg = "#87CEEB")
label3 = tk.Label(window, text = "creators who brought you Keropi and Kero Kero", bg = "#87CEEB")
