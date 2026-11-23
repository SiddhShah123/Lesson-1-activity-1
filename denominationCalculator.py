from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x350")
root.title("denomination Calculator")
root.config(bg = "lightblue")

Label(root,text = "Denomination Calculator").pack(pady=10)

def calculator():
    top = Toplevel(root)
    top.title("Calculator")
    Label(root,text="enter amount").pack()
    e = Entry(top)
    e.pack()

    entries = []
    for n in [2000,500,100]:
        Label(top,text = n).pack()
        x = Entry(top)
        x.pack()
        entries.append(x)

    def calculate():
        try :
            amount = int(e.get())
            for i , n in enumerate([2000,500,100]):
                count = amount//n
                amount%= n
                entries[i].delete(0,END)
                entries[i].insert(0,count)
        except ValueError:
            messagebox.showerror("error","enter valid number")

    Button(top,text="calulate",command=calculate).pack()        
Button(root,text="start",command=calculator).pack()  
root.mainloop()