# importing tkinter module into python so we can use
from tkinter import*
# Tk() makes a window
master = Tk()

def return_entry(en):
    """Gets and prints the content of the entry"""
    content = int(entry.get())
    print(content) 
    print(content **2)

Label(master, text = "Input: ").grid(row=0, sticky=W)

entry = Entry(master) 
entry.grid(row=1, column=1)

# Connect the rentry with the return button
entry.bind('<Return>', return_entry)

# mainloop is a function that allows the window to stay open. It REPEATS the code.
mainloop()
