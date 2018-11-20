class Battery(object):
    """
    Representation of a Battery containing the battery id, its x and y coordinate, and its current capacity
    """
    def __init__(self, x_coordinate, y_coordinate, capacity):
        """
        initialize battery characteristics
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = capacity


    def check_storage_space(self):
        """
        check if battery has storage space left
        """    
        if self.capacity > 0:
            return True
        else:
            return False