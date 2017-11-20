from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from time import sleep
from random import randint

class handler(LineReceiver):
users
table
gamestate

    @classmethod
    def setusers(_users, _table, _gamestate):
        handler.users = _users
        handler.table = _table
        handler.gamestate = _gamestate

    def __init__(self, _number, _role):
        self.name = None
        self.state = "INIT"
        self.number = _number #user number, AKA which list element they are
        self.role = _role #role token

    def sendtable():
        #sends the table over, word by word, to the client
        #no other information about the table is sent so it's just a list
        for x in handler.table:
            for y in x:
                self.sendLine(y[0])
    
    def sendfulltable():
        for x in handler.table:
            for y in x:
                self.sendLine(y[0]) #spymasters need both the word and the color
                self.sendLine(y[1])
    
    def sendrole(): #send each player their role #
        self.sendLine(self.role)

    def lineReceived(self, data):
        if(self.state == "NAME"):
            self.name = data
            self.sendrole()
            self.state = "WAIT"
        elif(self.state == "WAIT"):
            continue
        elif(self.state == "TURN"):
            handler.gamestate[handler.table[data[0]][data[2]][1]] -= 1 #updates the game state. Its awful.
            for x in handler.users:
                x.sendLine(handler.table[data[0]][data[2]][1]) #send all players the update
            self.state == "OVER"

    def connectionMade(self):
        self.sendLine("Connection Made! Enter your name")
        self.state = "NAME"         

class bighandler(Factory):
    
    def sendtables():
        for x in range (0,len(self.users)):
            if(self.roles[x] == 2 or self.roles[x] == 3):
                self.users[x].sendfulltable()
            else:
                self.users[x].sendtable()
    
    def sendroles():
        for x in self.users:
            x.sendrole()

    def setusers(): #hacky way to set the user list as a static variable
        handler.setusers(self.users, self.table)
    
    def __init__(self, table, mx, heavy): #TODO make less huge
        self.table = table
        self.users = []
        self.count = 0 #current number of players, used later
        self.roles = [0 for x in range (0, mx)] #list of roles for all players
        self.roles[randint(0, mx)] = 2 #mark red spy
        self.order = [0 for x in range(0,mx-2)] #turn order later on
        n = (mx - 2)/2 #the number of players on the red or blue teams that aren't spys
        counts [n,n] # for assigning blue and red plens
        while(True):
            k = randint(0,mx)
            if (self.roles[k] != 2): #make sure the spys are different
                self.roles[k] = 3 #assign blue spy
                break
        for x in self.roles:
            if(x == 2 or x == 3):
                continue
            else:
                i = randint(0,1)
                if(counts[i] > 0):
                    x = i
                    counts[i] -= 1
                else:
                    x = (i ^ 1) #hacky way to get the other one
                    counts[i^1] -= 1
        for x in range(0,mx): #getting order lists for later
            if(roles[x] == 0):
                rorder.append(x)
            elif(roles[x] == 1):
                border.append(x)
        if(heavy == 0): #which team goes first
            for(x in range(0,n)):
                self.order.append(rorder[x])
                self.order.append(border[x])
        else:
            for(x in range(0,n)):
                self.order.append(border[x])
                self.order.append(rorder[x])
        if(heavy == 0):
            self.gamestate = [9,8,1,7]
        else:
            self.gamestate = [8.9.1,7]

    def buildProtocol(self, addr):
        p = handler(self.count, self.roles[self.count], self.gamestate)
        self.count += 1
        self.users.append(p)
        return p
