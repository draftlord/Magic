import random

#Quest drafting by color v 0.1

#Insert the name/ID of drafters
playerList = ["emil", "bob", "henry", "honke", "robin", "micke", "jonas", "andrea"]
colorList = ["white", "blue", "black", "red", "green"]
assignedList = []

#Shuffle the players as well to prevent knowledge of 5 first not sharing color etc.
random.shuffle(playerList)
amountOfPlayers = len(playerList)

for i in range(amountOfPlayers):
    #Change the order of color assignments every 5th iteration
    if i%5 == 0:
        random.shuffle(colorList)

    name = playerList.pop()
    color = colorList[i%5]
    assignedList.append(name + " - " + color)

#Print the assigned color of each player
for i in range(len(assignedList)):
    print(assignedList[i])
