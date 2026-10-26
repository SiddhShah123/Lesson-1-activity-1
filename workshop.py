from tkinter import *
from datetime import date
window = Tk()
window.title('getting started with widgets')
window.geometry('750x750')
lbl = Label(text = " hey there!",fg = "white",bg = "#072F5F",height = 3,width = 300)
name_lbl = Label(text = "Full Name ",bg = "#3895D3")
name_entry = Entry()
def display():
    name = name_entry.get()
    global message 
    message = "welcome to the !!WORKSHOP!! \n today's date is :"
    greet = " hello "+ name + "\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box = Text(height=7)
btn = Button(text="Begin", command=display, height=2, bg="#1261A0", fg='white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()