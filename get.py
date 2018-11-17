from classes.battery import Battery
from classes.house import House
import re
import pandas as pd
INPUT='/resources/wijk1_batterijen.txt'
INPUT_HOUSE = '/resources/wijk1_huizen.csv'


class Get:
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
        """Remove a certain amount of capacity that is being taken."""
        self.power = self.power - power_amount


    def load_batteries(self, filename):
        """Gain a list of batteries from a given neighbourhood. The neighbourhood is an integer."""
        
        battery_list=[]
        with open(filename,'r') as file:
            next(file)
            for line in file:
                result = re.findall(r'\d+.?\d*\b', line)
                x = result[0]
                y = result[1]
                capacity = result[2]
                battery_list.append(Battery(x, y, capacity))
            return(battery_list)
            
    def load_houses(self, filename):
        """Gain a list of houses from a given neighbourhood. The neighbourhood is an integer."""
        data = pd.read_csv(INPUT_HOUSE)
        df = pd.DataFrame(data)
        huizen = []
        for row in df:
            x = df['x']
            y = df['y']
            output = df['max. output']
            huizen.append(House(x, y, output))
        return(huizen)