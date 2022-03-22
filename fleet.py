from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        technoBot = Robot("technoBot")
        tntBot = Robot ("tntBot")
        tornadoBot = Robot("tornadoBot")
         
        self.robots.append(technoBot)
        self.robots.append(tntBot)
        self.robots.append(tornadoBot)



# robot_fleet = Fleet()
# robot_fleet.create_fleet()
# print(robot_fleet.robots)

