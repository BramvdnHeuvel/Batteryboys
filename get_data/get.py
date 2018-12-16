from classes.battery import Battery
from classes.house import House
import re
import pandas as pd
 
def __load_batteries(filename):
    """
    Get a list of batteries from a given neighbourhood. The neighbourhood is an integer.
    """
    battery_list=[]
    id = 0
    with open(filename,'r') as file:
        next(file)
        for line in file:
            result = re.findall(r'\d+.?\d*\b', line)
            x = float(result[0])
            y = float(result[1])
            capacity = result[2]
            battery_list.append(Battery(id, x, y, capacity))
            id+=1
    return battery_list
        
def __load_houses(filename):
    """
    Get a list of houses from a given neighbourhood. The neighbourhood is an integer.
    """ 
    data = pd.read_csv(filename)
    huizen = []
    i = 0
    for index, row in data.iterrows():
        id = i
        x = row['x']
        y = row['y']
        output = row['max. output']
        huizen.append(House(id, x, y, output))
        i += 1
    return huizen

def batteries(neighbourhood):
    """
    Specify which neighbourhood to use.
    """
    return __load_batteries('resources/wijk{}_batterijen.txt'.format(neighbourhood))

def houses(neighbourhood):
    """
    Specify which neighbourhood to use.
    """
    return __load_houses('resources/wijk{}_huizen.csv'.format(neighbourhood))