import tkinter as tk
#import twisted
import random
from functools import partial #for a hack in buttons because late binding REEEE

def testgen():
    table = []
    temp = -1
    for x in range (0,5):
        table.append([["owo",-1, 0] for y in range(0,5)]) #makes the 2d array with 3 element list for each element
    counts = [9, 8, 7, 1] #red or blue is 0 and 1, 2 is neuts, 3 is dead
    for x in table:
        for ele in x:
            while(ele[1] == -1):
                temp = random.randint(0,3) 
                if(counts[temp] > 0): #if we have enough of that kind of number left
                    counts[temp] -= 1 #get rid of 1 from the count 
                    ele[1] = temp #and assign it to the space
    return table
def updateServer(x, y, frame):
    print(x,y) #TODO make this do network shit
def fool():
    print("baka") #TODO make the button disable itself when pressed once instead of just this

def drawtable(table, spy, seed):
    root = tk.Tk()
    root.geometry("800x560") #maybe change later, but window size
    root.title("Kodenames")
    tk.Label(text="Kodenames! Seed = " + str(seed)).grid(row=0, column=2)
    tk.Label(text="hi", width=20).grid(row=1,column=0)
    tk.Label(text="turn", width=20).grid(row=1,column=2)
    tk.Label(text="bye", width=20).grid(row=1,column=4)
    for x in range(0,5):
        for y in range(0,5):
            cmd=partial(updateServer, x, y, root)
            if(table[x][y][1] == -1):
                bgc = "green"
                cmd=fool
            if(table[x][y][1] == 0):
                bgc = "red"
            if(table[x][y][1] == 1):
                bgc = "blue"
            if(table[x][y][1] == 2):
                bgc = "yellow"
            if(table[x][y][1] == 3):
                bgc = "black"
            b = tk.Button(root, text=table[x][y][0], bg=bgc, width=15,
                    height=6,command=cmd) #so long I split the line
            b.grid(row=x+2,column=y)
            
    root.mainloop()


table = testgen()
drawtable(table, 1, 10)
