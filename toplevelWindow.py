from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Main")

def topWin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top level window")
    l2 = Label(top,text="This is a Top Level window")
    l2.pack()
    top.mainloop()

l3 = Label(root,text="This is the Main window")
btn = Button(root,text="Click me! to go to the top level window",command=topWin)
btn.pack()
l3.pack()
root.mainloop()