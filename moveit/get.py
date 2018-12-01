from classes.battery import Battery
from classes.house import House
import re
import pandas as pd
 
def __load_batteries(filename):
    """Get a list of batteries from a given neighbourhood. The neighbourhood is an integer."""
    
    battery_list=[]
    with open(filename,'r') as file:
        next(file)
        for line in file:
            result = re.findall(r'\d+.?\d*\b', line)
            x = float(result[0])
            y = float(result[1])
            capacity = result[2]
            battery_list.append(Battery(x, y, capacity))
    return battery_list
        
def __load_houses(filename):
    """Get a list of houses from a given neighbourhood. The neighbourhood is an integer."""
    
    data = pd.read_csv(filename)
    huizen = []
    for index, row in data.iterrows():
        x = row['x']
        y = row['y']
        output = row['max. output']
        huizen.append(House(x, y, output))
    return huizen

def batteries(neighbourhood):
    return __load_batteries('resources/wijk{}_batterijen.txt'.format(neighbourhood))

def houses(neighbourhood):
    return __load_houses('resources/wijk{}_huizen.csv'.format(neighbourhood))