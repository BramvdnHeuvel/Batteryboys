class Battery(object):
    """
    Representation of a Battery containing the battery id, its x and y coordinate, and its current capacity
    """
    def __init__(self, x_coordinate, y_coordinate, capacity):
        """
        initialize battery characteristics
        """
        self.x = int(x_coordinate)
        self.y = int(y_coordinate)
        self.capacity = float(capacity)
        self.power = float(capacity)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __repr__(self):
        return '<Battery x={} y={} cap={}>'.format(self.x,self.y,self.capacity)

    def check_storage_space(self):
        """
        check if battery has storage space left
        """    
        if self.capacity > 0:
            return True
        else:
            return False
    
    def store(self, amount):
        self.power = self.power - amount