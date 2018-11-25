import pandas as pd
class House:
    # open the first file, go through houses

    def __init__(self, x, y, output):
        self.x = x 
        self.y = y 
        self.output = output
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


    def connect(self, battery):
        self.connected = battery
        battery.store(self.output)
    
    def __repr__(self):
        return '<House x={} y={} out={}>'.format(self.x,self.y,self.output)

    
