# Creating the observer pattern

# You have a client that likes to subscribe to some subject S1, S2 ,etc and wants a notification whenever there is some activity going on in the subscribed subject. 




class Topic:
    def __init__(self, ):
        self.__clients = []
        
    def register(self, client):
        print('New subscriber: {}'.format(client))
        self.__clients.append(client)
    
    def notifyAll(self, *args, **kwargs):
        for client in self.__clients:
            if kwargs.get('menOnly') and isinstance(client, MenAbove40):
                print("These are the Men.")
            if kwargs.get('theMoreBeautifulGender') and isinstance(client,  LadiesAbove30):
                print("Ladies go first!")
            client.notify(self, *args, **kwargs)

class MenAbove40:
    def __init__(self, topic):
        topic.register(self)
    
    def notify(self, *args, **kwargs):
        print(type(self).__name__, "----> Got a", args, "From", topic)


class LadiesAbove30:
    def __init__(self, topic):
        topic.register(self)
    
    def notify(self, *args, **kwargs):
        print(type(self).__name__, "----> Got a", args, "From", topic)


topic = Topic()
#Obs_1 = Observer(topic)
#Obs_2 = Observer(topic)
#Obs_3 = AnotherObserver(topic)

Subscribers = []
for i in range(10):
    Subscribers.append(MenAbove40(topic))

for i in range(10):
    Subscribers.append(LadiesAbove30(topic))


topic.notifyAll('Thank you for watching this video, please leave a like and subscribe.', menOnly=True)
topic.notifyAll('Thank you being awesome! : ', theMoreBeautifulGender=True)
