from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("250x250")
root.title("Routine Checker")

def handle_keypress(event):
    print("Key pressed:", event.char)

root.bind("<Key>", handle_keypress)

def show_warning():
    if not entry.get():
        messagebox.showwarning("Alert!!", "Stop! No task found")
    else:
        messagebox.showinfo("Success", f"Routine saved: {entry.get()}")

def handle_click(event):
    print("The button was clicked")

entry = Entry(root)
entry.pack(pady=15)

button = Button(root, text="Check Routine", command=show_warning)
button.pack(pady=10)
button.bind("<Button-1>", handle_click)

root.mainloop()