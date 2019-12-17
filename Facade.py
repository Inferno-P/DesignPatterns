
class TravelOrganizer(object):
    def __init__(self):
        print("TravelOrganizeer:: Let me arrange the travel for you! :)")
    
    def arrangeTravel(self, destination, typeOfTravel):
        print("The destination is {}".format(destination))
        
        self.meansOfTransport = Transporter(destination = destination , typeOfTravel = typeOfTravel)
        self.meansOfTransport.bookTravel()
        
        self.meansOfSleeping = Hotelier()
        self.meansOfSleeping.bookRoom()
        self.meansOfSleeping.arrangeFood()
        
class Transporter(object):
    def __init__(self, destination, typeOfTravel):
        self.destination = destination
        self.typeOfTravel = typeOfTravel
        print("Arranging the transport to your destination {} by means {}".format(destination, typeOfTravel))
        
    def bookTravel(self,):
        if self.typeOfTravel == 'owncar':
            print("Nothing to book, customer uses his/her own car!")
        elif self.typeOfTravel == 'plane':
            print("Booking seats to destination: {} by PLANE!".format(self.destination))
        
        elif self.typeOfTravel == 'bus':
            print("Booking seats for travelling to your destination: {} by BUS!".format(self.destination))

class Hotelier(object):
    def __init__(self):
        print("Arranging the rooms for customers....")
    
    def roomFree(self):
        print("Checking if there are any rooms left free?")
        return True
    
    def bookRoom(self):
        if self.roomFree():
            print("Booking room for customer!")
    
    def arrangeFood(self):
        print("Arranging the food for customers!")
        
class RoadTripping(object):
    def __init__(self):
        print("Arranging some sightseeing for the customers.....")
    
    def arrangeTour(self):
        print("Arranging some fancy places to visit!")
    

class You(object):
    def __init__(self, name):
        print("Me:: Whohooooo we are travelling to {}".format(name))
    
    def talkToAgent(self):
        print("Me::Askign agent to arrange this weekend!")
        manager = TravelOrganizer()
        manager.arrangeTravel(destination='Greece', typeOfTravel='plane')
        
    def __del__(self):
        print("Me:: Thank you Mr. Manager for arranging this trip!")
    

Me = You('Daniel')
Me.talkToAgent()
        
    