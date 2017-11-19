import random
import sys
import getopt
from twisted.protocols import basic
import random

def getword():#TODO make this pull randomish words.
    return "owo"

def arraygen():
    table = []
    temp = -1
    for x in range (0,5): #creates our game table, with each element containing 3 things
        table.append([[getword(),-1, 0] for y in range(0,5)]) #the word, the color int, and the pressed bool/int
    return table

def arraycolors(table):
    if(random.randint(0,1) == 0):
        counts = [9, 8, 7, 1] #red is 0, blue is 1, 2 is neuts, 3 is dead
    else:
        counts = [8, 9, 7, 1] #Flop so teams go in different order
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
    port = input()
    if(port == ""):
        port = 9876
    plain_table = arraygen()
    secret_table = arraycolors(plain_table)
        

main()
