import random
import matplotlib.pyplot as plt
from classes.map import distance
import sys
sys.path.append("..")
from classes.house import House
from classes.map import Map


def hillclimber(map):
    """
    Performs a hillclimber with two random chosen houses.
    It takes two random chosen houses, checks if it is possible to switch and if the costs would be lower.
    """
    for i in range(40000):
        
        house1 = map.houses[random.randrange(150)]
        house2 = map.houses[random.randrange(150)]

        battery1 = house1.connected
        battery2 = house2.connected
        if battery1 is not None and battery2 is not None:
            if battery1.id == battery2.id:
                pass
            elif battery1.power + house1.output - house2.output < 0:
                pass            
            elif battery2.power + house2.output - house1.output < 0:
                pass
            elif (distance(house1, battery2) + distance(house2, battery1)) < (distance(house1, battery1) + distance(house2, battery2)):
                map.swap(house1, house2)

        elif battery1 is None:
            check(house1, map.batteries)
        
        else:
            check(house2, map.batteries)
    
def check(house, batteries):
    """
    Checks when a house is not connected to a battery if there is a battery which still has enough capacity.
    """
    for battery in batteries:
        if battery.power > house.output:
            House.connect(house, battery)
            break
            

