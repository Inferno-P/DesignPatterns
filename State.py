#Trying the State pattern 


from abc import abstractmethod, ABCMeta

class InternalState(metaclass=ABCMeta):
    @abstractmethod
    def changeState(self):
        pass
    
class TurnedOn(InternalState):
    def changeState(self):
        print("Turning ON.....")
        return "ON"
        
class TurnedOff(InternalState):
    def changeState(self):
        print("Turning OFF.....")
        return "OFF"
        
class IncreaseVolume(InternalState):
    def changeState(self):
        print("Increasing the volume by 10 !")
        return "+10"
        
class DecreaseVolume(InternalState):
    def changeState(self):
        print("Increasing the volume by 10 !")
        return "-10"

class RadioStation(InternalState):
    def __init__(self):
        self.state = None 
        
    def setState(self, status):
        self.state = status
    
    def getState(self):
        return self.state
        
    def changeState(self):
        self.state = self.state.changeState()
        
Radio  = RadioStation()
print('The radios internal state is currently : {}'.format(Radio.getState()))

ON = TurnedOn()
OFF = TurnedOff()


Louder = IncreaseVolume()
Lower = DecreaseVolume()


print("Turning OFF the Radio!")
Radio.setState(OFF)
Radio.changeState()
print("The radios internal state is currently: {}".format(Radio.getState()))


print("Turning ON the Radio!")
Radio.setState(ON)
Radio.changeState()
print("The radios internal state is currently: {}".format(Radio.getState()))

print("Increasing the volume!")
Radio.setState(Louder)
Radio.changeState()
print("The radios internal state is currently: {}".format(Radio.getState()))

print("Decreasing the volume!")
Radio.setState(Lower)
Radio.changeState()
print("The radios internal state is currently: {}".format(Radio.getState()))
