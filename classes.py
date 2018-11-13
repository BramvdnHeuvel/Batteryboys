from resources import get

class Map:
    def __init__(self,neighbourhood):
        self.batteries  = get.batteries(neighbourhood)
        self.houses     = get.houses(neighbourhood)
    
    def render(self):
        """Visualize the board, including any potentially made connections"""
        pass # TODO
    
class House(object):
    def __init__(self, X, Y, output, connection):
        self.X = X
        self.Y = Y
        self.output = output
        self.connection = connection 

        pass    
