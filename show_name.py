from tkinter import *

from datetime import date

window = Tk()
window.title('getting started with widgets')
window.geometry('400x500')

lbl = Label(text = " hey there!",fg = "white",bg = "#072F5F",height = 1,width = 300)

name_lbl = Label(text = "Full Name ",bg = "#3895D3")

name_entry = Entry()
def display():
    name = name_entry.get()
    global message 
    message = "welcome to the app \n today's date is :"
    greet = " hello "+ name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

text_box = Text(height=3)

# Add button and give value of command as name of the function

# Press button, display function will be called automatically

btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

# Organize all the widgets in the window

lbl.pack()

name_lbl.pack()

name_entry.pack()

btn.pack()

text_box.pack()

# Start the GUI event loop

window.mainloop()