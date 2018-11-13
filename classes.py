from resources import get

class Map:
    def __init__(self,neighbourhood):
        self.batteries  = get.batteries(neighbourhood)
        self.houses     = get.houses(neighbourhood)
    
    def render(self):
        """Visualize the board, including any potentially made connections"""
        pass # TODO
    
    def __find_object(self,x,y):
        """Find the object that is located on a given location."""
        for battery in self.batteries:
            if x == battery.x and y == battery.y:
                return battery
        
        for house in self.houses:
            if x == house.x and y == house.y:
                return house
        
        return None

    def __connect(self,x1,y1,x2,y2,must_connect_to_battery=True):
        """Connect the object of one location to another."""
        house = self.__find_object(x1,y1)
        battery = self.__find_object(x2,y2) # Note: doesn't have to be battery, per say

        if house is None:
            raise TypeError("Could not find house that needed to be connected.")
        if battery is None:
            raise TypeError("Could not find house/battery that needed to be connected to.")
        
        if must_connect_to_battery and battery.__class__.__name__ != "Battery":
            raise TypeError("Cannot connect to a non-Battery object")

        house.connect(battery)
        self.moneyspent += manhattan_distance(x1,y1,x1,y1) * config.cost_per_grid_section
    