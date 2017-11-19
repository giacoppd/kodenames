from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

#I need a statemachine so I know where I am in the game
#One to load users, one to play the game

class handler(LineReceiver):

    def __init__(self, users, table):
        self.users = users
        self.table = table
        self.name = None
        self.state = "NAME"

    def lineReceived(self, data):
        if(self.state == "NAME"):
            self.name = data
            self.state = "CORD"
        elif(self.state == "CORD"):
            

    #this will only ever be when I get coords from a player or their name
        
    def connectionMade(self):
        self.sendLine("Connection Made!")
        
class bighandler(Factory):

    def __init__(self, table):
        self.users = {} #for the user names later
        self.table = table

    def buildProtocol(self, addr):
        return handler(self.users, self.factory.table)
