import tkinter
import random

root = tkinter.Tk()
root.configure(bg="white")
valorantAgents=['skye','sage','omen','chamber','sova','astra','breach','brimstone','viper','raze']

def grabbel():
    if len(valorantAgents) <= 0:
        root.destroy()
        return
    GrabbelItem = random.choice(valorantAgents)
    valorantAgents.remove(GrabbelItem)
    print(f"Gefeliciteerd, je hebt een {GrabbelItem} gegrabbeld!")

button = tkinter.Button(root)
button.configure(text="Click me",command= grabbel)
button.pack(padx=20, pady=20, expand=True)


root.mainloop()