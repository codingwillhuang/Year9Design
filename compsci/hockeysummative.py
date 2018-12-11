from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x800+0+900")
root.configure(background="skyblue")
root.title("Hockey Pool")

can = Canvas(root, width=1000, height=475)
can.grid(row=0,column=0,padx=5, pady=5)
image1 = Image.open("connor.jpg")
photo = ImageTk.PhotoImage(image1)
can.create_image(0,0, anchor=NW, image=photo)

savebutton = Button(root, text="Check Pts",)
savebutton.grid(row=2, column=0, sticky=NW, padx=10)

rembutton = Button(root, text="Remove",)
rembutton.grid(row=1, column=0, sticky=NW, padx=10, pady=10)

ptsbutton = Button(root,text="Check pts")
ptsbutton.grid(row=0, column=0, sticky=NW, padx=10)

listbox = Listbox(root,height=7, width=16)
listbox.grid(row=2, column=0, sticky=NW, padx=10)
listbox.insert(END, "Position: Center")
listbox.insert(END, "Team: Pittsburgh")
listbox.insert(END, "Games Played: 19")
listbox.insert(END, "Goals: 9")
listbox.insert(END, "Assists: 15")
listbox.insert(END, "Points: 24")
listbox.insert(END, "+/-: 11")

OPTIONS = ["Crosby, Sidney", "McDavid, Connor", "Matthews, Auston", "Marner, Mitch"]
variable = StringVar(root)
variable.set(OPTIONS[0])
w = OptionMenu(root, variable, *OPTIONS)
w.grid(row=0, column=0, sticky=NW, padx=10)
mainloop()