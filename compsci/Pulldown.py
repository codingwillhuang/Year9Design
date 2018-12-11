OPTIONS = makeList()
variable = StringVar(root)
variable.set(OPTIONS[0])
w = OptionMenu(root,var,*OPTIONS,command=addplayers)

def makeList():
    if content != -99:
        names = content.findAll(attrs=("data-stat" : "player"})
        playerlist =[]
        for player in names:
            if(player != "None"):
                playerlist.append(player.get('csk'))
        return playerlist
        
def makeList():
    if content !=-99:
        names=content.findAll(attrs={"data-stat":"player"})
        for player in names:
            if (player.get("csk")!="None" or player.get("csk")!=""):
                        playerlist.append(player.get('csk'))
                return playerlist
        