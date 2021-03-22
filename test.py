import sys
import os
from tkinter import *
from tkinter.ttk import *

#Symptoms Predictor
def symptoms():
    os.system('python clean_code.py')

# Set the canvas
canv = Tk()
canv.geometry('1000x550')

filename = PhotoImage(file = "mbg.png")
background_label = Label(canv, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Create style object
sto = Style()

#configure style
sto.configure('W.TButton', font= ('Arial', 10, 'underline'),
foreground='Red')

w2 = Label(canv, justify=LEFT, text="Disease Predictor using Machine Learning", foreground="black")
w2.config(font=("Elephant",30,"bold"))
w2.grid(row=1, column=1, columnspan=2, padx=100)


#Button with style
btns = Button(canv, text='EXIT !',
      style='W.TButton',
      command=canv.destroy)
btns.grid(row=3, column=2, padx=100)

#Button without style
btnns = Button(canv, text='Click to Start !', command=symptoms)
btnns.grid(row = 2, column = 2, pady = 10, padx = 100)

btnns2=Button(canv,text="Button 2",width=10,height=10)






canv.mainloop()