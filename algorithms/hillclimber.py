import random
import matplotlib.pyplot as plt

import sys
sys.path.append("..")
from classes.house import House
from classes.map import Map

def hillclimber(map, houses, batteries):
    new_costs = []
    for i in range(20000):
        
        house1 = houses[random.randrange(149)]
        house2 = houses[random.randrange(149)]

        battery1 = house1.connected
        battery2 = house2.connected
        if battery1 is None:
            if batteries[0].power > house1.output:
                house1.connect(batteries[0])
            elif batteries[1].power > house1.output:
                house1.connect(batteries[1])
            elif batteries[2].power > house1.output:
                house1.connect(batteries[2])
            elif batteries[3].power > house1.output:
                house1.connect(batteries[3])
            elif batteries[4].power > house1.output:
                house1.connect(batteries[4])
            else:
                house1 = houses[random.randrange(149)]
        if battery2 is None:
            if batteries[0].power > house2.output:
                house1.connect(batteries[0])
            elif batteries[1].power > house2.output:
                house1.connect(batteries[1])
            elif batteries[2].power > house2.output:
                house1.connect(batteries[2])
            elif batteries[3].power > house2.output:
                house1.connect(batteries[3])
            elif batteries[4].power > house2.output:
                house1.connect(batteries[4])
            else:
                house2 = houses[random.randrange(149)]

        battery1 = house1.connected
        battery2 = house2.connected

        if house1.id == house2.id:
            pass
            
        elif battery1.id == battery2.id:
            pass
            
        elif battery1.power + house1.output - house2.output < 0:
            pass            
        elif battery2.power + house2.output - house1.output < 0:
            pass
        elif distance(house1, battery2) + distance(house2, battery1) < distance(house1, battery1) + distance(house2, battery2):
            map.swap(house1, house2)
        new_costs.append(map.moneyspent)
    print(new_costs[-1])
    plt.plot(range(len(new_costs)),new_costs,'r-')
    # plt.show()
    # map.visualize()

def distance(house, battery):
    return abs(house.x - battery.x) + abs(house.y - battery.y)
