from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_wecome(self):
        print("Welcome to the ultimate battle!!")
        print("________________________________________")
        print("Here are our dinosaurs!")
        dino_herd = Herd()
        dino_herd.create_herd()
        for dino in dino_herd.dinosaurs:
            print(dino.name)
        print("Here are out robots!")
        robot_fleet = Fleet()
        robot_fleet.create_fleet()
        for robot in robot_fleet.robots:
            print(robot.name)
        
        

    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass

    def robot_turn(self, robot):
        pass
        
        #show dinos still with health
    def show_dino_opponent_options(self):
        pass
        
        #show robos still with health
    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass


    