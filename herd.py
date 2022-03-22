from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        chompy = Dinosaur("chompy", 30)
        speedy = Dinosaur("speedy", 10)
        slashy = Dinosaur("slashy", 20)
         
        self.dinosaurs.append(chompy)
        self.dinosaurs.append(speedy)
        self.dinosaurs.append(slashy)
       

# team_dino = Herd()
# team_dino.create_herd()
# print(team_dino.dinosaurs)



