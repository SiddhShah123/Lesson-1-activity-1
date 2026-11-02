from tkinter import *

root = Tk()
root.geometry("100x100")
root.title('Event Handler')

def handle_keypress(event):
    print(event.char)

root.bind("<Key>",handle_keypress)

def handle_click(event):
    print("\n the button was clicked")

button = Button(text="Click Me")
button.pack()
button.bind("<Button-1>",handle_click)
root.mainloop()