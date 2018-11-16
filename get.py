from BatteryClass import Battery
import re
INPUT='wijk1_batterijen.txt'

class House:
    def __init__(self,x,y,output):
        self.x              = int(x)
        self.y              = int(y)
        self.output         = float(output)
        self.connection     = None
        self.route          = []
    
    def connect(self,connected_obect):
        """Connect the house to another object. The route also needs to be determined here."""

        pass # TODO
    
    def store(self,power_amount):
        """Increase its output, in case a house is connected to another house.
        If the house is already connected, pass on the energy to its connection."""

        pass # TODO


class Battery:
    def __init__(self,x,y,max_capacity):
        self.x              = int(x)
        self.y              = int(y)
        self.max_capacity   = int(max_capacity)
        self.power          = int(max_capacity)


    def store(self,power_amount):
        """Remove a certain amount of capacity that is being taken."""
        self.power = self.power - power_amount

# ---------------------------------------------

def batteries(neighbourhood):
    """Gain a list of batteries from a given neighbourhood. The neighbourhood is an integer."""
    
    battery_list=[]
    with open(INPUT,'r') as file:
        next(file)
        for line in file:
            result = re.findall(r'\d+.?\d*\b', line)
            x = result[0]
            y = result[1]
            capacity = result[2]
            battery_list.append(Battery(x, y, capacity))
        return(battery_list)


def houses(neighbourhood):
    """Gain a list of houses from a given neighbourhood. The neighbourhood is an integer."""

    pass # TODO