# from first_fit_batteries import first_fit_batteries
import random
import sys
sys.path.append("..")
from classes.house import House


# This will be the hill climber for our problem
# from main get first_fit_..

# pseudocode
# Get solution/grid from main.py
# get total costs of neighbourhood
# select random house from grid
# select other random house from grid
# swap houses
# calculate new costs of neightbouthood
# if new costs > old costs:
#     keep changes
# else:
#     swap back
def hillclimber(self, houses, batteries):
    house1 = houses[random.randrange(149)]
    house2 = houses[random.randrange(149)]

    house_batteries = list(house.connected for house in self.houses)
    # con_batteries_x = list(battery.x for battery in house_batteries)
    # con_batteries_y = list(battery.y for battery in house_batteries)
    con_batteries_id = list(battery.id for battery in house_batteries)
    battery1 = house_batteries[random.randrange(149)]
    battery2 = house_batteries[random.randrange(149)]
    print(house1)
    print(house2)
    if house1.id == house2.id:
        return False
    if battery1.id == battery2.id:
        return False
    if battery1.power + house1.output - house2.output < 0:
        return False
    if battery2.power + house2.output - house1.output < 0:
        return False
    if distance(house1, battery2) + distance(house2, battery1) < distance(house1, battery1) + distance(house2, battery2):
        self.connect(house1, battery2)
        self.connect(house2, battery1)
    else:
        print("succeeded")


    

    # print(con_batteries_x)

    # return con_batteries_y


def distance(house, battery):
    return abs(house.x - battery.x) + abs(house.y - battery.y)

# do this a lot of times    
# 
# 
# batterij 1 en batterij 2, huis 1 en huis 2
# als batterij 1 == batterij 2,
# stop
# als huis 1 == huis 2,
# stop
# als batterij 1 opslag + huis1 output - huis 2 output <0
# stop
# als batterij 2 opslag + huis 2 output - huis 1 output < 0
# stop


# import math

# increment = 0.1
# startingPoint = [1, 1]
# point1 = [1,5]
# point2 = [6,4]
# point3 = [5,2]
# point4 = [2,1]

# def distance(x1, y1, x2, y2):
#     dist = math.pow(x2-x1, 2) + math.pow(y2-y1, 2)
#     return dist

# def sumOfDistances(x1, y1, px1, py1, px2, py2, px3, py3, px4, py4):
#     d1 = distance(x1, y1, px1, py1)
#     d2 = distance(x1, y1, px2, py2)
#     d3 = distance(x1, y1, px3, py3)
#     d4 = distance(x1, y1, px4, py4)

#     return d1 + d2 + d3 + d4

# def newDistance(x1, y1, point1, point2, point3, point4):
#     d1 = [x1, y1]
#     d1temp = sumOfDistances(x1, y1, point1[0],point1[1], point2[0],point2[1],
#                                 point3[0],point3[1], point4[0],point4[1] )
#     d1.append(d1temp)
#     return d1

# minDistance = sumOfDistances(startingPoint[0], startingPoint[1], point1[0],point1[1], point2[0],point2[1],
#                                 point3[0],point3[1], point4[0],point4[1] )
# flag = True

# def newPoints(minimum, d1, d2, d3, d4):
#     if d1[2] == minimum:
#         return [d1[0], d1[1]]
#     elif d2[2] == minimum:
#         return [d2[0], d2[1]]
#     elif d3[2] == minimum:
#         return [d3[0], d3[1]]
#     elif d4[2] == minimum:
#         return [d4[0], d4[1]]

# i = 1
# while flag:
#     d1 = newDistance(startingPoint[0]+increment, startingPoint[1], point1, point2, point3, point4)
#     d2 = newDistance(startingPoint[0]-increment, startingPoint[1], point1, point2, point3, point4)
#     d3 = newDistance(startingPoint[0], startingPoint[1]+increment, point1, point2, point3, point4)
#     d4 = newDistance(startingPoint[0], startingPoint[1]-increment, point1, point2, point3, point4)
#     print(i,' ', round(startingPoint[0], 2), round(startingPoint[1], 2))
    
#     minimum = min(d1[2], d2[2], d3[2], d4[2])
#     if minimum < minDistance:
#         startingPoint = newPoints(minimum, d1, d2, d3, d4)
#         minDistance = minimum
#         print(i,' ', round(startingPoint[0], 2), round(startingPoint[1], 2))
#         i+=1
#     else:
#         flag = False