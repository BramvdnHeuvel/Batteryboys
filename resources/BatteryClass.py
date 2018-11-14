# werkt alleen op wijk 1 omdat bij de batterij het decimale getal nog niet goed wordt uitgelezen

import re

INPUT='wijk1_batterijen.txt'

# save the location and battery storage of battery
battery_list=[]
with open(INPUT,'r') as file:
    next(file)
    for line in file:
        result = re.findall(r'\d+', line)
        battery_list.append(result)
    x = battery_list[0][0]
    y = battery_list[0][1]    
    capacity = battery_list[0][2]
      
class Battery(object):
    """
    Representation of the Batteries
    """
    def __init__(self, battery_id, x_coordinate, y_coordinate, capacity):
        self.battery_id = battery_id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = capacity


    def check_storage_space(self):
        if self.capacity > 0:
            return True
        else:
            return False
