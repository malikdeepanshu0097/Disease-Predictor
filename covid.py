import tkinter
import webbrowser


def open():
    webbrowser.open('https://www.covid19india.org/')

root = tkinter.Tk()
root.geometry("400x700")
root.title("Covid Predictor")

lab0 = tkinter.Label(root, text="COVID-19 Predictor ",font=('Helvetica',20,'bold'), anchor='w')
lab0.pack()

lab10 = tkinter.Label(root, text="Please Maintain Social Distancing and Always Wear a Mask ",font=('Helvetica',10),fg='white',bg='red', anchor='w')
lab10.pack()
lab1 = tkinter.Label(root, text="Symptom 1",font=('Helvetica',12,'bold'), anchor='w')
lab1.pack()

variable1 = tkinter.StringVar(root)
variable1.set("                           None                                ") # default value

w = tkinter.OptionMenu(root, variable1, 'cough','loss of smell','fever','loss of taste','headache','sore throat','body pain','tiredness')
w.pack()

lab = tkinter.Label(root, text="", anchor='w')
lab.pack(pady=10)

lab2 = tkinter.Label(root, text="Symptom 2",font=('Helvetica',12,'bold'), anchor='w')
lab2.pack()

variable2 = tkinter.StringVar(root)
variable2.set("                           None                                ") # default value

w = tkinter.OptionMenu(root, variable2, 'cough','loss of smell','fever','loss of taste','headache','sore throat','body pain','tiredness')
w.pack()

lab = tkinter.Label(root, text="", anchor='w')
lab.pack(pady=10)

lab3 = tkinter.Label(root, text="Symptom 3",font=('Helvetica',12,'bold'), anchor='w')
lab3.pack()

variable3 = tkinter.StringVar(root)
variable3.set("                           None                                ") # default value

w = tkinter.OptionMenu(root, variable3, 'cough','loss of smell','fever','loss of taste','headache','sore throat','body pain','tiredness')
w.pack()

lab = tkinter.Label(root, text="", anchor='w')
lab.pack(pady=10)



lab4 = tkinter.Label(root, text="Have you travel outside your city recently?",font=('Helvetica',12,'bold'), anchor='w')
lab4.pack()

variable4 = tkinter.StringVar(root)
variable4.set("                           None                                ") # default value

w = tkinter.OptionMenu(root, variable4, 'yes', 'no')
w.pack()

lab = tkinter.Label(root, text="", anchor='w')
lab.pack(pady=10)


lab5 = tkinter.Label(root, text="Are you feeling any difficulty in breathing?",font=('Helvetica',12,'bold'), anchor='w')
lab5.pack()

variable5 = tkinter.StringVar(root)
variable5.set("                           None                                ") # default value

w = tkinter.OptionMenu(root, variable5, 'yes', 'no')
w.pack()

lab = tkinter.Label(root, text="", anchor='w')
lab.pack(pady=10)



'''entry1 = tkinter.Entry(root)
entry1.pack()

entry2 = tkinter.Entry(root)
entry2.pack()

entry3 = tkinter.Entry(root)
entry3.pack()

entry4 = tkinter.Entry(root)
entry4.pack()
'''
def on_button():
    li=['cough','loss of smell','fever','loss of taste','headache','sore throat','body pain','tiredness', 'yes']
    
    #if ((entry1.get().strip().lower() in li)&(entry2.get().strip().lower() in li)&(entry3.get().strip().lower() in li)&(entry4.get().strip().lower() in li)):
     #   slabel = tkinter.Label(root, text="covid positive")
      #  slabel.pack()
    if ((variable1.get() in li)&(variable2.get() in li)&(variable3.get() in li)&(variable4.get() in li)|(variable5.get() in li)):
        slabel = tkinter.Label(root, text="covid positive",fg="white", bg="red")
        slabel2 = tkinter.Label(root, text="This is just Preliminary. Get Covid Tested for 100% Confirmation",fg="white", bg="red")

        slabel.pack()
        slabel2.pack()
   
    else:
        tlabel = tkinter.Label(root, text="covid negative")
        tlabel.pack()

button = tkinter.Button(root, text="Enter", command=on_button)
button.pack()

button2 = tkinter.Button(root, text="For Latest Covid 19 Info Click Here", command=open)
button2.pack()

root.mainloop()