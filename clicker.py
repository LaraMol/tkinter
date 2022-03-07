import tkinter

root = tkinter.Tk()
root.title("Hello")
root.geometry("200x300")
root["background"] = 'pink'
Numbers = 0 

def UP():
    global Numbers
    Numbers += 1
    counter['text'] = Numbers
    if Numbers > 0:
        root["background"] = 'green'
    elif Numbers < 0:
        root["background"] = 'red'
    else:
        root["background"] = 'pink'

def DOWN():
    global Numbers
    Numbers -= 1
    counter['text'] = Numbers
    if Numbers >0:
        root["background"] = 'green'
    elif Numbers <0:
        root["background"] = 'red'
    else:
        root["background"] = 'pink'

button = tkinter.Button(root)
button.configure(text="UP",command=UP)
button.pack(padx=80, pady=20, expand=True)

button = tkinter.Button(root)
button.configure(text="DOWN",command=DOWN)
button.pack(padx=80, pady=20, expand=True)



counter= tkinter.Label(
    root,
    text= Numbers,
    bg="white",
    fg="black"
)

counter.pack(
    ipadx=100,
    ipady=10,
    expand=True,
)

root.mainloop()