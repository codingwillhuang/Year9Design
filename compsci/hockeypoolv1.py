from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("635x482+0+900")
root.configure()
root.title("Hockey Pool")

#to get the player images working again make all the numbers disappear in this canvas so no "can2"
can = Canvas(root, width=630, height=475)
can.place(x=0, y=0)
image = Image.open("connor.jpg")
photo1 = ImageTk.PhotoImage(image)
can.create_image(0,0, anchor=NW, image=photo1)

site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')
if site.status_code is 200:
    content = BeautifulSoup(site.content, 'html.parser')

def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
        return
    if site.status_code is 200:
               
            totalpts = 0
            for myplayer in lst: # loop to check my players
               dTag = content.find(attrs={"csk": myplayer})
               parent = dTag.findParent('tr')
               playerpts = int(parent.contents[8].text) # 8th tag is total points
               print(myplayer + " " + str(playerpts))
               totalpts = totalpts + playerpts         
            mypts.configure(text=totalpts)
            
def switchPhoto():
    global photo
    global image1
    
    name = variable.get()
    name1, name2 = name.split(",")
    
    name = name1[0:5].lower() + name2[0:2].lower() + '01'
    path = "headshots/" + name + ".jpg"
    image1 = Image.open(path)
    photo = ImageTk.PhotoImage(image1)
    
    can.create_image(470, 40, anchor=NW, image=photo)
    
    
def makeoptions():
    if content != -99:
        names = content.findAll(attrs={"data-stat": "player"})
        playerOptions = []
        for player in names:
            if(player != "None"):
                playerOptions.append(player.get('csk'))
        return playerOptions
            
            
def updatelab():
   lstprint = ""
   for item in lst:
       lstprint = lstprint + item + "\n"
   mylab.configure(text=lstprint) 

def addItem():
   item = entry.get()
   if (lst.count != 0):
      lst.append(item)
      listbox.insert(END, item)
      entry.delete(0, END)     
            
def remItem():
        items = listbox.curselection()
        pos = 0
        for i in items :
            idx = int(i) - pos
            listbox.delete( idx,idx )
            lst.remove(idx)
            pos = pos + 1
      
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Players saved to disk")
    
def addPlayer(event):
    players = []
    name = variable.get()
    if players.count(name) > 0:
        return
        listbox.insert(END, name)
        for i in range(listbox.size()):
            players.append(listbox.get(i))
            
def helpItem():
    helpwindow = Tk()
    helpwindow.geometry("300x320+700+0")
    helpwindow.title("Help")
    
    titleLabel = Label(helpwindow, text = "Help/Instructions")
    titleLabel.place(x = 100, y = 5)
    messageLabel = Label(helpwindow, text = "On the left side of this hockeypool software \n there are various buttons which \n help edit your player list. To add a \n player, type in the player's name \n in the following format 'Last,First' \n and press add. To remove a player, click \n the selected player in the listbox \n and click the remove button. \n To save the player list and check points, \n click the save button or check points \n button near the bottom left. \n \n The pull down in the top right is \n a list of all players in the NHL.\n Select a player to show individual \n statistics of the selected player. \n :) ")
    messageLabel.place(x = 0, y = 30)
    helpwindow.mainloop()
    
def createlistbox(evt):  
    
    var = variable.get()
    print(variable)
    if var != None:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        points=int(parent.contents[8].text)
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        games=int(parent.contents[5].text)
        minutes=int(parent.contents[21].text)
        team=parent.contents[3].text
        position=parent.contents[4].text
        age=int(parent.contents[2].text)
        average=float(parent.contents[20].text)
        plusminus=int(parent.contents[9].text)
    listbox2=Listbox(root)
    listbox2.place(x=440, y=255)
    listbox2.insert(END, "Age: "+ str(age))
    listbox2.insert(END,"Position: "+str(position))
    listbox2.insert(END,"Team: "+str(team))
    listbox2.insert(END,"Points: " + str(points))
    listbox2.insert(END,"Goals: " + str(goals))
    listbox2.insert(END,"Assists: "+str(assists))
    listbox2.insert(END,"+/-: "+str(plusminus))
    listbox2.insert(END,"Shooting %: "+str(average))
    listbox2.insert(END,"Games Played: "+str(games))
    listbox2.insert(END,"Minutes Played: "+str(minutes))
    
    
lst = []
lstprint = ""
totalpts = 0
print("Downloading hockey data")




button = Button(root, text= "Change photo", command=switchPhoto)
button.place(x = 480, y = 225)

OPTIONS = makeoptions()
variable = StringVar(root)
pulldown = OptionMenu(root, variable, *OPTIONS, command=createlistbox)
pulldown.place(x=470, y=5)

listbox= Listbox(root)
listbox.place(x=5,y=180)


instlab = Label(root,text="Input (e.g., McDavid,Connor): ")
instlab.place(x=5, y=5) 

entry = Entry(root)     
entry.place(x=5, y=35)

helpbutton = Button(root, text = "Help", command= helpItem)
helpbutton.place(x = 300, y = 5)

addbutton = Button(root, text="Add", command=addItem)
addbutton.place(x=5, y=80)

rembutton = Button(root, text="Remove", command=remItem)
rembutton.place(x=5, y=110)

savebutton = Button(root, text="Save", command=saveList)
savebutton.place(x=5, y=140)

#mylab = Label(root,text=lstprint,anchor=W,justify=LEFT)
#mylab.place(x=5, y=150)

ptsbutton = Button(root,text="Check Points", command=scrape)
ptsbutton.place(x=5, y=380)

mypts = Label(root,text=totalpts)
mypts.place(x=5, y=410)

mainloop()