from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor
from time import sleep
from random import randint

class handler(LineReceiver):
    table = [] #static var for the table
    users = [] #list of all users
    roles = [] #role list for the players. 0 is red, 1 is blue, 2 is rspy, 3 is bspy
    border = [] #turn order for the blue and red players
    rorder = []
    mx = 0  #max number of players
    heavy = 0 #which side is heavier, IE which has 9 instead of 8 tiles. 0 is red
    
    @classmethod
    def statinit(_table, _mx, _roles, _heavy):
        handler.table = _table
        handler.mx = _mx
        handler.roles = _roles
        if(_heavy == 1):
            handler.heavy = 0
        for x in range(0, _mx): #create list of red and blue plen for later
            if(_roles[x] == 0):
                handler.rorder.append(x)
            elif(_roles[x] == 1):
                handler.border.append(x)
            
    def __init__(self, _number):
        self.name = None
        self.state = "NAME"
        self.number = _number #user number, AKA which list element they are
        handler.users.append(self)
    
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
            self.state = "CORD"
        elif(self.state == "CORD"):
       #     handler.table[data[0]][data[1]][1]
            

    #this will only ever be when I get coords from a player or their name
        
    def connectionMade(self):
        self.sendLine("Connection Made!")
        self.sendLine(handler.roles[self.number])
class bighandler(Factory):

    def __init__(self, table, mx, heavy):
        self.count = 0 #current number of players, used later
        roles = [0 for x in range (0, mx)] #list of roles for all players
        roles[randint(0, mx)] = 2 #mark red spy
        n = (mx - 2)/2 #the number of players on the red or blue teams that aren't spys
        counts [n,n] # for assigning blue and red plens
        while(True):
            k = randint(0,mx)
            if (roles[k] != 2): #make sure the spys are different
                roles[k] = 3 #assign blue spy
                break
        for x in roles:
            if(x == 2 || x == 3):
                continue
            else:
                i = randint(0,1)
                if(counts[i] > 0):
                    x = i
                    counts[i] -= 1
                else:
                    x = (i ^ 1) #hacky way to get the other one
                    counts[i^1] -= 1
        handler.statinit(table, mx, roles, heavy)
    
    def buildProtocol(self, addr):
        self.count += 1
        return handler(self.count)
