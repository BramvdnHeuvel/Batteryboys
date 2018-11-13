import config

from resources import get
from scheme import manhattan_distance

class Map:
    def __init__(self,neighbourhood):
        self.batteries  = get.batteries(neighbourhood)
        self.houses     = get.houses(neighbourhood)
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
        self.moneyspent += manhattan_distance(x1,y1,x1,y1) * config.cost_per_grid_section

    def render(self):
        """Visualize the board, including any potentially made connections"""
        pass # TODO

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


    def __algorithm_first_fit(self):
        for i in range(len(self.houses)):
            house = self.houses[i]

            for battery in self.batteries:
                if battery.power > house.output:
                    self.__connect(house.x,house.y,battery.x,battery.y)
                    break
            
            # =========================================
            print("Ran out of batteries.")
            print("Money spent: " + self.moneyspent)
            print("\nPower left in batteries:")
            print([battery.power for battery in self.batteries])
            print("\nHouses left to distribute:")
            for j in range(len(self.houses) - i):
                unused_house = self.houses[i+j]
                print(unused_house.output)
            raise IndexError("Ran out of batteries to place houses in")

        print("Successfully distributed houses!")
        print("Money spent: " + self.moneyspent)
