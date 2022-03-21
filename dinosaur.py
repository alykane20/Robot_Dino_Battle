class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50

    
    # from list of dinos, choose one that has health >0 and attack_power >0
    def attack(self, robot):
        pass
    


chompy = Dinosaur("chompy", 30)
speedy = Dinosaur("speedy", 10)
slashy = Dinosaur("slashy", 20)

