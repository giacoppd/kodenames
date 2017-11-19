from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from time import sleep
from random import randint
#I need a statemachine so I know where I am in the game
#One to load users, one to play the game

class handler(LineReceiver):
table = [] #static var for the table
users = [] #list of all users
mx   #max number of players
rspy #number holders for the red and blue spy
bspy  
    
    @classmethod
    def statinit(_table, _mx, _rspy, _bspy):
        handler.table = _table
        handler.mx = _mx
        handler.rspy = _rspy
        handler.bspy = _bspy

    def __init__(self, _number):
        handler.table = _table
        self.name = None
        self.state = "NAME"
        self.number = _number #user number, AKA which list element they are
        handler.users.append(self)
        handler.mx = _mx
        handler.rspy = _rspy
        handler.bspy = _bspy
    
    def sendtable():
        #sends the table over, word by word, to the client
        #no other information about the table is sent so it's just a list
        for x in handler.table:
            for y in x:
                self.sendLine(y[0])
        
    def lineReceived(self, data):
        if(self.state == "NAME"):
            self.name = data
            sendtable() #TODO make this
            while(handler.mx != len(handler.users)):
                sleep(5) #wait for all players to join
            if(handler.locky == 0): #check the lock so only 1 person does role assignment
                handler.locky = 1 #"lock" the lock
                rspy = randint(0, len(users)) #assign the red and blue spy their role numbers
                while(True):
                    bspy = randint(0, len(users))
                    if (bspy != rspy): #make sure the spys are different
                        break
            
        elif(self.state == "CORD"):
       #     handler.table[data[0]][data[1]][1]
            

    #this will only ever be when I get coords from a player or their name
        
    def connectionMade(self):
        self.sendLine("Connection Made!")
        
class bighandler(Factory):

    def __init__(self, table, mx):
        self.table = table
        self.count = 0
        self.mx = mx
        self.rspy = randint(0,mx)
        while(True):
            self.bspy = randint(0, mx)
            if (self.bspy != self.rspy): #make sure the spys are different
                break
        handler.statinit(self.table, self.mx, self.rspy, self.bspy)
    def buildProtocol(self, addr):
        self.count += 1
        return handler(self.count)
