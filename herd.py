from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):

        self.dinosaurs.append(Dinosaur("Chompy", 30))
        self.dinosaurs.append(Dinosaur("Speedy", 10))
        self.dinosaurs.append(Dinosaur("Slashy", 20))
       

# dino_herd = Herd()
# dino_herd.create_herd()
# for dino in dino_herd.dinosaurs:
#     print(dino.name)



