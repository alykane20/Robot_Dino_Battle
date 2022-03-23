from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        technoBot = Robot("TechnoBot")
        tntBot = Robot("TntBot")
        tornadoBot = Robot("TornadoBot")
         
        self.robots.append(technoBot)
        self.robots.append(tntBot)
        self.robots.append(tornadoBot)



# robot_fleet = Fleet()
# robot_fleet.create_fleet()
# for robot in robot_fleet.robots:
#     print(robot.name)

