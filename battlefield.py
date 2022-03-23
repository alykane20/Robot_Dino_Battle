from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):
        pass

    def display_welcome(self):
        print("Welcome to the ultimate battle!!")
        print("________________________________________")
        print("Here are our dinosaurs!")
        for dino in self.herd.dinosaurs:
            print(dino.name)
        print("________________________________________")
        print("Here are our robots!")
        for robot in self.fleet.robots:
            print(robot.name)
        
    # main battle between dino and robot turns  
    def battle(self):
        chosen_dino = self.herd.dinosaurs[0]
        self.dino_turn(chosen_dino)
    
    # choose a dino with health >0, and attack robot
    def dino_turn(self, dinosaur):
        print("Dinos attack!")
        chosen_robot = self.show_dino_opponent_options()
        dinosaur.attack(chosen_robot)

    def robot_turn(self, robot):
        print("Robots attack!")
        
        #show dinos still with health
    def show_dino_opponent_options(self):
        for robot in self.fleet.robots:
            if robot.health > 0:
                return robot.health
            else:
                print("All robots DEAD")

         #show robos still with health
    
    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass


    