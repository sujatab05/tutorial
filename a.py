from abc import ABC, abstractmethod
class car(ABC):
    @abstractmethod
    def milage (self):
        pass
class tesla (car):
    def milage (self):
        print("milage is 300kmph")
class tata (car):
    def milage (self):
        print("milage is 400kmph")

t=tesla()
t.milage()
s=tata()
s.milage()
