import matplotlib.pyplot as plt

def first_distance(self,houses,batteries):  
    total_distance = 0    
    for house in houses:
        lowest_distance = 1000000
        if distance(house, batteries[0]) < lowest_distance:
            lowest_distance = distance(house, batteries[0])
        if distance(house, batteries[1]) < lowest_distance:
            lowest_distance = distance(house, batteries[1])
        if distance(house, batteries[2]) < lowest_distance:
            lowest_distance = distance(house, batteries[2])
        if distance(house, batteries[3]) < lowest_distance:
            lowest_distance = distance(house, batteries[3])
        if distance(house, batteries[4]) < lowest_distance:
            lowest_distance = distance(house, batteries[4])
        total_distance += lowest_distance
    print(total_distance * 9)



def distance(house, battery):
    return abs(house.x - battery.x) + abs(house.y - battery.y)
    