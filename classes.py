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
