import matplotlib.pyplot as plt
import config
from classes.map import distance

def first_distance(map):
    """
    Connects houses to batteries that have the lowest distance
    """  
    total_distance = 0    
    for house in map.houses:
        lowest_distance = 9000
        lowest_battery = 8
        for battery in map.batteries:

            if distance(house, battery) < lowest_distance:
                lowest_distance = distance(house, battery)
        
        total_distance += lowest_distance
    print(total_distance * config.cost_per_grid_section)

def highest_distance(map):  
    """
    Connects houses to batteries that have the farthest distance
    """  
    total_distance = 0    
    for house in map.houses:
        highest_distance = 0
        for battery in map.batteries:
            if distance(house, battery) > highest_distance:
                highest_distance = distance(house, battery)
        
        total_distance += highest_distance
    print(total_distance * config.cost_per_grid_section)



