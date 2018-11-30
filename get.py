from classes.battery import Battery
from classes.house import House
import re
import pandas as pd
INPUT='/resources/wijk1_batterijen.txt'
INPUT_HOUSE = '/resources/wijk1_huizen.csv'
 
def __load_batteries(filename):
    """Get a list of batteries from a given neighbourhood. The neighbourhood is an integer."""
    
    battery_list=[]
    with open(INPUT,'r') as file:
        next(file)
        for line in file:
            result = re.findall(r'\d+.?\d*\b', line)
            x = float(result[0])
            y = float(result[1])
            capacity = result[2]
            z= [x, y, capacity]
            battery_list.append(z)
        
def __load_houses(filename):
    """Get a list of houses from a given neighbourhood. The neighbourhood is an integer."""
    data = pd.read_csv(INPUT_HOUSE)
    huizen = []
    for index, row in data.iterrows():
        x = row['x']
        y = row['y']
        output = row['max. output']
        z= [x, y, output]
        huizen.append(z)

def batteries(neighbourhood):
    return __load_batteries('resources/wijk{}_batterijen.txt'.format(neighbourhood))

def houses(neighbourhood):
    return __load_houses('resources/wijk{}_huizen.csv'.format(neighbourhood))