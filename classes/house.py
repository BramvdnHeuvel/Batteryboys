class House:
    """
    The house class represents a house in the smart grid. Each house has an id,
    a x and y coordinate which determine the location of the house in the grid,
    and an output.
    """

    def __init__(self, id, x, y, output):
        self.id = id
        self.x = x 
        self.y = y 
        self.output = output
        self.connected = None
        
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def connect(self, battery):
        self.connected = battery
        battery.store(self.output)
        return self.connected
    
    def __repr__(self):
        return '<House id={} x={} y={} out={}>'.format(self.id,self.x,self.y,self.output)

    
