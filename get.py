from classes.battery import Battery
from classes.house import House
import re
import pandas as pd
INPUT='/resources/wijk1_batterijen.txt'
INPUT_HOUSE = '/resources/wijk1_huizen.csv'
 
def connect(self,connected_obect):
    """Connect the house to another object. The route also needs to be determined here."""

    pass # TODO


def store(self,power_amount):
    """Remove a certain amount of capacity that is being taken."""
    self.power = self.power - power_amount


def batteries(self, filename):
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
    print(battery_list)
        
def houses(self, filename):
    """Gain a list of houses from a given neighbourhood. The neighbourhood is an integer."""
    data = pd.read_csv(INPUT_HOUSE)
    huizen = []
    for index, row in data.iterrows():
        x = row['x']
        y = row['y']
        output = row['max. output']
        huizen.append(House(x, y, output))
    return huizen