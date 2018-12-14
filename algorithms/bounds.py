import matplotlib.pyplot as plt
import config
from classes.map import distance

def first_distance(self,houses,batteries):
    """
    Connects houses to batteries that have the lowest distance
    """  
    total_distance = 0    
    for house in houses:
        lowest_distance = 9000
        lowest_battery = 8
        if distance(house, batteries[0]) < lowest_distance:
            lowest_distance = distance(house, batteries[0])
            lowest_battery = 0
        if distance(house, batteries[1]) < lowest_distance:
            lowest_distance = distance(house, batteries[1])
            lowest_battery = 1
        if distance(house, batteries[2]) < lowest_distance:
            lowest_distance = distance(house, batteries[2])
            lowest_battery = 2
        if distance(house, batteries[3]) < lowest_distance:
            lowest_distance = distance(house, batteries[3])
            lowest_battery = 3
        if distance(house, batteries[4]) < lowest_distance:
            lowest_distance = distance(house, batteries[4])
            lowest_battery = 4
        self.connect(house, batteries[lowest_battery])
        total_distance += lowest_distance
    print(total_distance * config.cost_per_grid_section)

def highest_distance(self,houses,batteries):  
    """
    Connects houses to batteries that have the farthest distance
    """  
    total_distance = 0    
    for house in houses:
        highest_distance = 0
        highest_battery = 0
        if distance(house, batteries[0]) > highest_distance:
            highest_distance = distance(house, batteries[0])
            highest_battery = 0
        if distance(house, batteries[1]) > highest_distance:
            highest_distance = distance(house, batteries[1])
            highest_battery = 1
        if distance(house, batteries[2]) > highest_distance:
            highest_distance = distance(house, batteries[2])
            highest_battery = 2
        if distance(house, batteries[3]) > highest_distance:
            highest_distance = distance(house, batteries[3])
            highest_battery = 3
        if distance(house, batteries[4]) > highest_distance:
            highest_distance = distance(house, batteries[4])
            highest_battery = 4
        self.connect(house, batteries[highest_battery])
        total_distance += highest_distance
    print(total_distance * config.cost_per_grid_section)