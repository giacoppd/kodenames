import random
import sys
import getopt
import random
import kdnetworking.py
from time import sleep
def getword():#TODO make this pull randomish words.
    return "owo"

def arraygen():
    table = []
    temp = -1
    for x in range (0,5): #creates our game table, with each element containing 3 things
        table.append([[getword(),-1, 0] for y in range(0,5)]) #the word, the color int, and the pressed bool/int
    return table

def arraycolors(table, heavy):
    if(heavy == 0):
        counts = [9, 8, 1, 7] #red is 0, blue is 1, 2 is neuts, 3 is dead
    else:
        counts = [8, 9, 1, 7] #Flop so teams go in different order
    for x in table:
        for ele in x:
            while(ele[1] == -1):
                temp = random.randint(0,3) 
                if(counts[temp] > 0): #if we have enough of that kind of number left
                    counts[temp] -= 1 #get rid of 1 from the count 
                    ele[1] = temp #and assign it to the space
    print(table[4][4])
    return table 

def main():
    print("What seed?")
    random.seed(input())
    print("Port #, or just enter for the default of 9876")
    port = int(input())
    if(port == ""):
        port = 9876
    print("How many players?")
    playerc = int(input())
    heavy = random.randint(0,1) #which side goes first, 0 for red, 1 for blue
    alivegame = True
    winner
    plain_table = arraygen()
    secret_table = arraycolors(plain_table)
    factory = bighandler(secret_table)
    reactor.listenTCP(port, factory)
    reactor.run()
    while(len(factory.users) != playerc):
        sleep(5) #wait for all players to join and give names
    factory.setusers()
    factory.sendroles()
    factory.sendtables()
    sleep(5) #make sure everyone gets it, the easy way
    while(alivegame): 
        for x in range (0, len(factory.order)): #start taking turns here
            factory.users[factor.order[x]].state = "TURN"
            while(factory.users[factor.order[x]].state != "OVER"):
                sleep(2)
            for y in range (0,2):
                if(handler.gamestate[y] == 0):
                    alivegame = false 
    #game is over at end of loop
    reactor.stop()
     
            
main()
