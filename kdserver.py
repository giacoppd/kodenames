import random
import sys
import getopt
from twisted.protocols import basic
from twisted.internet import reactor, protocol, endpoints

def setseed(strong):
    random.seed(strong)

def getword():#TODO make this pull randomish words.
    return "owo"

def arraygen():
    table = []
    temp = -1
    for x in range (0,5):
        table.append([[getword(),-1, 0] for y in range(0,5)]) #makes the 2d array with 3 element list for each element
    return table
def arraycolors():
    counts = [9, 8, 7, 1] #red or blue is 0 and 1, 2 is neuts, 3 is dead
    for x in table:
        for ele in x:
            while(ele[1] == -1):
                temp = random.randint(0,3) 
                if(counts[temp] > 0): #if we have enough of that kind of number left
                    counts[temp] -= 1 #get rid of 1 from the count 
                    ele[1] = temp #and assign it to the space
    print(table[4][4])


print("What seed?")
setseed(input())
print("Port #, or just enter for the default of 9876")
port = input()
if(port == ""):
    port = 9876
arraygen()
