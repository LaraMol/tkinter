import tkinter as tk

root = tk.Tk()
root.title("Hello")
root.geometry("200x300")
root["background"] = 'pink'

box1 = tk.Label(
    root,
    text="Hello tkinter",
    bg="green",
    fg="purple"
)

box1.pack(
    ipadx=50,
    ipady=100,
    expand=True,
)


root.mainloop()