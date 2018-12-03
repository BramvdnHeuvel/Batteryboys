import config
from moveit.scheme import manhattan_distance
import moveit.get
import matplotlib.pyplot as plt

class Map:
    def __init__(self,neighbourhood):
        self.batteries  = moveit.get.batteries(neighbourhood)
        self.houses     = moveit.get.houses(neighbourhood)
        self.moneyspent = 0
        
        self.executions = []

    def start(self):
        for function in self.executions:
            function(self,self.houses,self.batteries)

    def execute(self,func):
        self.executions.append(func)

    def connect(self,house,battery,must_connect_to_battery=True):
        if house is None:
            raise TypeError("Could not find house that needed to be connected.")
        if battery is None:
            raise TypeError("Could not find house/battery that needed to be connected to.")
        
        if must_connect_to_battery and battery.__class__.__name__ != "Battery":
            raise TypeError("Cannot connect to a non-Battery object")

        house.connect(battery)
        self.moneyspent += manhattan_distance(house.x,house.y,battery.x,battery.y) * config.cost_per_grid_section + 5 * 5000

    def __connect(self,x1,y1,x2,y2,must_connect_to_battery):
        house = self.__find_object(x1,y1)
        battery = self.__find_object(x2,y2) # Note: doesn't have to be battery, per say

        return self.connect(house,battery,must_connect_to_battery)

    def __find_object(self,x,y):
        """Find the object that is located on a given location."""
        for battery in self.batteries:
            if x == battery.x and y == battery.y:
                return battery
        
        for house in self.houses:
            if x == house.x and y == house.y:
                return house
        
        return None

    def visualize(self):
        """Plots houses, batteries, and connections."""
        x = list(battery.x for battery in self.batteries)
        y = list(battery.y for battery in self.batteries)
        x1 = list(house.x for house in self.houses)
        y1 = list(house.y for house in self.houses)
        
        # # create lines between houses and batteries
        # random.choice([x, y])
        # if random.choice == x:
        #     pass
        #     # choose battery y coordinate
        #     # plot first line
        #     # plot second line

        # elif random.choice == y:
        #     # choose battery x coordinate
        #     # plot first line
        #     # plot second line
        #     plt.plot(x, y)
        
        
        # draw points and plot
        plt.scatter(x, y, color ='red')
        plt.scatter(x1, y1, color='blue')
        plt.grid(True)
        plt.show()

