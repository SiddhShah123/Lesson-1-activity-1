from tkinter import *

root = Tk()
root.title('ATM pin')
root.geometry('500x500')
frame= Frame(master=root,height = 200,width = 360,bg= '#d0efff' )
lbl1= Label(frame,text = "Full name ",bg = "#3895d3",fg = 'white',width = 12)
lbl2= Label(frame,text = "Enter Password ",bg = "#3895d3",fg = 'white',width = 12)
name_entry = Entry(frame)
pass_entry = Entry(frame,show = '*')

def display():
    name = name_entry.get()
    greet = "Hey " + name 
    Message = "\n You have entered the ATM"
    textbox.insert(END,greet)
    textbox.insert(END,Message)

textbox = Text(bg= "#bebebe",fg = 'black')
bnt = Button(text= "create account",command=display,bg = 'red')
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lbl2.place(x=20,y=80)
pass_entry.place(x=150,y=80)
bnt.place(x=130,y=210)
textbox.place(y=250)
root.mainloop()