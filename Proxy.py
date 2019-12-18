# Using the Proxy pattern 

#Provides a layer/interface to a expandable object in memory, for example. or a Expanding file resource.
import random
from random import randint

class Player(object):
    def __init__(self, name):
        self.name = name
        self.price = random.randint(1000000,90000000)
        self.training = False
        self.vacation = False
        
        
    def onTraining(self):
        self.training = True 
        return self.training
    
    def onVacation(self):
        self.vacation = True
        return self.vacation
    
    def getPrice(self):
        return self.price
        
    def status(self):
        return (self.vacation or self.training)

class Manager(object): #Acts as proxy for player
    def __init__(self, player):
        self.managed_player = player
        print("Managing player: {}".format(self.managed_player.name))
        
    def send_player_on(self,session):
        if session in ['vacation', 'training']:
            if session == 'vacation':
                print("Sending player:{} on vacation. HAVE FUN!!".format(self.managed_player.name))
            else:
                print("Sending player: {} on training. WORK HARD!!".format(self.managed_player.name))
        else:
            print("Can't send player on {}. Not a valid option.".format(session))
        
    def sell_player(self, offer):
        print("Price of the player {} is {}".format(self.managed_player.name, self.managed_player.getPrice()))
        if offer > self.managed_player.getPrice():
            print("Selling the player {} for {}".format(self.managed_player.name, offer))
        else:
            print("Not selling the player {} since the offer is less than the player's worth.".format(self.managed_player.name))
            
            
            

if __name__ == '__main__':
    fballer = Player('Adamya')
    mgr = Manager(fballer)
    mgr.send_player_on("training")
    mgr.sell_player(100000000   )