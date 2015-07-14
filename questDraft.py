import random

#Quest drafting by color v 0.1


#Insert the name/ID of drafters
playerList = ["emil", "bob", "henry", "honke", "robin", "micke", "jonas", "andrea"]
#Shuffle the players as well to prevent knowledge of 5 first not sharing color etc.
random.shuffle(playerList)
colorsList = ["white", "blue", "black", "red", "green"]
assignedList = []

amountOfPlayers = len(playerList)
loopAmount = int(amountOfPlayers/5) + 1
#old
#loopAmount = int((amountOfPlayers - amountOfPlayers % 5)/5) + 1

for i in range(loopAmount):

    #Change the order of color asigning each itteration
    random.shuffle(colorsList)
    #Determine how many players still needs asigning at begining of each itteration
    playersLeft = len(playerList)
    
    if playersLeft >= 5:

        for j in range(5):
            name = playerList.pop()
            color = colorsList[j]

            assignedList.append(name + " - " + color)

    else:
        for j in range(len(playerList)):
            name = playerList.pop()
            color = colorsList[j]

            assignedList.append(name + " - " + color)

#Print the assigned color of each player
for i in range(len(assignedList)):
    print(assignedList[i])
