from re import A
from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapon = Weapon("sword", 50)

    def attack (self, dinosaur):
        pass

technoBot = Robot("technoBot")
tntBot = Robot ("tntBot")
tornadoBot = Robot("tornadoBot")
