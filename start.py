import sys
import os
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.font as tkFont
    
app = tk.Tk()
app.geometry("1000x600")

#Symptoms Predictor
def symptoms():
    os.system('python symptoms.py')

#Heart Predictor
def heart():
    os.system('python heart.py')

#Covid Predictor
def covid():
    os.system('python covid.py')

filename = PhotoImage(file = "mbg.png")
background_label = Label(app, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
buttonExample1 = tk.Button(app,
                           text="Simple-Symptom Disease Predictor",
                           width=30,
                           height=2,
                           font=('Helvetika',20,'bold'),
                           command=symptoms
                           )

buttonExample2 = tk.Button(app,
                           text="Heart Disease Predictor",
                           width=30,
                           height=2,
                           font=('Helvetika',20,'bold'),
                           command=heart
                           )

buttonExample3 = tk.Button(app,
                           text="Covid 19 Predictor",
                           width=30,
                           height=2,
                           font=('Helvetika',20,'bold'),
                           command=covid
                           )

buttonExample4 = tk.Button(app,
                           text="EXIT !",
                           width=30,
                           height=2,
                           font=('Helvetika',20,'bold'),
                           fg='Red',
                           command=app.destroy
                           )

buttonExample1.place(x=250, y=100)
buttonExample2.place(x=250, y=200)
buttonExample3.place(x=250, y=300)
buttonExample4.place(x=250, y=450)



app.mainloop()