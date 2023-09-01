from tkinter import *
from tkinter import messagebox
import random


def no() :
    messagebox.showinfo('', 'Sounds Good!')
    quit()

def motionMouse(event):
    btnYes.place(x = random.randint(0, 400), y = random.randint(0, 400))

root = Tk()
root.geometry('500x500')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, text= "Do you like CS?", font= 'roboto 20 bold', bg = 'white').pack()
btnYes = Button(root, text= "No", font= 'roboto 20 bold', )
btnYes.place(x = 160, y = 100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text = 'Yes', font= 'roboto 20 bold', command= no)
btnNo.place(x=260, y=100)

root.mainloop()
