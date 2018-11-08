from resources import get

class Map:
    def __init__(self,neighbourhood):
        self.batteries  = get.batteries(neighbourhood)
        self.houses     = get.houses(neighbourhood)
    
    def render(self):
        """Visualize the board, including any potentially made connections"""
        pass # TODO