import tkinter

window = tkinter.Tk()
window.geometry('50x50')
window.configure(bg='white')
window.title("My first window")

def color6():
    window.geometry('100x100')
    window.configure(bg='red')
    print("6")
window.after(1000,color6)

def color5():
    window.geometry('150x150')
    window.configure(bg='orange')
    print("5")
window.after(2000,color5)

def color4():
    window.geometry('200x200')
    window.configure(bg='yellow')
    print("4")
window.after(3000,color4)

def color3():
    window.geometry('250x250')
    window.configure(bg='green')
    print("3")
window.after(4000,color3)

def color2():
    window.geometry('300x300')
    window.configure(bg='blue')
    print("2")
window.after(5000,color2)

def color1():
    window.geometry('350x350')
    window.configure(bg='purple')
    print("1")
window.after(6000,color1)






window.after(7000,lambda: [window.destroy(),print("BOOM")])

window.mainloop()