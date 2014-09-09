import Tkinter as tk
from Tkinter import *
from Tkinter import StringVar
import tkMessageBox
import sys


root = tk.Tk()
root.geometry('240x500+0+0')
root.title("Fuck")

display = StringVar()
speed = StringVar()

def hello():
	tkMessageBox.askquestion("Fuck","Fuck \n Yooooooooooooooooo",icon = "warning")
	print display.get()

def Get_scale_variable():
	print speed.get()

def get_food():
	print food.get()

tk.Label(fg = 'red',text = "Hello World").pack()
tk.Button(fg = 'red',text = "Exit",command = sys.exit).pack(side = "left")
tk.Button(text = "Hello",command = hello).pack()
tk.Button(text = "Scale",command = Get_scale_variable).pack()

scale = Scale(root, from_=1, to=20,resolution = 0.1,variable = speed)
scale.pack(side = "left")

tk.Entry(relief = "sunken",textvariable = display).pack()

food = IntVar()
namelist = ["Salad","Hambuger","Fish","Toast","Bacon","Egg","Chili"]
for i,j in enumerate(namelist):
	Radiobutton(root,text = j,value = i,variable = food).pack()
tk.Button(fg = "red",text = "I wanna this",command = get_food).pack()


	

tk.mainloop
