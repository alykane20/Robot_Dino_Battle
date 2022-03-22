from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapon = Weapon("sword", 10)

    def attack (self, dinosaur):
        if self.health > 0:
            dinosaur.health -= self.weapon.attack_power
            print(f"{dinosaur.name}'s health went down {self.weapon.attack_power}!" )
        else:
            print("All the robots crashed, can't attack")

technoBot = Robot("technoBot")
tntBot = Robot ("tntBot")
tornadoBot = Robot("tornadoBot")
