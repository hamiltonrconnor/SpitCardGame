import time
class Observer:


    def __init__(self,observers):
        self.observers = observers

    def registerObserver(self,observer):
        temp = []
        temp.extend(self.observers)
        temp.append(observer)
        print("registered: " + observer.__str__())
        return Observer(temp)


    def unregisterOberserver(self,observer):

        if(observer in self.observers):
            print("unregistered: "+ observer.__str__())
            self.observers.remove(observer)
            return Observer(self.observers)

        return Nones

    def getObservers(self):
        return self.observers
