from abc import ABCMeta, abstractmethod
# SuperClass Below
from SimUDuckProgram import QuackBehavior, FlyBehavior
class Duck():
    quackBehavior = QuackBehavior
    flyBehavior = FlyBehavior
    def performQuack(self):
        Duck.quackBehavior.quack()

    def performFly(self):
        Duck.flyBehavior.fly()

    def swim(self):
        print("I am Swimming.")
    @abstractmethod
    def display(self): pass

# ***** SubClasses *****
from SimUDuckProgram import Duck, MuteQuack, Quack, Squeak, FlyWithWings, FlyNoWay
class RedHeadDuck(Duck):
    def __init__(self):
        Duck.quackBehavior = Quack()
        Duck.flyBehavior = FlyWithWings()
    def display(self):
        print("I am a Red-Head Duck")

class DecoyDuck(Duck):
    def __init__(self):
        Duck.quackBehavior = MuteQuack()
        Duck.flyBehavior = FlyNoWay()
    def display(self):
        print("I am a Decoy Duck.")

class RubberDuck(Duck):
    def __init__(self):
        Duck.flyBehavior = FlyNoWay()
        Duck.quackBehavior = Squeak()
    def display(self):
        print("I am a Rubber Duck")

class MallardDuck(Duck):
    def __init__(self):
        Duck.quackBehavior = Quack()
        Duck.flyBehavior = FlyWithWings()
    def display(self):
        print("I am a Mallard Duck")

# ******* The QuackBehavior Interface  *******
from abc import ABCMeta, abstractmethod


class QuackBehavior:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self): pass

# ***** Quack Class Delegations *****
from SimUDuckProgram import QuackBehavior
class Quack(QuackBehavior):

    def quack(self):
        print("Quack!!")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("Mute")
class Squeak(QuackBehavior):

    def quack(self):
        print("Squeak!")

# ***** The FlyBehavior Interface *****
class FlyBehavior:
    __metaclass__ =  ABCMeta

    @abstractmethod
    def fly(self): pass

# **** Fly Class delegations ****
from SimUDuckProgram import FlyBehavior
class FlyWithWings(FlyBehavior):

    def fly(self):
        print("I'm Flying!")

class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I can\'t fly")

# ***** Testing The Duck program
from SimUDuckProgram import RubberDuck, MallardDuck, RedHeadDuck, DecoyDuck
rubberD = RubberDuck()
RedH = RedHeadDuck()
mallD = MallardDuck()
decoyD = DecoyDuck()

listing = [rubberD, RedH, mallD, decoyD]
for i in listing:
    i.Display()
    i.swim()
    i.performFly()
    i.performQuack()