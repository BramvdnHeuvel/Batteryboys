class Battery(object):
    """
    Representation of a Battery containing the battery id, its x and y coordinate, and its current capacity
    """
    def __init__(self, id, x, y, capacity):
        self.id = id
        self.x = x
        self.y = y
        self.capacity = float(capacity)
        self.power = float(capacity)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __repr__(self):
        return '<Battery x={} y={} cap={} id = {}>'.format(self.x,self.y,self.capacity,self.id)

    def check_storage_space(self):
        """
        check if battery has storage space left
        """    
        return self.capacity > 0
    
    def store(self, amount):
        self.power = self.power - amount
    
    def reset(self):
        self.power = self.capacity