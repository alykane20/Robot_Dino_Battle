

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50

    
    #if a dino has health about 0, subtract attack_power from a robot
    def attack(self, robot):
        if self.health > 0:
            robot.health -= self.attack_power
            print(f"{robot.name}'s health went down {self.attack_power}!" )
        else:
            print("All the dinosaurs are dead, can't attack")
    

chompy = Dinosaur("chompy", 30)
speedy = Dinosaur("speedy", 10)
slashy = Dinosaur("slashy", 20)


